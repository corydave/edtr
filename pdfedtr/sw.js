/* ===========================================================================
   PDFEDTR service worker - makes the app open with no network, and lets
   browsers install it as a proper app.

   What it keeps (in this browser only - nothing is ever sent anywhere):
     - the app itself: index.html, the manifest and the icons
     - index.html is the one-file edition, with both PDF libraries inside
       it, so it needs nothing else. The libraries' jsDelivr addresses are
       kept here too, for index-online.html (the source edition). Those
       addresses contain an exact version number, so a stored copy can
       never go stale. (1.13: the app uses the device's own fonts now, so
       there are no web fonts to keep.)

   How updates reach you:
     - The PAGE is "network first": with a network, every launch loads the
       newest index.html from the server (and keeps a copy); with no network,
       the stored copy opens instead. So uploading a new index.html is the
       whole deploy - there is no version number in this file to bump.
     - The splash also asks this worker whether the server has a newer
       version (the SUITE UPDATE CHECK at the bottom), for an installed app
       that has been left open for days.
   ======================================================================== */

const CACHE = 'pdfedtr';                 // one stable box; its contents get refreshed

// The app's own files, stored when the worker installs.
const APP_FILES = ['./', './index.html', './manifest.webmanifest',
                   './icon-192.png', './icon-512.png', './icon-maskable-512.png'];

// The outside files the app uses. Stored the first time they load.
const LIBRARY_HOSTS = ['cdn.jsdelivr.net'];
// ...and the two libraries, fetched up front so the first offline launch works.
const LIBRARIES = [
  'https://cdn.jsdelivr.net/npm/pdfjs-dist@3.11.174/build/pdf.min.js',
  'https://cdn.jsdelivr.net/npm/pdfjs-dist@3.11.174/build/pdf.worker.min.js',
  'https://cdn.jsdelivr.net/npm/pdf-lib@1.17.1/dist/pdf-lib.min.js'
];

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE);
    // Each file on its own, so one missing file never blocks the install.
    // cache: 'reload' goes to the server rather than the browser's own copy.
    await Promise.allSettled([
      ...APP_FILES.map((url) => cache.add(new Request(url, { cache: 'reload' }))),
      // mode: 'cors' gets a readable copy (these CDNs allow it), which is
      // far smaller to store than the unreadable "opaque" kind.
      ...LIBRARIES.map((url) => cache.add(new Request(url, { mode: 'cors' })))
    ]);
    await self.skipWaiting();            // take over now, not after every tab closes
  })());
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    // Clear out any other cache this app might have left behind.
    const names = await caches.keys();
    // Only this app's own old caches: on a site shared with the other apps (EDTR Studio)
    // their caches must be left alone.
    await Promise.all(names.filter((n) => n.startsWith('pdfedtr') && n !== CACHE).map((n) => caches.delete(n)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;      // only ever plain downloads
  const url = new URL(req.url);
  const mine = url.origin === self.location.origin;
  const library = LIBRARY_HOSTS.includes(url.hostname);
  if (!mine && !library) return;         // anything else: the browser handles it

  // The page: network first, stored copy when offline.
  if (req.mode === 'navigate') {
    event.respondWith((async () => {
      const cache = await caches.open(CACHE);
      try {
        const fresh = await fetch(req, { cache: 'no-cache' });   // always check with the server
        if (fresh.ok && fresh.type === 'basic') cache.put('./index.html', fresh.clone());
        return fresh;
      } catch (_) {
        return (await cache.match('./index.html')) || Response.error();
      }
    })());
    return;
  }

  // Everything else: the stored copy if there is one, otherwise fetch and keep it.
  event.respondWith((async () => {
    const cache = await caches.open(CACHE);
    const hit = await cache.match(req, { ignoreSearch: mine });
    if (hit) return hit;
    const fresh = await fetch(req);
    // Keep real successes only (and opaque font files, which cannot be read).
    if (fresh.ok || fresh.type === 'opaque') cache.put(req, fresh.clone()).catch(() => {});
    return fresh;
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
