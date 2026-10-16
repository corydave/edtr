# DSKEDTR spec

A desktop publishing app for the family: flyers, newsletters, brochures,
cards, certificates and signs. It fills the gap Microsoft Publisher leaves
behind, and fixes what Google Slides gets wrong for print work. Built to the
suite standard (`SUITE-STANDARD.md`) from the start: one file, works offline,
installable, nothing leaves the browser.

Status (2026-10-06): phase 0 (the text engine test) built as 0.1.0 and
approved. Phase 1 milestones 1 (objects, 0.2.0) and 2 (pages and layers,
0.3.0) built, then a tidier Inspector and guides (0.3.1) and Undo/Redo
in the top bar (0.3.2), milestone 3 (pictures and Merge Shapes, 0.4.0) and
milestone 4 (files and the suite shell, 0.5.0), then rulers, a grid and the
view toggles in the top bar (0.5.1), and milestone 5 (accessibility tools,
units and paragraph styles, 0.6.0). Next: milestone 6, formatting inside a
paragraph (character styles) and manual kerning. See `CHANGELOG.md` for what each version does and its
known limits.

## Identity

| | |
|---|---|
| Name | DSKEDTR |
| App id | `'dskedtr'` |
| Source folder | `productivity-suite/dskedtr/` |
| Project file | `.dskedtr` |
| Colour | emerald `#065f46` (7.7:1 with white). Chosen 2026-10-06 over magenta, since PDFEDTR (plum) and VCTREDTR (violet) already cover purple. |
| Dark-mode text | `#6ee7b7` (11.4:1 on `#171a21`) |
| Icon | an open two-page spread on the emerald plate: the left page has an orange picture block (`#f45922`, the family accent) and two text lines, the right page has a headline bar and three lines. 32 x 32 grid, plate `rx="7"` like VCTREDTR and 3DEDTR. Source: `dskedtr/icon.svg`. |

Emerald sits between IMGEDTR's olive green and SCRNCSTR's teal; on the
splash row it reads as its own colour. As everywhere in the suite,
colour is never the only difference: the icon's drawing and the name carry it.

## Why, in Dave's words

- Changing the document size in Google Slides resizes all the content.
- No linked text boxes that spill from one to the next.
- No odd/even page templates.
- Wants snapping, grouping, alignment, text boxes and shapes, Merge Shapes
  (union, combine, fragment, intersect, subtract), a layer pane, and text on
  a path.

## What the suite already has

- **VCTREDTR:** Paper.js shapes, Merge Shapes, opentype.js with bundled
  fonts, text as outlines, SVG import and export. DSKEDTR should share this
  code, not rewrite it.
- **PDFEDTR:** pdf-lib for writing PDFs, with fonts embedded and an offline
  build that inlines the libraries.
- **Shared block v4:** splash, crash backups, installing, update checks,
  help panel, More apps, credits.
- **Layout:** the suite's editor layout (rail, canvas, Inspector) plus
  PDFEDTR's bottom filmstrip as the page navigator, and VCTREDTR's status
  bar (pointer position, selection, page size).
- **Shared ways of working:** Space + drag pans the view; the layer list is
  an ARIA tree; long Inspectors fold into sections.

## Decisions so far

- **Changing the page size never scales content by default.** Page Setup
  offers "Keep content where it is" (the default) with a 9-point anchor grid
  (top-left, centre and so on), or "Scale content to fit." Objects that end
  up off the page are flagged, not deleted.
- **Odd/even templates become master pages.** A document can have several
  masters, each with a left and a right version. Master items (page numbers,
  running headers, picture placeholders) show on every page that uses that
  master and are locked there until you choose to override one.
- **Linked text boxes ("spill").** Any text box can link to another, on the
  same page or a different one. Text that doesn't fit flows into the next
  box. A box with text left over shows an overflow mark. "Continued on page X"
  and "Continued from page X" lines fill themselves in from the links.
- **Building blocks and starter templates are in, but they are our own.**
  Microsoft's templates and Building Blocks are its copyrighted content, so
  DSKEDTR ships original ones (the way GAMEDTR has an original art pack):
  borders, pull quotes, ad boxes and headline blocks, plus a starter gallery
  (flyer, newsletter, tri-fold brochure, greeting card, certificate, sign).
- **Mail merge is out.** Dave doesn't need it.
- **2-up and 4-up are in.** One page repeats two or four times on a sheet
  (half-page or quarter-page flyers, handouts), with cut marks. Business
  cards and labels use the same machinery with more copies.

## Feature list

### Pages and layout

- Page sizes: Letter, Legal, Tabloid, A4, A5, Half Letter, custom; portrait
  or landscape. Units: inches by default, with cm, mm and points.
- Facing pages (two-page spread view), with inside and outside margins.
- Margin guides, column guides, a baseline grid, rulers, and guides dragged
  out of the rulers.
- Bleed and a safe-area guide.
- Fold presets: tri-fold brochure, half-fold card, quarter-fold greeting
  card (two panels print upside down), booklet.
- Sheets of repeats: 2-up, 4-up, business cards, name badges, common label
  sheets.
- Page navigator (the filmstrip): add, duplicate, delete and reorder pages,
  apply a master; pick several pages; copy, cut and paste pages, also
  between documents and tabs (0.39.0).

### Text

- Text boxes, linked boxes with spill, an overflow mark.
- Autofit: do nothing, shrink text to fit, or grow the box.
- Columns inside one text box, with a gutter.
- **Text wrap** around objects: none, square, tight (follows the shape),
  top and bottom; with distance from the object.
- Paragraph styles and character styles that update everywhere.
  (Phase 1 has paragraph styles plus formatting on any words; named,
  reusable character styles are still to come.)
- Font, size, bold/italic/underline, colour, alignment, small caps.
  (Done in 0.8.0 except small caps; ten fonts and your own in 0.9.0.)
- **Type spacing**, all adjustable in the Inspector and saved in styles:
  - *Kerning* (the gap between two particular letters): the font's own
    kerning is on by default (read from the font through opentype.js), and
    any pair can be nudged by hand with the cursor between them. The
    shortcut must not take over Option/Alt + arrow, which Mac users rely on
    to move by word.
  - *Tracking* (even spacing across a selection or a whole paragraph).
  - *Leading* (the gap between lines): automatic (120% of the size) or an
    exact value in points.
  - *Paragraph spacing*: space before and after, first-line and left/right
    indents.
  - *Word spacing* and *baseline shift* (for superscripts, ornaments).
- Bullets and numbering, tabs with dot leaders, drop caps.
- Hyphenation.
- Text on a path (from VCTREDTR).
- Find and replace.
- Spell check with our own word list. (Found in phase 0: the browser's spell
  check marks only show in a visible text box, never on our drawn page.)
- Automatic page numbers and "continued" lines.

### Shapes, pictures and objects

- Rectangles, rounded rectangles, ellipses, lines, arrows, polygons, stars,
  pen paths (from VCTREDTR).
- Merge Shapes: union, combine, fragment, intersect, subtract (from VCTREDTR).
- Picture frames: crop by moving the picture inside its frame; fit, fill,
  centre. Picture placeholders on masters (0.23.0). Crop a picture to any
  shape on the page (0.23.0).
- A warning when a picture is too low-resolution for its printed size.
- Alt text on every picture and meaningful shape or group (required; see
  Accessibility).
- Tables (0.19.0).
- Templates and building blocks (0.20.0).
- Folds, booklet printing, 2-up and 4-up with cut marks (0.21.0).
- Group, ungroup, lock, hide, flip, rotate, z-order.
- Exact X, Y, width, height and rotation in the Inspector.
- Format painter.
- Colour schemes: a document palette that can be swapped in one step (0.24.0).

### Snapping and alignment

- **Guides** (0.3.1): up-and-down and across guides for the whole document,
  added singly or as column guides inside the margins, typed exactly or
  dragged on the page; objects snap to them.
- **The view in the top bar** (0.5.1, Dave: "they are global"): Rulers,
  Grid, Guides and Snap toggles, plus a panel (the arrow beside Guides) with
  the grid spacing and the guides list. Rulers in inches from the page's
  top-left; drag out of one to make a guide. The grid snaps unless a closer
  edge or object wins. These four are per-browser view settings, not part
  of the document; the guides themselves are. Keys: Alt+Shift+R, Ctrl+',
  Ctrl+;, Ctrl+Shift+;. Units (0.6.0): inches, cm, mm or points, for the
  rulers and every field, chosen in Page setup or the panel; inches for US
  English, cm elsewhere by default. 0.6.1: guides catch the page's middle
  from further away and every snap line is labelled (middle, margins, page
  edge); quick guide sets (Middle, Thirds, Quarters, Tri-fold, Half-fold);
  0.38.1 (Dave: "the Inspector should be the home for the guides"): the
  panel and its arrow are gone; everything in it is the Inspector's
  **Guides and grid** section, right under Document when nothing is
  picked, with Show guides / grid / rulers and Snap boxes that stay in
  step with the top-bar buttons (which are now plain on/off switches);
  Ctrl/Cmd + wheel and pinch zoom the page around the pointer, two-finger
  pan on touch, and the desk owns touch (touch-action: none). Later:
  a ruler origin you can move, and the baseline grid.

- Snap to margins, columns, guides, the grid, the baseline grid, the page
  centre, and other objects' edges and centres.
- Smart guides that show equal spacing ("these gaps match").
- Alt held down turns snapping off for one drag.
- Align left/centre/right/top/middle/bottom, to the selection, the margins
  or the page. Distribute horizontally and vertically.
- Arrow keys nudge (Shift: bigger steps).

### Layers

- Layer pane as an ARIA tree (suite standard): rename, hide, lock, reorder,
  open and close groups.
- Master items appear in the tree, marked as from the master.

### Output

- **PDF** with real, selectable text and embedded fonts (pdf-lib). Options:
  bleed, crop marks, single pages or spreads.
- **Booklet printing:** pages reordered so a folded, stapled stack reads in
  order.
- **2-up / 4-up** sheets with cut marks.
- PNG and JPG per page.
- **Accessible HTML** (later): one web page per document in reading order,
  with headings, alt text and language. Straightforward once the model
  carries roles and order, and the first step toward the reader below.
- Print through the browser using the exported PDF, since a browser's own
  print of a web page is unreliable for exact page sizes.

### Files and the suite

- `.dskedtr` project file, read as data with the same checks as a restored
  backup. Crash backups as in the other apps.
- Import SVG from VCTREDTR (with the suite's SVG rules: DOMParser, no
  entities, scripts and outside links stripped).
- Hand-off links: "Edit in IMGEDTR" for a picture, "Open in PDFEDTR" for an
  export.

### Accessibility, from the ground up

Added 2026-10-06 at Dave's request. Accessibility is part of the document
model from phase 0, not a checker bolted on at the end.

**Reading order (per page)**
- Every page keeps an ordered list of what a reader should meet, in order.
  A chain of linked text boxes counts as one entry (one story).
- A sensible order is made automatically (by story, then top to bottom and
  left to right within columns), and marked "automatic" until someone
  changes it.
