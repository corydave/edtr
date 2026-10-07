# GAMEDTR changelog

## 0.8.0 - 2026-09-30 (running)

Milestone 8 of phase 1: the guided quest, and a polish pass.

**The quest**
- "Make Cat Quest your own": seven small jobs in a box at the bottom left. 1 make the cat jump higher, 2 give the cat a new look, 3 paint more ground, 4 add another enemy, 5 make a new sound, 6 play the game, 7 export it.
- Each job ticks itself off when GAMEDTR sees it done: nothing to press. A ticked job stays ticked, even after Undo.
- Only the job being done now shows how to do it, with a Show me button that goes to the right workspace, tool and control (Show me for Play and Export just does it). The others show their short names, so the box stays small.
- Screen readers hear each job being ticked off, and what comes next.
- Start it from the splash (Take the quest), from Help, Getting started, or from the Sample games box. Starting it opens a fresh Cat Quest, and Undo brings back the game you had.
- On a phone it starts folded up, above the rail, and messages move up out of its way.

**Games seen from above**
- Corner help: walking into the edge of a wall with a gap within 7 pixels slides the player into the gap (never faster than walking), so a one-square corridor is easy to turn into. Tested from positions on either side of a gap, and with hundreds of random moves: the player never ends up inside a wall.

**The polish pass**
- The phase 1 demo story, done with the keyboard only: open a sample game, play it, recolour the cat, draw on its walk animation, paint ground, place a new beetle, add a Play the sound block to its rule, make a Hit sound, change the tune's speed and a note, play, stop, and export. Everything could be reached and used.
- Found and fixed: after switching workspace with 1 to 5 from a button in the old workspace, the focus was left on something hidden, so the next Tab went back to the top of the page (33 presses to reach the pixel editor; now 9). The focus now moves to the new workspace's rail button.
- Phone pass: every workspace and its Inspector sheet checked at 390 pixels wide; nothing scrolls sideways.
- Speed: with the computer slowed down six times (like a basic school Chromebook), all three sample games run at 60 frames a second, and a change in the editor (with everything redrawn) takes about 33 thousandths of a second.
- About now says what GAMEDTR makes (platformers, mazes, arcade games) and that games export as one web page.

## 0.7.0 - 2026-09-30

Milestone 7 of phase 1: export and input.

**Export**
- Export (the download button in the top bar, Export in the Play workspace, or Ctrl+E) saves the game as one `.html` file named after the game. It is the same page Play runs: the engine, the shared drawing and sound code, and the game's data, all inside.
- It opens from disk with the network off. Tested with every connection blocked: no requests at all. Cat Quest is about 100 KB (the target was under 300 KB).
- The page's own Content Security Policy (`default-src 'none'`, inline script and style only, `img-src data: blob:`) means it cannot connect anywhere, load anything, or send a form, even if someone edits the file. The game's data sits in a JSON block with `<`, `>` and `&` escaped, so no text in a game can break out of it.
- The file's title is the game's name. A game needs a player before it can be exported (GAMEDTR says so if not).
- In an exported game, Escape does nothing and the screen-reader words leave out "Escape to stop" (that is only for Play in GAMEDTR).

**Touch buttons**
- They appear by themselves on a phone or tablet, or the first time a finger touches a laptop's screen.
- Arrows on the left and a big Jump (A) on the right. Games seen from above get a four-way pad instead, and Jump only if a rule uses it. Action (B) appears when a rule uses the action button. A sound button turns sound off and on.
- A finger on a button holds it like a key. Several fingers work at once (run and jump). They keep clear of phone notches, and a long press does not open a menu.
- Tapping the game starts it, like Space.

**Gamepads**
- Any controller the browser knows (standard layout): left stick (with a dead zone) or d-pad to move, A / cross to jump, the other face buttons for Action, Start to start. Pressing a button also carries on after a pause.
- Keyboard, touch buttons and gamepads each keep their own list of what is held, and the game joins them every step, so letting go of one never lets go of another.
- Play in GAMEDTR lets its sandboxed frame use gamepads (and nothing more).

**Also**
- On a screen too small for 2x (a phone held upright), the game fills the space instead of staying at 1x.
- Cat Quest's first level is called Sunny meadow (it was "Test level").

## 0.6.0 - 2026-09-30

