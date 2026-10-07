# GAMEDTR — phase 1: the polished proof of concept

## The goal in one sentence

A kid can open GAMEDTR, start from a platformer template, draw their own
character, paint a level, add coins and a hazard with blocks, make a jump
sound and a tune, press Play, and export the finished game as one HTML file
that a friend can open anywhere.

**Narrow and polished beats broad and rough.** Phase 1 does one genre (the
side-on platformer) and does it properly.

## The demo story (what "done" looks like from a kid's side)

1. The splash offers **New from template**, **New empty game**, **Open**, and **Pick up where you left off** (if there's a crash backup).
2. They pick the platformer template. It plays straight away: a cat that runs and jumps, coins, spikes, a goal flag, two levels.
3. They open the cat in the **pixel editor**, recolour it, and edit its walk animation.
4. They paint a new section of level with the **tile painter**. Edges auto-tile.
5. They drop in a new enemy with the **Patrol** behaviour.
6. They add a block: *When player touches enemy → lose 1 life, play [hurt]*.
7. They make the hurt sound with the **sound-effect generator** and tweak the level music in the **step sequencer**.
8. They press **Play**, test, press **Stop**, fix something, and play again.
9. They press **Export** and get `my-cat-game.html`, which opens offline on any computer, tablet or phone.

## In scope

### App shell (suite-compliant)
- Editor layout from `SUITE-STANDARD.md` §1: tool rail on the left, canvas in the middle, Inspector on the right, status bar along the bottom. On phones: rail along the bottom, Inspector as a sheet above it.
- Top bar right-hand end in the standard order (§2): Backup, Inspector, Theme, Help, with Install just before.
- Help panel (§3): Keyboard shortcuts, Getting started, About, Changelog, More apps.
- Splash, crash backups, credits (§4); install, `sw.js`, update check (§6).
- The SUITE block v4 pasted in unmodified, with GAMEDTR added to the master copy.
- Light and dark themes; the app colour on the wordmark and main buttons.

### Workspaces (rail tools)
The rail switches between workspaces. The Inspector shows settings for whatever's selected in the current one.

1. **Level** — the tile painter and object placement.
2. **Sprites** — the pixel editor and animations.
3. **Logic** — event blocks for the selected object type.
4. **Sound** — the sound-effect generator and step sequencer.
5. **Play** — runs the game in the sandbox (also on a top-bar button and a shortcut).

### Level editor
- Levels list (add, rename, reorder, delete); a game has one or more levels played in order.
- Tile painter: brush, eraser, fill, rectangle, eyedropper. Three layers: background, ground, decoration.
- Auto-tiling on the ground layer (a 16-tile, 4-neighbour set is enough for phase 1).
- Tile properties painted on per tile type: **solid**, **hurts**, **one-way platform**.
- Object placement: drag from a palette, snap to the grid, select, move, duplicate, delete.
- Camera follows the player, clamped to the level's bounds. Level size is set in the Inspector.
- Toggle to show collision boxes.
- Fixed game resolution (proposal: 320×180) drawn with integer scaling and no smoothing, so pixels stay crisp.

### Objects and behaviours
An **object type** (like "Coin") has sprites, one behaviour, some properties and its block scripts. Placed **instances** share their type.

| Behaviour | What it does | Inspector settings |
|---|---|---|
| Platformer player | Run, jump, gravity, collides with solid tiles, one-way platforms | speed, jump height, gravity, coyote time, jump buffer |
| Patrol | Walks back and forth, turns at walls and ledges | speed, turn at ledges yes/no |
| Collectible | Vanishes when the player touches it | points it's worth |
| Hazard | Hurts the player on touch | damage |
| Goal | Touching it finishes the level | — |
| None | Just decoration, or controlled only by blocks | — |

Built-in game state: **score** and **lives**, shown on a simple HUD. Losing all lives restarts the level; finishing the last level shows a win screen. The title screen is automatic (the game's name and "Press start").

### Event blocks (core set)
A Scratch-like editor with a small, fixed set of blocks. Blocks are **data, interpreted by the runtime** — never turned into JavaScript and evaluated.

- **When** (events): game starts · level starts · this touches [type] · [key/button] pressed · every [n] seconds.
- **Do** (actions): add [n] to score · lose/gain [n] lives · play sound [x] · remove this · remove other · go to next level · restart level · change speed of this · show message [text] for [n] seconds · spawn [type] here.
- **If** (one condition block): if score/lives is [>, <, =] [n].

Blocks must be operable by keyboard: choose from a menu, insert, move up/down, delete — not drag-only.

### Pixel editor and animation
- Pencil, eraser, fill, line, rectangle, colour picker, mirror horizontally/vertically, zoom grid.
- Sprite sizes 16×16 and 32×32. Tiles are 16×16.
- Three to four curated palettes; the game's palette is chosen per project.
- Frames with onion skinning and a speed slider. Named animations **idle**, **walk**, **jump**, **hurt** are picked up by the Platformer and Patrol behaviours automatically.
- Borrow from IMGEDTR where it helps.

### Sound
- **Sound-effect generator**, sfxr-style: presets for Jump, Coin, Hit, Explosion, Power-up, Laser, plus "surprise me" and a few friendly sliders (pitch, length, wobble). Each sound is stored as its settings, not as audio, so projects stay tiny.
- **Step sequencer**: a 16-step grid, four instrument rows (lead, bass, two drums), locked to one of a few scales, tempo slider. One looping pattern per song; one song per level (or none).
- All audio synthesised live with Web Audio, so there are no sample files to embed.
- Borrow from SNDEDTR where it helps.

### Play and export
- **Play** runs the game in a sandboxed iframe; **Stop** throws the sandbox away, so the editor's state is untouched.
- **Export** writes one HTML file containing the runtime plus the game's data. It opens offline with no network requests. Target: under 300 KB for the template game.
- Input: keyboard (arrows/WASD + space/Z), gamepads (standard mapping), and on-screen touch buttons that appear automatically on touch screens.
- The exported file's `<title>` is the game's name.

### Saving and safety nets
- **Save project** downloads a `.gamedtr` file (JSON with assets inside); **Open** reads one back.
- Unlimited undo/redo across all workspaces.
- Crash backups through `SuiteBackup`, per the suite standard.

### Template and starter art
- One platformer template: a cat, coins, spikes, an enemy, a goal flag, two short levels, a jump and coin sound, one tune.
- A small original starter pack of tiles, characters and items in one style, drawn as project pixel data (no image files, no licensing questions).
- **Stretch:** a short guided quest on the template ("Make your cat jump higher!"). Cut this first if time is short.

## Out of scope for phase 1

JavaScript/code view, custom variables and timers, messages between objects,
dialogue, save progress for players, custom scenes and transitions,
top-down and other genres, extra templates, rooms and parallax, ladders and
water, 64×64 sprites, photo import, particles, paper dolls, song arranger,
voice recording, reactive music, folder or Drive projects, teacher mode,
lesson packs, hint helper, badges, remix, QR codes, play-test replay.

## Architecture

### One file, two halves
- **The editor**: everything the kid touches.
- **The runtime**: the game engine (loop, physics, rendering, input, audio, block interpreter). It lives inside the editor as one clearly marked block of code, and is used in two places: the Play sandbox and the exported file. **One runtime, so what you test is exactly what you export.**

### The game loop
- Fixed 60 Hz update with an accumulator, rendering on `requestAnimationFrame`. Physics stays the same on fast and slow screens.
- Axis-aligned box collision against the tile grid (move X, resolve; move Y, resolve), plus box-vs-box overlap for touching objects.
- Canvas 2D rendering at the fixed resolution, scaled up by whole numbers, `imageSmoothingEnabled = false`.
- Sprites are decoded from pixel data into canvases once when a level loads.

### The project spine (JSON)
Versioned from day one, so later phases can upgrade old files. A sketch:

```json
{
  "format": "gamedtr",
  "schemaVersion": 1,
  "title": "My Cat Game",
  "settings": { "width": 320, "height": 180, "palette": "sunset16" },
  "sprites": {
    "cat": { "size": 16, "animations": { "idle": { "fps": 4, "frames": ["<indexed pixels>"] } } }
  },
  "tiles": { "grass": { "sprite": "grass", "solid": true, "autotile": true } },
  "objectTypes": {
    "Coin": { "sprite": "coin", "behaviour": "collectible", "props": { "points": 1 },
              "scripts": [ { "when": { "event": "touches", "type": "Player" },
                             "do": [ { "action": "playSound", "sound": "coin" } ] } ] }
  },
  "levels": [
    { "name": "Level 1", "width": 60, "height": 12, "music": "tune1",
      "layers": { "background": "<tile ids>", "ground": "<tile ids>", "decoration": "<tile ids>" },
      "objects": [ { "type": "Player", "x": 32, "y": 96 } ] }
  ],
  "sounds": { "coin": { "preset": "coin", "pitch": 0.6, "length": 0.2 } },
  "songs": { "tune1": { "tempo": 120, "scale": "major", "steps": "<grid>" } }
}
```

Pixel data is palette-indexed (one byte or hex digit per pixel), which keeps files small and makes palette swaps free.

## Security and privacy (designed in, not added on)

- **No user code in phase 1.** Blocks are data read by an interpreter with a fixed list of events and actions. There is no `eval`, no `new Function`, and no script building from strings.
- **The Play sandbox** is an `<iframe sandbox="allow-scripts">` with **no** `allow-same-origin`, loaded by `srcdoc`. It gets an opaque origin, so it can't reach the editor's DOM, IndexedDB, backups or other projects. Messages go both ways by `postMessage`; the editor accepts only messages whose `event.source` is that iframe's window, and checks each message's shape.
- **Exported games carry a strict CSP** in a `<meta>` tag: `default-src 'none'`, inline script and style only, `img-src data: blob:`. They can't make network requests even if someone edits the file.
- **Embedding game data safely:** the project JSON goes into the exported file inside `<script type="application/json">` with `<` escaped as `\u003c`, so no text in a game can close the script tag.
- **Opening a project file** goes through one validator: check the format name and schema version, check every field's type, clamp sizes (level dimensions, sprite counts, string lengths, total file size), drop anything unknown. The same validator runs on restored backups.
- **All text** a kid types (game title, messages, names) is rendered with `textContent` or drawn on the canvas, never inserted as HTML.
- **The app's own CSP** follows the suite pattern. There are no network calls except the service worker's own update check.
- **Nothing leaves the device** unless the kid saves or exports a file themselves. No analytics, no accounts, no telemetry.

## Accessibility

- Every tool and control is reachable and usable by keyboard, including painting (a keyboard cursor on the grid), placing objects, and editing blocks.
- Every icon button has an `aria-label` and a tooltip. Canvas areas have text alternatives: the status bar announces the cursor position, the selected tile and the selection.
- Visible focus rings everywhere. Respects `prefers-reduced-motion`.
- Colour is never the only difference (tile properties get patterns or icons in the editor, not just tints).
- Short, plain wording throughout, aimed at around age 9.

## Suggested build order

Each milestone ends with something that works and is committed as a version.

1. **Shell.** Suite layout, splash, help panel, theme, install, `sw.js`, update check, empty workspaces, the project model, save/open with the validator, undo/redo, crash backups.
2. **Runtime and Play.** Game loop, tile rendering, the Platformer player, keyboard input, the sandboxed Play mode, a hand-written test level.
3. **Level editor.** Tile painter, layers, auto-tiling, tile properties, object placement, the Inspector, the levels list, the camera.
4. **Behaviours and blocks.** Patrol, Collectible, Hazard, Goal, score and lives, the HUD, title and win screens, the block editor and interpreter.
5. **Pixel editor and animation.** Drawing tools, palettes, frames, onion skin, named animations.
6. **Sound.** Sound-effect generator, step sequencer, music per level.
7. **Export and input.** Single-file export with its CSP, touch buttons, gamepads.
8. **Template and polish.** Starter art, the platformer template, a keyboard and screen-reader pass, phone layout pass, performance check, help text, changelog. Then the guided quest if there's time.

## "Phase 1 is done" checklist

- [ ] The demo story above works start to finish, on a laptop and on a phone or tablet.
- [ ] The whole demo story can be done with a keyboard only.
- [ ] An exported game opens from disk with the network off, on Chrome, Firefox and Safari.
- [ ] The exported template game is under 300 KB.
- [ ] The game runs at a steady 60 fps on a basic school Chromebook.
- [ ] A malformed or hostile `.gamedtr` file is rejected cleanly with a friendly message.
- [ ] A game in the Play sandbox cannot read the editor's storage or send network requests (tested on purpose).
- [ ] The app passes the suite checklist: layout, top bar, help panel, splash, backups, install, update check.
- [ ] Someone who isn't Dave, ideally a kid, makes a change to the template and exports it without help.
