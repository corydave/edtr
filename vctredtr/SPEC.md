# VCTREDTR - v1 Spec

A browser-only vector drawing app. It is **not** an Illustrator or Figma replacement. The job it is built for: *make simple vector art by drawing shapes and merging them (the PowerPoint Merge Shapes trick), then get it onto a slide, into a document or into code.* It exists because Google Slides has no Merge Shapes.

Part of the tool family: TXTEDTR, PDFEDTR, IMGEDTR, SNDEDTR, VIDEDTR, SCRNCSTR, VCTREDTR. Family colour: violet `#5b21b6` (9.0:1 with white); dark-mode text `#c4b5fd`.

---

## 1. Principles

1. **Security and privacy first.** Every drawing stays on the device. No uploads, no analytics, no accounts. The Content-Security-Policy blocks the page from sending data anywhere. SVG files are rebuilt from an allow-list before use; project files are checked before they replace anything.
2. **Merge Shapes is the headline.** It is always at the top of the Inspector, it has its own Help tab, and pick order is always visible.
3. **Everything stays editable.** Shapes are objects; rectangles, polygons, stars and shields stay "live" until their points are edited or they are merged.
4. **Beginner-readable code.** One `index.html` (HTML + CSS + JS), vanilla JavaScript, heavily commented. The one library (Paper.js) is pinned and hash-checked.
5. **Accessible.** Every action reachable from the keyboard (including drawing: Enter adds a shape, the Layers list picks shapes, arrow keys move them), visible focus, ARIA labels, light/dark, reduced motion.
6. **Family conventions.** See `_edtr-suite/SUITE-STANDARD.md`: the IMGEDTR/PDFEDTR editor layout (tool rail, canvas, Inspector), the top bar's right-hand end, the help panel, the splash, crash backups, install and update check.

## 2. Layout

- Top bar: logo (opens More apps), New, Open, Save project | Undo, Redo | zoom out, zoom %, zoom in, fit | SVG code, Copy as PNG, **Export** | Install, Inspector, Theme, Help, Settings.
- Tool rail (left): Select, Edit points | Rectangle, Ellipse, Polygon, Star, Shield (opens a flyout of styles), Line | Pen, Pencil, Text | Eyedropper, Hand.
- Canvas: the artboard (white, a colour, or a checkerboard when see-through) on a grey workspace.
- Inspector (right): Layers list, action bar, then fold-open property sections.
- Status bar (bottom, like SNDEDTR and VIDEDTR): pointer X/Y, what is selected and its size, the artboard size.
- Phones: the rail runs along the bottom, and the Inspector opens as a sheet above it (as in IMGEDTR); the drawing re-fits.
  - The sheet has a grab handle (0.12.0, as in DSKEDTR): rows are canvas | sheet | rail, so dragging the handle resizes the canvas instead of covering it. Open height starts at a third of the screen, 120px to (screen height - 220px), saved as `settings.sheet` (a share of the screen). Closed = just the 29px handle row; tap or the Inspector button toggles. Keyboard: `role="separator"`, Up/Down 8%, Home closes, End tallest, Enter/Space toggle. Code: `applySheet()`, `setSheetOpen()`.

## 3. Merge Shapes rules

| Operation | Paper.js | Result |
|---|---|---|
| Union | `unite`, in pick order | One shape: the outline around all of them |
| Combine | `exclude`, in pick order | One shape with holes where an even number overlap |
| Fragment | intersect + subtract of every pair | One shape per region (islands split apart); each keeps the colour it showed |
| Intersect | `intersect`, in pick order | Only where all of them overlap (a message if nothing is left) |
| Subtract | `subtract`, in pick order | The first shape with every other one cut out |

- Needs two or more mergeable shapes (closed paths or compound paths). Others in the selection are left alone, and the toast says how many.
- The result takes the first shape's fill, outline and opacity (gradients are rebuilt to fit the new shape), goes where the first shape was in the stack, and is selected. One undo step undoes the whole merge and picks the originals again.

## 4. Files