Milestone 6 of phase 1: sound.

**Sound effects**
- Seven buttons make a new sound each press: Jump, Coin, Hit, Explosion, Power-up, Laser and Surprise me.
- Change the one you picked: its kind, pitch (low to high), length (up to 2 seconds), wobble and loudness. Each change plays it. Try another makes one of the same kind that is a little different.
- A picture of the sound shows how long it is and how it fades (always 2 seconds wide, so longer sounds look longer).
- The Inspector lists the sounds, with rename (everything that plays it follows the new name), copy and delete (blocks that played it go too; Undo brings everything back). It says what plays each sound.

**Tunes**
- A grid of 16 steps: Lead and Bass (8 notes each, high at the top, one note per step) and two drums, Boom and Tss. Lit squares have a dot as well as a colour.
- Notes come from the tune's scale: Happy (major), Sad (minor), Easy (pentatonic) or Cool (blues). Speed 60 to 220 beats a minute; each step is half a beat.
- Play and Stop (P), with the step being played lit up. Changes are heard straight away. A new tune starts with a simple drum beat. Clear empties it (undoable).
- Keyboard: the grid is one Tab stop; the arrow keys move, Space or Enter taps, and each square says what it is ("Lead note 5, step 3: on").
- Each level's tune is picked in the Level workspace (Tune for this level), or with "Play it in the level" in the Sound workspace. The same tune carries on from one level to the next without starting again.

**Sounds in games**
- New job settings: Jump sound and Sound when it gets hurt (Platformer player), Sound when it gets hurt (Top-down player), Its sound (Collectible and Goal). Picking one plays it.
- The Play the sound block works.
- M turns all sound off and on while playing (the title screen says so when a game has sound). Sound pauses with the game.
- The sample games have sounds and a tune each: Cat Quest (jump, coin, ouch, extra life, flag), Gem Maze (gem, ouch, the portal) and Bee Garden (star, sting).

**How it works**
- Sounds and tunes are made while the game runs from their settings, sample by sample, by code in the shared block. The editor and the game use the same code, so what you hear while making it is what the game plays. No sound files: a sound is six numbers.
- A random-number maker with a seed means the same settings always give exactly the same sound.
- Tune notes are booked a tenth of a second ahead, so the beat stays steady when the page is busy.

## 0.5.1 - 2026-09-30

- Fixed: walking diagonally into a wall could pop the player through it. In Bee Garden the cat could walk through the hedges and end up outside the level. The collision check noted the thing's direction only after its first bump had already set its speed to 0, so the next square it touched "landed" it on top of the wall. The same mistake could lift a platformer player on top of a ceiling two squares wide. Direction is now noted before any squares are checked.
- Tested by walking at random through both top-down samples (hundreds of moves, with the enemies taken out) and checking that the player never overlaps a hedge.

## 0.5.0 - 2026-09-30

Milestone 5 of phase 1: the pixel editor and animation, plus sample games.

**The Sprites workspace (pixel editor)**
- Tools: Pencil (B), Eraser (E), Fill (F), Line (L), Box (R; hold Shift for a filled box) and Colour picker (I). Right-click with any tool rubs out.
- A whole stroke, line, box or fill is one step for Undo.
- Mirror drawing left and right (M) and top and bottom, with pink fold lines. Grid (G) with a stronger line every 8 pixels. Zoom (+ and -), which fits the space by default.
- Onion skin (O): the frame before shows faintly under the one you are drawing.
- A checkerboard shows see-through pixels. The status bar says which pixel is under the mouse and its colour.
- Keyboard: the arrow keys move a pixel cursor (Shift moves 4), Space or Enter uses the tool, holding Space with the Pencil draws as you move, Line and Box take Enter at each end, and [ and ] change colour. Screen readers hear the pixel and its colour.

**Animations and frames**
- Named animations the jobs already know: Standing still (idle), Walking (walk), Jumping (jump) and Hurt (hurt, shown just after losing a life). Auto-tile edges (auto) shows too, for tiles that have hand-made edges.
- Each animation has its own speed (1 to 30 frames a second) and a small moving preview that can be paused. It starts paused for people who ask for less motion.
- Frames: add (a copy of the one you are on), move earlier or later, delete. Previous and next frame with , and .
- Flip the frame across or upside down, or clear it.

