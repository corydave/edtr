# GAMEDTR — full feature list

Everything that would make GAMEDTR a serious option for a kids' or teens'
game-design programme. Each item is tagged with the phase it's planned for:

- **P1** — the polished proof of concept (detailed in `02-PHASE-1.md`)
- **P2** — more genres, and real code
- **P3** — classrooms and bigger projects
- **P4** — delight and community

Phases 2–4 are a rough order, not promises. Re-sort them once there's a real user.

## Guiding principles (all phases)

- **First game in 10 minutes.** A kid opens it, picks a template, presses Play, and changes something they can see straight away.
- **Low floor, high ceiling.** Blocks for everyone; real code behind a door for the kid who outgrows them.
- **Nothing can be broken permanently.** Unlimited undo, autosave, and crash backups.
- **Reading level around age 9.** Short words, and every icon has a label or tooltip.
- **Security and privacy from the ground up**, never bolted on.
- **Keyboard and screen-reader accessible** throughout, like every suite app.

## Making the game (logic)

| Feature | Phase |
|---|---|
| Event blocks: "When [player] touches [coin] → add 1 to [score], play [ding], remove [coin]". Snap-together, colour-coded, no syntax errors possible | P1 (core set) |
| Ready-made behaviours: Platformer player, Patrol, Collectible, Hazard, Goal | P1 |
| More behaviours: Top-down player (pulled into P1 on 2026-09-30, for the sample games), Follow, Bounce, Draggable, Shoot, Health bar | P1 (top-down) / P2 |
| Variables shown with pictures (score, lives and timers as meters, not bare names) | P1 (score, lives) / P2 (custom variables, timers) |
| Levels, with "go to next level", and an automatic title and win screen | P1 |
| Custom scenes (title, game over, menus) and screen transitions | P2 |
| Blocks ↔ JavaScript toggle, MakeCode-style (edit either side, the other updates) | P2 |
| Messages between objects ("send 'door open'" / "when I receive 'door open'") | P2 |
| Save progress for players: high scores, checkpoints, unlocked levels | P2 |
| Dialogue boxes and choices, with character portraits | P2 |
| Debug view: collision boxes, live variables, step one frame at a time | P1 (collision boxes) / P2 (the rest) |

## Sprites and art

| Feature | Phase |
|---|---|
| Pixel editor: pencil, eraser, fill, line, rectangle, colour picker, mirror drawing, zoom grid | P1 |
| Sprite sizes 16×16 and 32×32 | P1 (64×64 in P2) |
| Curated retro palettes, so games look good by default | P1 |
| Built-in starter art: characters, tiles, items, backgrounds in one consistent style | P1 (small pack) / P3 (larger library) |
| Frame animation with onion skinning and a speed slider; named animations (idle, walk, jump) that behaviours pick up automatically | P1 |
| Import a picture and auto-pixelate it (a drawing on paper → photo → sprite) | P4 |
| Paper-doll characters (swap hats, faces, colours on a base character) | P4 |
| Particle maker: sparkles, dust, explosions, rain, from a few sliders | P4 |

## Levels

| Feature | Phase |
|---|---|
| Tilemap painter with layers (background, ground, decoration) | P1 |
| Auto-tiling: edges and corners fix themselves as you paint | P1 |
| Drag-and-drop object placement, snapping to the grid | P1 |
| Tile properties painted on: solid, hurts, one-way platform, ladder | P1 (solid, hurts, one-way) / P2 (ladder, water, slippery) |
| Camera that follows the player, with level bounds | P1 |
| Screen-by-screen rooms (Zelda-style) and parallax backgrounds | P2 |

## Music and sound

| Feature | Phase |
|---|---|
| Sound-effect generator: Jump, Coin, Hit, Explosion, Power-up, Laser buttons, plus a "surprise me" dice | P1 |
| Step sequencer: tap squares on a grid, drums on the bottom rows, chiptune instruments, locked to a scale so nothing sounds wrong | P1 (one looping pattern per song) |
| Song arranger: build a song from patterns (verse, chorus) and set a loop point | P2 |
| Record your own voice, with filters (robot, chipmunk, echo) | P4 |
| Music that reacts (faster when time runs low, a boss-fight song) | P3 |

## Play, test, share

| Feature | Phase |
|---|---|
| One-button Play inside the editor; Stop puts everything back | P1 |
| Export as one self-contained HTML file that plays offline anywhere | P1 |
| Controls that just work: keyboard, on-screen touch buttons on tablets, gamepads | P1 |
| Play-test replay: watch a recording of a friend playing to see where they got stuck | P4 |
| Remix: open someone's exported game to make your own version, with credit to the original built in | P4 |
| QR code so a game opens on a phone (needs somewhere to host the file) | P4 |

## Learning

| Feature | Phase |
|---|---|
| Templates, each fully working and heavily commented | P1 (platformer) / P2 (maze, catcher, space shooter, story game) / P3 (pet game and more) |
| Guided quests: in-app tutorials that highlight the next button ("Make your cat jump higher!") | P1 stretch / P3 |
| Challenge cards: small prompts like "Add a second enemy" or "Make the floor lava" | P3 |
| Hint helper that explains problems in plain words ("Your player can't move because it has no behaviour yet") | P2 |
| Badges for concepts learned (loops, variables, conditions), as milestones, not a points grind | P4 |

## For teachers and schools

| Feature | Phase |
|---|---|
| Works on Chromebooks, offline, no install and no account needed | P1 |
| Folder-based projects (File System Access API, or a Google Drive folder) for hopping between computers | P3 |
| Teacher mode: lock features to reduce overwhelm (blocks only, no code), and hand everyone the same starter project | P3 |
| Lesson packs mapped to CS standards (CSTA K–12), with printable handouts | P3 |
| Class hand-in through exported files or Drive, with no server to run or pay for | P3 |

## Safety and privacy

| Feature | Phase |
|---|---|
| No accounts, no tracking, no analytics, no ads, no chat, no public gallery | P1 (and forever) |
| Games play in a sandboxed iframe with a strict CSP, so a game can't touch the editor, other projects, or the network | P1 |
| Project files and imported images and sounds are validated and re-encoded, like PDFEDTR's checks on opening a file | P1 |
| Exported games make no network requests at all | P1 |
| User-written code (from P2) runs only inside the sandbox | P2 |

## Accessibility

| Feature | Phase |
|---|---|
| Full keyboard navigation, including painting tiles, placing objects and snapping blocks | P1 |
| Screen-reader labels on everything, visible focus, respects reduced motion | P1 |
| High-contrast mode and a dyslexia-friendly font option | P2 |
| Read-aloud tooltips and tutorial steps | P3 |
| Accessibility options inside the games kids make: slow-motion mode, invincibility toggle, colour-blind-safe palettes (teaching kids that designers think about players) | P2 |

## Fitting the suite

- The editor layout, top bar, help panel, splash, crash backups, install and update checks all follow `SUITE-STANDARD.md`. **P1**
- The pixel editor can borrow from IMGEDTR and the audio code from SNDEDTR. **P1**
- A future 3D engine would share the runtime spine (game loop, input, audio, project format, sandbox, exporter). **Later, maybe**
- **First-person view** (decided 2026-09-30): after phase 1, as its own experiment. A Play option that turns any top-down level into a walk-through 3D maze (a Wolfenstein-style raycaster: the level's squares become walls, things become flat sprites that face you). Kid-friendly themes only (a first-person maze, water-balloon splat tag, a museum walk-through), no guns. **After P1**
