# WHTBRDR - start here (handoff from chat, 2026-10-19)

> **Update, 2026-10-19 (Cowork): steps 1-5 below are done.** 0.1.1 has the
> extension's bar, shared through `_edtr-suite/whtbrdr-bar.js` / `.css`
> (copied into the app and the extension by `_edtr-suite/paste_whtbrdr_bar.py`),
> and the master SUITE block. The extension is 1.3.0. Waiting for Dave's
> review of 0.1.1; then milestone 2 (0.2.0). See "Where 0.1.1 stands" below.
>
> **Later the same day: 0.2.0 built** (Select and the eraser; milestone 2 is
> split into 0.2.0-0.2.4, listed in the spec's Milestones). The extension is
> 1.3.1 (its eraser follows S/M/L). Waiting for Dave's review of 0.2.0.
> How it works: sections 8b (picking, the frame, moving, stretching, turning)
> and 8c (the eraser) of `index.html`.
>
> **Then 0.2.1:** arrow, line, rectangle, ellipse, text and sticky notes
> (section 8d, with the two fonts built in). **Then 0.2.2:** pictures and
> stamps (section 8e), and the phone rail folds its shapes. The extension is
> 1.3.2 (shared bar only).
>
> **Then 0.2.3:** copy, cut, paste, duplicate, front and back, lock, groups
> (double-click to work inside one) and the right-click menu (section 8f).
> **Then 0.2.4:** descriptions (alt text), the layers list, snapping and
> Line up (section 8g). That finishes milestone 2.
>
> **Then 0.3.0:** many pages and the filmstrip (section 8h). Milestone 3 is
> split in three (0.3.0 pages, 0.3.1 backgrounds and the grid, 0.3.2 step
> numbers; see the spec).
>
> **Then 0.3.1:** installable, with the splash (Dave asked for it early):
> `manifest.webmanifest`, `sw.js`, the icons (`make-icons.py` draws the
> PNGs from the same numbers as `icon.svg`), and `whtbrdr-thumb.webp` (the
> hub picture; the splash's `APP_HERO` is the same picture, smaller).
> **Then 0.3.2: Present mode** (section 8i): F5, full screen on black, the
> floating ink bar with the laser, spotlight and magnifier, B/W, and keep or
> take away the ink at the end.
>
> **Then 0.3.3:** backgrounds (dots, lines, graph paper), the coordinate
> grid and the background picture (section 8j).
>
> **Then 0.3.4:** step numbers across pages (section 8k), units (in, cm,
> mm, pt) in the Page section, and Escape in Present mode going back to the
> Pointer first. That finishes milestone 3. **Phone testing is on hold**
> until Dave has time: check builds on the desktop only. The extension is
> unchanged (1.3.2).
>
> **Then 0.4.0:** PDFs and pictures open as pages (section 8l), with the
> "Save it as a PDF first" dialog for Office files. **There are two
> editions now:** `index-online.html` is the SOURCE (edit it), and
> `python3 build-offline.py` makes `index.html` from it, with pdf.js
> (in `vendor/`) packed inside. Never edit `index.html` by hand. After
> `_edtr-suite/paste_whtbrdr_bar.py`, rebuild too.
>
> **Then 0.4.1:** the page pill over the filmstrip, DSKEDTR's look and
> feel (section 8h).
>
> **Then 0.4.2:** highlights that quote the PDF's words, the words for
> screen readers, Shift to snap a highlight to a line (end of section
> 8l); Present's Celebrate effects and a stronger magnifier (section 8i);
> copy, cut and paste pages (section 8h). That finishes milestone 4.
>
> **Then 0.4.3:** a big green check and a 3-2-1 countdown in Present mode
> (section 8i), fireworks that keep their colors on a light page, and
> "Mark up any PDF" in the Features tour.
>
> **Then 0.5.0:** saving and opening `.whtbrdr` boards, crash backups and
> "Pick up where you left off" (section 8m), and the file handler in the
> manifest.
>
> **Then 0.5.1:** Export: a PDF (PDF pages untouched, marks drawn on top
> as vector, words as words) or pictures (section 8n). pdf-lib and fontkit
> are in `vendor/` too now, and `make-export-fonts.py` keeps TrueType
> copies of the fonts in `index-online.html` (run it if the fonts change,
> then `build-offline.py`).
>
> **Then 0.5.2:** PDF marks kept editable (each a PDF annotation) or drawn
> in, both tagged for screen readers (section 8n: `pdfTags`,
> `exportUnits`, `annotKind`); the Export dialog's descriptions check with
> Go to it buttons; and three samples made in code (section 8o), the
> worksheet's PDF included. That finishes milestone 5.
>
> **Then 0.7.0:** the Accessibility tab beside the Inspector, with a
> top-bar count (section 8p): the checker, reading order you can change
> (`page.readOrder`), the color-vision preview; background pictures can be
> described; the Features tour is the planned five.
>
> **Then 0.7.1** (another session): the SUITE block pasted in again, with
> TELEDTR and WHTBRDR listed.
>
> **Then 0.7.2:** a fresh board's first page is the screen's shape and
> size ("Fit the screen", `screenPageSize` in section 3). Waiting for
> Dave's review of 0.7.2; next is 0.7.3 (PowerPoint export).

WHTBRDR is the suite's whiteboard and annotation app. The plan is in
`WHTBRDR-SPEC.md`. Milestone 1 was built in a chat as **0.1.0**
(`index.html` in this folder) without the WHTBRDR Chrome extension's source,
because chat could not reach it. This Cowork session's first job is to fold
the extension's annotation bar in, then carry on milestone by milestone.

## What is in this folder

| File | What it is |
| --- | --- |
| `00-START-HERE.md` | This file |
| `WHTBRDR-SPEC.md` | The full plan: pages, tools, step numbers, objects, filmstrip, Present mode, export, accessibility, security, milestones, open questions |
| `index-online.html` | The app's SOURCE since 0.4.0: edit this one. It fetches pdf.js from jsDelivr (SRI-pinned) when a PDF is opened |
| `index.html` | The offline edition, MADE by `build-offline.py` from `index-online.html`, with pdf.js inside. The site serves it. Don't edit it by hand |
| `build-offline.py`, `vendor/` | The build (checks the vendor files against their fingerprints first), and the libraries with their licenses: pdf.js 5.7.284, pdf-lib 1.17.1, @pdf-lib/fontkit 1.1.1 |
| `make-export-fonts.py` | Makes TrueType copies of the page's two fonts, kept in `index-online.html` for PDF export (needs fontTools and brotli) |

Put the folder at `productivity-suite/whtbrdr/` (the spec's source folder).

## Where 0.1.1 stands (2026-10-19)

Decided with Dave before building it:

- **Keys:** the extension's, which mostly agree with IMGEDTR's. 1-5 pick a pen and 6-9 a highlighter directly; P and H pick the tool; [ and ] the size (S, M, L). L line, K laser, S spotlight, M magnifier, O ellipse, E eraser. **N is step numbers** (as in IMGEDTR and PDFEDTR); sticky notes moved to **J ("jot")** in both. Stamps take **G** ("grade"). The spec's earlier L laser, S notes and M stamps were wrong and are fixed.
- **Colors:** the extension's five pens; the extension's three highlighters plus **blue on 9**, in both.
- **Size:** the extension's S/M/L for every tool. The app's Inspector keeps an exact size for the pen or highlighter (picking S, M or L lets it go).
- **Font:** Atkinson Hyperlegible is the default in both (Comfortaa the other).
- **Spotlight and magnifier** come to the app in Present mode (milestone 6). They were in the extension all along; the spec had missed them.
- Also as recommended: the app's smoothing, pressure and palm rejection now in the extension too; one Tab stop for the bar; 44px buttons on touch; a pressed tool is a tinted background with a ring (the shared bar's look; the suite's top-bar buttons keep their solid fill); the extension follows dark mode and keeps its blue until WHTBRDR's color is settled; highlights multiply on a light page and are 55% see-through on a dark one (the extension stays 55%).

Built in 0.1.1:

- The rail and the pill are the shared bar ("rail" layout): Pen and Highlighter on the rail (only the tools the app has so far), the tool's colors and S/M/L in the pill. On a phone the pill wraps to two rows.
- Fixes: a highlight being drawn no longer darkens where it crosses another (it is drawn into the highlight layer itself); a Shift straight line no longer jumps back at the end.
- The SUITE block is the master's; WHTBRDR's two entries are now in the master `suite-block.js` too (not pasted into other apps, as planned).
- Checked with Playwright: desktop 1366 x 768 light and dark, a 390 x 844 touch phone (finger drawing), simulated stylus pressure, keyboard only (Tab, F6, rail and pill arrows, Inspector radios), axe clean (light, dark, help, phone). The extension loaded unpacked in Chromium: draws, keys (9, ], 3, Shift line, J, Escape twice), stylus pressure, palm-rejection notice, Tab and arrows, dock left, light and dark, axe clean on its toolbar, toggling on and off.

Still Dave's to try: real stylus hardware, iPad Safari, the extension on his own pages (Gmail, Google Docs), screen readers.

## Where 0.1.0 stood

**Built and checked:**

- The suite shell: 52px top bar (New, Undo, Redo; Inspector, Theme, Help in the standard order), the tool rail, the Inspector, the status bar, the help panel (Features, Keyboard shortcuts, Getting started, About, Changelog, More apps), dark mode, F6 between areas, the phone layout with the Inspector as the bottom sheet with a grab handle.
- Five pens and four highlighters, picked from a floating pill on the board or with P / H and 1-5. Color and size per preset, kept in `whtbrdr.settings`. Highlights are drawn under ink with a multiply blend. Shift draws a straight line.
- Stylus pressure (variable-width outline), with smoothing. "A finger on the page" setting: draws until a stylus is used (default), always draws, or slides the page.
- Page sizes from the spec plus A4, square and custom (in or mm); Turn the page; Clear the page; page color; staging color (default DSKEDTR's `#eef1f4` / `#0f1115`).
- Zoom: Ctrl/Cmd + wheel and trackpad pinch around the pointer, Ctrl/Cmd + `+` / `-` / `0` (only with the pointer over the board or the board focused), two-finger pinch, the status-bar menu. Slide with the wheel, Space + drag, middle drag, arrow keys.
- Undo/redo for everything (whole-board snapshots, last 100), including Clear the page and New board.
- Checked with Playwright: desktop 1366 x 768 and a 390 x 844 touch phone (finger drawing, pinch, simulated stylus pressure), keyboard only (Tab, F6, radio arrows), and axe (no violations, light and dark, help panel too).

**Not done yet, on purpose:**

- **Saving.** No project files or crash backups until milestone 5; the browser asks before closing a tab with a drawing on it.
- **Installing.** No `manifest.webmanifest`, icons or `sw.js` until milestone 5. It runs from a disk or any web address as it is.
- **Select (V)** is not on the rail yet: there is nothing to select until objects arrive in milestone 2.
- **Splash.** Milestone 5. The Features tour has three drawings; five come later.

**Added beyond the spec (Dave has seen them; keep unless he says otherwise):**

- The floating pill of colors at the top of the board (a radio group).
- The size ring under a mouse or stylus.
- Clear the page, and New board as one undo step.

**Provisional:**

- **Color:** deep rose `#9f1239` (dark mode `#fda4af`) is a stand-in until Dave picks (see Open questions in the spec). To change it: `--brand` and `--suite-accent` in the CSS tokens, the `theme-color` meta tag, the favicon, the top-bar logo, and WHTBRDR's entries in `SUITE_APPS` and `SUITE_MARKS`.
- **Icon:** the spec's suggestion (a whiteboard on a stand, a marker stroke, an orange step badge).

## How 0.1.0 is put together

The file's header comment explains the whole thing. In short:

- **The SUITE block** (styles and script, between the `SUITE BLOCK v4` markers) was copied from **ANIMEDTR 0.22.1**, the newest app, because chat had no access to the master `_edtr-suite/suite-block.js`. Two changes were made in this copy only: WHTBRDR added to `SUITE_APPS` (with `listed: false`) and to `SUITE_MARKS`, and the block's comment listing the apps that carry it.
- **WHTBRDR's own code** follows the block, in 15 numbered sections (helpers, settings, page sizes, the board's data and undo, stroke shapes, drawing the board, the view, pointers, tools and presets, the Inspector, the status bar, New board, help/theme/sheet/keys, the Features tour and Changelog, start-up).
- **The data model:** `board = { app, version: 1, staging, pages: [{ id, w, h, color, items }] }`. Sizes are in points (72 to the inch, PDF's unit). A stroke is `{ id, type: 'ink' | 'highlight', color, size, pressure, pts: [[x, y, p], ...] }`. Milestone 2's objects should add types to `items` rather than a new list.
- **The rail's pens and highlighters** sit in a clearly marked part of the HTML and in sections 8-10 of the script. They were built to Dave's stated requirements (four or five pens, a few highlighters), not from the extension. That is the part to reconcile.

## First steps in this session (done 2026-10-19 - kept for the record)

1. **Read** `SUITE-STANDARD.md`, `WHTBRDR-SPEC.md`, then `index.html`'s header comment and sections 8-10. Ask Dave where the **WHTBRDR extension's source** lives, and read it.
2. **Compare** the extension's annotation bar with 0.1.0's: tools, presets (colors, sizes, names), icons, keys, how a stroke is drawn (smoothing, pressure, highlighter blend), and anything the extension has that 0.1.0 lacks. **Tell Dave what differs and which way each should go before changing anything.** Where they disagree, the extension is the starting point (the spec's rule), unless Dave says the app's version is better.
3. **Share the toolbar:** pull the agreed bar into `_edtr-suite/whtbrdr-bar.js` and `_edtr-suite/whtbrdr-bar.css`, between START and END markers like the SUITE block, and copy it into both the extension and `index.html`. Check the extension still works with the copy.
4. **Swap in the master SUITE block:** replace 0.1.0's ANIMEDTR copy with the master `suite-block.js` / `.css`, plus WHTBRDR's two entries (below). Add the same two entries to the master. Do **not** paste the block into the other apps: `listed: false` means they look the same either way, and they can take it at their next release.
5. **Release 0.1.1** with the reconciled bar (CHANGELOG entry in the file), check it with Playwright, and **stop for Dave's review.** Then milestone 2 (0.2.0), as the spec lists it.

Alongside, when Dave asks: PDFEDTR's step numbers and the extension's picture tool (spec: Changes to the extension and PDFEDTR).

## WHTBRDR's entries for the master SUITE block

In `SUITE_APPS`, after ANIMEDTR:

```js
  // WHTBRDR is being built (2026-10-19): listed: false keeps it out of the
  // other apps' lists until Dave says it is ready. Its color is not settled
  // (deep rose #9f1239 for now; indigo #3730a3 is the other candidate).
  { id: 'whtbrdr', name: 'WHTBRDR', color: '#9f1239', url: 'https://edtrapps.com/whtbrdr/', listed: false,
    blurb: 'A whiteboard: mark up PDFs and pictures, or draw on pages that work as slides.',
    icon: '<rect x="3" y="3" width="18" height="13" rx="2"/><path d="M8 21l1.5-5M16 21l-1.5-5"/><path d="M7 11.5c1.5-3 3-3 4-1s2.5 2 4-2"/>' }
```

In `SUITE_MARKS`, copy the `whtbrdr` line from `index.html` (search for `whtbrdr  :`). The `url` is a guess until the domain is settled (open question).

## Ways of working (Dave's)

- Build one milestone at a time and stop for his review after each.
- Surgical edits over full-file rewrites; heavily commented, beginner-readable code; hyphens, never em dashes.
- Security and privacy first, keyboard and screen-reader access from the start, touch-first on phones.
- Flag corrections and conflicts with suite conventions out loud, never as silent fixes.
- Verify with Playwright whenever it helps, without asking first.
- Not done by Claude, and Dave's to do: real stylus hardware, iPad Safari, VoiceOver, NVDA and ChromeVox.
