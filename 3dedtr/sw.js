/* =======================================================================
   3DEDTR service worker - makes the app work offline and installable.

   How versioning works: index.html registers "sw.js?v=0.1.0". Bumping
   APP_VERSION in index.html changes that address, the browser installs
   this worker again, and the cache name below changes with it - so old
   files are thrown away and the new release is downloaded.
   ======================================================================= */
const VERSION = new URL(self.location.href).searchParams.get('v') || 'dev';
const CACHE = '3dedtr-' + VERSION;

// The app's own files, saved at install time.
const APP_FILES = ['./', './index.html', './manifest.webmanifest', './icon-192.png', './icon-512.png',
  './icon-maskable-512.png', './apple-touch-icon.png', './favicon-32.png'];

// The 3D engine (the engine/ folder, about 3 MB). It lives in a cache of
// its own that is NOT thrown away with each new release, so an update does
// not download the engine again. Change ENGINE_CACHE only when the engine
// files themselves change (a new three.js version, say).
const ENGINE_CACHE = '3dedtr-engine-r186';
const ENGINE_FILES = [
  './engine/three.module.js', './engine/three.core.js',
  './engine/three-mesh-bvh.module.js', './engine/three-bvh-csg.module.js',
  './engine/addons/controls/OrbitControls.js', './engine/addons/controls/TransformControls.js',
  './engine/addons/exporters/STLExporter.js', './engine/addons/exporters/OBJExporter.js',
  './engine/addons/exporters/GLTFExporter.js', './engine/addons/loaders/STLLoader.js',
  './engine/addons/loaders/OBJLoader.js', './engine/addons/loaders/GLTFLoader.js',
  './engine/addons/utils/BufferGeometryUtils.js', './engine/addons/utils/SkeletonUtils.js',
  './engine/addons/geometries/RoundedBoxGeometry.js', './engine/addons/loaders/FontLoader.js',
  // Reads SVG drawings (loaded only when one is imported).
  './engine/addons/loaders/SVGLoader.js',
  // The video library (loaded only for video export; see make-mediabunny.sh).
  './engine/addons/mediabunny/mediabunny-3dedtr.min.js',
  // The Text shape's eight typefaces (see make-fonts.py): JSON, not JavaScript.
  './engine/fonts/sans.json', './engine/fonts/serif.json', './engine/fonts/slab.json',
  './engine/fonts/legible.json', './engine/fonts/rounded.json', './engine/fonts/display.json',
  './engine/fonts/script.json', './engine/fonts/stencil.json'
];

/**
 * Is this a complete engine file, worth keeping? A half-finished upload can
 * leave an empty or cut-off file on the server (or in a CDN such as
 * Cloudflare), and a missing one can come back as an HTML error page. Saving
 * any of those would keep the app broken even after the server is fixed.
 * Every engine file is a JavaScript module of more than 4 KB whose last
 * lines are its "export { ... }" list (sometimes followed by a comment),
 * so we check exactly that. The fonts (engine/fonts/*.json) are checked
 * differently: they must read as JSON and hold a set of letters.
 */
async function isWholeEngineFile(res) {
  if (!res || !res.ok || res.type !== 'basic') return false;
  if (/\/engine\/fonts\/[a-z]+\.json$/.test(new URL(res.url).pathname)) {
    try { const data = await res.clone().json(); return !!(data && data.glyphs && data.resolution); } catch (_) { return false; }
  }
  const type = res.headers.get('content-type') || '';
  if (!/javascript|ecmascript/i.test(type)) return false;
  const text = await res.clone().text();
  return text.length > 4096 && /export\s*\{[^}]*\}\s*;?\s*(\/\/[^\n]*\s*)*$/.test(text.slice(-20000));
}

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const c = await caches.open(CACHE);
    await c.addAll(APP_FILES);
    // The engine: fetched now (unless an earlier release already saved it)
    // so the app opens with no network from now on. If this fails, each
    // file is saved the first time the page loads it instead.
    try {
      const ec = await caches.open(ENGINE_CACHE);
      const have = new Set((await ec.keys()).map((r) => new URL(r.url).pathname));
      const missing = ENGINE_FILES.filter((f) => !have.has(new URL(f, self.location.href).pathname));
      // One at a time, and each one checked, so a bad file is simply left out.
      for (const f of missing) {
        const res = await fetch(f, { cache: 'no-store' });
        if (await isWholeEngineFile(res)) await ec.put(f, res);
      }
    } catch (_) { /* later */ }
    await self.skipWaiting();
  })());
});

// Delete caches from older versions (but keep the engine's own cache).
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k.startsWith('3dedtr-') && k !== CACHE && k !== ENGINE_CACHE).map((k) => caches.delete(k))))
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
  // Other files: cache first, then network (and remember what we fetched).
  event.respondWith(
    caches.match(req).then((hit) => hit || fetch(req).then(async (res) => {
      if (url.pathname.includes('/engine/')) {
        // Engine files go in the engine cache, which outlives releases -
        // but only once they have passed the check above.
        if (await isWholeEngineFile(res)) {
          const copy = res.clone();
          caches.open(ENGINE_CACHE).then((c) => c.put(req, copy));
        }
      } else if (res.ok && res.type === 'basic') {
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
