# IMGEDTR - v1 Spec

A lightweight, browser-only image editing and annotation tool. It is **not** a Photoshop or Photopea replacement. The job it is built for: *take a screenshot or photo, mark it up, clean it up, and get it where it is going.*

Part of the tool family: TXTEDTR, PDFEDTR, SCRNCSTR, VIDEDTR, SNDEDTR, IMGEDTR, VCTREDTR.

---

## 1. Principles

1. **Security and privacy first.** Every pixel stays on the device. No uploads, no analytics, no accounts. A Content-Security-Policy blocks the page from sending data anywhere (`connect-src 'self'`), so "nothing leaves your computer" is enforced by the browser, not just promised.
2. **Everything is an object.** Images, arrows, text and shapes are separate, editable layers. Nothing is "burned in" until export. Undo/redo, crop and re-editing all fall out of this.
3. **Non-destructive.** Crops, erasing and transforms are stored as settings on a layer and can be changed or reversed later.
4. **Beginner-readable code.** One `index.html` (HTML + CSS + JS), vanilla JavaScript, heavily commented.
5. **Accessible.** Every tool reachable by keyboard, visible focus, ARIA labels, respects light/dark and reduced motion.
6. **Family conventions.** Installable PWA (`index.html`, `sw.js`, `manifest.webmanifest`), version badge beside the wordmark, info panel with Keyboard shortcuts / About / Changelog tabs, per-shortcut on/off switches, inlined Lucide-style icons, bare app name in `<title>` and manifest.

## 2. Canvas and documents

- Opening the app shows a **start screen**, not a blank canvas: Paste, Open, drag-and-drop, or New blank canvas (size presets, background color or transparent).
- **Paste / open into the empty app:** the canvas takes the image's exact pixel size.
- **Paste / open when a document is open:** the image arrives as a new image layer, centered, scaled down to fit if it is larger than the canvas. The canvas never resizes by surprise.
- **Canvas size command:** set size exactly, add padding, or "fit to contents."
- **Halve size** one-click for 2x (high-DPI) screenshots.
- **Zoom is separate from pixel size:** zoom-to-fit, 100%, zoom in/out, pan (Space+drag, middle mouse, or trackpad).
- Very large images (over 8000 px on a side) are downscaled on load with a notice.

## 3. Importing

- Open (file picker), drag-and-drop, clipboard paste (Ctrl/Cmd+V and a Paste button).
- Formats: PNG, JPEG, WebP, GIF (first frame), BMP, SVG (rasterized), AVIF where the browser supports it.
- **HEIC / HEIF auto-convert to PNG.** The native decoder is tried first (Safari has one). If that fails, the `heic-to` library (libheif compiled to WebAssembly) is loaded on demand from jsDelivr, pinned to one version with a Subresource Integrity hash. The conversion runs locally; the image is never sent anywhere. The service worker caches the library after first use so it works offline afterward.

## 4. Layers

- Layer types: **image**, **text**, **arrow/line**, **rectangle**, **ellipse**, **pen**, **highlighter**, and later **step marker**, **cursor stamp**, **spotlight**, **redaction**, **magnifier**.
- **Every layer can be moved, resized and rotated** (rotate handle, Shift snaps to 15 degrees, plus a numeric angle field).
- **Slim layer list:** select, reorder (forward/back/front/back), show/hide, lock, rename, duplicate, delete. Top of list = top of stack.
- **Image layers:** non-destructive per-layer crop (double-click), border, drop shadow, rounded corners, eraser mask, perspective tilt.
- **Text layers:** multi-line text, font (sans, serif, mono, rounded), size, bold, italic, alignment, text color, optional background box with padding and corner radius. Double-click to edit in place. Resizing scales the font.

## 5. Tools

