/* =======================================================================
   GAMEDTR service worker - makes the app work offline and installable.

   How versioning works: index.html registers "sw.js?v=0.1.0". Bumping
   APP_VERSION in index.html changes that address, the browser installs
   this worker again, and the cache name below changes with it - so old
   files are thrown away and the new release is downloaded.

   Privacy: this worker only ever fetches GAMEDTR's own files, from the
   server GAMEDTR came from. It never touches anything else.
   ======================================================================= */
const VERSION = new URL(self.location.href).searchParams.get('v') || 'dev';
const CACHE = 'gamedtr-' + VERSION;

// The app's own files, saved at install time. GAMEDTR is one HTML file plus
// its icons and manifest - there is nothing else to download.
const APP_FILES = ['./', './index.html', './manifest.webmanifest', './icon-192.png', './icon-512.png',
  './icon-maskable-512.png', './apple-touch-icon.png', './favicon-32.png'];

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const c = await caches.open(CACHE);
    await c.addAll(APP_FILES);
    await self.skipWaiting();            // take over straight away, no need to wait for a restart
  })());
});

// Delete caches left by older versions.
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k.startsWith('gamedtr-') && k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;                  // never cache anything but plain downloads
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;   // not ours: let the browser handle it

  // Pages: the network first (so every launch gets the newest version), and
  // the stored copy when there is no network. A fresh copy is kept for next time.
  if (req.mode === 'navigate') {
    event.respondWith(fetch(req).then((res) => {
      if (res.ok) { const copy = res.clone(); caches.open(CACHE).then((c) => c.put('./index.html', copy)); }
      return res;
    }).catch(() => caches.match('./index.html')));
    return;
  }
  // Other files (icons, the manifest): the stored copy first, then the network.
  event.respondWith(
    caches.match(req).then((hit) => hit || fetch(req).then((res) => {
      if (res.ok && res.type === 'basic') { const copy = res.clone(); caches.open(CACHE).then((c) => c.put(req, copy)); }
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
