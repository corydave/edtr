# GAMEDTR — start here

A 2D game maker for kids and teens, built as the ninth app in the EDTR suite:
one self-contained HTML file, vanilla JavaScript, installable, works offline.

"GAMEDTR" is a working name (see open questions).

## The files in this handoff

| File | What it's for |
|---|---|
| `00-START-HERE.md` | This file: background, decisions so far, open questions, first steps |
| `01-FEATURES.md` | The full dream feature list, each item tagged with the phase it belongs to |
| `02-PHASE-1.md` | The spec for the first proof of concept: scope, architecture, security, build order, and a "done" checklist |

Bring these into the Cowork session too:

- `SUITE-STANDARD.md` (the family rules: layout, top bar, help panel, splash, backups, installing)
- `suite-block.js` and `suite-block.css` (the shared SUITE block, **version 4**, the master copies in `_edtr-suite`)
- `sw-update-check.js` (the handler every `sw.js` ends with)
- IMGEDTR's and SNDEDTR's `index.html`, if you want to borrow pixel-editing or audio code

## How we got here (the short version)

- **The question:** can modern browsers host a Godot/Unity/Roblox-style engine as a single-file offline app? Yes. Canvas 2D, WebGL2, Web Audio, the Gamepad API, IndexedDB, service workers and sandboxed iframes cover everything a 2D engine needs.
- **Not competing with Godot.** Godot already runs in the browser (compiled to WebAssembly), but it's tens of megabytes and aimed at professionals. The target here is closer to PICO-8, GB Studio, MakeCode Arcade and Construct.
- **Two apps, not one.** A 2D engine and a 3D engine share about a third of their code and differ in everything a person touches. So 2D and 3D get separate apps sharing a runtime "spine". **2D comes first.** 3D may never happen, and that's fine.
- **The caliber of game:** real, finishable games like a Game Boy–era Zelda, a Celeste-style platformer, a puzzle or story game. Not commercial Steam releases. A polished 15–30 minute game is the success case.
- **The audience:** younger kids and high schoolers, especially on locked-down school laptops and Chromebooks where Unity can't be installed. A URL that works offline, needs no account and exports a shareable file fits that world better than the big engines do.
- **Honest framing:** Dave isn't a game developer, and there's no confirmed user yet. So this is an **experiment first**: see how far a browser gets, build it well, and find a real user (a teacher or a class) along the way. Talking to one high-school CS or game-design teacher early would sharpen everything.

## Decisions so far

1. **2D engine first**, as its own app. A 3D engine would be a separate, later app.
2. **3DEDTR gets parked cleanly, not finished first.** The 2D engine doesn't depend on it. Tag its current state as a release, write "what phase two would have been" in its changelog, and make sure it's stable as it stands.
3. **Blocks first, code later.** Kids build logic with snap-together event blocks. A MakeCode-style blocks ↔ JavaScript toggle comes in phase 2. **Phase 1 runs no user-written code at all**, which keeps the security story simple.
4. **A JSON "spine" describes each game:** scenes, objects, behaviours, blocks, and assets. Versioned from day one.
5. **Phase 1 saves one project file** with its assets inside it. Folder-based projects (the File System Access API, or a Google Drive folder, for hopping between computers) come later, once projects outgrow one file.
6. **Every game exports as a single HTML file** that plays offline anywhere. This is the headline feature.
7. **Privacy is the selling point for schools:** no accounts, no tracking, no ads, no chat, no public gallery. Nothing leaves the device unless the kid chooses to share a file.
8. **The first POC should be polished**, not a rough demo. It's narrow (one genre, done properly) rather than broad.

## Open questions to settle in Cowork

- **Name.** GAMEDTR? GMEDTR? Something else in the EDTR pattern?
- **App colour.** Every suite colour so far is taken (orange, blue, green, gray, plum, teal, violet, bronze). Proposal: **crimson `#991b1b`** (8.3:1 with white text), dark-mode text **`#fca5a5`** (about 9:1 on near-black; check against the app's actual dark background). Plum is PDFEDTR's, so make sure the two read as clearly different side by side.
- **Project file extension.** `.gamedtr`? It's JSON inside either way.
- **Age target for the reading level.** "Around age 9" is the working assumption.
- **Starter art.** Draw an original starter pack (small, consistent, clearly licensed), or bundle an existing CC0 pack? Original is cleaner for licensing and offline size.
- **Phase 1 extras.** Does phase 1 get a guided tutorial "quest", or is a well-built template enough? (Currently marked as a stretch goal.)

## First steps in the Cowork session

1. Read `SUITE-STANDARD.md`, then `02-PHASE-1.md`.
2. Settle the name and colour, and add the app to `SUITE_APPS` and `SUITE_MARKS` in the master `suite-block.js`. That block then needs pasting into every app.
3. Build milestone 1 (the empty app shell, fully suite-compliant) before any game code.
