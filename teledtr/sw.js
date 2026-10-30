/* =======================================================================
   TELEDTR service worker - makes the app work offline and installable.

   How versioning works: index.html registers "sw.js?v=0.1.0". Bumping
   APP_VERSION in index.html changes that address, the browser installs
   this worker again, and the cache name below changes with it - so old
   files are thrown away and the new release is downloaded.

   Only TELEDTR's own files are cached, and only caches whose names start
   with "teledtr-" are ever deleted (other apps share this site).
   ======================================================================= */
const VERSION = new URL(self.location.href).searchParams.get('v') || 'dev';
const CACHE = 'teledtr-' + VERSION;

// The app's own files, saved at install time.
const APP_FILES = [
  './', './index.html', './camera-lab.html', './manifest.webmanifest',
  './icon-192.png', './icon-512.png', './icon-maskable-512.png', './apple-touch-icon.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE).then((c) => c.addAll(APP_FILES)).then(() => self.skipWaiting()));
});

// Delete this app's caches from older versions. Other apps' caches are left alone.
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k.startsWith('teledtr-') && k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;                  // never cache anything but plain downloads
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;   // TELEDTR loads nothing from outside

  // Pages: try the network first (to pick up fixes), fall back to the cache offline.
  if (req.mode === 'navigate') {
    // Offline: the page itself if we have it (the camera lab is a page too), else the editor.
    event.respondWith(fetch(req).catch(() => caches.match(req, { ignoreSearch: true }).then((hit) => hit || caches.match('./index.html'))));
    return;
  }
  // Other files: cache first, then network (and remember what we fetched).
  event.respondWith(
    caches.match(req).then((hit) => hit || fetch(req).then((res) => {
      if (res.ok && res.type === 'basic') {
        const copy = res.clone();
        caches.open(CACHE).then((c) => c.put(req, copy));
      }
      return res;
    }))
  );
});

/* ---------------------------------------------------------------------------
   SUITE UPDATE CHECK (the same in every app's sw.js)
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