- Two ways to change it, both saving to the same list:
  - **Reading Order tool** (on the rail): numbered badges on every object,
    with lines joining them in order. Click objects one after another to
    renumber them.
  - **Inspector list**: drag to reorder, or Alt + Up/Down from the keyboard.
    Each row says what it is ("Story: Spring Concert...", "Picture: Students
    on stage").
- Decorative items (page borders, background shapes, master headers and
  page numbers) are marked as decoration and left out of the order.

**Meaning, not just looks**
- Every paragraph style has a role: Heading 1-6, body, list, caption,
  quote, label. The starter styles come with roles already set.
- Document title and language, plus a language on any passage in another
  language.
- Tables have header rows (0.19.0: on by default, read as the column
  headings; the checker suggests one when a table has none).

**Alt text is required**
- Placing a picture opens its alt text field at once.
- Every picture, and every shape or group that carries meaning, needs alt
  text or a "decorative" mark. Export walks through the ones still missing
  before it makes the file.

**Contrast checker**
- Live in the Inspector whenever text is selected: the ratio against what
  is actually behind the text (sampled from the drawn page, so text over a
  photo is checked too), with AA and AAA marks.
- When it fails, it suggests the nearest shade of the same colour that
  passes.

**Colour-blindness preview**
- A View option that shows the page as someone with protanopia,
  deuteranopia, tritanopia or no colour vision would see it. Preview only;
  the document is unchanged. Also a greyscale preview for black-and-white
  printing.

**Accessibility Checker** (runs as you work)
Flags missing alt text, reading order still automatic on a busy page,
low contrast, skipped heading levels, text below a minimum print size,
overflowing text, objects off the page or in the bleed, empty
placeholders and low-resolution pictures. Each item jumps to the object.

## The hard part: the text engine

A browser's own editable text cannot flow from one box into another or wrap
around a shape. Chrome removed CSS Regions, the feature that would have
done it. So DSKEDTR needs its own text engine:

- **Model:** a *story* is the text, its styles and their roles (heading,
  body, list...). A chain of frames shows one story. Each page holds its
  reading order as a list of stories and objects.
- **Layout:** break the story into lines that fit each frame's width (minus
  any wrap shapes), measured with the bundled fonts' metrics through
  opentype.js. When a frame fills, carry on in the next one.
- **Editing:** our own caret and selection drawing, with the typing itself
  going through the browser's EditContext API (Chrome and Edge) or a hidden
  text field (Firefox, Safari). That keeps accents, other-language input
  (IMEs), dictation and screen readers working.
- **Accessibility:** a screen reader reads the story, not the screen
  fragments; caret moves are announced.

This is more work than everything VCTREDTR does with shapes, so it gets
built and tested first, on its own (phase 0), before the rest of the app.

## Phases

**Phase 0 - text engine spike.** One page, two linked text boxes, typing,
selection, copy/paste, undo, overflow, one font family, and the story
model with roles and reading order in place. Tested with the keyboard, a
screen reader and an IME. Stop for Dave's review.

**Phase 1 - a working publisher.** Pages and page sizes (with the no-scale
resize), margins and guides, text boxes with linking and overflow,
paragraph and character styles, shapes and pictures, snapping and
alignment, grouping, layers, Merge Shapes, PDF export, project files,
backups, the full suite shell. Accessibility from the start: required alt
text, the Reading Order tool and list, heading roles, document title and
language, the contrast checker, colour-blindness preview and the
Accessibility Checker.

Phase 1 is built in milestones, each stopping for Dave's review:

1. **Objects** (0.2.0): draw, select, move, resize, snap, align,
   distribute, order, duplicate, delete; text box linking on the page and
   in the Inspector; shapes with decoration or alt text; document title and
   language; margin guides.
2. **Pages and layers** (0.3.0): one page at a time on the desk (Dave's
   call, like Publisher) with the filmstrip along the bottom; stories
   flowing across pages; Page Setup with the keep-in-place resize; the
   layers list (ARIA tree); grouping (one level); hide, lock, rename;
   rotation; reading order per page.
3. **Pictures and Merge Shapes** (0.4.0; all built except shaped picture
   frames, which wait):
   - Add pictures with a Picture tool (F, for frame), a file picker,
     drag-and-drop onto the page or into a frame, or paste (a paste only
     fills an empty picked frame; it never replaces a picture by surprise).
   - Pictures are redrawn as they come in, which strips hidden data such
     as a phone photo's GPS location; they never leave the browser.
   - Picture frames, rectangle or ellipse; empty frames work as
     placeholders ("add a picture here").
   - Crop inside the frame: double-click to move and scale the picture
     within it; Fit, Fill and Centre buttons.
   - Alt text asked for the moment a picture lands (or "decoration"); it
     joins the reading order like a shape with alt text.
   - A warning when a picture will print blurry at its size (under 150
     pixels per inch).
   - Replace a picture and keep its frame, crop and place.
   - Merge Shapes (union, combine, fragment, intersect, subtract;
     Alt+Shift+U/C/F/I/S as in VCTREDTR), using VCTREDTR's Paper.js. The
     result is a new path object that fills, outlines, turns, resizes and
     takes alt text like any shape.
   - Maybe: merge a picture frame with a shape to make a shaped frame (a
     photo in a star or a speech bubble).
