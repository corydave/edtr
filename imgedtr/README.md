# IMGEDTR

A lightweight image editing and annotation tool that runs entirely in the browser. Part of the TXTEDTR / PDFEDTR / SCRNCSTR / VIDEDTR / SNDEDTR / VCTREDTR family.

## Files

| File | What it is |
|---|---|
| `index.html` | The whole app: HTML, CSS and JavaScript in one file |
| `sw.js` | Service worker: offline support and the HEIC-library cache |
| `manifest.webmanifest` | Makes the app installable |
| `icon-192.png`, `icon-512.png` | Placeholder icons - replace with your own (same names and sizes) |
| `SPEC.md` | The v1 spec and build phases |
| `CHANGELOG.md` | Long-form release notes |

## Project files (.imgedtr)

- **Save project** (Ctrl+Shift+S) keeps everything editable. The file is plain JSON: the document plus each picture as a PNG data URL. Undo history is not included.
- **Open** accepts `.imgedtr` files (also drag-and-drop, and "Open with" in the installed app). Every value is validated before anything on the canvas is replaced.
- A project keeps the original pixels under Redact boxes. Share exported images, not project files.

## Running it

- **Hosted (recommended):** upload all files to one folder on an HTTPS server. The service worker and install button only work over `https://` (or `localhost`).
- **Straight off a disk:** double-clicking `index.html` works for editing, but there is no offline caching or install option.

## Releasing a new version

1. Bump `APP_VERSION` near the top of the script in `index.html`.
2. Add the release to the `CHANGELOG` table in `index.html` **and** to `CHANGELOG.md`.
3. Upload. The new version number changes the service worker address, which clears the old cache.

## Privacy and security notes

- A Content-Security-Policy in `index.html` sets `connect-src 'self'`, so the page cannot send data to other servers.
- The only outside code is the HEIC converter, pinned to `heic-to@1.5.2` with a Subresource Integrity hash. If you ever upgrade it, update the URL and hash in `HEIC_LIB` (in `index.html`) and `HEIC_PREFIX` (in `sw.js`) together. The CSP's `'unsafe-eval'` and `'wasm-unsafe-eval'` entries exist only for that library.
- Exports are re-encoded from a canvas, so EXIF metadata (camera, GPS) never survives.