**Pictures and colours**
- The Inspector lists every picture. New 16 by 16 or 32 by 32, copy, rename (tiles and things that use it follow the new name) and delete (Undo brings it back). It says which tiles and things use each picture.
- Four colour sets for the whole game: Sunset, Meadow, Ocean and Candy. Every number keeps the same job in each set (0 is the darkest outline, 12 is white...), so changing the set recolours the game and keeps it looking right.
- Level workspace: New tile makes a solid tile with its own picture, and Draw it jumps straight to a tile's or thing's picture.

**Games seen from above**
- A new job, Top-down player: the arrow keys walk in any direction, with no gravity or jumping. Patrols in those levels do not fall either.
- Patrols have a new setting, Walks: Side to side, or Up and down.
- The title screen and the screen-reader words say "arrow keys walk" in these games.

**Sample games**
- The test level is now Cat Quest, one of three sample games. Play a sample game on the splash, the Play workspace and Help's Getting started open a chooser. Opening one can be undone, like opening a file.
- Cat Quest (platformer): coins, beetles, spikes and a flag, over two levels.
- Gem Maze (top-down maze): find 5 gems in a hedge maze while bats patrol across and up and down, then step into the portal. The portal's rule shows "if" blocks: too few gems says "Find all 5 gems first!".
- Bee Garden (arcade): flowers grow a star every 4 seconds, stars fade after 5, bees speed up every 8 seconds, and 15 stars wins. Shows "every few seconds", making new things and a thing that removes itself.
- New starter art for them: a stone path, grass, a hedge, a gem, a bat, a portal, a flower, a star and a bee.

**Also**
- Messages shown in a game ("Find 5 gems, then the portal!") are read out to screen readers too.
- Decided: a first-person view (a kid-friendly maze or explorer, no guns) comes after phase 1. It is noted in 01-FEATURES.md.

## 0.4.0 - 2026-09-30

Milestone 4 of phase 1: behaviours and blocks.

**The Logic workspace (blocks)**
- Pick a thing ("Rules for"), then Add a rule. A rule is a When block and a list of Do blocks, done top to bottom.
- When blocks: this touches a (thing), the game starts, a level starts, the (button) button is pressed, every (n) seconds.
- Do blocks, in colour families that each have their own icon too: Score and lives (add to the score, lose lives, get more lives), Things (remove this thing, remove the thing it touched, make a new thing here, change its speed), Words and sounds (show words for n seconds; play a sound, switched on once the Sound workspace arrives), The level (finish the level, start it again) and Checking ("If the score is more than 10", with blocks inside; a check can hold one more check).
- Blocks read as sentences with blanks: lists to pick from and number or word boxes. A block cannot be written wrong, and the numbers are kept in range.
- All from the keyboard: every blank is a normal form control; each block and rule has Move up, Move down and Delete buttons; Add a block and Add a rule open keyboard menus (arrows, Enter, Escape). The focus stays on the right control after every change.
- Each thing's card says what its job already does by itself, so kids know when no blocks are needed.
- Blocks are data read by the engine; nothing is ever turned into code.

**Every job works**
- Patrol walks back and forth, turning at walls, the level's edges and (if chosen) ledges.
- Collectible adds its points to the score and disappears. Hazard costs lives. Goal finishes the level.

**Score, lives and screens**
- Score and lives at the top of the screen (lives with a heart).
- Losing a life: a little hop, "OUCH!", and a moment of safety while the player blinks (see-through instead, for people who ask for less motion). Tiles that hurt, hazards, falling out of the level and "Lose lives" blocks all use it.
- No lives left: "OH NO!", then the level starts again with full lives and the score it started with.
- Finishing a level: "LEVEL COMPLETE!", then the next level with its name shown. After the last one: "YOU WIN!" with the score, and Space plays again.
- Lives at the start (1 to 9) is a setting under Your game; the file stores it.
- Screen readers hear the state changes, lives lost, and the score now and then (not every coin).

**Also**
- The test game has coins, two beetles, a flag, a second level, and example rules: the beetle's "When this touches a Player: Lose 1 lives", an extra life at 10 coins, and a message when the game starts.
- Tested: 361 things in one level run at 60 frames a second here.

## 0.3.0 - 2026-09-29

