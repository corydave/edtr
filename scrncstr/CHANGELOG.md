# SCRNCSTR changelog

Newest first. The short form of each entry also lives in the `CHANGELOG`
table inside `index.html` (shown in Help > Changelog), so the tab still works
offline and opened straight off a disk. A new release goes in both.

Releases before 1.18.0 went out without notes. Rather than guess at them, this
file starts at 1.18.0; `README.md` describes how everything works as of 1.17.0.

## 1.20.4 - 2026-10-07 - DSKEDTR joins the family

- **DSKEDTR joins the family.** More apps and the splash's row of apps now include DSKEDTR (dskedtr.app), the new desktop publishing app: newsletters, flyers and booklets, with text that flows between boxes, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js`.
- The splash's row now fits nine apps: the eight others on one line on a computer, and 4 + 4 on a phone (shared styles pasted in again from `_edtr-suite/suite-block.css`).

## 1.20.3 - 2026-10-03 - Links to the other apps

- Names of the other apps in Help (in the changelog, About and the guides) are now links that open that app. Each link opens in a new tab; this app's own name stays plain. Shared SUITE block: new `suiteLinkApps()` (called from `renderSuiteApps()`, so no app wiring needed).

## 1.20.2 - 2026-09-29 - 3DEDTR joins the family

- **3DEDTR joins the family.** More apps and the splash's row of apps now include 3DEDTR (3dedtr.app), the new 3D modeling app with shape merging, ready for 3D printing, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js`.
- The splash's row now fits eight apps: the seven others on one line on a computer, and 4 + 3 on a phone (shared styles pasted in again from `_edtr-suite/suite-block.css`).

## 1.20.1 - 2026-09-28 - VCTREDTR joins the family

- **VCTREDTR joins the family.** More apps and the splash's row of apps now include VCTREDTR (vctredtr.app), the new vector drawing app with PowerPoint-style shape merging, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js`.
- The row of apps on the splash is now an even grid (shared styles pasted in again from `_edtr-suite/suite-block.css`), so the six others fit on one line on a computer, and 3 + 3 on a phone.

## 1.20.0 - 2026-09-26

- **Installing:** the top-bar Install button now runs on the shared `SuiteInstall`, so it and the splash's new **Install app** share the browser's one-time install prompt. On iPhone and iPad the splash explains Share, then Add to Home Screen; in Safari on a Mac, File, then Add to Dock.
- **Check for updates on the splash.** The foot of the splash shows the version and asks the server whether a newer one is out; when there is, **Update now** loads it. The question goes through the service worker (`sw.js` now answers a `suite-check-update` message), which fetches `index.html` with `cache: 'no-store'` and reads its `APP_VERSION`. Nothing else is sent.
- Dave Ghidiu's name in the credits now links to his website, daveghidiu.com.
- Shared SUITE block moves to v4 (`SuiteInstall`, `SuiteUpdate`, the author link).

## 1.19.1 - 2026-09-26

- More apps and the splash now show each app's real icon, instead of a simple drawing on a coloured square. The icons live in the shared block as `SUITE_MARKS` (data: URIs, so they work offline).

## 1.19.0 - 2026-09-25

- **Splash screen** at start-up, with the rest of the family underneath. One button (Set up a recording): SCRNCSTR has no file to open and nothing to back up, since recordings stream straight to disk.
- **Credits** in About: made by Dave Ghidiu with Claude, provided by FLX AI Hub and Finger Lakes Community College.
- **Its own colour: teal** (`#00565d`, 8.4:1 with white), in place of blue. The icon, wordmark and main buttons follow it; dark mode uses a light teal (`#7fd8de`). The icons and the manifest's theme colour are redrawn.
- **Fixed:** in dark mode, buttons filled with the accent colour had white text at 2.9:1. They now use dark text on the light fill (11:1).

## 1.18.0 - 2026-09-24 - Family alignment

- **One help panel** with four tabs - Keyboard shortcuts, About, Changelog,
  More apps - replacing the separate shortcuts and About dialogs. Same tabs,
  same order, as every app in the family.
- **Help button moved** to the right-hand end of the header, where it sits in
  every other app. The keyboard icon beside the wordmark is gone; the one in
  the recording bar stays and opens the Keyboard shortcuts tab. `F1` opens the
  panel as well as `?`.
- **Theme button** (new): light or dark by hand. It starts out following the
  system and remembers a choice in `localStorage` under `scrncstr.theme`,
  kept apart from the other settings so a missing or odd value just means
  "follow the system".
- **More apps tab** (new): the rest of the family - TXTEDTR, PDFEDTR, IMGEDTR,
  SNDEDTR, VIDEDTR, SCRNCSTR - from the shared SUITE block, which is pasted
  identically into every app and needs no network. The logo opens it directly.
