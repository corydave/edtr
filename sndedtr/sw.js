/* ============================================================================
   SNDEDTR service worker
   ----------------------------------------------------------------------------
   A service worker is a small script the browser keeps running in the
   background, separate from the page. Every request the app makes passes
   through the fetch handler below, which decides whether to answer from the
   cache or go to the network. That is what lets SNDEDTR open with no network
   at all once it has been visited once.

   DEPLOY RITUAL
   -------------
   Bump CACHE_VERSION below whenever you upload a new index.html. The cache
   name changes with it, so the new worker installs a fresh copy of everything
   and deletes the old cache on activation. Forgetting this is the usual reason
   a browser keeps showing yesterday's version.

   Keep this in step with APP_VERSION inside index.html.
   ========================================================================== */

const CACHE_VERSION = '0.7.5';
const SHELL_CACHE = `sndedtr-shell-${CACHE_VERSION}`;   // the app itself
const RUNTIME_CACHE = `sndedtr-runtime-${CACHE_VERSION}`; // fonts, optional bits

/* The files that make up the app. Everything here is fetched and stored when
   the worker installs, so a later visit needs no network. */
const SHELL_FILES = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icon.svg',
  './icon-192.png',
  './icon-512.png',
  './icon-maskable-512.png',
  './apple-touch-icon.png',
  './favicon-32.png',
];

/* Hosts whose responses are worth keeping but which are not part of the app:
   the web fonts, and the MP3 encoder that export loads only if you ask for MP3.
   Caching the encoder means MP3 export keeps working offline after one use. */
const RUNTIME_HOSTS = [
  'fonts.googleapis.com',
  'fonts.gstatic.com',
  'cdnjs.cloudflare.com',
];

/* ---------------------------------------------------------------------------
   INSTALL - fetch and store the app shell.
   ------------------------------------------------------------------------ */
self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(SHELL_CACHE);
    // cache.addAll fails the whole install if any single file 404s, so each
    // file is added on its own and a missing extra never blocks the update.
    await Promise.all(SHELL_FILES.map(async (url) => {
      try {
        await cache.add(new Request(url, { cache: 'reload' }));
      } catch (err) {
        console.warn('[sw] could not precache', url, err);
      }
    }));
    // Take over as soon as this worker is ready rather than waiting for every
    // tab to close. The running page keeps the code it already loaded, so this
    // only affects the next reload.
    await self.skipWaiting();
  })());
});

/* ---------------------------------------------------------------------------
   ACTIVATE - throw away caches belonging to older versions.
   ------------------------------------------------------------------------ */
self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const names = await caches.keys();
    await Promise.all(names.map((name) => {
      const mine = name.startsWith('sndedtr-');
      const current = name === SHELL_CACHE || name === RUNTIME_CACHE;
      return mine && !current ? caches.delete(name) : Promise.resolve();
    }));
    await self.clients.claim();
  })());
});

/* ---------------------------------------------------------------------------
   FETCH - three strategies, chosen by what is being asked for.
   ------------------------------------------------------------------------ */
self.addEventListener('fetch', (event) => {
  const request = event.request;

  // Never touch anything that is not a plain GET: a POST has side effects and
  // must always reach the network.
  if (request.method !== 'GET') return;

  const url = new URL(request.url);

  /* 1. Page loads: network first.
        Going to the network first means an uploaded update is picked up on the
        very next load. If the network is not there, the cached copy answers
        and the app opens offline. */
  if (request.mode === 'navigate') {
    event.respondWith((async () => {
      try {
        // cache: 'reload' skips the browser's own HTTP cache on the way out.
        // Without it a host that sends a long max-age on index.html can keep
        // handing back yesterday's page even though this worker asked the
        // network for it - which looks exactly like a failed deploy.
        const fresh = await fetch(request.url, { cache: 'reload', credentials: 'same-origin' });
        const cache = await caches.open(SHELL_CACHE);
        cache.put('./index.html', fresh.clone());
        return fresh;
      } catch (err) {
        const cached = await caches.match('./index.html', { ignoreSearch: true });
        return cached || new Response(
          '<!doctype html><meta charset="utf-8"><title>SNDEDTR is offline</title>' +
          '<body style="font-family:system-ui;padding:2rem">' +
          '<h1>SNDEDTR is offline</h1><p>Open it once while connected and it will ' +
          'work without a network from then on.</p>',
          { headers: { 'Content-Type': 'text/html; charset=utf-8' } },
        );
      }
    })());
    return;
  }

  /* 2. The app's own files: cache first.
        These only change when a new version is uploaded, and a new version
        gets a new cache name, so serving them from the cache is both correct
        and instant. */
  if (url.origin === self.location.origin) {
    event.respondWith((async () => {
      const cached = await caches.match(request, { ignoreSearch: true });
      if (cached) return cached;
      try {
        const fresh = await fetch(request);
        if (fresh.ok) {
          const cache = await caches.open(SHELL_CACHE);
          cache.put(request, fresh.clone());
        }
        return fresh;
      } catch (err) {
        return new Response('', { status: 504, statusText: 'Offline' });
      }
    })());
    return;
  }

  /* 3. Fonts and the optional MP3 encoder: serve the stored copy at once, and
        quietly refresh it in the background for next time. */
  if (RUNTIME_HOSTS.includes(url.hostname)) {
    event.respondWith((async () => {
      const cache = await caches.open(RUNTIME_CACHE);
      const cached = await cache.match(request);
      const network = fetch(request).then((response) => {
        if (response.ok || response.type === 'opaque') cache.put(request, response.clone());
        return response;
      }).catch(() => cached);
      return cached || network;
    })());
  }

  // Anything else is left alone and goes straight to the network.
});

/* ---------------------------------------------------------------------------
   MESSAGES - the page can ask this worker which version it is running, which
   is what the "a new version is ready" notice uses.
   ------------------------------------------------------------------------ */
self.addEventListener('message', (event) => {
  if (event.data === 'version' && event.source) {
    event.source.postMessage({ type: 'version', version: CACHE_VERSION });
  }
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
