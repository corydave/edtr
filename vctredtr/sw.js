/* =======================================================================
   VCTREDTR service worker - makes the app work offline and installable.

   How versioning works: index.html registers "sw.js?v=0.1.0". Bumping
   APP_VERSION in index.html changes that address, the browser installs
   this worker again, and the cache name below changes with it - so old
   files are thrown away and the new release is downloaded.
   ======================================================================= */
const VERSION = new URL(self.location.href).searchParams.get('v') || 'dev';
const CACHE = 'vctredtr-' + VERSION;

// The app's own files, saved at install time.
// index.html is the one-file edition (everything inside); index-online.html is
// the online edition, which also needs the fonts below.
const APP_FILES = ['./', './index.html', './index-online.html', './manifest.webmanifest', './icon-192.png', './icon-512.png',
  './icon-maskable-512.png', './apple-touch-icon.png', './favicon-32.png'];

// The included fonts (the fonts/ folder). They live in a cache of their own
// that is NOT thrown away with each new release, so an update does not
// download a megabyte of fonts again. Change FONTS_CACHE only when the
// font files themselves change.
const FONTS_CACHE = 'vctredtr-fonts-2';     // 2: the fonts became .woff files (0.9.0)
const FONT_FILES = [
  './fonts/atkinson-hyperlegible-400.woff', './fonts/atkinson-hyperlegible-700.woff',
  './fonts/montserrat-400.woff', './fonts/montserrat-700.woff', './fonts/poppins-400.woff',
  './fonts/poppins-700.woff', './fonts/comfortaa-400.woff', './fonts/comfortaa-700.woff',
  './fonts/fredoka-400.woff', './fonts/fredoka-700.woff', './fonts/oswald-400.woff',
  './fonts/oswald-700.woff', './fonts/anton-400.woff', './fonts/bebas-neue-400.woff',
  './fonts/playfair-display-400.woff', './fonts/playfair-display-700.woff', './fonts/merriweather-400.woff',
  './fonts/merriweather-700.woff', './fonts/abril-fatface-400.woff', './fonts/arvo-400.woff',
  './fonts/arvo-700.woff', './fonts/coustard-400.woff', './fonts/coustard-900.woff',
  './fonts/alfa-slab-one-400.woff', './fonts/holtwood-one-sc-400.woff', './fonts/bangers-400.woff',
  './fonts/bungee-400.woff', './fonts/luckiest-guy-400.woff', './fonts/righteous-400.woff',
  './fonts/lobster-400.woff', './fonts/press-start-2p-400.woff', './fonts/permanent-marker-400.woff',
  './fonts/pacifico-400.woff', './fonts/caveat-400.woff', './fonts/caveat-700.woff',
  './fonts/dancing-script-400.woff', './fonts/dancing-script-700.woff', './fonts/indie-flower-400.woff',
  './fonts/space-mono-400.woff', './fonts/space-mono-700.woff'
];

// The ONE outside file we allow: the pinned drawing engine (Paper.js). It is
// saved at install time too, so the app opens with no network afterwards.
// (The page checks its fingerprint - the "integrity" attribute - every time.)
const PAPER_URL = 'https://cdn.jsdelivr.net/npm/paper@0.12.18/dist/paper-core.min.js';
// The second allowed outside file: opentype.js, which reads letter outlines
// for "Turn into shapes". Also pinned and fingerprint-checked by the page.
const OPENTYPE_URL = 'https://cdn.jsdelivr.net/npm/opentype.js@1.3.4/dist/opentype.min.js';

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const c = await caches.open(CACHE);
    await c.addAll(APP_FILES);
    // If jsDelivr cannot be reached right now, the engine is saved the first time the page loads it instead.
    try { await c.add(new Request(PAPER_URL, { mode: 'cors', credentials: 'omit' })); } catch (_) { /* later */ }
    try { await c.add(new Request(OPENTYPE_URL, { mode: 'cors', credentials: 'omit' })); } catch (_) { /* later */ }
    // Fonts: fetched now (unless already saved by an earlier release) so every
    // font works offline. If this fails, each font is saved the first time it is used.
    try {
      const fc = await caches.open(FONTS_CACHE);
      const have = new Set((await fc.keys()).map((r) => new URL(r.url).pathname));
      const missing = FONT_FILES.filter((f) => !have.has(new URL(f, self.location.href).pathname));
      if (missing.length) await fc.addAll(missing);
    } catch (_) { /* later */ }
    await self.skipWaiting();
  })());
});

// Delete caches from older versions.
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k.startsWith('vctredtr-') && k !== CACHE && k !== FONTS_CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;                  // never cache anything but plain downloads
  const url = new URL(req.url);
  const sameSite = url.origin === self.location.origin;
  const isPaper = req.url === PAPER_URL || req.url === OPENTYPE_URL;   // the two pinned libraries
  if (!sameSite && !isPaper) return;                 // everything else: let the browser handle it

  // Pages: the network first (so every launch gets the newest version), and
  // the stored copy when there is no network. A fresh copy is kept for next time.
  if (req.mode === 'navigate') {
    // Two pages share this worker: index.html (the one-file edition, also what
    // "/" means) and index-online.html. Each is stored under its own name, so
    // opening one never replaces the stored copy of the other.
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
        // Font files go in the fonts cache, which outlives releases.
        caches.open(sameSite && url.pathname.includes('/fonts/') ? FONTS_CACHE : CACHE).then((c) => c.put(req, copy));
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