Milestone 3 of phase 1: the Level editor.

**Painting tiles**
- Tools: Brush (B), Eraser (E), Fill (F), Rectangle (R), Eyedropper (I), plus Place things (P), Select (V) and Hand (H). A brush stroke is one step for Undo, however many squares it paints; a fast stroke leaves no gaps.
- Three layers, with words kids know: Behind (scenery), Ground (what you stand on and bump into) and In front. L cycles them.
- Auto-tiling: a tile with Auto-tile on looks at its four neighbours and outlines its open edges and rounds its corners. A tile can also carry its own 16 pictures (an "auto" animation); the test level's ground uses that to grow grass on top. Both the editor and the game use the same code for this.
- Tile jobs, painted on per tile type: Solid, One-way (switching it on switches Solid off) and Hurts. Show tile jobs (T) marks them on the map with the same marks as Play's collision boxes: a red outline, a yellow top bar and an orange X, so colour is never the only clue.
- Zoom (1x to 6x, + and -, or Ctrl + mouse wheel), a grid (G), and the middle mouse button or the Hand to look around. The map opens at the player, and keeps the ground in view when it changes size.

**Things**
- Place things by picking one in the Inspector and clicking the level, or by dragging it on with a mouse. Things snap to the grid; hold Alt (Option) to move them freely.
- A level has one player: placing a player moves the one already there.
- Select a thing to move it, face it left, copy it (Ctrl+D) or delete it (Delete).
- Make new things, copy them, rename them (every placed one follows) and delete them. Each has a picture, a job (Player, or "just for looks"; the other jobs arrive next version) and the job's settings as sliders: running speed, jump height, gravity, plus late-jump and early-jump times under More settings.

**Levels**
- The Inspector's level list: add (with a strip of ground ready), copy, move earlier or later, rename and delete. Arrow keys move through the list, F2 renames.
- Level size: a level grows or shrinks on the right and at the top, so its ground stays put; things left outside are removed (Undo brings them back).
- The sky colour, chosen from the palette (for every level).

**The keyboard**
- The map has a square cursor: arrow keys move it (Shift: 4 squares), Space or Enter uses the tool, holding Space with the Brush paints as you move, the Rectangle takes two presses (one per corner), and Select picks a thing up, carries it with the arrows and puts it down (Escape cancels). The status bar and screen readers are told what is at each square.
- Tools, tiles, things, layers and sky colours are radio groups (arrow keys move and choose); the level list is a list box.

**The game**
- Hurts tiles work in the game: touching one sends the player back to the start with an "OUCH!" (until lives arrive in the next version).
- The engine now draws auto-tiles, and Play starts at the level you were building.

**Under the hood**
- A new shared block (`<script id="gamedtrShared">`) holds the palettes, picture painting, auto-tiling and the pixel font. It runs in the editor and is copied into every game's page before the engine, so the editor and the game can never draw a level differently.
- Measured on the largest allowed level (512 x 128 squares): about 6 ms to draw the map, 11 ms for a change, 33 ms to flood-fill it all.

## 0.2.0 - 2026-09-29

Milestone 2 of phase 1: the runtime and Play.