4. **Files and the suite shell** (0.5.0; built, waiting only for Dave's
   word to list DSKEDTR in the other apps):
   - Save and open `.dskedtr` project files, with the pictures inside;
     opened files are read as data and checked like any other file.
   - Crash backups (the suite's SuiteBackup, kept in this browser only),
     offered only after a session ended without saving.
   - PDF export: every page at its real size, text as real selectable
     text in the embedded font, shapes and merged shapes as vectors,
     pictures at full resolution, document title and language set.
   - PNG export of the page showing.
   - The suite shell: the shared SUITE block (splash with New / Open /
     Pick up where you left off, the More apps tab, credits), the full help
     panel (Keyboard shortcuts, Getting started, About, Changelog, More
     apps), installing as an app (manifest, icons, service worker) and
     update checks.
   - DSKEDTR joins the family: added to SUITE_APPS and SUITE_MARKS, and to
     the hub page, once Dave says it's ready to show.
   - A new, empty document as well as the sample.

   How it was built (0.5.0):
   - **Project file:** JSON, `{ format: "dskedtr-project", version: 1, app,
     saved, doc, images }`, where `doc` is exactly what the undo history
     keeps and each picture is a base64 `data:` URL. Opening rebuilds the
     document field by field from a whitelist (numbers in range, `#rrggbb`
     colours, id-shaped ids, text without control characters, roles from
     the list, chains checked against their boxes) and refuses what can't
     be repaired. Pictures must be real JPEG or PNG (first bytes), at most
     8000 px a side (read from the header before decoding) and must decode.
     Crash backups (IndexedDB, with the pictures as Blobs) go through the
     same checks.
   - **Since 0.33.0 the project file is a zip** (Dave asked for smaller
     files; base64 made pictures a third bigger): `mimetype`
     (`application/x-dskedtr`, first and stored, as EPUB does),
     `project.json` (deflated; pictures and fonts named by `path`),
     `pictures/<id>.jpg|png` and `fonts/<key>-<variant>.font`, stored as
     they are. Our own small zip writer and reader (no library): every
     offset and size checked, CRC-32 checked, at most 20,000 entries,
     encrypted entries refused, unpacking capped per file (pictures 40 MB,
     fonts 15 MB, anything 300 MB), names only looked up. Older one-JSON
     files still open (told apart by their first bytes, "PK"). Considered
     and not chosen: saving only picture file names (the project would
     break as soon as it moved to another computer).
   - **PDF:** pdf-lib 1.17.1 with @pdf-lib/fontkit 1.1.1 (both pinned with
     SRI, inlined in the one-file edition). The page is flipped once so all
     numbers match the desk. Text is real text in the embedded, subset
     font; each word gets its own start point and each letter inside it is
     placed from our own layout (kerning included), so the PDF matches the
     screen exactly (tested to within 0.6 pt with pdftotext). Shapes are
     PDF paths (merged shapes even-odd), pictures are embedded once each,
     clipped to their frames. Title (shown in the window bar), language,
     creator. Not tagged yet (see Out of scope).
   - **PNG:** drawn on a canvas from the same numbers (96, 150 or 300 ppi).
   - **Suite shell:** the SUITE block v4, pasted whole. The master block now
     has DSKEDTR in `SUITE_APPS` and `SUITE_MARKS` with `listed: false`, a
     new flag that keeps an app out of every list the other apps show (More
     apps, the splash's row, help-text links) while letting the app itself
     use its entry for its splash. Dropping the flag is all "joining the
     family" now takes (plus pasting the block into the others and the hub
     page). DSKEDTR's own splash is widened in its own CSS (eight other
     apps), as the nine-app block was.
   - **Keys** (the family's): Ctrl+O open, Ctrl+Shift+S save project,
     Ctrl+S export. They work while typing too.
5. **Accessibility tools and type** (0.6.0; built):
   - Units (Dave, 2026-10-06: "going to CM should be prioritized").
   - Paragraph styles per document (`doc.styles`, one per role): size,
     weight, line spacing, letter spacing, kerning on/off, space before and
     after, alignment including justified, colour. Look only; the role's
     meaning never changes. Shown while typing, in the Paragraph section.
   - The Accessibility tab beside the Inspector (tabs: Inspector |
     Accessibility) and a top-bar button with the problem count. Rules:
     title, alt text, measured contrast (WCAG 4.5:1 / 3:1 for 18 pt+ or
     14 pt+ bold; the page is drawn without its text and the colour behind
     each line is read from it), overflow, text under 9 pt, justified text
     (tip), headings missing or skipped (tips), blurry pictures, objects off
     the page, empty frames (tip). Each goes to the object and field.
   - Colour-blindness and low-vision preview on the desk (Machado 2009
     matrices; blur), never in exports.
   - The Export box's warnings come from the checker.
   - 0.7.0, between milestones (Dave's asks): a Shapes tool (U) with 24
     gallery shapes made as path objects (the table SHAPES, 100-unit
     boxes, many shared with VCTREDTR); rounded corners on rectangles and
     rectangular picture frames (`radius`, points); copy, cut and paste
     (an in-tab clipboard with pictures, plus the system clipboard's text
     and a private marker; outside text pastes as a new text box); and
     Ctrl/Cmd + drag to copy (Alt stays "no snapping").
   - 0.7.1: the staging area (Dave's name for the grey around the page):
     the drawing covers the page plus half a page at each side and a
     quarter above and below; objects there (not touching the page) are
     left out of printing, export, reading order and the checker. Space
     panning fixed (key repeats were scrolling the desk) and works mid-drag;
     Ctrl+Shift+drag copies along a straight line.
   - 0.7.2: Preview (the eye at the start of the view group, or W): a
     `proofing` class on the desk frame hides every helper layer and clips
     the content layer to the page (`#pageClip`), so only what prints
     shows. Look, don't touch: drags pan, editing keys stand down; W,
     Escape, the banner button, a tool or typing go back. Not saved in the
     view settings: the app always opens ready to edit. 0.38.1: the
     Preview banner (and the master-page banner) sit in a bar of their own
     above the rulers (`#deskBar`, grid row 1 of the desk frame), so they
     never cover the top of the page; the bar takes no room when empty.
6. **Formatting inside a paragraph** (done, 0.8.0): bold, italic,
   underline, colour and size for a word or phrase, links, and kerning by
   hand. A story is now text, roles, frames and `runs`: a sorted,
   non-overlapping list of `{ s, e, b, i, u, c, sz, href, k }` that only
   covers text differing from its paragraph style (`b: false` = not bold
   inside a bold heading; `k` = space before a letter in 1/1000 of its
   size). Edits spread runs to one format per letter (`charFormats`),
   change them and pack them back (`packRuns`). New letters copy the
   letter before (a link only continues inside a link; kerning never
   does); Ctrl+B with nothing highlighted sets `pendingFormat` for the
   next letters typed there. Layout measures each letter in its own font
   and size, and a line is as tall as its biggest letters. Links are
   always underlined (never colour alone), become clickable PDF link
   annotations described by their words, and only https, http, mailto and
   tel addresses are kept (`cleanLink`). The PDF embeds only the fonts
   used. Real Atkinson Hyperlegible italics (fontsource 5.3.0, latin, OFL)
   were added, about 30 KB. Project files are version 2 (an older
   DSKEDTR refuses them rather than dropping the formatting). Kerning keys:
   Alt+Left/Right, but Ctrl+Cmd+Left/Right on a Mac (Option+arrows move by
   word there). The checker measures contrast per colour stretch and flags
   links whose words don't say where they go, and tiny formatted words.
   Phase 1 is complete.
   - 0.9.0, between phases (Dave's ask): fonts. `FAMILIES` (section 2)
     lists ten built-in families (Atkinson Hyperlegible, Andika, Lexend,
     Comfortaa, Comic Neue, Literata, Fraunces, Zilla Slab, Archivo Black,
     Atkinson Hyperlegible Mono; fontsource 5.3.0 latin .woff files, OFL),
     loaded when first used (`loadFamily`, `requestFamily` relays out after).
     A font is "family/style"; `pickFontKey` falls back to the nearest
     style a family has, and to Atkinson until a family is loaded. Styles
     have `family`; runs have `f`. Own fonts (`customFamilies`, ids `uf1`...)
     are .ttf/.otf/.woff, checked and parsed, grouped by their name table,
     and saved in the project's `fonts` (data: URLs; Blobs in backups).
     `embedRule` reads each font's fsType: restricted or bitmap-only fonts
     are drawn as outlines in the PDF (`pdfGlyphShape`), no-subsetting and
     CFF fonts are embedded whole. Project files are version 3.

**Phase 2 - Publisher's strengths.** Text wrap (done, 0.10.0, below).
Master pages with odd/even, page numbers and "continued" lines (done,
0.12.0, below). Facing pages, columns in a box, "continued" lines, page numbers,
tables, bleed and crop marks, booklet printing, 2-up/4-up, fold presets,
building blocks, the starter template gallery (all done by 0.21.0, below).

- 0.10.0, text wrap: any non-text object can have `wrap: { mode, gap }`,
  mode `box`, `tight` or `topBottom` (absent = none), gap in points.
  `wrapObstacles(f)` gathers a box's obstacles as polygons in the box's
  upright directions (skipping hidden ones and any obstacle the box sits
  entirely inside); `freeSegment` finds the widest free stretch for a
  line's band (gap added up, down and sideways); `placeWrappedLine` moves
  down 1 pt at a time until a stretch of at least six letters (6 em, or
  36 pt) fits without cutting a word. Lines use one side only (InDesign's
  "largest area"); wrapping both sides could come later as an option.
  Tight wrap: ellipses (48-point polygon), merged shapes (each curve in 8
  steps), and PNG pictures traced from their alpha (`traceSeeThrough`: at
  most 256 px, rows' leftmost and rightmost visible pixels), clipped to
  the frame. Project files are version 4.
- 0.11.0, shapes (Dave's ask, with Publisher's gallery as the model):
  `SHAPES` holds 115 shapes as path data (`open: true` for outline-only
  lines, `line: 'end'|'both'|'none'` for gallery entries that make real
  line objects), grouped by `SHAPE_GROUPS` into Publisher-like sections,
  with a Recently used row (localStorage, this browser only). The nine
  shields are VCTREDTR's `SHIELD_STYLES` outlines, unchanged. Lines have
  `arrows: 'start'|'end'|'both'` (`lineParts` shortens the line and makes
  the heads, 5 x the stroke, at least 8 pt). Project files are version 5.
  Not done from Publisher's gallery: line callouts (a box with a leader
  line), scrolls, curved and circular block arrows, connectors that stay
  attached to shapes.
- 0.12.0, master pages: `doc.masters` = [{ id, name, objects, even? }];
  `page.master` names one. Inside the app masters are pages after the real
  ones (index doc.pages.length + i; `pageNo`, `allPages`, `isMasterIndex`),
  so every tool works on them. `masterFor(pi)` resolves odd/even;
  `pageObjectsWithMaster(pi)` draws and prints master things behind the
  page's. Page-number fields are U+E000 (page) and U+E001 (number of pages)
  in the story text, measured as one "letter" whose glyph has `parts` (the
  digits); `masterLayout(story, pi)` lays out master text for each page.
  Text boxes have `contPrev` / `contNext`: layout keeps a line's room and
  `continuedLine` adds "Continued from/on page N" (Caption style, italic) to
  `layout.notes`, drawn and exported like any line. Stories never span a
  master and a page. Project files are version 6. Not done yet: facing-page
  spreads on the desk, a starting page number, section numbering, master
  text tagged as "artifact" in a tagged PDF (phase 3).
- 0.13.0, details from Dave's testing: the Inspector button (suite standard,
  `view.inspector`, `.work.inspector-hidden`); `o.opacity` and `o.shadow`
  { x, y, blur, colour, opacity } on non-text objects (desk: `withEffects`,
  an unturned group with feDropShadow; canvas: each such object drawn on its
  own layer by `drawObjectOn`, then composited with a canvas shadow; PDF: an
  ExtGState for opacity, `pdfShadow` a 2 px/pt PNG of the shadow alone);
  picture frames in gallery shapes (`frameShape: 'shape'`, `o.mask`, drawn
  through `maskObj`, clipped even-odd); a Lock button and Ctrl+Shift+L; a
  hint when a click lands on something locked or on a master's thing.
  Project files are version 7.
- 0.13.1: one click on the Shapes rail button opens the gallery (it
  picks the tool too); a second click closes it. The button carries the
  `.has-flyout` corner triangle, as in VCTREDTR. U still picks the tool and
  U again opens the gallery.
- 0.13.2: the rail has one Shapes button (square, circle, triangle) in
  place of Rectangle, Ellipse and the star. It and U open the gallery; it
  is pressed while the rect, ellipse or shape tool is in use, and its name
  says what is being drawn. `GALLERY_TOOLS` adds Rectangle and Ellipse to
  the start of Basic shapes; they pick the `rect` and `ellipse` tools
  (real rectangles and ellipses, with rounded corners and so on) and are
  hidden in the frame gallery. R and O are unchanged.
- 0.13.3: Chromebook fix. `.desk-frame` tracks are `minmax(0, 1fr)` (not
  `1fr`), every child has min sizes 0, the frame has `overflow: clip`, and
  `.ruler` has `contain: strict`. Before, Chrome on ChromeOS let the ruler
  canvases' backing-store size (CSS size x devicePixelRatio) feed the grid
  row's automatic minimum, so each `drawRuler` grew the row, the
  ResizeObserver redrew, and the desk crept over the filmstrip. Seen in
  Dave's screen recording; reproduced by forcing the canvases to size from
  their pixel count.
- 0.14.0, mobile and linking UX from Dave's phone testing:
  - Phone sheet (max-width 760px): body is a fixed 100dvh grid; `.work`
    rows are rail / desk (`minmax(0, 1fr)`) / sheet (`var(--sheet-h)`).
    `#sheetHandle` (role separator) drags the sheet; `view.sheet` is its
    share of the screen (default 1/3, saved with the view settings);
    `applySheet`, `wireSheet`, `sheetLimits` (120px to window - 220px);
    closed = `.inspector-hidden`, which on a phone keeps just the 29px
    handle. `keepSelectionInView` after a drag. Smaller phone filmstrip.
  - Ports: `portSpots(f)` puts the in-port 16px above the top edge and 26px
    in from the left, the out-port 16px below the bottom edge and 26px in
    from the right; boxes under 96px wide on screen get them 18px off the
    corners diagonally. `portMark` draws a 11px-radius tab (chain link out,
    arrow in; green linked, red overflow, white free). `portReach` is 16px
    on coarse pointers. `inPortAt` (a green in-port) picks the box before.
    Touch panning skips ports.
  - Quick-action pill `#quickBar` (role toolbar, one Tab stop, Alt+F10):
    `quickBarState`, `updateQuickBar` (called from `renderSelection` and
    after every pointer drag), `placeQuickBar` (46px clear of the box,
    above, else below, else top of the desk), `wireQuickBar`. Copy keeps
    DSKEDTR's own copy and also fires the browser copy.
  - Fixed `duplicateSelected` picking a copied text box before `layoutAll`.
- 0.15.0: the pill gains Group / Ungroup (`groupSelected`,
  `ungroupSelected`) and Arrange, a popover menu `#arrangeMenu`
  (`moveOrder`; stays open for repeated steps; opens away from the picked
  things, using the pill's `data-side`). Shared menu helpers
  `openMenuFrom(menu, button, where)` and `wireMenu(menu, button)`
  (Up/Down/Home/End, Escape closes just the menu, focus returns to its
  button). Filmstrip `#pageMasterBtn` opens `#pageMasterMenu`
  (`fillPageMasterMenu`, `showPageMasterBtn`, `wirePageMasterMenu`);
  hidden while the masters show. The phone film-tools grid is 3 across.
  `#desk` is `tabindex="0"` with a `:focus-visible` ring and an
  `aria-describedby` key summary (axe's scrollable-region-focusable on a
  page with no text boxes).
- 0.16.0: filmstrip tools are `#addPageBtn` (+) and `#masterMode`. With
  masters, + opens `#addPageMenu` (`fillAddPageMenu`, `wireAddPage`;
  `addPage(masterId)`, '' for none, undefined to copy the page showing's).
  The page pill `#pagePill` (`.quick-bar`, role toolbar, inside
  `.filmstrip`, `bottom: calc(100% + 6px)`): Move left / right
  (`movePage`; `aria-disabled` at the ends, so focus never falls off),
  Master (`#pageMasterBtn`, `#pageMasterMenu`), Duplicate (`#dupPageBtn`),
  Delete (`#delPageBtn`). `setPagePill`, `updatePagePill` (from
  `renderFilmstrip`), `placePagePill`, `wirePagePill`. Opens on a page
  click, or when focus arrives in the page list from anywhere but another
  page or the pill; closes on a press outside the filmstrip and its menus,
  on Escape, or when focus leaves the filmstrip (`focusThumbQuietly` puts
  focus back without reopening it). Covers WCAG 2.5.7 (a single-pointer
  alternative to dragging pages).
- 0.17.0: columns in a text box (section 5d): `o.cols` (2 to 6; absent =
  1) and `o.gutter` (points; `DEFAULT_GUTTER` 18). `boxCols(f)`,
  `columnLimits(f, ci)` (equal columns; the gap shrinks so each column keeps
  12 pt). `layoutStory` steps column by column (`ci`), lines carry `col`;
  "Continued from" room only in the first column, "Continued on" only in
  the last. `freeSegment` and `placeWrappedLine` take the column's edges
  (`lim`). `posAtPoint` picks the column first (the middle of each gap
  divides). `renderFrames` draws the gaps dashed. Inspector: `#boxCols`,
  `#boxGutter` in Text flow. Project version 8. Not yet: a line between
  columns, columns of different widths.
- 0.18.0: facing pages and bleed (section 4c). `doc.page.facing`,
  `doc.page.bleed` (points, 0 to 72). `isFacing`, `isLeftHand(pi)` (page
  2, 4...), `spreadPartner(pi)`, `partnerOffset(pi)` (+W or -W),
  `marginBox(pi)` (left = inside, mirrored on left-hand pages). `stage()`
  is W + 72 wide each side with facing pages. New first layer `spread`:
  `renderSpread()` draws the partner (paper, content clipped to its page,
  margins, bleed) beside the page; `partnerPoint(p)`; a click there goes
  to that page and picks what is under the pointer; a link pick can land
  there (`textFrameAt(p, pi)`); `carryAcrossSpread()` after a move drag.
  `fitZoom` fits 2W; `showPage` centres the spread. `bleedLine(target,
  spine)`; active page outline. Filmstrip `.page-list.facing` pairs.
  PDF: `exportPDF(name, { bleed, marks })`: page W + 2e (e = b, or
  max(b, 9) + 18 + 6 with marks), TrimBox and BleedBox, the flip shifted by
  e, a clip at the bleed, `pdfCropMarks`, link rects shifted by e. Project
  version 9. Not yet: master pages drawn as spreads, objects spanning the
  spine (one object on two pages), PNG with bleed.
- 0.19.0: tables (sections 4d and 5e). Object type `table`: `cols`
  (widths), `rows` (smallest heights, 0 = fit), `cells[r][c]` = `{ id,
  type: 'text', story, cellOf, inset }` kept inside the table (not in
  `page.objects`), `header`, `banded`, `headerFill`, `bandFill`, `fill`,
  `stroke`, `strokeWidth`, `pad`, `fitH` (the height last laid out: a
  different `h` means a resize, and rows scale in step). `reindex`
  registers cells in `objIndex`/`objPage`; `layoutAll` runs `layoutTable`
  first (scale `cols` to `w`; measure each cell in a 1e6-tall box; row =
  max(need, min); place cells); cells ignore wrap. Header bold through
  `roleStyle(story, p)` (replaces `styleOf(story.roles[p])` in layout,
  `paraStyleAt`, `formatText`, `selectionLook`). Drawing: `tableEdges`,
  `rowFill`, `tableLinesD`, `tableElement` (desk), a `drawObjectOn` branch
  (PNG), `pdfTable` (+ `pdfLinks` per cell; `pdfShadow` takes texts).
  `linesByFrame` counts cells as on their page (and a master's tables).
  `textFrameAt` returns the cell under the point; `isLinkTarget` refuses
  cells; `stopEditingToFrame` picks the table. Reading order: the table is
  one item; `orderInputsInDom` expands it to its cells' stories, so Tab
  goes cell to cell; `storyLabel` names row, column and the column's
  heading. `tableColAt`/`moveTableCol` (drag kind `tableCol`; tabs drawn
  above column lines); no rotate handle, `setRotation` ignores tables.
  `tableAddRow/DeleteRow/AddCol/DeleteCol`, `setTableSize`,
  `afterTableChange`. Inspector `#secTable` (`fillTable`); Look applies;
  Meaning and Story hidden. Pill `addRow`, `addCol`. Rail tool `table`
  (B). Loader: `checkObject` 'table' (at most 100 x 20, rectangular, no
  rotation), cells join `textFrames` and `objectIds`, and a cell's story
  must have exactly that one frame. Checker tip: no header row. Project
  version 10. Not yet: merged cells, row heights by dragging, cell
  shading per cell, vertical alignment in cells, a table across pages,
  tagged PDF tables.
- 0.20.0: templates and building blocks (section 17). `storyParts(paras)`
  (paragraphs `[role, text, marks]`, marks `[[words or '*', format]]`;
  the sample uses it too). `docMaker(page)`: `page(master)`, `master`,
  `style(role, patch)`, `text`, `flow` (link a box), `rect`, `ellipse`,
  `line`, `picture` (empty frame), `table(pg, [x, y, w], rows, opts)`,
  `group`, `done()`. `TEMPLATES` (flyer, newsletter, trifold, certificate,
  card, sign; each `make()` returns a document), `newFromTemplate(t)`
  (loads its fonts first). `BLOCKS` (`size(m)`, `place` centre / top /
  bottom / fill, `make(k, pg, m)` at the origin of the margin box);
  `buildBlock` (in this document's styles, placed on the page showing),
  `addBlock` (as Copy items through `placeItems`, one undo step).
  `placeItems(src, off, suffix)` is the body of the old `pasteClip`.
  `previewSVG(d, pi, view, label)` sets the open document aside, lays out
  and draws `d` with `renderContent`, then restores it (and drops the
  preview's layouts). `#newDialog` (`openNewDialog`, `startNew`) replaces
  New's straight-to-blank; `#blocksDialog` (`openBlocks`), rail
  `#blocksBtn`, key K. Templates are checked in tests through
  `checkDocument`. Not yet: user-saved templates, more blocks (calendar,
  tear-off tabs, mailing panel), colour schemes to restyle a template.
- 0.21.0: folds and printing layouts (section 4c). `doc.page.fold` (a key
  of `FOLDS`: half, tent, tri, z, gate, quarter; fractions of the page,
  `wide` ones turn the Page setup to landscape); `foldLines()`,
  `foldLinesEl(target)` (violet dash-dot, "Fold" labels, also on the
  spread partner); folds join `snapTargets`, `snapName` says "Fold".
  Export: `printPlan(opts)` -> `{ sheets: [{ w, h, trim, bleedBox, places:
  [{ pi, x, y, s, clip }], marks }], note }` for `layout` pages / booklet /
  up2 / up4 (`paper` letter / a4 / exact). Booklet: M = pages rounded up
  to 4, side i holds [M - i, i + 1] (even i) or [i + 1, M - i], no bleed at
  the spine, a fold mark there. Copies: grids 2x1 or 1x2 (2-up), 2x2
  (4-up), the best scale on either paper orientation, cut marks outside
  the group at every cut, fold marks per column or row. `exportPDF` draws
  each place with one flip-and-scale matrix and its clip, then
  `pdfPageContent` (the old object loop) and `pdfMarks` (folds dashed
  [3 2]); `pdfLinks` takes a page-to-sheet mapping. Project version 11.
  Not yet: creep for thick booklets, imposition for 4-page folded
  sheets (quarter-fold cards with turned panels), cutting a page into
  tiles for a poster, printing straight from the browser.
- 0.21.1: the cell pill. `quickBarState()` returns `{ list: [table], cell:
  { r, c }, only: 'cell' }` while typing in a cell (any other typing: no
  pill); pill buttons `rowAbove`, `rowBelow`, `rowDel`, `colLeft`,
  `colRight`, `colDel` call `tableAddRow/DeleteRow/AddCol/DeleteCol`
  beside the cell; a mousedown on them is cancelled so the textarea keeps
  focus; Escape in the pill returns to the cell's textarea; the desk's
  scroll handler places the pill from the state's list.
- 0.21.2: `showDropTarget(o)` draws the picture under a file drag (its
  `frameShapeEl`, green, with a "Drop to fill" / "Drop to replace" label)
  on the snap layer, redrawn only when the target changes; cleared on
  dragleave out of the desk, drop and dragend.
- 0.21.3: gallery shapes `puffy` and `scallop`, made by `smoothPath`
  (Catmull-Rom points to cubic curves) over `polarPoints(n, r)` (r of the
  angle, stretched to the 0-100 box): `puffySquarePath()` is
  |x|^2.4 + |y|^2.4 = 1 times (1 - 0.2 cos^2 2t); `scallopPath(13)` is
  1 + 0.06 sqrt(cos^2(6.5 (t + pi/2)) + 0.06).
- 0.22.0: tagged PDF (section 4e). `pdfTagTree(pdf, L)` lays out the
  elements first, page by page in reading order (stories -> H1/H2/P per
  paragraph; tables -> Table/TR/TH (A /O /Table /Scope /Column)/TD with
  their paragraphs; pictures and shapes with alt text -> Figure with /Alt
  and a Layout BBox), then hands out MCIDs while drawing: `beginSheet`,
  `mcr(elem, sortKey)`, `para`, `link` (a Link inside its paragraph),
  `figure`, `lineKey` (line index x 10000 + letter offset, so kids sort
  into reading order whatever the drawing order), `annot` (StructParent
  on the link annotation, an OBJR kid), and `finish` (prunes empty
  elements, writes StructElems, the ParentTree, StructTreeRoot, MarkInfo,
  each page's StructParents and /Tabs /S). `pdfText` wraps each stretch of
  letters in BDC/EMC (split at link edges and around shape-drawn letters,
  which get Span + ActualText); notes, underlines, table grids, shadows,
  decoration, master objects and N-up copies after the first are
  /Artifact. Tested with pdfinfo -struct-text and a content-stream audit
  (no painting operator outside marked content, MCIDs match the
  ParentTree). Lists (L/LI) came in 0.37.0; XMP with the PDF/UA
  identifier and the PDF/UA-1 audit in 0.45.0 (section "PDF/UA").
- **Crop to shape and master picture placeholders (0.23.0, done).**
  `cropToShape` (section 10c, beside Merge Shapes): one picture plus one
  or more closed shapes on its page (`cropToShapeParts`; rect, ellipse,
  gallery or merged shape, not an open gallery line). The shapes are
  joined (Paper.js unite), turned back by the picture's rotation about its
  centre, and become `o.mask` (frameShape 'shape') exactly where they lay;
  the new frame's centre is placed where the turned picture shows that
  point, and ox/oy are re-measured so the picture doesn't move. If the
  picture no longer covers the frame it grows (about the frame's middle)
  only as much as needed, then slides just far enough. The shapes are
  removed; one undo. In the pill (`cropShape`), Arrange (`#cropShapeBtn`)
  and Alt+Shift+P. Placeholders (section 4, master pages): an empty,
  visible picture frame on a master is a placeholder. A page fills one by
  getting its own copy of the frame (`fillPlaceholder`: same box, shape,
  outline, wrap and alt text; `o.fromMaster` = the master frame's id;
  first in the page's objects), and `masterObjectsOn(pi)` leaves that
  master frame out on that page everywhere (drawing, printing, wrap,
  tagging, hints), so `pageObjectsWithMaster` stays the one source.
  Ways in: drop a picture file on it (it lights up: "this page only"),
  double-click or double-tap it, or the Document section's "Add a picture
  to ..." buttons (the keyboard way). Placeholders show in teal with a
  label that fits; the page's copy is an ordinary picture (a Figure in
  the PDF, not an artifact). Deleting the copy brings the placeholder
  back. Copies made with Duplicate, paste or Ctrl+drag drop `fromMaster`;
  a duplicated page keeps it. Project version 12 (`fromMaster` checked
  against ID_RE; anything else is dropped). Not yet: text placeholders,
  a page's copy following later moves of the master frame.

- **Colour schemes (0.24.0, phase 3, done).** `doc.scheme = { name,
  colours: [Text, Main, Accent 1, Accent 2, Pale, Light] }` (section 2,
  `SCHEMES`: 13 presets, Lakeside first and the default; each checked for
  Text at least 7:1 on white, Pale and Light, Main at least 4.5:1 with
  white). Colours stay plain hex everywhere; a swap RECOLOURS
  (`colourMapper(from, to)`: an exact slot colour becomes the new slot's;
  a mix of a slot with white or black, found by least squares to within
  2.5 levels a channel, becomes the same mix of the new one; anything else
  stays). `recolourDoc` covers fills, outlines, table header and band
  shading, shadows, text runs and role styles, on pages and masters.
  `setScheme` is one undo step (the snapshot carries the scheme). The
  Document section's scheme button opens `#schemeDialog`: a card per
  preset showing the current page recoloured (`previewSVG`, one per
  animation frame), the one in use pressed, and the document's own six
  colour fields with contrast warnings. Swatch rows (one Tab stop, arrow
  keys) under Fill, Outline, text colour, style colour and table shading;
  Fill and Outline swatches untick None. New rectangles, ellipses, gallery
  shapes, lines and tables start in the scheme; building blocks are made
  in Lakeside then recoloured; each template sets its scheme (`k.scheme`)
  and uses its colours or `tint()`s of them. Project version 13 (a
  scheme is six valid colours and a cleaned name, else Lakeside). Not
  yet: choosing a scheme in the New dialog, schemes saved for reuse
  across documents.

- **Drop caps, tab stops and leaders (0.25.0, phase 3, done).** Drop cap:
  `story.dropCap = { lines 2-5, font 'text'|'h1', main }` on the story's
  first letter (a letter or digit). `applyDropCap` swaps the measured
  letter for a big one (cap height spanning the lines, from the font's
  OS/2 sCapHeight or its H), widens it by the letter plus a gap, and marks
  `m.drop`; `lineMetrics` ignores it; lines 2..N of the paragraph (same
  box and column) get that indent on the left (also through
  `placeWrappedLine`); line 0 records `drop.baseline` = line N's baseline
  (a short paragraph pushes the next one clear). `baselineAt(ln, i)` gives
  every drawer (desk, PNG, PDF real text and shape letters) the letter's
  baseline. Main colour is read from the scheme at layout, so it follows a
  swap. In Story (Inspector); copied with its box; checked on load
  (`cleanDropCap`). Tabs: typed with Ctrl+Alt+Shift+T or Insert, Tab (Tab
  itself still moves to the next story). `style.tabs` (per role, at most
  8): `{ at (pt from the line's left, or null = the right edge), align
  left|center|right, leader none|dots|line }`; past the last stop, every
  36 pt. `tabWidth` is used by `breakLine` and by the x positions; a line
  with a tab isn't justified. Leaders (`line.leaders` -> `leaderMarks`):
  the font's own full stop every half em on a shared grid (columns of dots
  line up), or an underline-weight rule, drawn as shapes on the desk and
  as artifacts in the PDF (never text). Edited in Paragraph's style box
  (`fillTabStops`, `setTabStops`). Project version 14. Not yet: decimal
  tabs, tab stops for a single paragraph, a ruler to drag stops on.

- **Hyphenation (0.26.0, phase 3, done).** `style.hyphenate` per role,
  English documents only (`hyphenationLang`). Liang's method: the
  hyph_en_US patterns (Hyphen / Pyphen, after plain TeX hyphen.tex and the
  TUGboat exceptions; BSD-style), ASCII patterns only (9,782, about 93 KB),
  in a `<script type="text/plain" id="hyphEnUs">` block read once
  (`hyphenPatterns`); `hyphenPoints(word)` (2 letters before, 3 after,
  cached). `breakLine` now returns `{ end, hyphen }`: when a word runs over
  and breaking at the last space would leave more than 8% of the line
  empty (or there is no space), `hyphenBreak` breaks it at the latest
  point where the part plus a hyphen fits. Never words in capitals, with
  digits, or under 5 letters; at most 2 hyphenated lines in a row. The
  hyphen is drawn (with the leaders, `leaderMarks`), never typed: the text
  doesn't change, the PDF tags the word whole and the hyphen is an
  artifact. A hyphenated break isn't "forced" for text wrap. The
  newsletter template hyphenates its body. Project version 15. Not yet:
  other languages, soft hyphens typed by hand, a hyphenation zone setting.

- **Text on a curve (0.27.0, phase 3, done).** `o.curve = { kind:
  arch|dip|circle, bend 10-100 }` on a text box (Text flow, "Shape of the
  text"). The story is laid out flat as usual; `curveMap(f, vRef)` takes a
  flat point to the curve plus a turn (arch: centre below, the box's width
  bending through bend% of a full turn on the first baseline, lower lines
  on smaller circles; dip: centre above, the ends on the first baseline;
  circle: round a circle that fits the box, a line as long as the circle
  is round via `columnLimits`). `curvedLetter` places each letter by its
  middle and turns it; `frameCurves(lines, flatStory)` finds each box's
  first baseline. Drawn on the desk, thumbnails and PNG (`pageTextPaths`,
  through `pushOutline(..., T)`), and in the PDF as real text with a turned
  text matrix per letter `[cos, sin, sin, -cos]` (shape letters through
  `pdfGlyphShape(..., T)`); underlines follow the curve (`curvedBar`), link
  areas cover the curved words, the contrast checker samples where the
  letters really are. The box being typed in shows flat on the desk. A
  curved box has one column and ignores text wrap. Project version 16.
  Not yet: text along any shape's outline, tab leaders on a curve,
  dragging the bend on the page.

- **Calendars (0.28.0, phase 3, done).** `calendarBlock(cfg)` makes a
  building block (`{ year, month, weekStart 0|1, fill page|half, role,
  lang }`): the month as a heading, then a real table (`monthWeeks`):
  a header row of day names (`weekdayNames`, long when a column is at
  least 70 pt wide, else short; `Intl` in the document's language), a row
  per week, each row's minimum height sharing the room left so there is
  space to write; grouped, named "Calendar, <month>". The Building blocks
  card (`ask: true`) opens `#calDialog` (month, year 1600-2400 checked by
  us, week start, size). A "Monthly calendar" template (Ocean scheme, a
  photo placeholder, this month). Not yet: several months at once, a
  year-at-a-glance page, holidays or dates filled in automatically.

- **Accessible HTML export (0.29.0, phase 3, done).** Export's third
  choice: one .html file (`buildHTML`, `exportHTML`). Built with
  `document.implementation.createHTMLDocument` and DOM calls only (text
  always as text nodes), serialized at the end. Each page a `<section
  aria-label="Page N">` (one page: straight into `<main>`), following its
  reading order: stories as h1 / h2 / p / p.caption with strong, em, u,
  coloured spans and links (`htmlParagraphs`, runs by `charLook`; tabs as
  `span.tab`; page-number fields as numbers; a drop cap as a class);
  tables with `th scope=col` header rows and a caption when named
  (`htmlTable`); pictures as figures with their alt text (cropped or
  shaped frames drawn to a PNG of just what shows) and meaningful shapes
  as inline SVG `role=img` named by their alt (`htmlFigure`). Decoration,
  empty frames and master pages are left out. Styles from the roles (em
  sizes from Body, family names with a generic fallback, hyphens: auto
  where on). The file's CSP: `default-src 'none'; img-src data:;
  style-src 'unsafe-inline'`, no scripts, nothing fetched; a skip link;
  passes axe (WCAG 2.2 AA and best practice). Not yet: fonts inside the
  file, the text boxes' own fills and backgrounds, lists.

- **Tables, round 2 (0.30.0, done).** Merged cells: `cell.rs` / `cell.cs`
  on the top-left cell; the cells under it stay in the grid, empty, their
  typing areas hidden (`tableCover`, `visibleCells`). Merge right / down
  moves the other cells' words in as paragraphs (`moveCellWords`), refuses
  to merge the header row down or into another merged cell; Split undoes
  it; a row or column inserted or deleted through a merged cell splits it
  (`unmergeAcross`). Layout: each visible cell measured at its own width;
  rows from one-row cells and `t.rows`, a merged cell taller than its rows
  growing the last one; `t.heights` kept for drawing. Lines as segments
  that skip merged insides (`tableSegments`), fills per cell (`cell.fill`
  over the row's, `cellFill`). `t.valign` (middle, bottom) via `cell.vOff`,
  added where `layoutStory` starts. Row heights: drag the line under a
  row (`tableRowAt`, drag kind `tableRow`, row-resize pointer) or "This
  row's height". "Move this row and the ones below to the next page"
  (`tableBreak`): a new table at the next page's top margin (a page is
  added if needed), the header row copied, one undo step; the checker
  suggests it for a table off the bottom. Tagged PDF: hidden cells left
  out, `RowSpan` / `ColSpan` attributes, a row whose cells are all under
  merged ones kept as an empty TR; the web page uses rowspan / colspan.
  Project version 17 (spans cut to the table, overlapping ones split,
  first come first served). Not yet: tables that flow across pages by
  themselves, picking several cells with the mouse to merge them.

- **Performance (0.31.0, done).** Layout only what changed: each story's
  layout is kept with a fingerprint (`storyLayoutKey`: its text, roles,
  runs and drop cap; each box's place, size, settings and page; and
  `wrapKey`, every wrap object on those pages and their masters, with the
  PNG trace state). `globalLayoutKey` (styles, fonts loaded, page count,
  language, scheme, masters) clears them all when it changes; tables keep
  their rows and columns while `tableLayoutKey` matches. Drawing: each
  box's letters are kept while its line objects are the same ones
  (`textPathMemo`, keyed also on being typed in and on its curve), and a
  letter's outline is cached as relative path text placed with one "M x
  y" (`relOutline`, `pushGlyph`; points rounded first, so no drift).
  Typing in a 22-page newsletter went from about 90 ms a key to about
  16; a layout after no change takes about 1 ms instead of 36. Tested by
  an oracle: after each of 17 kinds of change, the kept layouts and
  drawing equal a fresh layout of everything. Not yet: redrawing only the
  boxes that changed in the page's SVG (the browser's own drawing is now
  most of the time left).

**Phase 3 - polish.** Colour schemes (done, 0.24.0), drop caps and tab
leaders (done, 0.25.0), hyphenation (done, 0.26.0), text on a path (done, 0.27.0: arch, dip, circle), picture resolution warnings,
calendars (done, 0.28.0), accessible HTML export (done, 0.29.0), tagged PDF (done, 0.22.0), and
`.pub` import (done, 0.32.0; below).

**Someday (decided 2026-10-10, not planned yet).**
- *Open a shared .dskedtr from Google Drive, in Preview.* A plain Drive
  share link can't be read by another web page (Google doesn't allow it),
  so it would go through the Drive API: `files/{id}?alt=media` with an API
  key locked to DSKEDTR's web address, for files shared "Anyone with the
  link" (hosted edition only; not the one-file edition). Opens in Preview
  with "Shared from Google Drive" and Edit a copy; same checks as opening a
  file. Files shared only inside FLCC would need Google sign-in (OAuth,
  Google's app review, maybe Workspace admin approval): a bigger job.
- *Open from any address that allows it* (`?open=https://...`), e.g.
  GitHub's raw files, which send the header that allows it.
- Not doing: a whole project inside the link itself. Text-only documents
  fit (about 1,100 to 4,400 characters), but one photo is about 134,000,
  and most documents will have pictures.

**Down the road - the DSKEDTR reader.** A reading view for published
documents, built on the same reading order and roles: a screen reader gets
a proper document, readers can zoom and reflow, and pages can carry
interactive pieces (embedded video, quizzes, buttons, hotspots), closer to
Lucidpress or Marq than to Publisher. Not planned yet; the model is shaped
so it can come later without a rewrite.

## Out of scope (for now)

- Mail merge (not needed).
- **Tagged (accessible) PDF, until phase 3.** Correction (2026-10-06): this
  is hard, not impossible. pdf-lib has no ready-made support, but its
  lower-level parts can write what a tagged PDF needs: each piece of text
  and each picture marked as it is drawn, plus a structure tree listing
  them in reading order with roles and alt text. The reading order and
  roles above are exactly that data. It needs its own spike and testing
  with a PDF accessibility checker and real screen readers before it is
  promised.
- **CMYK colour:** browsers work in RGB. Fine for school, office and home
  printers; a commercial print shop may ask about it.

## Opening `.pub` files

LibreOffice reads `.pub` through **libmspub**, a C++ library from the
Document Liberation Project. People spent years working out the closed
format by taking files apart, since Microsoft never published it. It sits
on librevenge (their shared plumbing) and a few other C++ libraries.

DSKEDTR could, in principle, do the same in two ways:

1. **Compile libmspub to WebAssembly.** Possible, but it likely brings several
   megabytes of code (libmspub, librevenge and their helpers) into a one-file app, and what it hands back is a
   drawing of each page (shapes and positioned text), not linked text boxes
   and styles. Fidelity varies by Publisher version.
2. **Write our own importer in JavaScript,** using libmspub's source as the
   map of the format. Pulls in the parts that matter (text boxes, pictures,
   shapes, page size) as real DSKEDTR objects. A sizeable project of its own.

Until then, the route for old files: open the `.pub` in LibreOffice Draw,
export SVG or PDF, and bring that in. Given Publisher's retirement, a
working importer would be a strong reason for teachers to switch, so it is
worth revisiting after phase 2.

**Dave is keen on option 2 (2026-10-06), down the road.** Two shapes it
could take, and they share one parser:

- **Inside DSKEDTR:** Open a `.pub` and keep editing it.
- **A standalone converter:** drop in a `.pub`, get a PDF (and maybe SVG or
  PNG pages) without learning a new app. Useful to educators on its own,
  given how many `.pub` files are sitting in shared drives.

Build the parser as its own module (reads the file into DSKEDTR's page and
object model), so DSKEDTR and a converter page can both use it. The file is
an OLE compound file (the same container old `.doc` and `.xls` files use),
so the first step is a small, careful reader for that container. Treat every
`.pub` as untrusted: strict bounds checks on every offset and length, limits
on sizes and counts, no recursion without a depth cap.

**Built (0.32.0, 2026-10-08): option 2, inside DSKEDTR.** Section 16b of
the code, our own JavaScript with libmspub's source as the format map
(MPL-2.0; nothing copied, credited in About). Tested on four real files
from Dave (three Publisher 2000 worksheets, one Publisher 2002+ flyer),
compared page by page with LibreOffice's conversions; on several points
DSKEDTR now reads more than LibreOffice does (Publisher 2000 fonts, clip
art pictures, the embedded equation).

How it works, in order:
1. **The container** (`readCompoundFile`): FAT and DIFAT, mini stream,
   the directory tree; every chain checked for loops and length, streams
   capped at 120 MB, files at 150 MB.
2. **The words** (`readQuill`): TEXT, STRS, SYID, FDPC/FDPP (character
   and paragraph formatting), STSH (defaults), FONT, PL (text colours),
   TCD (table cell ends). Publisher 2000 stores a run's font number
   directly in its font block; 2002+ one container deeper.
3. **Pages and shapes**: `readContents2k` (Publisher 2000: a chunk index
   at 0x16; shapes positioned from the page centre, in EMUs) and
   `readContents2002` (blocks; a trailer directory of chunks; pages,
   masters, shape chunks with text ids, tables with their row and column
   sizes and merged cells; positions, fills, outlines, shadows, alt text
   and pictures from the Escher drawing, through its groups).
4. **Pictures**: PNG and JPEG as they are; DIB bitmaps get their file
   header back; WMF and EMF (clip art, OLE presentations such as MathType
   equations) are played onto a canvas by a small metafile player
   (`drawMetafile`); each is redrawn at its frame's size, cropped and
   stretched as Publisher showed it.
5. **The project** (`pubToProject`): roles from size and weight against
   the document's usual text; role styles from the majority look;
   letters that differ keep their own format; paragraphs keep their own
   alignment (format field `al`, version 18). Fonts (0.35.0): Times New
   Roman, Arial, Calibri, Cambria, Georgia and Courier New use built-in
   metric twins (Tinos, Arimo, Carlito, Caladea, Gelasio, Cousine: the
   same advance widths, so lines break where they did). Any other font
   becomes a **missing font** (see below), drawn by a stand-in set to the
   original's widths. Any box that still overflows is fitted
   (`shrinkToFit`). Publisher drop caps (paragraph property 0x08, lines)
   become the story's drop cap when its first paragraph has one (2 to 5
   lines). The result opens through `openProjectData`, so it passes
   every project check.

**Indents (0.34.0).** Styles have `indentLeft`, `indentFirst` (negative:
hanging) and `indentRight`, in points; a paragraph can carry its own
(`li`, `fi`, `ri`) and its own tab stops (`tb`, positions), as formats
on its first letter, like `al`. Layout: `lineIndents` (at least 12 pt
left for words) and `lineTabs` (stops measured from where the line
starts; a hanging indent adds a stop at the left indent, as Word and
Publisher do; the every-half-inch stops stay put on the page). The
Publisher import takes each role's majority indents and tab stops and
keeps the rest per paragraph. Checked against the Weekly Review
worksheet: where LibreOffice puts "Find" after "A." further right, the
file's own tab stop (0.25 in) puts it where DSKEDTR does.

Not yet, roughly in order of what teachers' files will need:
- Text boxes linked across pages in Publisher 2000 (2002+ shared text
  ids are joined into one story; no 2000 sample had links).
- Border art, gradient and picture fills (the first colour stands in),
  WordArt, superscript and subscript, per-side borders on boxes, page
  backgrounds, Publisher 98 and earlier.
- A standalone converter page (drop in a .pub, get a PDF), sharing the
  reader.
- More sample files: newsletters, brochures, a file from Publisher 2016
  or 365 with linked boxes and WordArt.

## Spelling, find and replace, small caps (0.38.0)

- **Word list:** hunspell en_US (SCOWL size 60, from npm dictionary-en
  4.0.0, "(MIT AND BSD)" with SCOWL/Ispell/WordNet notices), affixes
  expanded at build time to 123,618 words, front-coded (a base-36 digit
  for the shared prefix, then the rest), zlib, base64, in
  `<script type="text/plain" id="wordsEnUs">` with the licence in an HTML
  comment beside it (about 230 KB). `loadWords` unpacks it once
  (DecompressionStream via `inflateBytes`) when the browser is idle.
- **Checking:** `wordOK` (straight or curly apostrophes; capitals,
  digits, other alphabets skipped; Capitalised words also as lower case;
  possessive 's checks the base); `misspellings(story)` memoised by text
  and dictionary version; English documents only. The document's own
  words: `doc.words` (version 22, validated letters/apostrophes, 5000 at
  most), in the undo snapshot; Ignore all is for the session.
- **Marks:** layer `spell` (hidden in Preview, never exported), wavy
  path per box, skipping the word at the cursor while it is typed.
- **Suggestions:** one edit, then two (words up to 10 letters), then two
  words; ranked by edits, a short COMMON_WORDS list, swapped letters,
  first and last letters, length, keyboard neighbours.
- **UI:** right-click menu (`#spellMenu`, manual popover, arrow keys);
  Spelling dialog (F7) from the cursor through `storiesInOrder`, with
  Change, Change all (whole word, same case), Ignore, Ignore all, Add.
- **Find and replace:** non-modal panel (`#findPanel`) in the desk frame;
  literal text, Match case, Whole words (Unicode lookarounds); matches
  never cross a paragraph end; reading order (`storiesInOrder`: each
  page's reading order, tables cell by cell, then masters); the match
  showing is `findHit`, drawn yellow, the keyboard staying in the panel;
  `replaceRange` keeps the first replaced letter's format; Replace all is
  one undo; Escape puts the cursor on the match. Ctrl/Cmd+F, Ctrl+H, F3.
- **Small caps:** format `sc`; `measureParagraph` draws a lower-case
  letter as its capital at 75% (`m.alt[k]` holds the code drawn); the PDF
  uses it and wraps the stretch in a Span with ActualText (the typed
  letters). Publisher's small caps flag now maps to `sc`.
- **List items said:** `sayListItem` on moving into an item or Enter;
  `moveVertical` prefixes a list item's first line with its number.

## Lists, superscript and subscript (0.37.0)

- **Lists live in the role string:** `'body'`, `'body|•|0'`,
  `'body|1.|1'`, `'body|1.|0|5'` (role | kind | level 0-4 | start
  again at). `baseRole`, `paraList`, `withList`; `styleOf` reads the base
  role, so every copy, split, join, undo and save carries the list with
  no extra bookkeeping. Kinds: `LIST_KINDS` (• – 1. 1) a. a) A. i. I.).
- **Markers are drawn, not typed** (`listMarkers` per story: counters
  per level, deeper levels reset under each new item, a start number
  restarts; paragraphs outside the list don't stop the count). Layout:
  marker column `listStep` (1.8 × size, at least 18 pt) per level; words
  at `indentLeft + (level + 1) × step`; a too-wide marker pushes the first
  line's words. Bullets are shapes (`bulletPath`: disc, ring, square by
  level), numbers are glyphs of the first letter's font (`measureMarker`).
- **Keys:** Ctrl/Cmd+Shift+8 / 7; Tab / Shift+Tab at an item's start
  (not right after arriving by Tab: `arrivedByTab`), Ctrl+] / [; Enter on
  an empty item ends it (or outdents); Backspace at an item's start
  removes the marker.
- **Output:** tagged PDF `L > LI > Lbl + LBody` (ListNumbering
  attribute; nested lists inside the LI above); numbers as real text in
  Lbl, bullets as artifact shapes. HTML: `ul` / `ol` (type, li value),
  nested.
- **Superscript / subscript:** format field `va` ('sup' / 'sub');
  `charLook` draws it at 65% (`VA_SCALE`), raised 0.33 or lowered 0.14
  of the size (`shift`, per letter in `m.shift`, used by `baselineAt`
  and `lineMetrics`); `ownSize` keeps the real size for the Inspector.
  PDF starts a new text position where the shift changes. Publisher:
  char property 0x0F, low byte 1 or 2.
- Project version 21.

## Page views and Preview (0.36.0)

- `pageView` (not saved in the document): `'one'`, `'two'` or `'grid'`.
  A document with facing pages opens in `'two'`, any other in `'one'`;
  turning facing pages on or off in Page setup switches with it.
- **Two pages** reuses the facing-pages machinery: `spreadPartner` pairs
  2-3, 4-5 for facing pages and 1-2, 3-4 otherwise; `partnerOffset`
  adds `spreadGap()` (0 for a spread, else 4% of the width, at least
  18 pt). Clicking the partner, dragging across, linking to a box on it
  and fit-to-window all work the same for both. A bleed line is open at
  the spine only for a real spread.
- **All pages** (`renderPageGrid`): a list of page buttons (roving
  tabindex; arrows, Home, End; Enter or click opens the page in the view
  it came from, keeping its zoom; Escape goes back). Zoom changes the
  picture width (80-480 px, 200 usual). A tool, building blocks or a
  paste go back to the page first.
- **Moving pages there (0.36.1):** pointer events (`wireGridDrag`): a
  mouse or pen drag starts after 6 px; a finger must hold still 0.4 s
  first (moving sooner is a scroll; a non-passive `touchmove` stops the
  scroll once dragging). The nearest page under the pointer and its left
  or right half set the drop place (a bar); a ghost copy follows; the
  grid auto-scrolls near its edges; Escape cancels; the click that ends a
  drag is ignored. Alt + arrows move the focused page. All through
  `movePage` (one undo step).
- **Preview** shades and makes `inert` the top bar, tool rail, filmstrip
  and side panel (`shadedParts`), and darkens the desk around the page;
  the banner carries previous/next page (`pageStep`: a pair at a time in
  Two pages), zoom out/in and Back to editing. Dialogs (Help) still open.
- **Zoom keys** (Ctrl/Cmd with +, =, -, 0, by `e.code` too) are handled
  before the typing check, so they never fall through to browser zoom.
  0.39.2 (Dave: clicking the other page made the pages "jump around"):
  `stage()` now has a left (`x`) and right (`r`) side; in Two pages the
  side the partner is on also gets the partner's room, so the drawing area
  is the same size and the pair sits in the same place whichever page is
  current. `relayoutAndRender` re-sizes the area when the stage changes
  (`stageShown`), and `goToPage` doesn't re-centre (`showPage`) when
  moving to the partner. The grey on each outer side keeps its full room.
  0.41.1 (Dave: "the staging area has limits"; a shape dragged below
  the page was cut off): the drawing's size is no longer fixed. Each side
  of the grey (`stage()`: x, r, y, b) is the biggest of the usual room
  (`baseStage`), what is on the page and its partner plus an inch
  (`stageReach`), and enough to fill the desk. `placeCanvas(px, py)` sizes
  the SVG and scrolls so the page's corner is at (px, py) on the desk, in
  whole pixels; `canvasP()` reads where it is now. Everything that sized
  or scrolled before goes through it: `applyZoom(at)`, `zoomKeeping`,
  `showPage`, `goToPage` (the partner of the pair keeps its place), and
  `checkCanvas()` after every redraw and when the desk is resized, so the
  page never moves while the grey grows or shrinks under a drag.
  0.39.1: zoom runs 25% to 800% (`MIN_ZOOM`, `MAX_ZOOM`; was 400%), and
  `zoomBy` (keys, buttons) keeps the page point in the middle of the desk
  in the middle (`zoomKeeping`), as the wheel and pinch already kept the
  point under the pointer. All pages' picture sizes are unchanged.
- Decided 2026-10-10 (Dave): the eye opens the View menu (his idea);
  Preview is in it with W as its key.
- **Facing pages, easier to find (0.39.0, Dave: "when making a booklet,
  you want the first page shown by itself").** It was always Page setup's
  Facing pages; now also a box in Document (`#docFacing`) and "Booklet:
  page 1 on its own" in the View menu (`#viewMenuFacing`). Both call
  `setFacing`: `applyPageSetup` with the same size and a top-left anchor
  (nothing moves; one undo step). It stays a document setting, not a view,
  because it also makes the margins inside/outside and the bleed open at
  the spine. Turning it off from Two pages keeps Two pages (1-2, 3-4).

## Picking, copying and pasting pages (0.39.0)

Dave: "allow multiple select copying and pasting of pages right from the
bottom rail". Decided with him 2026-10-10: like files in a folder, and
pasting works into other documents and other DSKEDTR tabs.

- **Picking.** `pagePick` (a Set of page ids; empty = just the page on the
  desk) and `pickAnchor`. Click: one page. Shift+click: a run from the
  anchor. Ctrl/Cmd+click: add or take out one. Keys in the filmstrip:
  Shift+arrows stretch, Ctrl+arrows move without changing the pick, Space
  toggles, Ctrl+A all, Escape (once the pill is closed) back to one.
  `goToPage` empties the pick, so anything else that changes page drops it;
  the filmstrip sets it again after. Masters are always one at a time. The
  listbox is `aria-multiselectable`; picked pages have `aria-selected` and,
  when several are picked, a tick by the number (not colour alone); the
  page on the desk has class `here` (dashed outline if not picked).
  `setPagePick` speaks "Pages 1 to 3 picked" (`pageListWords`).
- **On every picked page:** Alt+arrows / the pill's arrows
  (`movePickedPages`: each picked page swaps with the unpicked page beside
  it, so a block moves together), dragging one of them (`movePagesBefore`),
  Master page (`setPagesMaster`, ticked only when all share it), Duplicate
  / Ctrl+D (`duplicatePickedPages`: copies after the last), Delete
  (`deletePickedPages`; a document keeps one page, so the bin greys when
  all are picked), Copy, Cut, Paste. Each is one undo step. The pill's
  buttons say how many ("Duplicate 3 pages").
- **A set of pages** (`pageSetFrom` / `insertPageSet`): pages, the masters
  they use (and their even-page masters), stories, groups. A story whose
  boxes all come keeps its whole chain; otherwise each run of consecutive
  boxes becomes a story holding the words they show (`framesText`).
  Duplicating one page now goes this way too, so boxes linked to each
  other on the page stay linked (before, every box was unlinked).
  `insertPageSet` gives new ids to everything; from this document it
  reuses its masters, from another it brings them as new masters (keeping
  the name if free), remembered in `importedMasters` so pasting again
  reuses them (pictures likewise, `importedImages`).
- **Copy** (`makePageClip`): the set as a small project (the saved-file
  format), with the pictures and the added fonts its words use (a missing
  font as its name). Kept in `pageClip`, and the newest one in IndexedDB
  (`dskedtr-page-clipboard`, key `latest`) for other tabs. The system
  clipboard gets the words (for other apps) and a random marker
  (`application/x-dskedtr-pages`). Ctrl+C / Ctrl+X when focus is in the
  filmstrip (or its pill) copy pages; elsewhere they copy objects as before.
- **Paste** (`pasteCopiedPages`, `pastePages`): by the clipboard marker
  (this tab's copy, or the stored one with that marker), or the pill's
  Paste (the newest). Always checked like a file: `checkPictures`,
  `checkFonts`, `checkDocument`. Fonts: one with the same name here is
  used, else added (`installCustomFamily`, now shared with opening).
  Pictures added. The source's own spelling words are added. Styles are
  this document's (as with copied text boxes). A different page size keeps
  everything in place with a toast to check. Pages go after the last
  picked page; the pasted pages are picked.
- **Privacy:** pages never leave the computer. The stored copy is thrown
  away after two hours, or when its tab closes: the copying tab keeps a
  localStorage note (`dskedtr-page-clip-open-<tab>`, refreshed every 30 s,
  removed on `pagehide`), and a stored copy whose tab has no fresh note
  (five minutes) is deleted when next looked for. (An IndexedDB delete in
  `pagehide` alone doesn't reliably finish.)
- **Fixed on the way:** Undo after deleting a page that held the end of a
  linked story crashed (the overflowing story's last box wasn't found):
  `restore` now rebuilds the lookups (`reindex`) before redrawing.

## Touch handles (0.42.2)

Unlinking was tried as a split (each box keeping its words) and rolled
back the same day at Dave's request: he prefers the text collapsing back
into the first box's overflow, the next boxes emptied (as before).

- **Touch handles:** `touchScreen()` (pointer: coarse) gives `handlePx()`
  15 (9 with a mouse; 18 until 0.43.1), with corners rounded by
  `handleRound()` (a fifth of the size; 0 with a mouse), `handleReach()` 22 (7.5), `rotHandlePx()` 48 (26);
  the quick bar keeps 70 px clear above (46); table column tabs 1.8 times
  bigger, with a matching reach. On pointerdown, when a handle and a port
  are both in reach, the nearer one wins; on narrow boxes the diagonal
  ports sit 26 px out on touch (18).

## Teal (0.46.0)

Dave, 2026-10-16: DSKEDTR's colour becomes `#37c6d0`. Decided with him:
deep teal with white for filled controls (the suite's 7:1 rule), the
sample newsletter stays green, and DSKEDTR's entries change everywhere.

- **Tokens:** `--brand #37c6d0` (new: the mark, soft highlights, never
  under text), `--accent` and `--accent-text #195d61` (light), dark mode
  `--accent #195d61` with `--accent-text #37c6d0`; `--suite-accent
  #195d61`; `--sel-on` rgba(55, 198, 208, 0.38); theme-color `#37c6d0`.
- **On the page** (editing marks, not the document): every `#065f46` is
  `#195d61`, every `#10b981` is `#37c6d0`, rgba(16,185,129,a) is
  rgba(55,198,208,a), the focused text selection `#a8e4e9`.
- **Kept green on purpose:** the sample newsletter's objects and art, the
  Lakeside scheme, new tables' header fill (`#d1fae5`, Lakeside's pale:
  `setScheme` recolours it with the scheme, which a teal default would
  break).
- **Mark:** plate `#37c6d0`, text lines `#195d61`, white pages, orange
  block, in icon.svg, make-icons.py (PLATE, INK), the top bar and
  `SUITE_MARKS`. The suite list's `color` is `#195d61` (white icon on it).
  The splash hero (`APP_HERO`, 1120 x 630 WebP) was redrawn: the new mark
  on a deep teal plate beside the app.
- **Elsewhere** (2026-10-16): every app's copy of the block, the master
  `_edtr-suite/suite-block.js`, the feature-tour sources, edtrapps-site
  (colours, its family logo square, `icons/dskedtr.png`) and apps-landing
  (colours, `og-image.jpg` patched). The screenshots on the two sites
  still show 0.45's green editing marks.

## PDF/UA (0.45.0)

Decided with Dave 2026-10-15: finish the tagged PDF so it can claim
PDF/UA-1 (ISO 14289-1).

- **XMP** (`pdfXmp`): an uncompressed `/Metadata` stream (Type Metadata,
  Subtype XML, UTF-8) with dc:format, dc:title (x-default), dc:language,
  xmp:CreatorTool / CreateDate / ModifyDate / MetadataDate (`xmpDate`,
  local time with offset), pdf:Producer, pdfuaid:part 1. Text goes through
  `xmlEscape`. `exportPDF` uses one `Date` for the Info dates and the XMP.
- **Headings:** `tagFor(role)` in `pdfTagTree`: a heading's level is at
  most one deeper than the deepest so far (`deepestHeading`), so the first
  is H1 and none is skipped (7.4.2). The roles themselves are unchanged.
- **Nested lists:** the inner L goes in the item's LBody (`top.body`),
  keyed 1e12 + order so it sorts after the item's words (whose keys are
  line positions). An LI holds only Lbl and LBody (7.2-20).
- **Links outside the read words** (7.18.1, 7.18.5): `linkTags` in
  `pdfPageContent`. Master text: `looseLink(pi, ...)`, a Link element
  under the Document with /Alt = the link's words and an OBJR, keyed just
  after page pi's elements (`pageEnd`). Copies of a page (N-up): the
  annotation joins the original Link element (`kit.allTags`).
- **.notdef** (7.21.8): in `pdfText`, a glyph with index 0 (`notdef`) is
  drawn like a letter of a font that can't be embedded: its outline as a
  shape, in a Span whose ActualText is the letter (the whole of a
  surrogate pair: the run's end is widened by one when it ends on a high
  surrogate).
- **Checking.** veraPDF (the reference checker, Java) could not be
  downloaded in the build sandbox, so the rules it applies that matter
  here are re-implemented with pikepdf and fontTools (scratchpad
  `pdfua/audit.py` and `pdfua/fontaudit.py`): XMP (5-1, 7.1-8), Display
  DocTitle, Lang, MarkInfo, standard tags, Figure Alt, L/LI/Lbl/LBody and
  table nesting, Link OBJR, heading order, Tabs /S with annotations,
  annotation Contents and StructParent, marked content (no paint outside
  it, no Artifact inside tagged content or the reverse), fonts embedded,
  CIDToGIDMap, ToUnicode for every code used, widths matching the font
  (within 1/1000 em), no CID 0. Test t68; the other forty-odd PDFs the
  tests export are audited too. A third-party checker (pdfua 0.1.3 on
  PyPI) agrees, but covers only 16 of 106 rules.
- **To run veraPDF** (on a computer with Java): download it from
  verapdf.org, then `verapdf --flavour ua1 file.pdf` (or open the GUI
  and pick "PDF/UA-1"). Worth doing once on the sample before saying
  "PDF/UA" in public.
- Not machine-checkable, so still up to the person (the Accessibility
  tab helps): meaningful alt text, a sensible reading order, real
  headings rather than big bold paragraphs, a title.

## Touch pass (0.44.0)

Decided with Dave 2026-10-15 (after the number panel and touch handles):
everything that needs Shift, Ctrl or a mouse should have a finger way.

- **Pick several (objects).** `pickMore` flag. A touch pointerdown on a
  picked object sets `drag.press` (timer `LONG_PRESS_MS` 500); moving more
  than 8 px, lifting, or a second finger (`cancelPointerWork`) stops it.
  `longPressPick(d)` drops the move drag and toggles the object's unit
  (its group, unless Ctrl) against what was picked before the press
  (`press.before`), sets `pickMore`, buzzes (`navigator.vibrate`, where
  there is one) and shows a top toast. While `pickMore`: a tap adds (now)
  or takes out (on lift without a drag, `drag.unpickUnit`), the marquee
  keeps what is picked, a tap on the empty page or the grey picks nothing.
  `selectObjects([])` ends it. The quick bar's `pickMore` button (touch
  only, `aria-pressed`) toggles it (`setPickMore`). A finger's move drag
  needs 6 px (not 2) before it starts, so a hold doesn't nudge. The
  browser's callout and the spelling menu are held back after a hold.
- **A picked group's member:** on touch, a tap (no drag, not a double
  tap) on a member of the picked group sets `drag.narrowTo`.
- **Pages:** the filmstrip's pointerdown (touch) starts a hold; when it
  fires, `pagesPickMore` is set and the page toggles as Ctrl+click does
  (the click that ends the hold is swallowed; any new pointerdown clears
  that). While `pagesPickMore`, a click acts as Ctrl+click. `setPagePill
  (false)` ends it. Thumbnails are not `draggable` on a touch screen.
- **No Shift:** on touch, rotation settles on a 15 degree step within 4
  degrees; a picture's corner keeps its shape (`keepShape`).
- **Tab stops on the ruler.** `rulerTabs()`: while typing in an upright,
  uncurved box on the page showing, the column of the cursor's line
  (`columnLimits(f, ln.col)`) and `styleOf(role).tabs` for the role in
  `#styleBox`. `drawRuler(..., tabs)` draws the column as a band and each
  stop (`at` from the column's left; the right-edge stop faint). On the
  top ruler's pointerdown, a stop within reach (6 px, 14 by finger) starts
  `tabDrag` (moves settle by `tabStep`: 1/16 in, 1 mm, 0.1 cm or 1 pt;
  more than 28 px below the ruler marks it for removal); a press over the
  column remembers `tabAt`, and if it is let go on the ruler (the guide it
  started is "off"), `addTabFromRuler` adds a left stop. Dragging onto the
  page makes a guide as before (guides only turn on then).
- **Toasts at the top:** `toast(msg, ms, 'top')` uses `#toastsTop`, placed
  just inside the desk, so picking hints never cover the filmstrip.
- **Quick bar placement:** with no room above or below, the place down
  the desk covering least of the handle rows and ports (the turn handle
  weighted three times) instead of the top of the desk.

## Number fields on touch (0.43.0)

Dave's goal: on a phone, never need the on-screen keyboard unless the
user asks for it or it can't be helped (names, hex codes, links).

- `wireNumberPop()` runs only when `touchScreen()`. Every
  `input[type=number]` is made `readOnly` (a MutationObserver locks ones
  added later), so a tap brings up no keyboard. A tap opens `#numPop`
  (`popover="manual"`) beside the field (`placeNumPop()`: below, or above
  when there is no room; it follows scrolling). Inside a `<dialog>` the
  panel is moved into the dialog first, because an open modal dialog
  makes everything outside it inert.
- The panel: label (`numName()`, the field's label text), value, a range
  slider (`numRange()`: a table of sensible ranges in the user's units,
  always widened to include the current value), -/+ (one step; held, a
  step every 70 ms after 400 ms) and a keyboard button. Values go in
  through `numPut()`, which clamps to the field's min/max, rounds to its
  step and fires the field's own `input` (and `change` when done), so
  every field keeps its own handler and undo grouping.
- A second tap on the lit field, or the keyboard button, calls
  `numStartTyping()`: not read-only, `inputmode="decimal"`, focus and
  select. When it loses focus it is read-only again. Focus arriving by a
  keyboard (no pointer in the last 600 ms) unlocks the field at once.
- Lists that redraw when a value changes (tab stops, guides):
  `numWhere()` / `numFollow()` find the fresh copy of the field (the
  nearest parent with an id, and its index) so the panel stays open.
- A tap on the grey (a pan shorter than 8 px) deselects.

## The sample newsletter (0.42.0)

Dave: "add a few more pages to the sample newsletter. Let's show off the
multi-page capabilities." `sampleDocument()` now has four Letter pages,
all on Master A (footer rule and "Page # of #"). Pages 1 and 2 are as
before (masthead, main story s1 flowing f1 > f2 > f4, sidebar, lunch menu,
the drawn concert picture, an empty ellipse frame). Page 3: a tinted band
with "Around the School"; the garden feature s6 in two columns (f11, f12,
contNext) continuing to page 4 (f16, contPrev); a bulleted checklist
(roles `body|•|0`) in a grouped tinted sidebar; "After-school clubs" with
table t1 (header row, banded; cells c1... with stories sc1...) and a note.
Page 4: the end of the feature, a grouped boxed book fair notice, a
numbered list (`body|1.|0`), the costume parade and picture retakes items,
and contact details in a band under a rule. Nothing overflows, and the
checker reports only the empty frame's tip. Tests written for the old two
pages trim the sample back to two after loading it.

The Reading order tool's icon is an open book with an arrow under it (the
old three joined dots read as Share).

## Missing fonts and Google Fonts (0.35.0)

- **Missing fonts.** A font a document names but DSKEDTR doesn't have
  (Stencil, Impact, Bell MT from a `.pub`) is an entry in
  `customFamilies` with `missing: true`, its `name`, a built-in `standIn`,
  an optional `fit` (`[[size factor, closer], [same for bold]]`, from
  `widthMatch`) and no files. Words keep the missing font's key and their
  real size; `pickFontKey` draws them with the stand-in and `charLook`
  applies the fit, so lines break about where the original's did. Saved
  in projects as `{ name, missing, standIn, fit, files: {} }`
  (`checkFonts`/`checkFit` keep every number in range).
- **Filling one.** Document, Your fonts lists each with four buttons:
  *Add its file…* (any font file fills it), *From this computer*
  (Chrome/Edge's `queryLocalFonts`, after the browser asks; only the
  family with that exact name is read), *Google Fonts…*, and *Keep the
  stand-in* (the words move to the stand-in, with the fit baked in as
  their own size and spacing, so nothing moves). Filling it drops the
  fit; a lookalike (Stardos Stencil for Stencil) takes its own name.
  Every file is checked like any added font.
- **Google Fonts, only when asked.** The dialog (also from *Google
  Fonts…* under Your fonts) suggests a close match
  (`GOOGLE_LOOKALIKES`) and says, before anything is sent, that it asks
  jsDelivr for that one font, sending only its name. It fetches
  `@fontsource/<slug>@5/metadata.json`, then the latin WOFF files for
  regular, bold, italic and bold italic (nearest weights it has), with
  no cookies or referrer, each capped (200 KB details, 15 MB per file).
  The details are data: only plain numbers and names are used. The font
  is then saved inside the project, so it works offline from then on.
- Decided 2026-10-10 (Dave): ask first, then fetch; never by itself.

## Security and privacy

- No network calls unless you ask for a Google font (Document, Your
  fonts): then only that font's name goes to jsDelivr, and only its
  files come back. Fonts, templates, building blocks and libraries are
  inside the file. The Content Security Policy allows `connect-src` to
  `https://cdn.jsdelivr.net/npm/@fontsource/` and nowhere else.
- Pictures, project files and exports never leave the browser.
- Every file read (project, SVG, image) is treated as data: parsed, never
  run, never inserted with `innerHTML`; pictures are decoded through
  `createImageBitmap` and redrawn.
- A strict Content Security Policy, as in VIDEDTR.

## Inspector and touch

- Decided 2026-10-06: Inspector sections start folded and remember the ones
  opened (suite standard); Arrange uses small captioned groups of icon
  buttons split by thin rules. Touch and phones first: headings are 44 px
  tall buttons, icon buttons at least 38 px.
- **Context menus (right-click, long-press): someday, not now.** No other
  app in the suite has them yet; if they come, they should come to the
  whole suite together, and everything in them must also be in the
  Inspector or a shortcut.

## Open questions

- Rendering: phase 0 draws the page as SVG (each box's letters as one
  vector path, crisp at any zoom and the same shapes a PDF will get).
  Revisit only if long documents get slow.
- Layout speed: phase 0 redoes all layout on every keystroke (about 16 ms
  for one page). Phase 1 should only redo the stories that changed, and
  only from the changed paragraph on.
- Which fonts ship in the box (they decide the file size), and a fallback
  font for letters the main fonts don't have (other alphabets, emoji).
- Default page size: Letter, with A4 for other regions.
