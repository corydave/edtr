/* ============================================================================
   TXTEDTR service worker
   ============================================================================

   What it is for: letting an installed TXTEDTR open with no network at all.
   Installing a PWA gives it a window, an icon and file associations, but the
   browser still fetches index.html from the server every launch. This is the
   only thing that changes that.

   TWO STRATEGIES, ON PURPOSE
   --------------------------
   The document is fetched NETWORK FIRST, and only falls back to the cache when
   the network is unreachable. That matters for a file you edit often: the
   usual cache-first service worker will happily serve last week's index.html
   after you upload a new one, and you spend an afternoon wondering why your
   change did not take. Network first means online you always get exactly what
   you uploaded, and offline you get the last copy that reached this machine.

   Everything else - the icons, the manifest - is fetched CACHE FIRST, because
   those change roughly never and there is no reason to wait on them.

   VERSIONING
   ----------
   The version comes from the query string on this worker's own URL, which
   index.html sets from APP_VERSION. So bumping APP_VERSION is the whole ritual:
   the browser sees a new worker URL, installs it, and the activate step below
   deletes every cache that is not the current one.
   ========================================================================== */

const VERSION = new URL(self.location).searchParams.get("v") || "dev";
const CACHE = "txtedtr-v" + VERSION;

const SHELL = [
  "./index.html",
  "./manifest.webmanifest",
  "./icon-192.png",
  "./icon-512.png",
  "./icon-maskable-512.png"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE).then((cache) =>
      /* Deliberately not cache.addAll: that rejects as a whole if any single
         file is missing, which would leave the app with no offline support at
         all because one icon was not uploaded. Each file is allowed to fail on
         its own. */
      Promise.all(SHELL.map((url) => cache.add(url).catch(() => null)))
    ).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys()
      .then((names) => Promise.all(
        names.filter((name) => name !== CACHE).map((name) => caches.delete(name))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const request = event.request;

  /* Only ever interfere with plain reads of our own files. */
  if (request.method !== "GET") return;
  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;

  const isDocument = request.mode === "navigate"
    || url.pathname.endsWith("/")
    || url.pathname.endsWith(".html");

  if (isDocument) {
    event.respondWith(
      /* Built from the URL rather than passing the navigation Request through,
         and with cache: "no-store" - otherwise the browser's own HTTP cache can
         hand back a stale copy without ever asking the server, which defeats
         the entire point of going to the network first. Measured: without this,
         a freshly uploaded index.html does not reach the page. */
      fetch(url.href, { cache: "no-store", credentials: "same-origin" })
        .then((response) => {
          /* Keep the offline copy in step with what was just served. The
             response body can only be read once, hence the clone. */
          const copy = response.clone();
          caches.open(CACHE).then((cache) => cache.put(request, copy));
          return response;
        })
        .catch(() => caches.match(request)
          .then((hit) => hit || caches.match("./index.html")))
    );
    return;
  }

  event.respondWith(
    caches.match(request).then((hit) => hit || fetch(request).then((response) => {
      const copy = response.clone();
      caches.open(CACHE).then((cache) => cache.put(request, copy));
      return response;
    }))
  );
});
