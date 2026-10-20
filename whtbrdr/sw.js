/* =======================================================================
   WHTBRDR service worker - makes the app work offline and installable.
   (Same pattern as DSKEDTR's and VCTREDTR's sw.js.)

   How versioning works: index.html registers "sw.js?v=0.3.1". Bumping
   APP_VERSION in index.html changes that address, the browser installs
   this worker again, and the cache name below changes with it - so old
   files are thrown away and the new release is downloaded.

   Privacy: this worker only stores the app's own files (the page, the
   manifest and the icons; the fonts are inside the page). It never sees,
   stores or sends your boards: they stay in the page, in this browser.
   ======================================================================= */
const VERSION = new URL(self.location.href).searchParams.get('v') || 'dev';
const CACHE = 'whtbrdr-' + VERSION;

// The app's own files, saved at install time.
const APP_FILES = ['./', './index.html', './manifest.webmanifest', './icon.svg', './icon-192.png',
  './icon-512.png', './icon-maskable-512.png', './apple-touch-icon.png', './favicon-32.png'];

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const c = await caches.open(CACHE);
    await c.addAll(APP_FILES);
    await self.skipWaiting();
  })());
});

// Delete caches from older versions.
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k.startsWith('whtbrdr-') && k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;                  // never cache anything but plain downloads
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;   // anything from elsewhere: let the browser handle it

  // The page: the network first (so every launch gets the newest version),
  // and the stored copy when there is no network. A fresh copy is kept for next time.
  // (0.4.0: the online edition, index-online.html, is kept under its own name, so it never
  // takes the place of the offline edition that the app opens with.)
  if (req.mode === 'navigate') {
    const key = /index-online\.html$/.test(url.pathname) ? url.pathname : './index.html';
    event.respondWith(fetch(req).then((res) => {
      if (res.ok) { const copy = res.clone(); caches.open(CACHE).then((c) => c.put(key, copy)); }
      return res;
    }).catch(() => caches.match(key)));
    return;
  }
  // Other files (the manifest, the icons): the stored copy first, then the network
  // (and remember what was fetched).
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