| Tool | Notes |
|---|---|
| Select (V) | Click to select, drag to move, handles to resize/rotate, arrow keys nudge (Shift = 10 px) |
| Arrow (A) / Line (L) | Each end: none, closed arrowhead, open arrowhead, closed circle or open circle; Shift snaps to 45 degrees |
| Rectangle (R) | Stroke, optional fill, corner radius; Shift = square |
| Ellipse (E) | Stroke, optional fill; Shift = circle |
| Shapes (U) | One rail button opens a panel of 22 shapes (basic, symbols, signs, callouts, awards); stroke, fill, flip; signs start with their usual colors |
| Text (T) | Click to place a text layer |
| Pen (P) | Smoothed freehand |
| Highlighter (H) | Semi-transparent, multiplies over the image so text stays readable |
| Step marker (N) | Numbered circles that count up by themselves; renumber when one is deleted |
| Cursor stamps (C) | Arrow pointer, link hand, open hand, closed hand, I-beam, move, 4 resize directions, crosshair, not-allowed, click burst. Vector, large by default, fill `#0046ad` with white outline |
| Spotlight (S) | Ellipse or rounded-rectangle holes; outside area gets dim (color + opacity, default black 50%) and/or blur; adjustable feather; multiple holes per spotlight |
| Redact (X) | Solid fill or coarse pixelate. Real redaction, flattened on export. (Blur is a look, not a privacy tool) |
| Magnifier (M) | Zoom callout of one region, round or rectangular (adjustable corners), with optional leader line |
| Eraser (Shift+E) | On image, pen and highlighter layers; square or circle; size and feather; paints a hidden mask; **Restore** brush paints pixels back |
| Crop (K) | Canvas crop with aspect presets (free, 16:9, 4:3, 1:1, 3:2) |

Most annotations are removed by selecting and deleting them. Pen and highlighter strokes can also be partly erased (since 1.8.0).

## 6. Transforms

- Rotate canvas 90 degrees left/right, flip horizontal/vertical, resize (pixels, percent, presets).
- **Perspective tilt** (tilt left/right, tilt up/down, rotate) on any image layer, drawn with a short, commented per-pixel projective-mapping routine (no WebGL needed).
- **Showcase** export step: tilt, padding, background (transparent, solid, gradient), rounded corners and shadow applied to the *whole* composition, so annotations tilt with the screenshot.
- Light adjustments on image layers: brightness, contrast, saturation. That is where adjustments stop.

## 7. Exporting

- PNG, JPEG, WebP; quality slider; scale (0.5x, 1x, 2x); file name.
- **Copy to clipboard** (PNG) for pasting straight into Brightspace, email or slides.
- Visible note: "Metadata removed" (re-encoding strips EXIF, including phone GPS location).
- JPEG warning: transparent areas fill with the background color.
- **Alt-text prompt** on export with a copy button.
- **Project save/load** (`.imgedtr` - JSON with embedded images) so annotations stay editable later.

## 8. Deliberately out of scope

Layer blend modes, masks panels, adjustment layers, selection tools (lasso, and a magic wand that *selects* rather than erases), brushes, healing/clone, filter galleries, text on a path, background removal (maybe much later). A magic wand that *erases* was added in 1.11.0 (see below).

---

## 9. Build phases

### Phase 1 - Foundation (done, v0.1.0)
- App shell: top bar, tool rail, properties panel, layer list, start screen, light/dark, settings modal, info panel (shortcuts with per-shortcut switches, About, Changelog), toasts.
- PWA files, CSP, versioned service worker.
- Import: open, drop, paste (event and button), HEIC auto-convert, large-image downscale.
- Document model, layers, undo/redo, viewport zoom/pan.
- Select, move, resize, **rotate** every layer; nudge; duplicate; delete; reorder; hide; lock; rename.
- Tools: arrow, line, rectangle, ellipse, **text layers**, pen, highlighter.
- Export PNG/JPEG/WebP with quality + scale, copy to clipboard, metadata note.

### Phase 2 - Image tools (done, v0.2.0)
Canvas crop with presets, canvas size / padding / fit to contents, halve size, rotate/flip canvas, resize canvas; per-layer crop; eraser + restore with square/circle, size and feather; image layer border, shadow, rounded corners.

### Phase 3 - Teaching tools (done, v0.3.0)
Step markers, cursor stamps, spotlight (dim + blur + feather, multiple holes), redact (solid/pixelate), magnifier callout.

### Phase 4 - Showcase and polish (v0.4 to v1.0)
- **4a - done, v0.4.0:** perspective tilt per image layer, Showcase export.
- **4b - done, v1.0.0:** brightness/contrast/saturation, alt-text prompt, `.imgedtr` project save/load, merged canvas background control, accessibility audit.

