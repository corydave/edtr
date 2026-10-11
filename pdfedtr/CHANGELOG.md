# PDFEDTR changelog

Newest first. The short form of each entry also lives in the `CHANGELOG`
table inside `index.html` (shown in Help > Changelog), so the tab still works
offline and opened straight off a disk. A new release goes in both.

The version lives in one place - `APP_VERSION` in `index.html` - which fills in
the badge beside the wordmark and the help panel. After editing `index.html`,
run `build-offline.py` to regenerate `pdf-offline.html`; never hand-edit the
offline file.

Releases before 1.4 went out without notes. Rather than guess at them, this
file starts at 1.4.

## 1.12 - 2026-10-10 - A new splash

- **A picture of PDFEDTR in use across the top of the splash** - the same picture as on edtrapps.com, built into the app (as a data: URI), so it shows offline too. With it, the small icon beside the name goes, since the picture already shows it.
- **Every way to begin is a card with a picture:** a folder opening for Open (the icon everybody knows), and pictures of their own for the rest.
- **"Pick up where you left off" is smaller and quieter:** a slim row under the cards rather than the big first button. It still only appears when the last session ended without saving, and the app's main way to begin keeps the focus.
- **Links to edtrapps.com and GitHub** under the credits (on the splash and in About): "All the apps at edtrapps.com - Free and open source on GitHub (MIT license)".
- The splash is a little wider (760px) with the picture; on a phone the cards stack in one column. The shared SUITE block was pasted in again from `_edtr-suite`.

## 1.11 - 2026-10-10 - A tour of the features

- **Features, a new first tab in Help:** an animated tour of five of PDFEDTR's favorite features - Turn any PDF into a form, Clickable checkboxes, Draw your signature, Rearrange and merge pages and Highlight, note and date - each with a small looping drawing, a title and a sentence or two. Previous and Next, the dots, or the Left and Right arrow keys move between them; the animation has a pause button, and it starts paused when the device asks for less motion.
- **? or F1 and the Help button now open Help on Features.** Keyboard shortcuts is one tab over.
- **The splash has a "See what PDFEDTR can do" card** that opens the same tour over the splash.
- The shared SUITE block was pasted in again from `_edtr-suite` (new: `renderSuiteFeatures`, `suiteFeaturesOpen`, `suiteFeaturesCard` and their styles). The drawings are inline SVG with SVG's own animation tags, so they work offline and straight off a disk.

## 1.10 - 2026-10-07 - DSKEDTR joins the family

- **DSKEDTR joins the family.** More apps and the splash's row of apps now include DSKEDTR (dskedtr.app), the new desktop publishing app: newsletters, flyers and booklets, with text that flows between boxes, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js`.
- The splash's row now fits nine apps: the eight others on one line on a computer, and 4 + 4 on a phone (shared styles pasted in again from `_edtr-suite/suite-block.css`).

## 1.9 - 2026-10-03 - Links to the other apps

- Names of the other apps in Help (in the changelog, About and the guides) are now links that open that app. Each link opens in a new tab; this app's own name stays plain. Shared SUITE block: new `suiteLinkApps()` (called from `renderSuiteApps()`, so no app wiring needed).

## 1.8 - 2026-09-29 - 3DEDTR joins the family

- **3DEDTR joins the family.** More apps and the splash's row of apps now include 3DEDTR (3dedtr.app), the new 3D modeling app with shape merging, ready for 3D printing, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js`.
- The splash's row now fits eight apps: the seven others on one line on a computer, and 4 + 3 on a phone (shared styles pasted in again from `_edtr-suite/suite-block.css`).

## 1.7 - 2026-09-28 - VCTREDTR joins the family

- **VCTREDTR joins the family.** More apps and the splash's row of apps now include VCTREDTR (vctredtr.app), the new vector drawing app with PowerPoint-style shape merging, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js`.
- The row of apps on the splash is now an even grid (shared styles pasted in again from `_edtr-suite/suite-block.css`), so the six others fit on one line on a computer, and 3 + 3 on a phone.

## 1.6 - 2026-09-26 - Installable, offline, updates

