/* ============================================================================
   SCRNCSTR service worker
   ============================================================================

   Exists for one reason: so the installed app launches without a network.
   Nothing here talks to a server - the app has no backend.

   VERSIONING
   ----------
   The version arrives in this file's own URL, because index.html registers it
   as `sw.js?v=<APP_VERSION>`. Changing APP_VERSION therefore changes this
   script's URL, which is what makes the browser treat it as a new worker and
   reinstall. That is what keeps the deploy ritual to a single edit:

       bump APP_VERSION in index.html  ->  upload  ->  cache rotates

   If the version were hardcoded here instead, you would have to remember to
   edit two files and the stale-cache bug would be waiting for the one time you
   forgot.
   ============================================================================ */

const VERSION = new URL(self.location.href).searchParams.get('v') || 'dev';
const CACHE   = `scrncstr-${VERSION}`;

// Same-origin app shell. Cross-origin things (web fonts) are deliberately NOT
// listed - see the fetch handler for why.
const SHELL = [
  './',
  './index.html',
  './manifest.webmanifest',
  './scrncstr-icon.png',
  './icon-192.png',
  './icon-maskable-512.png',
  // Sound files are OPTIONAL and only the FIRST extension that exists is
  // cached, mirroring the app's own SFX_EXTS precedence. Caching every
  // extension meant that a folder holding both an mp3 and the wav it replaced
  // stored both - 23MB of superseded wav files pinned offline for sounds the
  // app would never reach for.
];

const SFX_IDS  = ['applause', 'trombone', 'celebrate', 'laugh', 'rimshot'];
const SFX_EXTS = ['mp3', 'wav', 'm4a', 'ogg'];

/** Cache the first extension that answers, then stop looking for that sound. */
async function cacheFirstSound(cache, id) {
  for (const ext of SFX_EXTS) {
    const url = `./sfx-${id}.${ext}`;
    try {
      const res = await fetch(new Request(url, { cache: 'reload' }));
      if (!res.ok) continue;
      await cache.put(url, res);
      return url;
    } catch (_) { /* missing or unreachable - try the next extension */ }
  }
  return null;
}

self.addEventListener('install', (e) => {
  e.waitUntil((async () => {
    const cache = await caches.open(CACHE);
    // cache: 'reload' bypasses the HTTP cache, so a bump genuinely refetches
    // rather than re-storing whatever the browser already had.
    await Promise.allSettled([
      ...SHELL.map(url => cache.add(new Request(url, { cache: 'reload' }))),
      ...SFX_IDS.map(id => cacheFirstSound(cache, id))
    ]);
    await self.skipWaiting();     // take over immediately on a version bump
  })());
});

self.addEventListener('activate', (e) => {
  e.waitUntil((async () => {
    // Drop every cache from a previous version.
    const names = await caches.keys();
    await Promise.all(names.filter(n => n !== CACHE).map(n => caches.delete(n)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', (e) => {
  const req = e.request;

  // Only ever handle same-origin GETs. Cross-origin requests (Google Fonts)
  // pass straight through: caching them would mean storing opaque responses of
  // unknown success, and the app already falls back to the system font stack
  // when they fail. Offline the type is slightly plainer, nothing breaks.
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;

  e.respondWith((async () => {
    const cache = await caches.open(CACHE);

    // THE DOCUMENT IS NETWORK-FIRST, AND THIS IS NOT OPTIONAL.
    //
    // Serving index.html from cache creates a deadlock: the cached page carries
    // the OLD APP_VERSION, so it registers the OLD sw.js?v=... , so the version
    // never changes, so the cache never rotates. The app would be frozen at
    // whatever version was cached first, and no amount of uploading would fix
    // it. Fetching the document fresh is what lets a new version announce
    // itself. Falling back to cache keeps offline launching working.
    if (req.mode === 'navigate') {
      try {
        const fresh = await fetch(req);
        if (fresh && fresh.ok && fresh.type === 'basic') cache.put(req, fresh.clone());
        return fresh;
      } catch (_) {
        return (await cache.match('./index.html')) || Response.error();
      }
    }

    // Everything else - icons, manifest - is cache-first. These only change
    // when the version changes, and the install step refetches them.
    const cached = await cache.match(req, { ignoreSearch: true });
    if (cached) return cached;

    try {
      const fresh = await fetch(req);
      // Only store real successes - never a 404 or an opaque response.
      if (fresh && fresh.ok && fresh.type === 'basic') cache.put(req, fresh.clone());
      return fresh;
    } catch (err) {
      throw err;
    }
  })());
});

/* ---------------------------------------------------------------------------
   SUITE UPDATE CHECK (the same in every app's sw.js)
   The splash asks "is there a newer version?". This worker answers, because
   a service worker can always reach the network - even in an app whose page
   is forbidden to (VIDEDTR). It fetches index.html fresh from the server
   (cache: 'no-store' skips every stored copy), reads the APP_VERSION line out
   of it, and replies down the private MessageChannel the page sent along.
   Nothing is stored and nothing is sent except that one ordinary request.
   ------------------------------------------------------------------------ */
self.addEventListener('message', (event) => {
  const data = event.data;
  if (!data || data.type !== 'suite-check-update') return;
  const port = event.ports && event.ports[0];
  if (!port) return;
  event.waitUntil((async () => {
    try {
      const res = await fetch('./index.html', { cache: 'no-store' });
      if (!res.ok) { port.postMessage({ status: 'offline' }); return; }
      const html = await res.text();
      const found = /const APP_VERSION\s*=\s*["']([^"']{1,32})["']/.exec(html);
      port.postMessage({ status: 'ok', version: found ? found[1] : null });
    } catch (_) {
      port.postMessage({ status: 'offline' });      // no network
    }
  })());
});
