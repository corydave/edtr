/* =========================================================================
   EDTR Studio - service worker (offline copy of the Studio itself)
   -------------------------------------------------------------------------
   Keeps a copy of the Studio page and its icons so it opens with no
   internet. The APPS are not handled here: each app has its own service
   worker in its own folder, which answers for it.

   Two rules that matter because every app shares this one site:
     1. Only answer for addresses inside the Studio's own folder. A request
        for anything else (an app's files) passes straight through.
     2. Only ever delete caches whose names start with "edtr-studio-". The
        apps' caches live on this same site and must never be touched.

   Updating: the page registers sw.js?v=<STUDIO_VERSION>, so a new version
   of the Studio installs a fresh worker, which refreshes the copy.
   ========================================================================= */
const VERSION = new URL(self.location.href).searchParams.get('v') || 'dev';
const CACHE = 'edtr-studio-' + VERSION;
const SCOPE = new URL('./', self.location.href).href;          // e.g. https://edtrapps.com/create/
const FILES = ['./', './index.html', './manifest.webmanifest', './icon.svg', './icon-192.png', './icon-512.png'];

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE).then((c) => c.addAll(FILES)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      // Rule 2: only the Studio's own old copies.
      .then((keys) => Promise.all(keys.filter((k) => k.startsWith('edtr-studio-') && k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET' || !req.url.startsWith(SCOPE)) return;   // Rule 1: not ours - let it pass
  if (req.mode === 'navigate') {
    // The page: the newest from the network when online, the saved copy when not.
    event.respondWith(
      fetch(req).then((res) => {
        if (res.ok) { const copy = res.clone(); caches.open(CACHE).then((c) => c.put('./index.html', copy)); }
        return res;
      }).catch(() => caches.match('./index.html'))
    );
    return;
  }
  // Icons and the manifest: the saved copy first.
  event.respondWith(caches.match(req).then((hit) => hit || fetch(req)));
});
