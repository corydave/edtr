/* ===========================================================================
 * VIDEDTR service worker - OPTIONAL
 * ---------------------------------------------------------------------------
 * The editor works perfectly without this file. Drop it next to index.html
 * and two things become possible:
 *
 *   1. Chrome and Edge offer a proper "Install" button, rather than making you
 *      dig for "Create shortcut" in the menu.
 *   2. The app opens with no network at all - on a plane, in a classroom with
 *      the wifi down, anywhere.
 *
 * It is deliberately tiny. There is exactly one page to cache, and the page
 * itself never talks to the network, so there is no data layer to think about.
 *
 * ---------------------------------------------------------------------------
 * WHY THIS FILE LOOKS DIFFERENT FROM THE USUAL EXAMPLE (v3.1)
 * ---------------------------------------------------------------------------
 * Up to v3.0 this worker did the textbook thing: cache the page on install,
 * then answer every request from the cache, and rely on the CACHE name being
 * bumped by hand to push a new version out. Three things went wrong with that
 * on a real installed copy, and all three had to be fixed together:
 *
 *   1. `cache.addAll()` fetches go through the browser's ORDINARY HTTP cache.
 *      So on install, the "fresh" copy it stored could be the stale one the
 *      browser already had on disk. A new worker would install, congratulate
 *      itself, and cache the old page. Fixed by fetching every shell file with
 *      `cache: "reload"`, which forces a real trip to the server.
 *
 *   2. Cache-first with no revalidation means an installed app NEVER notices a
 *      new page unless this file's own bytes change. Forgetting to bump a
 *      constant silently shipped nothing. Fixed by serving the page
 *      stale-while-revalidate: you still get the instant, offline-capable
 *      answer from the cache, and a fresh copy is quietly fetched behind it
 *      for next time.
 *
 *   3. There was no way for the page to ASK. Its Content-Security-Policy sets
 *      `connect-src 'none'` - on purpose, so the editor can never phone home -
 *      which also means the page itself cannot fetch anything, not even its
 *      own newer self. A service worker runs under its own policy, so it can.
 *      Fixed by the `message` handler at the bottom: the page asks, this file
 *      fetches, and the answer comes back over a MessagePort.
 *
 * Because content is now refreshed rather than cache-busted, the cache name no
 * longer carries a version number. It is a stable box that gets new contents.
 * ======================================================================== */

const CACHE = "videdtr";

// The page under both of the addresses it can be reached at. A link written as
// ".../index.html" is a DIFFERENT cache key to ".../", and someone will always
// have bookmarked it that way.
const APP_SHELL = ["./", "./index.html"];

/**
 * Fetch one shell file straight from the server and store it.
 *
 * `cache: "reload"` is the important bit: it tells the browser to ignore
 * whatever it already has on disk for this URL and go and ask properly. That
 * is the difference between shipping an update and shipping the illusion of
 * one.
 *
 * Returns the response text when it worked, or null when it did not - the
 * caller decides whether a failure matters. Offline, it always fails, and
 * that is fine: we simply keep what we already had.
 */
async function fetchAndStore(url) {
  const response = await fetch(url, { cache: "reload" });
  if (!response || !response.ok) return null;

  // A Response body can only be read once, so clone before storing.
  const cache = await caches.open(CACHE);
  await cache.put(url, response.clone());
  return await response.text();
}

/** Pull the version string out of the page's own source. */
function versionOf(html) {
  if (typeof html !== "string") return null;
  const found = html.match(/const APP_VERSION\s*=\s*"([^"]{1,32})"/);
  return found ? found[1] : null;
}

