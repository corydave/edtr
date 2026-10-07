/* =======================================================================
   IMGEDTR service worker - makes the app work offline and installable.

   How versioning works: index.html registers "sw.js?v=0.1.0". Bumping
   APP_VERSION in index.html changes that address, the browser installs
   this worker again, and the cache name below changes with it - so old
   files are thrown away and the new release is downloaded.
   ======================================================================= */
const VERSION = new URL(self.location.href).searchParams.get('v') || 'dev';
const CACHE = 'imgedtr-' + VERSION;

// The app's own files, saved at install time.
const APP_FILES = ['./', './index.html', './manifest.webmanifest', './icon-192.png', './icon-512.png'];

// The ONE outside file we allow: the pinned HEIC converter. It is saved
// the first time it is used, so HEIC photos also open offline afterwards.
const HEIC_PREFIX = 'https://cdn.jsdelivr.net/npm/heic-to@1.5.2/';

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE).then((c) => c.addAll(APP_FILES)).then(() => self.skipWaiting()));
});

// Delete caches from older versions.
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k.startsWith('imgedtr-') && k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;                  // never cache anything but plain downloads
  const url = new URL(req.url);
  const sameSite = url.origin === self.location.origin;
  const isHeicLib = req.url.startsWith(HEIC_PREFIX);
  if (!sameSite && !isHeicLib) return;               // everything else: let the browser handle it

  // Pages: try the network first (to pick up fixes), fall back to the cache offline.
  if (req.mode === 'navigate') {
    event.respondWith(fetch(req).catch(() => caches.match('./index.html')));
    return;
  }
  // Other files: cache first, then network (and remember what we fetched).
  event.respondWith(
    caches.match(req).then((hit) => hit || fetch(req).then((res) => {
      if (res.ok && (res.type === 'basic' || res.type === 'cors')) {
        const copy = res.clone();
        caches.open(CACHE).then((c) => c.put(req, copy));
      }
      return res;
    }))
  );
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