Perspective tilt per layer, Showcase export, brightness/contrast/saturation, alt-text prompt, `.imgedtr` project save/load, polish and accessibility audit, then 1.0.
- Project save must warn when a file contains Redact layers: a project keeps the original pixels underneath (so it can be edited later), unlike an export, which is flattened.

### Phase 5 - Multi-select and groups (done, v1.1.0)
- **Multi-select first:** Shift/Ctrl+click on the canvas and in the layer list, drag a selection box, then move, align, distribute, restyle or delete several layers at once.
- **Groups (Ctrl+G / Ctrl+Shift+G):** a group is a folder in the layer list (collapse/expand, show/hide, lock, drag in and out). Moving, resizing and rotating a group transforms everything inside it together.
- **Why:** reconstructed UI (a dropdown screenshot + its shadow + an arrow + a step marker) should move as one piece, and a finished callout should be reusable with Duplicate.
- **Design notes (as built - changed from the first plan):** layers stay in one flat list; each member carries a `groupId`, and `doc.groups` holds `{ id, name, collapsed }`. Members are always kept side by side (checked on every save to history), and groups with fewer than two members dissolve. This kept every existing feature - rendering, spotlight, magnifier, canvas operations, projects - working unchanged, instead of teaching each one about nested layers. Group transforms apply to each member (even scaling from a corner, turning around the shared center). There is no separate group opacity; one slider sets every member's opacity.
- **Not included (possible later):** nested groups, group-level opacity or blend.

### 1.2.0 - Snapping and smart guides (done)
- Moving a layer, multi-selection or group snaps its left/center/right and top/middle/bottom to the canvas and to other visible layers, within 6 screen pixels. Pink guide lines show each match.
- Alt/Option while dragging skips snapping; a Settings switch turns it off. Snapping while resizing is a possible later addition.

### 1.5.0 - Rectangular magnifier (done)
- Magnifier Shape switch: Circle or Rect. Rect resizes freely and has a Corners slider; the spot outline and leader line follow the shape. Projects without a shape open as round.

### 1.6.0 - Shapes panel, Layers splitter, tooltips (done)
- Shapes panel replaces the Rectangle and Ellipse rail buttons. New `shape` layer type: one SVG path per kind, used to draw, hit-test and make the button icon.
- Layers pane height is adjustable (separator with drag and keyboard), saved in settings.
- Custom rail tooltips on hover and keyboard focus, with shortcut keys.

### 1.7.0 - Regular shapes, Pad contents, opacity in the layer bar (done)
- Shapes carry an `aspect` (width / height of the regular version); Shift draws and resizes to it, and a Make regular button snaps an existing one. Outlines inset uniformly so the box ratio is the drawing's ratio.
- Pad contents: +10 px canvas on every side (beside Fit contents).
- Opacity is a layer-bar control (button + popover with slider and number box) for any selection; not offered for redact, spotlight or locked layers.

### 1.8.0 - Erase pen and highlighter (done)
- Pen/highlighter layers keep `erase` strokes in box fractions (`su`, `sv`, `pts`) and are drawn through a mask. Eraser strokes are validated on project open.
- Segmented choice buttons share their row's width.

### 1.9.0 - Copy and paste layers (done)
- Ctrl+C/X/V for any selection. In-tab layer clipboard (layers + pictures); the system clipboard only gets a short note, so the newest copy wins and no external data is parsed as layers.

### 1.10.0 - Perfect shapes, line ends, color picker (done)
- Click-to-place shapes are regular; corner resize keeps proportions, edges stretch, Shift = regular.
- Line caps: `startCap`/`endCap` in none/arrow/open/dot/ring (legacy `headStart`/`headEnd` read by `capOf`).
- Own color picker (SV square, hue, Hex/RGB/CMYK boxes, EyeDropper where available) replaces `<input type=color>` in the properties panel.

### 1.11.0 - Magic wand erase (done)
- Tool `wand` (W): flood fill from the clicked source pixel (tolerance on max channel difference incl. alpha, contiguous or global, soft edge via canvas blur where supported), limited to the crop. Stored in the image's `erase` list as `{ kind: 'wand', x, y, tol, contiguous, soft, mode }` and replayed into the eraser mask; results cached per click.