- **Install PDFEDTR as an app.** An Install button appears in the top bar, and **Install app** on the splash, whenever the browser can install it (Chrome, Edge and friends, desktop and Android). On iPhone and iPad the splash explains Share, then Add to Home Screen; in Safari on a Mac, File, then Add to Dock.
- **A real manifest and a service worker.** The manifest used to be a data: URI inside the page, which browsers do not treat as installable - that is why PDFEDTR was the one app with no Install. `build-icons.py` now writes `manifest.webmanifest`, `icon-192.png`, `icon-512.png` and `icon-maskable-512.png` beside `index.html` (upload them with it), and runs from its own folder. The new `sw.js` keeps the app, PDF.js and pdf-lib, so the installed app opens with no network. The page itself is network-first, so uploading a new `index.html` is still the whole deploy.
- **Check for updates on the splash.** The foot of the splash shows the version and asks the server whether a newer one is out; when there is, **Update now** loads it. The question goes through the service worker (`sw.js` now answers a `suite-check-update` message), which fetches `index.html` with `cache: 'no-store'` and reads its `APP_VERSION`. Nothing else is sent.
- Dave Ghidiu's name in the credits now links to his website, daveghidiu.com.
- Shared SUITE block moves to v4 (`SuiteInstall`, `SuiteUpdate`, the author link).

## 1.5.1 - 2026-09-26

- More apps and the splash now show each app's real icon, instead of a simple drawing on a coloured square. The icons live in the shared block as `SUITE_MARKS` (data: URIs, so they work offline).

## 1.5 - 2026-09-25 - New layout, splash, crash backups

- **Layout matching IMGEDTR.** The toolbar is now a tool rail down the left; Open, undo/redo, zoom, Add pages and Download sit in the top bar; the page thumbnails are a filmstrip under the page; and a new **Inspector** on the right holds the selected element's settings (they used to float beside it) and the radio-button fields (they used to float too). The Inspector button shows or hides it; on a phone it is a drawer, and the tools run along the bottom. The app now fits a phone screen.
- **Filmstrip keys:** Left/Right move between pages, Alt+Left/Right moves a page. **Tool rail:** Up/Down move between tools.
- **Splash screen** at start-up (Open a PDF), with the rest of the family underneath. Skipped when a PDF is opened straight into the app.
- **Crash backups.** The PDF (with any added pages) and everything placed on it are kept in this browser while you work. Downloading clears it, so a backup is only offered after a crash or a closed tab - on the splash, and as a backup icon in the top bar.
- **Credits** in About: made by Dave Ghidiu with Claude, provided by FLX AI Hub and Finger Lakes Community College.
- **Em dashes:** the tooltips and messages set from code still had them (1.4 only caught the ones in the HTML). Now hyphens.
- **Its own colour: plum** (`#8a1c5c`, 8.8:1 with white), in place of amber. The icon, wordmark, Download button and highlights follow it; dark mode uses a light plum (`#f4b3d8`) with dark text on it. `icon.svg` and `build-icons.py` (theme colour) are updated and the icon block regenerated.

## 1.4 - 2026-09-25 - Family alignment

- **Help panel** (new): the ? button beside the theme toggle, or press `?` or
  `F1`. Four tabs - Keyboard shortcuts, About, Changelog, More apps - the same
  four, in the same order, as every app in the family. App shortcuts stand
  down while it is open, so arrows move between tabs instead of nudging the
  selection or changing page behind it.
- **More apps** lists the rest of the family (TXTEDTR, PDFEDTR, IMGEDTR,
  SNDEDTR, VIDEDTR, SCRNCSTR) with this app marked "You are here". It is the
  shared SUITE block, pasted identically into every app, so it needs no
  network. Clicking the logo opens it directly.
- **Theme button** uses the family's sun and moon icons, and its name now says
  where it will take you ("Switch to dark mode"). It also sets `data-theme` on
  `<html>` alongside the existing `dark` class, which is what the shared More
  apps styles read.
- **Tooltips** use hyphens instead of em dashes ("Select - Esc", "Undo -
  Ctrl+Z" and four more), and so do three screen-reader labels.
- **Version** comes from a single `APP_VERSION` constant.
- **Renamed** `pdf.html` to `index.html`, matching the other apps, so the
  server serves it at the folder's address. `build-offline.py` and
  `build-icons.py` now read `index.html`. The offline build is still
  `pdf-offline.html`.
- **`icon.svg`** had picked up an 8 KB content-credentials (C2PA) metadata
  block again on the way down from a chat; stripped back to the clean 648-byte
  file. The HTML embeds its own icons, so the app was never affected.
