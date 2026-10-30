# WHTBRDR spec

Written 2026-10-19 with Dave. Status: milestone 1 built as 0.1.0 in a chat;
the extension's toolbar folded in and shared as 0.1.1, and milestone 2's
first steps built as 0.2.0 (Select and the eraser), 0.2.1 (shapes, text
and sticky notes) and 0.2.2 (pictures and stamps), all in Cowork on
2026-10-19. Waiting for Dave's review of 0.2.2 (see `00-START-HERE.md`).

## What it is

WHTBRDR is a whiteboard and annotation app for the suite: open a PDF or a picture and mark it up, or start on a blank page, where every page doubles as a slide. Built to `SUITE-STANDARD.md` from the start: one file, works offline, installable, nothing leaves the browser. It shares its annotation bar with the WHTBRDR Chrome extension, so a teacher who learns one knows the other.

| | |
| --- | --- |
| Name | WHTBRDR (same as the extension; the extension is its Chrome companion) |
| App id | `'whtbrdr'` |
| Source folder | `productivity-suite/whtbrdr/` |
| Project file | `.whtbrdr` (zip: mimetype, project.json, pages/, pictures/ - the same shape as `.animedtr`) |
| Color | Open question. Two candidates, to compare side by side: deep rose `#9f1239` (8.0:1 with white; reads as a red dry-erase marker, but sits near GAMEDTR's paused crimson and PDFEDTR's plum) and indigo `#3730a3` (9.9:1; sits between VIDEDTR's blue and VCTREDTR's violet). Dark-mode text: `#fda4af` (9.2:1 on `#171a21`) or `#a5b4fc` (8.7:1). 0.1.0 uses the rose for now. |
| Icon | Open question. Suggestion: a whiteboard with a marker stroke across it and a small numbered step badge in the corner, 32 x 32, plate `rx="7"` like VCTREDTR, 3DEDTR, DSKEDTR and ANIMEDTR. 0.1.0 draws this suggestion. |

As everywhere in the suite, color is never the only difference: the icon's drawing and the name carry it too.

## Where it fits

WHTBRDR is for quick, loose marking-up and teaching; the other page apps are for finished documents.

- **vs PDFEDTR:** PDFEDTR edits the PDF itself (forms, signing, text, pages). WHTBRDR draws on top of pages and presents them. A PDF can go between the two.
- **vs DSKEDTR:** DSKEDTR lays out print documents precisely. WHTBRDR is freehand-first, with pages that work as slides.
- **vs IMGEDTR:** IMGEDTR marks up one picture. WHTBRDR marks up many pages at once and can present them.
- **vs the extension:** the extension annotates a live web page. The app annotates documents and blank boards, and adds pages, a filmstrip, present mode and export.

**What it reuses, so it isn't built twice:**

- **Shared block v4, pasted whole:** splash, crash backups, installing, update checks, help panel, More apps, credits, the Features tour, `SUITE_TOUCH` handles and `suiteNumberPop`. `listed: false` until Dave says.
- **Layout:** the suite editor layout (rail, canvas, Inspector), the 52px top bar, the bottom filmstrip from PDFEDTR and DSKEDTR, and the phone Inspector sheet with its grab handle.
- **DSKEDTR:** the SVG desk with its staging area (`#eef1f4` light, `#0f1115` dark - its `--bg`), Preview, snapping and alignment, grouping, the layers tree, the picture intake (redrawn, strips GPS), the zip reader and writer, the contrast checker and color-vision preview.
- **PDFEDTR:** pdf.js page rendering and pdf-lib writing, its two editions (`index-online.html` as source, `build-offline.py` to make `index.html`), the grading stamps and the hex-first color pickers.
- **IMGEDTR:** step markers (N) and its 22-shape panel.
- **VCTREDTR:** SVG import under the suite's SVG rules.
- **The extension:** its annotation bar (pens, highlighters, sizes, sticky notes, arrows and shapes, text, eraser, laser, spotlight, magnifier). Since 0.1.1 it is one shared file, `_edtr-suite/whtbrdr-bar.js` and `.css`, copied into both (see Changes to the extension).

## Pages

Every page is a slide: a size, a background, and the annotations on top. Pages come from a document or start blank.

### Opening documents (no conversion where possible)

