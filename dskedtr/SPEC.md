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
  apply a master.

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
  centre. Picture placeholders on masters.
- A warning when a picture is too low-resolution for its printed size.
- Alt text on every picture and meaningful shape or group (required; see
  Accessibility).
- Tables (0.19.0).
- Templates and building blocks (0.20.0).
- Folds, booklet printing, 2-up and 4-up with cut marks (0.21.0).
- Group, ungroup, lock, hide, flip, rotate, z-order.
- Exact X, Y, width, height and rotation in the Inspector.
- Format painter.
- Colour schemes: a document palette that can be swapped in one step.

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
     view settings: the app always opens ready to edit.
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

**Phase 3 - polish.** Colour schemes, drop caps and tab
leaders, hyphenation, text on a path, picture resolution warnings,
calendars, accessible HTML export, tagged PDF (below), and a look at
`.pub` import (below).

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

## Security and privacy

- No network calls at all once loaded: fonts, templates, building blocks
  and libraries are inside the file.
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