### 1.12.0 - Drag a copy, resize from the center (done)
- Ctrl/Cmd+drag duplicates (copy made on first movement; Ctrl+Shift = axis-locked); Ctrl/Cmd on a handle = resize from center, Ctrl+Shift = evenly; handle snapping for unrotated layers.
- Pad contents = `fitToContents(10)`. Color picker replaces the native inputs in the New canvas and Settings dialogs.

### 1.13.0 - Magic wand Fill and Recolor (done)
- Wand `action`: erase / fill / recolor. Colour changes live in `layer.paint` (`{ id, kind: 'fill'|'recolor'|'revert', x, y, tol, contiguous, soft, color }`), replayed onto a cached copy (`paintedSource`) before the eraser mask. Edge band of 2 px recoloured by "share of the clicked colour" (line from C through P to the RGB cube's edge). Alpha untouched.

### 1.14.0 - Phone Inspector grab handle (done)
- Phone layout (max-width 820px): rows canvas / sheet / rail. Sheet row = 29px closed (handle only) or `--sheet-h` open; the canvas shrinks and re-fits (ResizeObserver), never covered. `resizeStage()` now renders immediately.
- Handle `#sheetHandle` (role separator, Up/Down 8% of the screen, Home closes, End tallest, Enter/Space toggle; tap toggles, drag below 90px closes). Matches DSKEDTR 0.14.0.
- `settings.sheet` = top of the sheet as a share of the screen from the bottom (default 1/3; the tool rail sits under the sheet). Limits: 120px open, and keep 140px of canvas. Closed on load, as before.

### 1.15.0 - Make a headshot (done)
A guided screen (splash: "Make a headshot"; start screen: "Headshot") for round or square profile photos. One image layer on a square canvas of 400, 800 or 1024 px: the layer's crop is the framing (drag, zoom 100-500%, arrow keys, + and -), its radius makes the circle or the rounded square, plus border and shadow; the document background is None (transparent), White or a colour. The margin for the shadow is computed (ceil(1.5 x softness + drop) + 1, drop = softness / 3), so the shadow is never clipped. Rail, Layers list and layer actions are hidden; only a short list of shortcuts works. Export is always PNG. "Open in full editor" leaves the mode with nothing lost. The style is remembered in `settings.headshot` (validated key by key). Code: section 22 of `index.html`.

### 1.22.0 - Animated GIFs, milestone 1 (done)
Open, play and re-save GIFs (`IMGEDTR-GIF-SPEC.md`, milestone 1). `doc.frames` = [{ id, imageId, delay }], `doc.loop`. The frame pictures are shown by ONE image layer marked `frameLayer: true` (always index 0, kept there by `normalizeFrameLayer()` in `commit()`); `syncFrameLayer()` points its `imageId` at the showing frame (`state.frame`) without adding an undo step. So every canvas command that transforms layers changes all frames at once. GIF reader/writer: `GIF BLOCK v1` (`GifCodec`, `GifWorker`; master copy `_edtr-suite/gif-block.js`). Projects: version 2 for animations only. Code: section 24.

## Roadmap (as of 1.22.0)
1. **Animated GIFs, milestones 2-4** - see the project doc `IMGEDTR-GIF-SPEC.md` (2: layers on a range of frames and onion skin - spotlight, magnifier and pixelate already use each frame's own pixels, and Export this frame as PNG is done; 3: images and video to GIF, Make a GIF on the splash; 4: smaller files).
2. **Batch headshots (headshot phase 2).** Pick many photos at once (a department directory) and make them all with the same style and size: a strip of thumbnails to frame each face (auto-centred to start), then download them all (a ZIP made on the device, or one file at a time). Nothing uploaded.
3. **Selection system** (after the GIF milestones). A real selection: the wand gets a **Select** action, plus a lasso and a rectangle select. Marching ants; actions on a selection: Fill, Recolor, Delete (erase), Copy to a new layer, Invert, Grow/Shrink, Feather; Escape clears it. The wand's Erase / Fill / Recolor stay as one-click shortcuts. Stored as recipes like the wand clicks, so it stays non-destructive.