self.addEventListener("install", (event) => {
  // Take over as soon as we are ready rather than waiting for every tab to
  // close, which for a single-page tool is just confusing.
  self.skipWaiting();
  event.waitUntil(
    // One failure must not abort the install, or a flaky connection would
    // leave the app with no offline copy at all.
    Promise.all(APP_SHELL.map((url) => fetchAndStore(url).catch(() => null)))
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys()
      .then((names) => Promise.all(
        // This also sweeps up the old version-stamped caches from v3.0 and
        // earlier ("videdtr-v3-0" and friends), which are now dead weight.
        // ...but only this app's own: on a site shared with the other apps
        // (EDTR Studio) their caches must be left alone.
        names.filter((n) => n.startsWith('videdtr') && n !== CACHE).map((n) => caches.delete(n))
      ))
      .then(() => self.clients.claim())
  );
});

/**
 * Answering requests.
 *
 * The page itself gets STALE-WHILE-REVALIDATE: the cached copy is handed back
 * immediately, so the app opens instantly and works with no network, and at
 * the same time a fresh copy is fetched in the background and stored for next
 * launch. You are therefore at most one launch behind, automatically, with no
 * version numbers to remember.
 *
 * Everything else - the muxer libraries, the icons - gets CACHE-FIRST, because
 * those URLs are pinned to an exact version and never change underneath us.
 */
self.addEventListener("fetch", (event) => {
  const request = event.request;
  if (request.method !== "GET") return;

  // Only ever touch our own origin. Cross-origin requests (the pinned CDN
  // muxers) fall through to the cache-first branch below, which is safe
  // because their URLs contain their version.
  const isDocument = request.mode === "navigate" || request.destination === "document";

  if (isDocument) {
    event.respondWith(staleWhileRevalidate(request, event));
    return;
  }

  event.respondWith(
    caches.match(request).then((hit) => {
      if (hit) return hit;
      return fetch(request).then((response) => {
        // Stash anything that came back cleanly, so the muxer libraries are
        // there next time even if you are offline.
        if (response && response.status === 200 && response.type !== "error") {
          const copy = response.clone();
          caches.open(CACHE).then((cache) => cache.put(request, copy)).catch(() => {});
        }
        return response;
      }).catch(() => hit);
    })
  );
});

/**
 * Hand back the cached page now; quietly fetch a fresh one for next time.
 *
 * If there is nothing cached yet (a first visit), we have to wait for the
 * network, which is exactly what a first visit does anyway.
 */
async function staleWhileRevalidate(request, event) {
  const cache = await caches.open(CACHE);
  const hit = await cache.match(request);

  const fromNetwork = fetch(request, { cache: "reload" }).then((response) => {
    if (response && response.ok) cache.put(request, response.clone()).catch(() => {});
    return response;
  }).catch(() => null);

  if (hit) {
    // Do not make the page wait on the background fetch - but DO tell the
    // browser to keep this worker alive until it finishes, or it may be shut
    // down the moment the page has its answer and the refresh never lands.
    event.waitUntil(fromNetwork);
    return hit;
  }
  const fresh = await fromNetwork;
  return fresh || new Response("Offline and nothing cached yet.", { status: 503 });
}

/**
 * The page asking "is there a newer me?".
 *
 * The page cannot answer this itself - its CSP forbids it from fetching
 * anything at all - so it posts a message here and we do the asking. We reply
 * over the MessagePort that came with the request, which keeps the exchange
 * tied to the one question rather than broadcast to every open tab.
 *
 * Note we re-fetch and re-store the shell BEFORE replying. That way, by the
 * time the page decides to reload, the new bytes are already in the cache and
 * the reload is guaranteed to land on the new version rather than racing it.
 */
self.addEventListener("message", (event) => {
  const data = event.data;
  if (!data || data.type !== "videdtr-check-update") return;

  const port = event.ports && event.ports[0];
  if (!port) return;

  event.waitUntil((async () => {
    try {
      // "./index.html" is the copy we can read a version out of. Refresh the
      // "./" key too so whichever address the app was opened at is current.
      const html = await fetchAndStore("./index.html");
      await fetchAndStore("./").catch(() => null);

      if (html === null) {
        port.postMessage({ status: "offline" });
        return;
      }
      port.postMessage({ status: "ok", version: versionOf(html) });
    } catch (_) {
      port.postMessage({ status: "offline" });
    }
  })());
});