- **Open:** `.svg` (cleaned first; into an empty drawing it becomes the drawing at the SVG's own size, otherwise it arrives as a group in the middle of the view) and `.vctredtr` projects.
- **Paste:** shapes copied in VCTREDTR (full detail), or SVG code from anywhere (cleaned).
- **Export:** PNG 1x-4x or SVG, whole artboard or selection only, with a title and description. **Copy as PNG** for pasting onto slides.
- **Save project:** `.vctredtr` JSON (format name, version, artboard, Paper.js JSON of the drawing).

## 4b. Perfect shapes and tessellation (0.2)

- A click (or Enter) makes a perfect shape; a drag stretches; Shift+drag keeps it perfect.
- Polygons and stars remember whether they are perfect (`data.shape.regular`) and stay that way through changes to their sides or points, until stretched. Make regular restores them.
- Moving shapes snaps their corners onto other shapes' corners, so perfect hexagons, triangles and squares tile with shared edges.

## 4c. Shields (0.6)

- One Shield tool (D), nine styles: Classic, Heater, Pointed, Round, Arched, Dipped, Notched, Peaked, Scalloped. Each is SVG path data in a 100 x 120 box, in one table (`SHIELD_STYLES`); adding a style is one line there.
- The rail button picks the tool and opens a flyout of the styles (a radio group: arrow keys, Enter, Escape). The button then shows the chosen style. D picks the tool; D again opens the flyout.
- Stored as `data.shape = { type: 'shield', shield: '<style>' }`. The Inspector's Shield section (same grid) switches a drawn shield's style, keeping its box. A style name from a file is checked against the table's own keys; anything unknown becomes Classic.
- A click drops a shield in its natural proportions; a drag stretches; Shift+drag keeps its proportions.

## 4d. Dragging layers (0.7)

- Each Layers row starts with a dotted grip. Dragging it (mouse, pen or finger) moves the row; with a mouse or pen the name drags too, after 5 px of movement, so a click still picks. A finger on the name scrolls the list.
- A picked row brings every picked row with it; an unpicked row moves alone and the selection is left as it was (pick order matters for merges).
- A line shows the drop point, the list scrolls near its edges, Escape cancels, and the drop is one undo step. Alt+Up/Down on a row remains the keyboard way.

## 4e. Fonts (0.8)

- `FONTS` holds 5 system font stacks (keys unchanged since 0.1) and 27 included fonts in `fonts/` (Latin `.woff2`, 400 and the font's bold where it has one). Grouped in the Font box with `<optgroup>`; a sample line shows the font.
- Included fonts load from the app's own origin only (CSP `font-src 'self' data:`), are precached by the service worker in `FONTS_CACHE` (kept across releases), and are loaded with `document.fonts.load` before the canvas draws with them; text is re-measured when they arrive.
- Exports pack used fonts as `data:` @font-face rules (PNG, Copy as PNG, SVG files).
- Rockwell: system font only (not licensable); Arvo is its stand-in and is what exports pack.
- Bold uses the font's real bold (700, or 900 for Coustard); one-weight fonts disable Bold.

## 4f. Text to shapes, Pad contents, offline edition (0.9)

- Merge Shapes accepts text: `mergeShapes` turns selected text into compound paths (`textsToShapes`, section 13b) in pick order, then merges; one undo step, reverted if the merge fails. `convertSelectedText` (button, Ctrl+Shift+O) does the conversion alone.
- Outlines: opentype.js 1.3.4 (jsDelivr, SRI, lazy-loaded, precached) parses the included `.woff` font files; lines laid out on baselines `leading` apart, shifted for centre/right, then `text.matrix` applied. System fonts are refused with an explanation; Rockwell uses Arvo. Default font for new text: Montserrat.
- Pad contents: artboard = union of visible items' stroke bounds + `settings.padding` (default 10, 0-2000) on every side; drawing moved so the margin starts at 0, 0. Fit to drawing = padding 0.
- Offline edition: `build-offline.py` inlines Paper.js and opentype.js (verified against the SRI hashes in index.html), embeds fonts in `VCTR_EMBEDDED.fonts`, removes jsDelivr from the CSP, drops manifest/icons. The app reads `VCTR_EMBEDDED` for fonts and export packing, skips the service worker, and labels itself offline.

## 4g. Letter spacing and collapsed sections (0.10)

- Text keeps `data.tracking` (% of font size, -50 to 200). `addLetterSpacing` wraps Paper's `PointText._draw` / `_getBounds`: native `ctx.letterSpacing` where supported (widths measured before it is switched on, since Paper measures on the same context), per-letter placement otherwise. The gap follows every letter, the last one too, matching CSS and opentype.js (`letterSpacing` option in ems).
- SVG export sets `letter-spacing` on each `<text>` (matched to text items in order). The text editor overlay copies it.
- Inspector sections are closed by default; their open state is `settings.openSections`, saved in localStorage.

## 4h. Editions (0.10.1)

- `index.html` is the one-file edition, built by `build-offline.py` from the source `index-online.html`; it is what the site serves. It keeps the manifest and service worker, so it installs and updates on the website, and works from a file with no network.
- `sw.js` stores each page under its own name (a visit to one never replaces the other), precaches both, and checks for updates against `index.html`.

## 4i. Curved text, Shapes, Repeat, Outline to shape, Pictures (0.11)

- Text curve: `data.curve` (-100..100). `textLayout(item)` (section 4) returns every glyph's position and turn (cached by content, font, spacing, curve, leading, alignment); the wrapped `_draw` / `_getBounds`, SVG export (per-letter `<tspan x y rotate>`, multi-line straight text as one `<tspan>` per line) and Turn into shapes (per-glyph opentype outlines placed by the layout) all use it. Arc: the widest line's width spans `|curve|/100` of a full turn; all lines share the centre.
- Shapes tool (`symbol`, U): `SYMBOL_SHAPES` (100 x 100 path data), sharing the gallery code with shields (`GALLERIES`, `galleryGrid`, `openGallery`). `data.shape = { type: 'symbol', symbol }`.
- Repeat around a centre: `repeatAround()` clones the selection `count - 1` times, turned (`turnItem`) or just moved round a centre `distance` below the selection's middle.
- Outline to shape (section 13c): flatten, offset both sides by half the stroke width with the item's joins and caps, `resolveCrossings`; closed paths make a ring (outer XOR inner). Merge Shapes converts open outlined paths first.
- Pictures (section 16b): Raster items from PNG/JPEG/WebP/GIF, redrawn through a canvas (metadata dropped), max 2048 px. Projects accept `Raster` only with a `data:image/(png|jpeg|webp|gif);base64,` source. Clip: a clipped Group whose first child (the top picked shape; text is converted first) is the mask; its look is kept in `data.maskLook` and restored on Unclip/Ungroup.

## 5. Later (not in 0.1)

- **Outline stroke** (turn a line's thickness into a filled shape, so lines can be merged).
- **Offset path** and **simplify path** commands.
- **Repeat around a centre** (radial copies) for flowers, gears and mandalas.
- Symbols, multiple artboards, blend, mesh gradients, a shape-builder tool.
