# GAMEDTR

A 2D game maker for kids and teens, the ninth app in the EDTR family.
One self-contained `index.html` (HTML, CSS and JavaScript), vanilla
JavaScript, no dependencies. Installable, works offline, no account,
nothing uploaded.

Live address (planned): https://gamedtr.app/

## What is in this folder

| File | What it is |
|---|---|
| `index.html` | The whole app. |
| `manifest.webmanifest` | Makes it installable, and lets the installed app open `.gamedtr` files. |
| `sw.js` | The service worker: offline support, network-first for the page, and the family's `SUITE UPDATE CHECK` at the end. |
| `icon.svg`, `make-icons.py` | The mark and the script that draws every PNG icon from it (`python3 make-icons.py`, needs Pillow). |
| `icon-*.png`, `apple-touch-icon.png`, `favicon-32.png` | The icons. |
| `CHANGELOG.md` | The long changelog. The short one is `CHANGELOG` inside `index.html`. |
| `00-START-HERE.md`, `01-FEATURES.md`, `02-PHASE-1.md` | The plan. |

## Releasing a version

1. Bump `const APP_VERSION = '...'` in `index.html` (keep that line's exact form: the update check reads it).
2. Add the release to `CHANGELOG` in `index.html` and to `CHANGELOG.md`.
3. Upload all the files.

## The shared block

`index.html` carries an exact copy of the SUITE BLOCK v4 (script and
styles, between the START and END markers), from `../_edtr-suite/`.
Never edit that copy on its own: change the master, then paste it into
every app.

## How Play works

`index.html` holds three scripts:

- **The shared block** (`<script id="gamedtrShared">`): palettes, painting
  pictures, auto-tiling and the pixel font. It runs in the editor, and is
  also copied into every game, so both draw levels the same way.
- **The editor** (the main `<script>`), which you use to build a game.
- **The runtime** (`<script type="text/x-gamedtr-runtime" id="gamedtrRuntime">`),
  the game engine. The browser does not run it in the editor. `buildGameHtml()`
  copies it, as text, into a complete page with the game's data, and Play runs
  that page in a sandboxed frame. Export saves the same page as a file,
  so what you test is exactly what you share.

## Where phase 1 stands

- Milestone 1 (the shell): 0.1.0.
- Milestone 2 (the runtime and Play): 0.2.0.
- Milestone 3 (the Level editor): 0.3.0.
- Milestone 4 (behaviours and blocks): 0.4.0.
- Milestone 5 (the pixel editor and animation, the Top-down player and
  three sample games): 0.5.0.
- Milestone 6 (sound: sound effects, tunes, music per level): 0.6.0.
- Milestone 7 (export, touch buttons, gamepads): 0.7.0.
- Milestone 8 (the guided quest and a polish pass): 0.8.0.
- Phase 1's build order is done. Left on the "phase 1 is done" checklist:
  test an exported game in Firefox and Safari, try it on a real phone
  or tablet and a basic Chromebook, and watch someone who isn't Dave (a
  kid, ideally) change the template and export it without help.
