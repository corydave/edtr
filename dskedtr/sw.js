/* =======================================================================
   DSKEDTR service worker - makes the app work offline and installable.
   (Same pattern as VCTREDTR's sw.js.)

   How versioning works: index.html registers "sw.js?v=0.5.0". Bumping
   APP_VERSION in index.html changes that address, the browser installs
   this worker again, and the cache name below changes with it - so old
   files are thrown away and the new release is downloaded.

   Privacy: this worker only stores the app's own files and its four
   pinned libraries. It never sees, stores or sends your documents.
   ======================================================================= */
const VERSION = new URL(self.location.href).searchParams.get('v') || 'dev';
const CACHE = 'dskedtr-' + VERSION;

// The app's own files, saved at install time.
// index.html is the one-file edition (everything inside); index-online.html is
// the online edition, which also needs the fonts and the libraries below.
const APP_FILES = ['./', './index.html', './index-online.html', './manifest.webmanifest', './icon.svg', './icon-192.png',
  './icon-512.png', './icon-maskable-512.png', './apple-touch-icon.png', './favicon-32.png',
  './fonts/atkinson-hyperlegible-400.woff', './fonts/atkinson-hyperlegible-700.woff',
  './fonts/atkinson-hyperlegible-400-italic.woff', './fonts/atkinson-hyperlegible-700-italic.woff'];

// The only outside files allowed: the four pinned libraries the online
// edition loads. The page checks each one's fingerprint (integrity) every time.
const LIBRARIES = [
  'https://cdn.jsdelivr.net/npm/opentype.js@1.3.4/dist/opentype.min.js',
  'https://cdn.jsdelivr.net/npm/paper@0.12.18/dist/paper-core.min.js',
  'https://cdn.jsdelivr.net/npm/pdf-lib@1.17.1/dist/pdf-lib.min.js',
  'https://cdn.jsdelivr.net/npm/@pdf-lib/fontkit@1.1.1/dist/fontkit.umd.min.js'
];

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const c = await caches.open(CACHE);
    await c.addAll(APP_FILES);
    // If jsDelivr cannot be reached right now, each library is saved the first time the page loads it instead.
    for (const url of LIBRARIES) {
      try { await c.add(new Request(url, { mode: 'cors', credentials: 'omit' })); } catch (_) { /* later */ }
    }
    await self.skipWaiting();
  })());
});

// Delete caches from older versions.
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k.startsWith('dskedtr-') && k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;                  // never cache anything but plain downloads
  const url = new URL(req.url);
  const sameSite = url.origin === self.location.origin;
  const isLibrary = LIBRARIES.includes(req.url);
  if (!sameSite && !isLibrary) return;               // everything else: let the browser handle it

  // Pages: the network first (so every launch gets the newest version), and
  // the stored copy when there is no network. A fresh copy is kept for next time.
  if (req.mode === 'navigate') {
    // Two pages share this worker: index.html (the one-file edition, also what
    // "/" means) and index-online.html. Each is stored under its own name.
    const page = url.pathname.endsWith('/') ? './index.html' : '.' + url.pathname.slice(url.pathname.lastIndexOf('/'));
    event.respondWith(fetch(req).then((res) => {
      if (res.ok) { const copy = res.clone(); caches.open(CACHE).then((c) => c.put(page, copy)); }
      return res;
    }).catch(() => caches.match(page).then((hit) => hit || caches.match('./index.html'))));
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