**Play**
- Press Play (the top-bar button, the Play workspace, or Ctrl+Enter) and your game runs right inside GAMEDTR. Stop (or Escape inside the game) throws it away, so every Play starts fresh and nothing the game did can change your project.
- The game runs in a sandboxed frame (`sandbox="allow-scripts"`, no `allow-same-origin`, loaded with `srcdoc`). It gets an anonymous origin, so it cannot read the editor's page, its storage, the crash backups or other games. Its page carries its own stricter security policy (`default-src 'none'`), so it cannot make network requests either. Tested on purpose: reading the parent page, localStorage, IndexedDB, fetch (to GAMEDTR's own server and to the web), images from the web, pop-ups and navigating the editor away are all blocked.
- The editor's own policy did not need loosening: `frame-src 'none'` stays, because a `srcdoc` frame is not loaded from any address.
- The game's page is built by `buildGameHtml`, the same function Export will use: the game's data goes in as JSON with `<`, `>` and `&` escaped, so no text in a game can break out of its `<script>` element.
- Play options: Start at (any level) and Show collision boxes (solid tiles in red, one-way platform tops in yellow, each thing's box dotted).
- A game with no player shows a friendly card instead, with a button for the test level.
- The editor only listens to messages from its own game frame, and only three kinds (ready, state, exit/error), each checked.

**The engine (the runtime)**
- One engine, kept in `index.html` as text (`<script type="text/x-gamedtr-runtime">`, which the browser does not run), copied into each game's page.
- A fixed 60-steps-a-second game loop with an accumulator, so jumps are the same height on any screen. Measured at a steady 60 fps.
- Crisp pixels: a 320 x 180 screen scaled up by whole numbers, no smoothing. Sprite frames are painted once, at the start.
- Tiles on three layers (background, ground, decoration); solid tiles and one-way platforms; the sides of the level are walls; falling out of the bottom puts you back at the start.
- The Platformer player: running with acceleration, jumping (hold for a higher jump, tap for a hop), gravity, walls and ceilings, coyote time and a jump buffer, Down + Space to drop through a one-way platform, walk, jump and idle animations, and facing left or right.
- Each thing's collision box is worked out from the drawn part of its picture, so it fits whatever a kid draws.
- A camera that follows the player smoothly (and snaps instead, for people who ask for reduced motion), staying inside the level.
- A title screen with the game's name, a pause when the game loses focus, and a 3 x 5 pixel font for words in the game. Screen readers are told what is on screen.
- Keys: arrows or WASD to move, Space, Up, W, Z or K to jump; X or J for the action button (used by later versions).

**Also**
- A test level to play (a cat, bricks, one-way planks and three gaps), from the splash or the Play workspace, until the Level workspace arrives. Loading it is undoable.
- The splash now offers New empty game, Open a game and Try the test level.
- The game file stores a sky colour (`settings.background`, one palette colour).
- The Keyboard shortcuts tab lists the game controls.

## 0.1.0 - 2026-09-29

First release: milestone 1 of phase 1, the empty shell. No game code yet.

**The shell**
- The family's editor layout: a workspace rail on the left, the workspace in the middle, the Inspector on the right and a status bar along the bottom. On a phone the rail runs along the bottom and the Inspector opens as a sheet above it.
- Five workspaces on the rail: Level, Sprites, Logic, Sound and Play. Each rail button has a short word under its icon (GAMEDTR is for readers around age 9). Until a workspace is built, it shows a card saying what it will be for.
- The top bar: New, Open, Save, Undo, Redo and a big Play button, then the family's Install, Inspector, Theme and Help buttons in the standard order. Every button has a tooltip that also shows when you Tab to it.
- Light and dark themes in GAMEDTR's crimson (`#991b1b`, with `#fca5a5` for text in dark mode).
- The family's splash (New empty game, Open a game, Pick up where you left off), the Help panel (Keyboard shortcuts, Getting started, About, Changelog, More apps), crash backups, installing and the update check.

**Your game file**
- The `.gamedtr` project format, schema version 1: one JSON file with the whole game inside (sprites as palette-indexed pixel strings, tiles, object types with their blocks, levels, sounds and tunes).
- One checker (`validateProject`) for every file and every restored backup. It checks the format and version, the type of every field, clamps numbers, caps sizes, drops anything unknown or badly named (including `__proto__` and similar), and fixes broken links, then says how many small problems it fixed. Files that are not GAMEDTR games, are damaged, or come from a newer GAMEDTR get a short, friendly message.
- Name your game in the Inspector; Save downloads `your-game-name.gamedtr`; Open (or dropping a file on the window, or opening it from the desktop once installed) reads one back.

**Safety nets**
- Undo and redo for every change, including New and Open, so starting over never loses anything. Typing a name counts as one step. The history keeps the last 500 changes.
- Crash backups through the shared block: kept in this browser only, removed when you save, and offered back (splash and top-bar icon) only if a session ended without saving.

**Security and privacy**
- A strict Content-Security-Policy from the first line: no eval, no `new Function`, no outside scripts, no frames, and no network requests except the update check to GAMEDTR's own site.
- All typed text is shown with `textContent`, never as HTML.

**Family**
- GAMEDTR added to the master shared block (`SUITE_APPS` and `SUITE_MARKS`), and the splash's row of apps now fits the eight others on one line (the splash is 660px wide) and 4 + 4 on a phone. The other eight apps still carry the older copy of the block.
