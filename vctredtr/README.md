# VCTREDTR

A vector drawing app that runs entirely in the browser, built around **Merge Shapes**: Union, Combine, Fragment, Intersect and Subtract, the way PowerPoint does them. Part of the TXTEDTR / PDFEDTR / IMGEDTR / SNDEDTR / VIDEDTR / SCRNCSTR family. Its family colour is violet, `#5b21b6`.

## Files

| File | What it is |
|---|---|
| `index.html` | **The app** - the one-file edition, and the one vctredtr.app serves: HTML, CSS, JavaScript, the drawing engine, opentype.js and every font, all in one file (about 2 MB). It installs and updates on the website, and the same file works from a USB stick or a double-click with no internet. **Made by `build-offline.py` - never edit it by hand.** |
| `index-online.html` | **The source**, and the online edition: the same app, loading Paper.js and opentype.js from jsDelivr and its fonts from `fonts/`. Edit this file, then run `build-offline.py`. |
| `build-offline.py` | Makes `index.html` from `index-online.html`, `vendor/` and `fonts/`: `python3 build-offline.py` (Python 3 only, nothing to install). Run it after every change to `index-online.html`. |
| `vendor/` | Exact copies of the two libraries `index-online.html` loads from jsDelivr (Paper.js, opentype.js) and their MIT licences. `build-offline.py` puts them inside `index.html`, after checking their fingerprints against `index-online.html`. |
| `sw.js` | Service worker: offline support, and it keeps a copy of the drawing engine |
| `manifest.webmanifest` | Makes the app installable (and lets the installed app open `.svg` and `.vctredtr` files) |
| `icon-192.png`, `icon-512.png`, `icon-maskable-512.png`, `apple-touch-icon.png`, `favicon-32.png` | App icons, drawn by `make-icons.py` |
| `icon.svg` | The mark as an SVG (the same drawing as the top bar and the shared block's `SUITE_MARKS`) |
| `make-icons.py` | Redraws every PNG icon: `python3 make-icons.py` (needs Pillow) |
| `fonts/` | The included fonts for text (`.woff`, Latin letters, regular and bold where there is one) and `LICENSES.txt`, every font's licence. Upload the folder with the app. |
| `SPEC.md` | What the app does and why, and what comes later |
| `CHANGELOG.md` | Long-form release notes |

## The drawing engine

The shapes and the Merge Shapes geometry come from **Paper.js** (MIT licence), `paper@0.12.18`, the `paper-core` build (no PaperScript, so the page never needs `eval`). It is loaded from jsDelivr with a Subresource Integrity hash, so the browser refuses it if one byte differs. The service worker saves it at install time, so the app works offline after the first visit.

**It never changes by itself, so nothing needs updating to keep up with it.** The page asks for one exact version and checks its fingerprint, so a new Paper.js release has no effect on VCTREDTR until you choose to move to it. Paper.js changes rarely (0.12.18 is its current release), so there is normally no reason to.

To upgrade Paper.js, change the version in **four** places together: the `<script>` tag in `index-online.html` (URL and `integrity` hash), `PAPER_URL` in `sw.js`, the About text, and `vendor/paper-core.min.js` (then run `build-offline.py`, which refuses to build if the vendor copy and the hash disagree).

## Turning text into shapes (opentype.js)

To merge text with shapes, the letters' outlines are read out of the font file by **opentype.js** (MIT licence), `opentype.js@1.3.4`, pinned and fingerprint-checked the same way as Paper.js. It is only downloaded the first time text is turned into shapes (the service worker also saves it at install). The text becomes one compound path, laid out exactly as Paper.js draws the text (baseline, line spacing, alignment, then the text's own turn and scale). Only the included fonts can be turned: a web page cannot read the fonts built into the computer. That is also why the fonts are `.woff` rather than `.woff2`: opentype.js cannot unpack WOFF2. Upgrading it works like Paper.js: `OPENTYPE_URL` / `OPENTYPE_SRI` in `index-online.html`, `OPENTYPE_URL` in `sw.js`, and `vendor/opentype.min.js`.

## Project files (.vctredtr)

- **Save project** (Ctrl+Shift+S) keeps everything editable. The file is plain JSON: the artboard settings plus the drawing in Paper.js's own JSON form. Undo history is not included.
- **Open** accepts `.vctredtr` files (also drag and drop, and "Open with" in the installed app). Every part is checked before anything is replaced: the format name, sensible numbers, and only the kinds of object a drawing is made of (layers, groups, paths, compound paths, text, colours and gradients). Anything else, such as a picture or a link to an outside file, means the file is refused.

## Shape tools, symbols and artboards (0.13)

- **Shape tools** (Inspector): Offset path, Simplify, Blend and Make symbol. **Shape builder** (K) joins or deletes the pieces of overlapping shapes by dragging across them.
- **Symbols** are groups that keep their own place, size and turn (`applyMatrix = false`) and share their insides: Edit symbol, then Done editing, updates every copy.
- **Artboards:** the first is always at 0, 0 (`doc.width` x `doc.height`); more live in `doc.boards` and are saved in projects. Export can save every artboard at once.
- **Mesh fills** (Fill > Mesh) keep four corner colours in the shape's data and are drawn (and exported) as a smooth picture cut to the shape.