| What comes in | What happens | Exports back to |
| --- | --- | --- |
| PDF | Each PDF page becomes a page of the same size, painted by pdf.js under the marks. (Correction, 0.4.0: pdf.js 5 can no longer draw a page as vector SVG, so it is painted as a picture: the whole page at 2048 pixels, and the part on screen again at the screen's own sharpness when zoomed in, so text stays crisp at any zoom. The original PDF bytes are kept, and go back out as vector in PDF export.) | PDF |
| PNG, JPG, WebP, GIF (first frame) | Opened (Open, Ctrl+O) or dropped on the filmstrip: one page per picture, sized to the picture, the picture as the page's background picture. Dropped on the board or pasted: a picture mark, as before. | The same picture format |
| SVG (e.g. from VCTREDTR) | One page, cleaned under the suite's SVG rules | PNG or PDF |
| Word, PowerPoint, Excel, Google files, Keynote, Pages | Not opened. A dialog explains how to save as PDF in each program, in one line each, then accepts the PDF. | PDF (it came in as one) |
| `.whtbrdr` project | Opens as saved | Any |
| Nothing (New) | One blank page at the chosen size | PDF by default |

Why no Office files: drawing a .docx or .pptx faithfully needs its fonts and a layout engine, and a .pptx doesn't contain pictures of its slides. A rough PPTX importer (text, shapes, pictures) is on the later list, not phase 1.

A document can be opened into an existing project too: its pages go in after the current page.

### Page sizes

New blank pages pick from these (New dialog and the page Inspector). Google Slides and PowerPoint both default to 16:9, and old PowerPoint is 4:3, so both are covered.

| Name | Size |
| --- | --- |
| Fit the screen (the first page's size, 0.7.2) | the display's own size, a CSS pixel to 0.75 pt (a 1440 x 900 laptop: 1080 x 675 pt, 15 x 9.375 in) |
| Letter, portrait | 8.5 x 11 in |
| Letter, landscape | 11 x 8.5 in |
| A4, portrait and landscape | 210 x 297 mm |
| Widescreen 16:9 (Google Slides and PowerPoint default) | 10 x 5.625 in (PowerPoint's 13.333 x 7.5 in is the same shape) |
| 16:10 | 10 x 6.25 in |
| Standard 4:3 (old PowerPoint) | 10 x 7.5 in |
| Square | 8 x 8 in |
| Custom | width and height, in the units picked (inches, centimeters, millimeters or points) |

Uploaded pages keep their own size. A new blank page copies the size of the page you're on. A fresh board starts the size of the screen (Dave, 2026-10-23): it fills the board, and Present fills the screen edge to edge. The size is worked out once, as the app opens, and is then a size like any other, so resizing the window or opening the Inspector never reshapes what is drawn. Pages in one project can differ in size, and changing a page's size never rescales what's on it (DSKEDTR's rule).

### The page Inspector (nothing selected)

Sections start closed, as in every suite Inspector.

- **Page:** size and orientation; Apply to all pages.
- **Colors:** page color (default white), and the staging-area color (default DSKEDTR's `#eef1f4`, or `#0f1115` in dark mode). The staging color is a project setting, not per page.
- **Background:** none, dots, small ruled lines, large ruled lines (wide-ruled with a margin line), small graph paper, large graph paper. Each has a line color and spacing. Apply to all pages.
- **Coordinate grid:** on or off, on top of any background. Settings: all four quadrants or the first only, where the origin sits, units per square, labeled axes with arrows, number labels every N squares. Made for math teachers: one tap gives a ready graphing page.
- **Background picture:** add a picture under everything (fit, fill, or centered), with fade. It sits on a locked bottom layer and is never selected by accident. Apply to all pages.

On a PDF or picture page the same Inspector shows only size (read-only), staging color, and a "Lay a background over this page" switch for grids.

## The tool rail

The rail starts with the extension's annotation bar (the shared bar file), then adds the app's own tools below a divider. The bar's keys are the extension's, which mostly agree with IMGEDTR's (V A L R T P H S M); where the two differ, the extension's win (O ellipse, E eraser, K laser, [ ] size). Agreed with Dave 2026-10-19.

The rail is one button per tool; the tool's colors, its size (S, M, L) and, for text, its font sit in the pill at the top of the board. The extension shows the same tools flat, every color and size its own button. Same tools, names, icons, order and keys either way.

| Tool | Key | Notes |
| --- | --- | --- |
| Select | V | First on the rail. Escape returns to it (after dropping a stroke being drawn). In the extension this slot is Interact. See Working with objects. |
| Pens (5) | P, or 1-5 to pick one | Black `#1f2937`, blue `#0046ad`, red `#dc2626`, green `#15803d`, purple `#7e22ce` (the extension's; all 4.5:1 or more on white). Pressure from a stylus (Apple Pencil, Wacom, Chromebook stylus) when the pointer reports it; smoothing on. Colors can be changed in the Inspector (the app only). |
| Highlighters (4) | H, or 6-9 to pick one | Yellow, green, pink, blue. Drawn under pens (multiply blend on a light page, 55% see-through on a dark one), so ink stays readable. On PDF text, Shift+drag snaps to text lines. |
| Size | [ and ] | Small, Medium, Large for every tool (pen 2/4/8 px, highlighter 12/20/32, text 18/28/44; 1 px = 0.75 pt). The app's Inspector also takes an exact size for the pen or highlighter. |
| Sticky notes | J ("jot") | From the extension: a colored square you type on, text wraps and the note grows. In the extension J drops one mid-screen. |
| Shapes and arrows | A arrow, L line, R rectangle, O ellipse, U shape panel | From the extension, plus IMGEDTR's 22-shape panel (U). Shift snaps (45 degrees, squares, circles). Arrows: straight, curved, double-ended, with an arrowhead choice. |
| Text box | T, F switches font | Plain text with no note behind it. Atkinson Hyperlegible is the default, Comfortaa the other (both the extension's). |
| Step numbers | N | IMGEDTR's step markers, across pages - see the next section. App only for now. |
| Picture | I | Insert from file, paste, or drop. Redrawn on the way in (strips GPS and other hidden data), size-capped. Also added to the extension. |
| Stamps | G ("grade") | PDFEDTR's grading stamps (green check, red X, colors changeable), plus a star and a question mark. |
| Eraser | E | Two modes: whole stroke (taps a stroke away; the extension's) and partial (rubs out part of a stroke, splitting it; the app only). Never erases the page itself. |
| Laser pointer | K | A fading trail in the pen's color that leaves no mark (the extension's). Most useful in Present mode, but works anywhere. |
| Spotlight | S | From the extension: dims everything but a circle around the pointer. In the app, part of Present mode. |
| Magnifying glass | M, + and - zoom | From the extension: a round lens that follows the pointer. In the app, part of Present mode; it redraws the page larger itself (no screenshots needed). |

**Settings that apply to all drawing tools:**

- **Pen draws, finger pans** (on by default when a stylus is first seen): a finger slides and pinches the page, so a resting palm leaves no mark.
- **Stay in tool** (IMGEDTR's setting): pens, highlighters and step numbers stay picked after use; other tools go back to Select.
- **Disappearing ink:** a switch on the pen tool that makes strokes fade after a few seconds. Off by default, handy in Present mode.

Tools stay out of the Tab order's way: the rail is one toolbar with arrow-key movement (roving tabindex), so Tab skips past it in one step.

## Step numbers across pages

Step numbers continue from page to page by default, and any step can restart the count. This is IMGEDTR's step marker (N) with one addition: a restart point.

**How numbering works:**

1. All step markers form one run, in page order, then in the order they were placed on each page (IMGEDTR's `seq`).
2. Each step's number is the one before it plus one, so deleting a step closes the gap and moving a page renumbers everything after it.
3. Any step can be marked **Start new numbering here**, with its own first number (default 1) and style (1 2 3, A B C, a b c). Steps after it count from there until the next restart.
4. Copying a page copies its steps, and they take their places in the run (a copy of a page with steps 4-6 placed after it becomes 7-9). A restart point on a copied page stays a restart, so a copied "lesson 2" page still starts at 1.

**In the Inspector, for a selected step:**

- **Number:** type a number and the step moves to that place in its run; the others shift (IMGEDTR's `setStepNumber`).
- **Earlier / Later:** swap with its neighbor.
- **Start new numbering here:** a switch, then **Start at** and **Style**.
- A line saying what it continues from, e.g. "Continues from step 6 on page 2", so the rule is never a surprise.
- Size, color, number color, white ring (as in IMGEDTR).

**Elsewhere:**

- With the keyboard, N adds a step at the center of the visible page, then the arrow keys move it (Shift: 10 px steps).
- Each step's alt text is filled in for you: "Step 3". If you add words ("Step 3: click Submit"), the number part stays live.
- A page's filmstrip tooltip names its steps ("Steps 4 to 7").

## Working with objects

Every annotation is an object you can select, move, lock and describe; nothing is baked into the page until export.

**Selecting:**

- With Select (V): click picks one; Shift+click adds or removes; dragging on an empty spot draws a selection box (anything it touches is picked; Alt+drag picks only what's fully inside). Ctrl/Cmd+A picks everything on the page.
- Without changing tools: Ctrl/Cmd+click picks an object while a pen is active, so a quick fix doesn't need a tool switch.
- On touch: a long press on the page starts a selection box (DSKEDTR 0.44.0's gesture).
- With the keyboard: Tab moves through the page's objects in reading order, Shift+Tab back; arrows nudge (Shift: 10x).

**Changing what's picked** (one or many at once):

- Move, resize (corner handles keep the shape with Shift), rotate (the turn handle, 15-degree snaps with Shift), using the suite's touch handles.
- Group (Ctrl/Cmd+G) and ungroup (Ctrl/Cmd+Shift+G). Groups nest. Double-click a group to work inside it.
- Order: bring forward/back, to front/back (Ctrl/Cmd+] and [, with Shift for front/back).
- Align and distribute (left, center, right, top, middle, bottom; to the selection or the page), with DSKEDTR's snapping to page edges, centers and other objects. Alt held while dragging turns snapping off.
- Copy, cut, paste, duplicate (Ctrl/Cmd+D), and copy to other pages ("Paste on every page" in the context menu).
- Flip horizontal and vertical.

**Locking:**

- Lock (Ctrl/Cmd+Shift+L, the padlock in the Inspector, or the context menu). A locked object ignores clicks, drags and the selection box, so pens draw straight over it.
- Locked objects still appear in the layers tree with a padlock, and Tab still reaches them, so keyboard and screen-reader users can unlock them. A right-click on the page offers "Unlock all on this page".
- Background pictures and the coordinate grid are locked from the start.

**The layers tree** (a section in the Inspector, the suite's ARIA tree): one row per object, top of the page first; drag or Alt+Up/Down to reorder; H hides, a padlock locks, F2 renames.

**Alt text on everything:**

- Every object gets a description written for it as it's made: "Red arrow pointing right", "Yellow highlight", "Sticky note: check this date", "Step 3", "Picture: diagram.png". Text boxes and sticky notes read their own words.
- Highlights on PDF text quote the words underneath (from pdf.js's text layer): "Highlight on: the mitochondria is the powerhouse".
- The Inspector's **Description** field is at the top of every object's settings. Typing there replaces the written description, and a reset button puts it back.
- Freehand ink has no meaning a computer can guess, so it gets "Freehand drawing" and the Accessibility checker flags it until someone describes it (or marks it decorative).
- **Decorative** switch: for marks that carry no meaning (an underline flourish). Decorative objects are skipped by screen readers and in exports.

**Context menus** (Dave, 2026-10-11) on objects, the page, the staging area and filmstrip thumbnails, with everything in them also reachable from the Inspector or a key.

## Filmstrip, zoom and layout

The layout is the suite's: tool rail on the left, the page in the middle, the Inspector on the right, and the filmstrip along the bottom (as in PDFEDTR and DSKEDTR). On a phone the rail goes along the bottom, the filmstrip folds into a Pages button, and the Inspector is the bottom sheet with its grab handle.

**The filmstrip:**

- One thumbnail per page (live: annotations show), numbered, with the current page marked by more than color (a thick outline and "current" read aloud).
- **Insert a page** at any spot: a + button between thumbnails (it shows on hover and focus), and Ctrl/Cmd+Enter after the current page. A new page copies the current page's size and background.
- **Copy a page:** Ctrl/Cmd+Shift+D, or the thumbnail's context menu. The copy goes right after the original, annotations and all.
- Reorder by dragging, or Alt+Left/Right on a focused thumbnail (announced: "Page 3 moved to 2 of 8").
- Pick several (Shift+click, Ctrl/Cmd+click) to copy, delete or move them together. Delete asks first when the pages hold annotations; undo always brings them back.
- The filmstrip is a listbox: arrows move, Enter opens, Delete removes, Home/End jump to the ends.
- Page Up / Page Down move between pages from anywhere on the canvas.

**Zoom:**

- Zoom out, a zoom-level menu (25% to 400%, Fit page, Fit width), zoom in, at the right of the status bar.
- Ctrl/Cmd + scroll wheel (and a trackpad pinch, which browsers send as Ctrl + wheel) zoom around the pointer.
- Ctrl/Cmd + `+` / `-` zoom around the page center; Ctrl/Cmd + 0 fits the page. These stop the browser's own page zoom only while the canvas has focus or the pointer is over it, so the rest of the app still honors a reader's browser zoom.
- Two-finger pinch on touch; Space + drag pans (the suite rule), as does a middle-button drag.
- Zoom level is announced politely ("150 percent").

**Status bar** (VCTREDTR's): page N of M, page size, what's selected, the zoom controls.

## Present mode

Present mode shows one page at a time, full screen, on a black staging area (Dave, 2026-10-19), and you can keep drawing while you teach.

- **Start:** the Present button in the top bar, F5 (from the first page) or Shift+F5 (from this page). Uses the browser's full-screen mode where allowed; otherwise fills the window.
- **Look:** the staging area is pure black `#000000` whatever the project's staging color or theme; the page is fitted and centered. Rail, Inspector, filmstrip and status bar are hidden; Preview's rules apply (no handles, guides or staging-area objects).
- **Move between pages:** Right, Down, Space, Page Down or Enter go forward; Left, Up, Page Up or Backspace go back; Home and End jump; typing a number then Enter goes to that page. Clicker remotes send Page Up/Down, so they work.
- **Draw while presenting:** a small floating bar (bottom center, fades when the pointer is still) holds the pens, highlighter, laser pointer, spotlight, magnifying glass, disappearing ink, eraser and undo (the shared bar's tools and keys: K, S, M with + and -). Marks made here are real annotations and are kept (an "Ink from this presentation" choice at the end: keep or discard).
- **B / W:** black or white screen, as in PowerPoint. Any key returns.
- **Escape** steps back (Dave, 2026-10-20): from any tool but the Pointer it goes back to the Pointer; with the Pointer it leaves Present mode, back on the page you ended on. In Chrome and Edge, Keyboard Lock keeps Escape for the app in full screen (holding Escape leaves full screen); elsewhere, leaving full screen follows the same rule. F, or the bar's Full screen button, goes in and out of full screen.
- **Screen readers:** each new page announces "Page 4 of 12" and its title or first text; the page's objects are read in reading order.
- Presenter view (notes and next page on a second screen) is on the later list.

## Export

Export offers the format the work came in as first, then PDF, PNG and PPTX (Dave, 2026-10-19). Objects in the staging area are never exported; decorative objects are drawn but carry no alt text. (Word and PowerPoint files come in as PDFs, so they go back out as PDFs - Dave agreed, 2026-10-19.)

| Format | When it's the default | What you get |
| --- | --- | --- |
| PDF | The project started from a PDF, from blank pages, or mixes kinds of page | The original PDF pages untouched (vector), with annotations on top, in one of two ways (below) |
| Same picture format (PNG, JPG, WebP) | The project started from pictures | Each page in its original format; several pages come as a zip, named `page-01.png` and so on |
| PNG | Never the default; always offered | The current page or all pages (zip), at 1x, 2x or 3x |
| PPTX | Never the default; always offered | One slide per page, annotations as editable PowerPoint objects (below). Opens in PowerPoint, Keynote and Google Slides (File, Import slides) |

**The two kinds of PDF:**

- **Annotations kept editable** (the default when the project came from a PDF): each annotation becomes a real PDF annotation (ink, highlight, free text, square, line, stamp). Acrobat, Preview and most PDF readers can still move or delete them. Each one's alt text goes in its `/Contents`, which screen readers read.
- **Flattened:** annotations are drawn into the page itself, so nobody can move them. To keep alt text, this uses DSKEDTR's tagged-PDF writer: each annotation is a Figure with its description, in reading order. Blank-page projects use this one by default. (Built in 0.5.2, where both kinds are tagged: see Milestones.)

**PPTX:**

- Written by the app's own zip writer and a small set of OOXML templates (no library). Each slide's background is the page: a PDF page rendered at 2x as a locked picture, or the page color and pattern.
- Annotations go across as native objects: text boxes and sticky notes as text shapes, shapes as PowerPoint's preset shapes, arrows as lines with arrowheads, ink as freeform shapes, pictures as pictures, steps as numbered circles. Each carries its alt text (`descr`).
- A deck has one slide size, so it takes the first page's size; pages of another shape are fitted inside their slide, and the export dialog says so.
- Built after PDF and PNG (see Milestones), because it's the most work for the least-used format.

**Before exporting:** the dialog shows the Accessibility checker's count ("2 drawings have no description") with Go to it links. It warns but never blocks: an annotation tool shouldn't stand between a teacher and their class.

## Files, backups and the suite shell

WHTBRDR carries the whole suite shell from its first build, like ANIMEDTR did.

- **Project file `.whtbrdr`:** a zip with `mimetype`, `project.json` (pages, objects, settings), `pages/` (original PDF bytes and page pictures) and `pictures/`. Save Ctrl/Cmd+S (Ctrl/Cmd+Shift+S for Save as), Open Ctrl/Cmd+O, or drop anywhere. Opening uses ANIMEDTR's checked zip reader (every offset, size, CRC and entry count; no locked entries; zip-bomb limits) and a `cleanProject` whitelist.
- **Crash backups:** `SuiteBackup`, with PDF bytes and pictures stored as Blobs. Export or Save deletes the backup; a leftover means Pick up where you left off on the splash and the top-bar badge.
- **New, Open or a sample** asks before replacing unsaved work (Save it first / Go ahead / Keep working).
- **Splash:** New (with the page-size picker inline), Open, Paste a picture, Samples, Pick up where you left off, the hero picture, the Features card and the family row.
- **Samples:** a math graphing page (coordinate grid), a marked-up PDF worksheet, and a four-slide lesson with step numbers - each clean in the checker.
- **Help panel:** Features, Keyboard shortcuts, Getting started, About, Changelog, More apps. `APP_FEATURES` tour: annotate a PDF, step numbers across pages, the coordinate grid, Present mode with the laser, alt text everywhere.
- **Installing and updates:** `manifest.webmanifest` with a file handler for `.whtbrdr` and PDF, PNG icons (192, 512, maskable), `sw.js` with the suite update check, the Install button.
- **Studio:** works in a Studio frame with no extra work; add `whtbrdr: 'Whiteboard'` to the Studio's `KIND` table when it's listed.
- **Two editions** as in PDFEDTR (built in 0.4.0): `index-online.html` (pdf.js from jsDelivr with SRI; pdf-lib joins it in 0.5.0, for export) is the source; `build-offline.py` makes `index.html`, packing the libraries from `vendor/` (gzip, then base64, in an inert `<script type="application/octet-stream">`) after checking them against the same fingerprints. The page checks the fingerprint again before unpacking.

## Accessibility, from the ground up

Everything in WHTBRDR can be done with a keyboard alone, and every mark it makes can be read by a screen reader.

- **Keyboard:** F6 cycles the regions (top bar, rail, page, Inspector, filmstrip, status bar). The rail and filmstrip use arrow keys inside; the page uses Tab through objects in reading order. Every pointer action has a key or an Inspector field: placing a shape or step at the page center, moving by arrows, resizing and rotating by number.
- **Drawing without a pointer:** shapes, arrows, text, notes, steps and pictures can all be placed by keyboard. Freehand ink can't, which is honest; the checker never asks for it.
- **Screen readers:** the page is a labeled region; each object is an item with its alt text, read in reading order (top to bottom, left to right by default, changeable in the Accessibility tab's Reading order, built in 0.7.0; the spec first said an Inspector section, as in DSKEDTR). Tool changes, adds, deletes, moves and page changes are announced politely.
- **Accessibility tab** beside the Inspector, with a count on a top-bar button (ANIMEDTR's pattern): must (pictures and freehand ink with no description), warn (text or sticky-note contrast under 4.5:1, text under 12 pt, objects off the page), tip (reading order on a busy page). Each item has Go to it.
- **Color:** pen and highlighter presets are checked against white and against the dark staging area; color-vision preview (protan, deutan, tritan, grayscale) on the page, from DSKEDTR.
- **Motion:** disappearing ink and the laser pointer respect "reduce motion" (the laser becomes a ring that doesn't trail; fading ink fades in one step).
- **Touch:** suite touch handles and `suiteNumberPop`; every target at least 44 px on a touch screen.
- **Testing:** keyboard only at 1366 x 768, axe, and a Chromebook; real VoiceOver, NVDA and ChromeVox runs are Dave's to do.

## Security and privacy

No document, picture or annotation ever leaves the browser, and every file read is treated as data, never run. This shapes the design from the first milestone, not the last.

- **No network calls** in the offline edition (except its own `index.html`, for the suite's update check, hence `connect-src 'self'`); the online edition loads only pdf.js (and, from 0.5.0, pdf-lib) from jsDelivr, pinned with SRI (`connect-src` adds `https://cdn.jsdelivr.net` there only; the build takes it out). A strict CSP as in VIDEDTR and DSKEDTR (no inline event handlers, no `eval`). pdf.js runs from `blob:` addresses the page makes itself, so `script-src` and `worker-src` allow `blob:` (`worker-src` keeps `'self'` for `sw.js`).
- **PDFs:** PDF JavaScript never runs (pdf.js's scripting part is not loaded). (Correction, 0.4.0: `isEvalSupported` no longer exists: pdf.js 5 removed eval altogether, and the CSP forbids it anyway.) Links in a PDF are shown but not followed inside the app (only the page's picture is drawn). Encrypted PDFs ask for the password and never store it. Pictures inside a PDF are capped at 60 megapixels; a PDF at 100 MB.
- **Pictures** are redrawn on the way in (strips GPS and other hidden data), with size caps on pixels and bytes, as in DSKEDTR.
- **SVG** follows the suite rules: DOMParser, no entities, scripts, pictures and outside links stripped, `<use>` expanded with a limit, previews drawn from the app's own numbers.
- **Project files** go through the checked zip reader and `cleanProject`: known keys only, numbers range-checked, text length-capped, colors matched against a hex pattern. Nothing from a file is inserted with `innerHTML`; text goes in with `textContent`.
- **Exports** are written from the app's own model, never by copying input markup. A PPTX's XML is built with escaping on every value.
- **Storage:** backups and settings in IndexedDB and localStorage, namespaced `whtbrdr.` (the Studio shares one origin). The service worker clears only caches starting with `whtbrdr`.
- **No analytics, telemetry, crash reporting or cookies.** Check the Cloudflare analytics beacon is off on whtbrdr's domain (it was found injected on others).

## Changes to the extension and PDFEDTR

Two sister projects change alongside WHTBRDR: the extension gets pictures and a shared toolbar, and PDFEDTR gets step numbers (Dave, 2026-10-19).

### The WHTBRDR extension

- **One toolbar, two homes (done: app 0.1.1, extension 1.3.0, 2026-10-19).** The annotation bar is a master file in `_edtr-suite/` (`whtbrdr-bar.js` and `.css`, between `WHTBRDR BAR v1` START and END markers like the SUITE block). `python3 _edtr-suite/paste_whtbrdr_bar.py` (run from `productivity-suite`) copies it into the app's `index.html` and the extension's `content.js` (default path `Documents/Chrome Extensions/whtbrdr/`), never edited in one place only. A Chrome extension can't load code from elsewhere, so copying is the only way, and it keeps the extension reviewable. It holds the tools, colors, sizes, fonts, icons, keys (`wbKeyAction`), stroke smoothing and pressure (`wbSmoothPath`, `wbPressurePath`, `wbNextPoint`) and the bar builder (`wbBuildBar`: "flat" for the extension, "rail" plus the pill for the app). Drawing, notes, undo and export stay in each home. The extension's accent stays its blue `#0046ad` until the app's color is settled.
- **The shared bar, version 2: three homes (done: app 0.8.0, extension 1.4.0, SCRNCSTR 1.25.0, 2026-10-22).** Dave: "sync the tools from WHTBRDR to be the same across the app, the extension, and the SCRNCSTR app". SCRNCSTR's Draw row is now the shared bar (flat), and `paste_whtbrdr_bar.py` copies the master into `scrncstr/index.html` too. New in the master: **section F, the handle** (`wbDock`: grip to float the bar anywhere, Fold to its handle, Dock / Float, Tuck away when not in use or as soon as a mark starts; each home styles its places through `data-wb-place`, `data-wb-orient`, `data-wb-folded`, `data-wb-peek`); **section G, click ripples** (`WB_RIPPLE`, `wbRippleAdd`, `wbRippleDraw`; the shared rule: a click ripples, a click that starts a mark doesn't); **section H, marks on a canvas** (`wbDrawMark` and friends, the extension's drawing code, now SCRNCSTR's too; the app keeps SVG). A flat bar's color buttons follow a home's own colors (`penColors`), for SCRNCSTR's right-click colors and the app's Present bar.
- **Recording (done: extension 1.4.0, Dave 2026-10-22).** Record the tab (`tabCapture`, recorded in an offscreen document), a camera bubble on the page (`camera.html` in a frame, `use_dynamic_url`), the microphone, Pause, saved straight to Downloads as `.webm`; survives moving between pages in the tab. Camera and microphone are allowed once on `setup.html`. New permissions: `tabCapture`, `offscreen`, `storage`.
- **Color settled (Dave, 2026-10-22): deep rose** `#9f1239` (`#fda4af` on dark), with the app's icon, for the app, the extension and the Web Store listing (`store/` in the extension folder).
- **Insert a picture:** from a file picker, paste or drop. Redrawn on the way in (strips hidden data), size-capped, kept in the page's memory only. Needs no new permissions.
- Bump the extension's version and note it in its changelog.

### PDFEDTR: step numbers

- The same step tool and numbering model as WHTBRDR (see Step numbers across pages): one run through the document in page order, any step can start new numbering, Number / Earlier / Later in the Inspector, "Continues from step 6 on page 2".
- Key: N, if PDFEDTR doesn't already use it (Cowork checks its shortcut table first).
- Saved into the PDF as drawn circles and numbers, plus a PDF annotation carrying "Step 3" (and any added words) in `/Contents`, so screen readers get it.
- Reopening a PDFEDTR-made PDF keeps its steps editable if PDFEDTR can recognize its own marks; otherwise they come back as page content. Cowork to confirm which, and tell Dave.
- Version bump, CHANGELOG entry in both places, both editions rebuilt (`build-offline.py`).

## Milestones

Built one milestone at a time, stopping for Dave's review after each, as with ANIMEDTR and DSKEDTR. Checked with Playwright at each stop.

1. **0.1.0 - the shell and one page (built):** the suite shell (top bar, rail, Inspector, status bar, help panel, theme), a blank page at any size, pens and highlighters with stylus pressure, undo/redo, zoom and pan (all the keys). **0.1.1 (built):** the shared toolbar file pulled from the extension, the extension's keys, colors and sizes, the master SUITE block. Proves the drawing model and the shared toolbar.
2. **0.2.x - objects**, in five stops (agreed with Dave 2026-10-19; 0.2.3 was split in two the same day):
   - **0.2.0 (built):** Select, the selection box, move, resize, turn, delete, nudge, Tab through objects, Ctrl/Cmd+A, Ctrl/Cmd+click with a pen, long press for a box on touch, the Inspector's color, width and position/size/turn fields, and the eraser (whole strokes and part of a stroke, sized by S/M/L). Decisions made building it: a stroke's width grows and shrinks with it; strokes keep no turn of their own, so the frame stands upright again once you let go (the Turn field counts from how things stood when picked); Escape steps back one thing at a time.
   - **0.2.1 (built):** the extension's tools onto the rail: arrow, line, rectangle, ellipse (A L R O), text (T, both fonts built in), sticky notes (J drops one in the middle, as in the extension). Decisions made building it: Stay in this tool is on by default (the extension's way); a single line or arrow is edited by its two ends; text keeps its shape when resized (its letters grow); a note's words stay dark on any paper; the eraser leaves notes alone, as the extension's does. Still open: on a phone the rail (10 tools) scrolls sideways.
   - **0.2.2 (built):** pictures (I, paste, drop; checked and redrawn, kept outside the undo list in a picture store) and stamps (G: check, X, star, question mark). Decisions made building it: the eraser leaves pictures alone, as it does notes; stamps stay square; on a phone the shapes fold into one Shapes button and Picture moves to the top bar (Dave, 2026-10-19).
   - **0.2.3 (built):** copy, cut, paste and duplicate; bring to front / forward, send backward / to back; lock; group and ungroup (nested, double-click to work inside a group); the right-click menu (also Shift+F10 and the Menu key) and an Arrange row in the Inspector. Decisions made building it: copies stay inside the app, and the clipboard only gets a short note with a one-off code, so Paste never reads outside data into a board (a copied picture still pastes in as a picture); a locked mark ignores clicks, drags, the selection box, Ctrl/Cmd+A and the eraser, but Tab and the right-click menu still reach it so it can be unlocked from the keyboard; a long press on a touch screen stays the selection box, not the menu; highlights stay under the ink whatever their order.
   - **0.2.4 (built):** descriptions (alt text) written for every mark as it's made, the Description field with a reset button, and the Decorative switch; the layers list; snapping (moving, resizing, line ends, drawing shapes) to the page's edges and middle and other marks, Alt to skip, a switch in the Select tool's settings; Line up (align and space evenly, to each other or the page). Decisions made building it (Dave, 2026-10-19): renaming a row in the layers list *is* writing its description (F2 there and the Description field are one thing); a group can have a description of its own (kept on the page as `groupAlt`); highlights sit in their own band at the bottom of the layers list and move only among themselves (Bring forward and Send backward step within a band everywhere); H hides and L locks only while the layers list has focus. Freehand ink keeps "Black pen stroke" as its written description (rather than "Freehand drawing"), and the Description field's tip asks for what it shows; the checker flags undescribed ink in 0.7.0. Hidden marks aren't drawn, clicked, boxed, erased or reached by Tab (the layers list reaches them). The layers list draws at most 500 rows.

   **Phone testing is on hold** (Dave, 2026-10-19) until he has time: builds are checked on the desktop only, and no phone checks are listed for his review. The phone layout is kept working as it is, not re-checked.
3. **0.3.x - pages**, in three stops:
   - **0.3.0 (built):** many pages and the filmstrip: add (the + button, Ctrl/Cmd+Enter, or the + between pages under the mouse), copy (Ctrl/Cmd+Shift+D), move (buttons, Alt+Left/Right, drag), delete (asks first when there are marks), pick several (Ctrl/Cmd+click, Shift+click, Shift+arrows), a right-click menu on the pages, Page Up / Page Down, undo and redo showing the page the change was on, and "Make every page this size / color" in the Inspector. Decisions made building it: the filmstrip's buttons (add, copy, move left, move right, delete) sit beside it, so nothing needs a drag (WCAG 2.5.7); the arrow keys in the filmstrip go straight to the page (as in DSKEDTR) and Enter goes back to the board; the + between pages is a mouse shortcut, the + button and Ctrl/Cmd+Enter do the same from the keyboard; copies of several pages go after the last of them; a board keeps at least one page; at most 500 pages. On a phone the filmstrip folds behind a Pages button in the top bar (built, not yet checked on a phone).
   - **0.3.1 (built, pulled forward from milestone 5, Dave 2026-10-19):** installable and the splash: `manifest.webmanifest`, `sw.js` (network first for the page, the suite's update check), the icon set from `make-icons.py` (`icon.svg`, 192, 512, maskable 512, apple-touch, favicon), the top-bar Install button, and the splash (New board, Pick a page size, Draw on a picture, the Features card; hero picture `APP_HERO`, also saved as `whtbrdr-thumb.webp` for the hub). A picture pasted or dropped on the splash closes it and goes onto the page. No "Pick up where you left off" yet: that arrives with crash backups in milestone 5.
   - **0.3.2 (built, pulled forward from milestone 6, Dave 2026-10-19):** Present mode, as described in its section above (section 8i of `index.html`). Decisions made building it: the top bar's Present button starts from the page on show (F5 from the first page, Shift+F5 from this one); the number keys still pick pen and highlighter colors while presenting, and a number then Enter goes to that page and puts the tool back as it was; with the Pointer, a click on the page goes forward and the mouse wheel moves page by page (one page per turn); B or "." blacks the screen, W or "," whites it; the floating bar is the shared bar laid out flat (as in the extension) on a dark pill, plus disappearing ink, undo, the pages and Stop, and it fades after 2.5 seconds of stillness (the mouse arrow hides too, with the Pointer); disappearing ink works for pens and highlighters, fades after 2.5 seconds, and is never kept or undone; the laser, spotlight and magnifier use the extension's numbers, and the magnifier redraws the page from its marks; leaving the browser's full screen also stops presenting; when presenting stops, "Keep the ink from this presentation?" is asked only if the pages changed, with Keep it focused first, and taking it away is one undo step. For now the laser, spotlight and magnifier are Present mode only (the spec's "laser works anywhere" waits for a place on the rail).
   - **0.3.3 (built):** the page Inspector's backgrounds (dots, small lines, large lines with a margin, small and large graph paper; line color and spacing; on every page), the coordinate grid, and the background picture (section 8j of `index.html`). Decisions made building it: the three are page settings (`bg`, `grid`, `bgPic`), not marks, so they are never picked, moved or erased; from the bottom up a page is its color, the picture, the lines, the grid, then the marks; the default spacings are a quarter inch for dots and small graph paper, a half inch for large graph paper, college (9/32 in) and wide (11/32 in) ruling for lines, with the margin line 1.25 in from the left; the grid sits half an inch inside the page edges, its origin counted in whole squares from the grid's left and bottom (the middle for four quadrants, one square in for the first), with a number every 2 squares by default; a picture already on the page can be made the background from its Inspector; a new page copies all three from the page on show. The help panel's tour gained "A graph in one tap" (five features now).
   - **0.3.4 (built):** step numbers (N) across pages (section 8k), plus two of Dave's asks (2026-10-20): Escape in Present mode goes back to the Pointer first and stops only from the Pointer; and **units** - inches, centimeters, millimeters or points - one choice at the top of the Page section ("Measure in"; also in Position and size), for every measurement. Decisions made building it: units are the person's setting, not the board's (as in DSKEDTR, whose table WHTBRDR now shares, ruler numbers included, ready for a ruler); the first choice follows the browser's language (inches for US English, centimeters elsewhere), and metric means a first page of A4, 5 mm dots and graph squares, 1 cm large squares and 5 mm grid squares; steps take one of the pens' five colors (blue first, as in IMGEDTR's default), with white numbers and a white ring, S / M / L for 24, 33 and 48 points, and always stay round and upright; a step's number can only be one its own page holds (steps on other pages keep theirs); a restart point is a property of its step, so it moves with it; new numbering starts at 1 in the style already in use; copied or pasted steps (not pages) take the next numbers and drop any restart; steps are erased whole. The rail gained the Step tool below Stamp.
   - **0.4.0 (built):** opening documents (section 8l of `index-online.html`) and the two editions. `page.doc = { src, index, name, rot, k }` names a PDF in `docStore` (outside the board, like `pictureStore`); pdf.js paints it in three tiers (240 px thumbnail, 2048 px page, an on-screen detail at the screen's sharpness), one at a time, the board's first, then thumbnails nearest the page on show. Decisions made building it: Open (top bar, Ctrl+O, the splash) puts the pages after the page on show, and replaces a board that is still one blank page; a picture opened this way is a page sized to it with the picture as its background picture (so it can be faded or taken away); a picture dropped on the board stays a mark, and on the filmstrip becomes a page where it lands; a PDF page's size is read only, "Turn the page" turns the PDF a quarter, Background lines and grids may go over it, its Inspector has no Background picture section, and "Make every page this size" skips PDF pages; PDF pages bigger than 100 inches are shrunk to fit (`k`); pdf.js is the legacy build of 5.7.284 (it supports older Safari), loaded only when the first PDF opens. Not yet: CJK PDFs that rely on outside CMaps may miss some text, and JPEG 2000 pictures inside a PDF don't show (both need pdf.js's extra files, which would add a few MB); a PDF's own text for screen readers comes with 0.4.1.
   - **0.4.1 (built, Dave's ask 2026-10-20):** the page pill, DSKEDTR's look and feel (section 8h): a floating toolbar over the page on show in the filmstrip, opened by a click or tap on a page or by the keyboard coming into the filmstrip, with Move left, Move right, Present from this page, Open a PDF or pictures after this page, Duplicate and Delete, acting on every picked page. Decisions made building it: the filmstrip's side keeps only the + (its other buttons moved into the pill, as in DSKEDTR); grayed buttons use aria-disabled so they stay reachable along the pill; "Copy this page" became "Duplicate this page" (DSKEDTR's word); the actions are WHTBRDR's own (no master pages, and no page copy and paste yet).
   - **0.4.2 (built):** highlights that quote the PDF words under them, the PDF page's words for screen readers, and Shift to snap a highlight to a line of text (end of section 8l); plus Dave's asks (2026-10-20): Present mode's Celebrate (SCRNCSTR's confetti, fireworks and hearts, Shift+C / F / H) and a magnifier that zooms 2 to 8 times (wheel, + and -, Ctrl with them, two fingers), never below where it starts; and from the wings, copy, cut and paste pages in the filmstrip (this tab only). Decisions made building it: a quote is worked out live from the highlight's place (not stored), a word counting when half its letters are covered; snapping works on straight-across text only, word to word, with the stroke 1.15 times the letters' height; screen readers get up to 4,000 characters of a page's words through the board's description; effects follow reduced motion by showing a still that fades; page copies don't cross tabs (PDF bytes and pictures live in the tab). That finishes milestone 4.
   - **0.4.3 (built, Dave's ask 2026-10-21):** two more Present effects: a big green check (Shift+G) and SCRNCSTR's 3-2-1 countdown (Shift+L); the bar's Celebrate button became Effects. From the wings: fireworks keep their colors on a light page, and the Features tour's "Any page, any shape" became "Mark up any PDF". Decisions made building it: both new effects run on the clock (no particles), the check in the middle of the screen for about 1.7 seconds, the countdown opaque over everything (as SCRNCSTR's) and stopped by Escape before Escape stops presenting; reduced motion keeps the countdown's numbers but not its sweep, punch-in or grain.
   - Milestone 5 is split in three: **0.5.0** files and backups, **0.5.1** export (flattened PDF with pdf-lib, PNG and the picture formats), **0.5.2** the PDF whose marks stay editable annotations, descriptions in the PDF (annotation `/Contents`, and tags for the flattened one), the export dialog's checker count, and samples.
   - **0.5.0 (built):** `.whtbrdr` save (Ctrl+S, Save as Ctrl+Shift+S) and open (section 8m), crash backups with "Pick up where you left off", asking before replacing work not saved, the file handler. Decisions made building it: the zip reader and writer are written fresh to ANIMEDTR's rules (positions, sizes, CRCs, no locked entries, name whitelist, unpack limits), since ANIMEDTR's own copy couldn't be read while the Mac was away; compared afterward (2026-10-21): the same design, WHTBRDR's a little stricter (a name whitelist, unpack limits on the whole zip, local headers checked against the directory), and two of ANIMEDTR's ways taken over (a name twice: the first counts; a failed squeeze stores the file as is); PDFs are kept byte for byte, so a password-locked PDF asks for its password again when the board opens; opening a board is a fresh start (the undo list begins again), while New board stays one undo step and does not ask (Undo brings the old board back); a quote is never stored, so nothing in the file can make a highlight say something else; a backup is kept only when there are changes not saved.
   - **0.5.1 (built):** Export (section 8n): a flattened PDF (PDF pages embedded untouched as form XObjects with `embedPage`, turned and scaled as on the board; everything else drawn as PDF operators) and pictures (PNG, JPEG, WebP at 1x, 2x, 3x; a zip for several). Decisions made building it: one walk of the board's own SVG feeds two painters (canvas and PDF), so pictures and PDFs agree; pdf-lib cannot embed WOFF2 (the letters come out invisible), so `make-export-fonts.py` keeps TrueType copies of the two fonts in the page; a password-locked PDF can't be copied by pdf-lib, so its pages go out as pictures (3x); highlights are multiplied one by one (the board multiplies them as one layer); note shadows are left out; Export is a solid button beside Present, as the suite standard has the main action (Dave to say if two solid buttons is one too many); the PDF gets a title and a language but no tags yet (0.5.2).
   - **0.5.2 (built):** the PDF whose marks stay editable (each mark a PDF annotation whose appearance is WHTBRDR's own drawing of it, carrying its description in `/Contents`), tags in both kinds of PDF, the Export dialog's descriptions check, and samples (section 8o). Decisions made building it: tags go in both kinds (the spec named them for the flattened one; an editable PDF gets Annot elements pointing at its annotations); a PDF page placed whole is a Div, so readers find its own words inside it, and a locked page's picture is a Figure described with its words; a text or note drawn in is a P (its own words, read as words) rather than a Figure saying "Text: ..."; a group with a description of its own is one element; the background picture and the coordinate grid are described, ruled lines and dots are Artifacts; not claimed as PDF/UA, since a placed PDF page keeps its own untagged insides. A straight highlight is a Highlight annotation, a freehand one Ink (a PDF app that redraws a Highlight draws its box); a turned rectangle is a Polygon. The check counts pen strokes and pictures with no description of their own (decorative, hidden, and grouped-with-a-description marks don't count), a row per page with Go to it; it never blocks. The samples are made in code, the worksheet's PDF too (its key words are bold, each its own run, so the highlights fit them exactly); each opens like a saved board and is clean in the check. Fixed on the way: New board kept the open file's name, so Save wrote over that file; it now forgets it. That finishes milestone 5.
   - Milestone 7 is split in two (Dave, 2026-10-21): **0.7.0** the Accessibility tab (checker, reading order, color-vision preview) and the Features tour; **0.7.1** PPTX export (moved to 0.7.3: 0.7.1 became the suite's listing of TELEDTR and WHTBRDR, 2026-10-22, and 0.7.2 the screen-sized first page, 2026-10-23).
   - **0.7.0 (built):** the Accessibility tab and top-bar button (section 8p of `index-online.html`), as in Accessibility below. Decisions made building it: reading order lives in the Accessibility tab, under the checker, not in an Inspector section (all the accessibility tools in one place; the spec said Inspector); it is kept per page as `readOrder` (keys "i:<mark id>" and "g:<group id>" for a group with a description of its own), absent while automatic, and marks added later go at the end, as in DSKEDTR; contrast follows WCAG (4.5:1, 3:1 for letters of 14 pt and up, since WHTBRDR's letters are all bold; 3:1 for marks), measured from the page itself on PDF pages and background pictures (the page drawn at half a pixel per point without its marks, the middle value under each mark; the 30 most recent drawings kept); "text under 12 pt" applies to text marks, and sticky notes are checked against their usual 11 pt (the extension's size), so a new note isn't flagged; a background picture gained a description and a Decorative switch (`bgPic.alt`, `bgPic.decorative`), and the checker asks for it; the busy-page tip starts at 8 things to read; scans are one tip per PDF; marks wholly off the page are left out of PDF tags (they were in); the pens' check is shown in their settings (on white, and on the dark staging area's #0f1115) rather than as checker rows; the samples' busy pages have their order set (notes last), so they stay clean. The Features tour became the planned five (Pens and highlighters, and Zoom where you point, left it).
   - **0.7.1 (built in another session, 2026-10-22):** the SUITE block pasted in again, so TELEDTR and WHTBRDR are listed in the splash and More apps, with "You are here".
   - **0.7.2 (built, Dave's ask 2026-10-23):** a fresh board's page is the screen's shape and size ("Fit the screen", first in the New dialog and the Inspector's sizes), instead of Letter or A4. Decisions made building it: the display's shape, not the board area's (Dave chose it), so the page fills the board with a slim margin and Present fills the screen with no bars; worked out once at start-up from `screen.width` and `screen.height`, then fixed (a board saved on a laptop opens the same size on a projector's computer, as "Custom" there); a phone held upright gets an upright page; people who measure in centimeters no longer start on A4 either.
   - **0.8.0 (built, Dave's asks 2026-10-22, released 2026-10-28 on top of 0.7.2, between milestones):** the rail's handle and Show clicks (section 8q of `index-online.html`), Present mode's bar with the same handle, from the shared bar's version 2. Decisions made building it: a folded or floating rail gives its column to the board (`.app:has(...)`), folded in place it is a small tab at the board's top-left; a floating rail stays inside the app (between the top bar and the status bar); on a phone the rail keeps no handle (no room on its row) and ignores a folded or floating state from a bigger screen; Show clicks sits in the status bar and on Present's bar, and draws on one canvas over the whole window that never catches the mouse.
   - **Next: PPTX export (it was planned as 0.7.3; it is now the next version after 0.8.0).**
4. **0.4.0 - documents:** PDF and picture import, the "Save as PDF first" dialog for Office files, the two editions (built). **0.4.1:** the page pill (built). **0.4.2:** highlights quoting PDF text, Present's effects and magnifier zoom, page copy and paste (built).
5. **0.5.0 - files and export:** `.whtbrdr` projects, crash backups (and "Pick up where you left off" on the splash), samples, PDF export (editable and flattened-tagged), PNG and picture export, file handlers in the manifest. `listed: false` in the SUITE block. (The splash, manifest, icons, `sw.js` and Install came early, in 0.3.1.)
6. **Present mode** came early, as 0.3.2 (see milestone 3).
7. **0.7.0 - PPTX export and accessibility tools:** PPTX with native objects, the Accessibility tab and checker, reading order, color-vision preview, the Features tour.

Alongside, each as its own small release when Dave asks: the extension's picture tool and shared toolbar, and PDFEDTR's step numbers.

**Later list (not planned yet):** a rough PPTX importer, presenter view on a second screen, shape recognition (a rough circle becomes a circle), a page-and-ink recording mode handed to SCRNCSTR or VIDEDTR.

## Open questions

- [x] Color: deep rose `#9f1239` (Dave, 2026-10-22, for the Web Store listing).
- [x] Icon: the whiteboard with a marker stroke and a step badge (the extension uses it too since 1.4.0).
- [ ] Domain: `whtbrdr.app`, or only edtrapps.com/whtbrdr/?
- [ ] Should the extension get step numbers too, now that the toolbar is shared?
- [ ] Present mode: keep ink made while presenting by default, or ask every time?

First steps for Cowork are in `00-START-HERE.md`.