## Opening SVG files

An SVG can carry scripts, links and event handlers. Before Paper.js sees one, VCTREDTR rebuilds it from an **allow-list** of elements (`svg`, `g`, `path`, `rect`, `circle`, `ellipse`, `line`, `polyline`, `polygon`, `text`, `tspan`, `defs`, gradients, `stop`, `title`, `desc`) and attributes (geometry, fill, stroke, opacity, font and gradient settings). Everything else is left out: `<script>`, `<foreignObject>`, `<image>`, `<use>`, `<style>`, every `href`, every `on...` handler, and any `url(...)` that does not point inside the file (`url(#id)`).

## Running it

- **Hosted:** upload the folder to an HTTPS server (vctredtr.app). Visitors get `index.html`, the one-file edition: it installs, works offline once visited, and checks for updates. Upload `index-online.html`, `sw.js`, `fonts/` and the icons too: the online edition needs the fonts, and the service worker keeps both pages for offline use (each under its own name). The service worker and install button only work over `https://` (or `localhost`).
- **From a file:** `index.html` on its own, anywhere - a USB stick, an email attachment, a computer that has never been online. No network, no other files. It shows a small "o" beside its version number, has no updates to fetch (copy the new `index.html` to update), and its rule book allows no outside addresses at all. (`index-online.html` opened from a file needs the internet, and its exports cannot carry the fonts.)
- **Why one file is the main edition:** it never depends on jsDelivr being reachable, and the browser only fetches it again when it has changed. The online edition downloads less the very first time (about 0.4 MB plus the fonts it uses), which is its one advantage.

## Pictures

Pictures placed in a drawing (PNG, JPEG, WebP, GIF, opened, dropped or pasted) are redrawn onto a canvas first, so only the pixels go in: hidden details such as the camera, date and GPS location are left behind. They are shrunk to at most 2048 px across (`MAX_PICTURE_SIDE`). A project stores them inside itself as picture data; `checkPaperJSON` refuses a project whose picture points anywhere else. The SVG importer still leaves out `<image>` entirely.

## Fonts

The Font box lists five fonts built into every computer, then 27 included fonts, grouped (sans serif, serif, slab serif, display, handwriting, monospace). The list lives in `FONTS` near the top of the script; each included font names its CSS family, its file name and its weights.

- **Adding a font:** put `fonts/<file>-400.woff` (and `-700` for a bold) in the folder, add one `incl(...)` line to `FONTS`, add the files to `FONT_FILES` in `sw.js` and bump `FONTS_CACHE` there, and add its licence to `fonts/LICENSES.txt`. Only fonts whose licence allows sharing them (SIL OFL, Apache) can be included. The files here are Fontsource's Latin subsets of the Google Fonts releases (`npm pack @fontsource/<name>`, then `files/<name>-latin-<weight>-normal.woff`), and rebuild `index.html` so the one-file edition has the new font too.
- **Rockwell** is a paid Monotype font and cannot be included. Macs and Microsoft Office have it; elsewhere Arvo, included, shows instead.
- The service worker saves every font at install, in a cache of its own (`FONTS_CACHE`) that survives app updates, so new releases do not download the fonts again.
- The canvas does not wait for a font file, so the app loads a font before drawing with it and redraws the text when it arrives (`loadDrawingFonts`).
- PNG export draws an SVG into a picture, and a picture cannot use the page's fonts, so exports (PNG, Copy as PNG, SVG files) carry the included fonts they use (`embeddedFontCSS`). The SVG code view and Copy SVG code leave them out, to stay readable.

## Releasing a new version

1. Bump `APP_VERSION` near the top of the script in `index-online.html` (keep the line as `const APP_VERSION = '...'`: the update check reads it).
2. Add the release to the `CHANGELOG` table in `index-online.html` **and** to `CHANGELOG.md`.
3. Run `python3 build-offline.py` to make the new `index.html`.
4. Upload. The new version number changes the service worker address, which clears the old cache.

## Privacy and security notes

- The Content-Security-Policy in both editions sets `connect-src 'self' data: blob:`, so the page cannot send data to other servers. It has no `'unsafe-eval'`.
- The only outside code is Paper.js, pinned and hash-checked (see above).
- Fonts come from the app's own `fonts/` folder, not a font service (the CSP's `font-src 'self' data:` would block one anyway). Exports pack the fonts they use inside the file, as `data:` URLs.
- Copying shapes keeps their full details in memory only. What goes on the system clipboard is SVG code, and SVG code pasted from anywhere else goes through the same cleaner as an opened file.
- Exported PNGs are drawn fresh from the vectors, so they carry no metadata. Exported SVGs leave out the app's own notes about each shape (`data-paper-data`).
