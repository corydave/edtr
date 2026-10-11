# VIDEDTR changelog

Newest first. The short form of each entry also lives in the `CHANGELOG`
table inside `index.html` (shown in Help > Changelog), so the tab still works
offline and opened straight off a disk. A new release goes in both.

The version lives in one place - `APP_VERSION` in `index.html`. Bumping it and
uploading `index.html` is the deploy: `sw.js` keeps one stable cache and
refreshes the page inside it, and Check for updates compares the server's
`APP_VERSION` with the running one. (`sw.js` itself does not read the version.)

Releases before 3.4 went out without notes. Rather than guess at them, this
file starts at 3.4.

## 3.28 - 2026-10-10 - A tour of the features

- **Features, a new first tab in Help:** an animated tour of five of VIDEDTR's favorite features - Blur private information, Multitrack timeline, Split a clip, Effects and transitions and Spotlight and magnifier - each with a small looping drawing, a title and a sentence or two. Previous and Next, the dots, or the Left and Right arrow keys move between them; the animation has a pause button, and it starts paused when the device asks for less motion.
- **? or F1 and the Help button now open Help on Features.** Keyboard shortcuts is one tab over.
- **The splash has a "See what VIDEDTR can do" card** that opens the same tour over the splash.
- The shared SUITE block was pasted in again from `_edtr-suite` (new: `renderSuiteFeatures`, `suiteFeaturesOpen`, `suiteFeaturesCard` and their styles). The drawings are inline SVG with SVG's own animation tags, so they work offline and straight off a disk.

## 3.27 - 2026-10-09 - .videdtr project files, with the media inside

- **Projects save as `.videdtr`, with the media inside.** Save project (the disk button, Ctrl+S, or Export > Project file) writes one file holding the edit and every media file in the pool, byte for byte. Open it on any computer and everything is there, with no relinking. Built-in sound effects are left out, because VIDEDTR makes them again.
- **It is a zip**, laid out like DSKEDTR's `.dskedtr`: `mimetype` (`application/x-videdtr`, first and stored), `project.json` (the same JSON a `.vidproj` holds, plus each file's name inside the zip, deflated), and `media/<the file's own name>`, stored as it is. Any zip tool can open one.
- **Built for video sizes.** Nothing is loaded into memory: saving makes the zip from the media Files themselves (the browser reads them as the download is written), and opening reads only the zip's directory and `project.json`, then hands each media file to the player as a slice of the project file. Zips and files over 4 GB use ZIP64. The one cost is reading each file once to work out its CRC-32 check number, shown in a progress box (with Cancel) for big projects; the number is remembered, so saving again is quick.
- **Checked like any file from outside.** Every position and size is checked against the file; names inside are only looked up; encrypted entries refused; at most 20,000 entries; `project.json` at most 40 MB, CRC-checked and then validated field by field as before; media must be stored, is CRC-checked up to 128 MB a file, and is opened by the browser's own decoders like any import.
- **Leave the media out** with the new checkbox in Export > Project file, for a tiny file with only the edit (remembered in this browser). Older `.vidproj` files still open, and a folder import still offers a project file inside it, now either kind.

## 3.26 - 2026-10-09 - Dissolve sound fix

- **Fixed: sound starting early under a cross dissolve.** During a dissolve the incoming clip's picture starts before the cut, so its video element plays early - and its sound, which was not yet routed through VIDEDTR's audio graph, went straight to the speakers for up to a second before the cut, at full volume, ignoring the clip's volume, the track's mute and the preview's mute. Both pieces were heard at once, which could make a split sound as if it had not happened. The element is now routed (and held silent) before it plays, so the sound starts at the cut, as it always did in the export. Preview only; exported files were never affected.

## 3.25 - 2026-10-07 - DSKEDTR joins the family

- **DSKEDTR joins the family.** More apps and the splash's row of apps now include DSKEDTR (dskedtr.app), the new desktop publishing app: newsletters, flyers and booklets, with text that flows between boxes, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js`.
- The splash's row now fits nine apps: the eight others on one line on a computer, and 4 + 4 on a phone (shared styles pasted in again from `_edtr-suite/suite-block.css`).

## 3.24 - 2026-10-03 - Links to the other apps

- Names of the other apps in Help (in the changelog, About and the guides) are now links that open that app. Each link opens in a new tab; this app's own name stays plain. Shared SUITE block: new `suiteLinkApps()` (called from `renderSuiteApps()`, so no app wiring needed).

## 3.23 - 2026-10-01 - Match my media

- **A new project takes the shape of the first video or picture you import.** A phone clip held upright makes a vertical project, a square image a square one, and a toast says which shape it picked and that Project settings can change it.
- **Match my media** is the first card in New project, and chosen to begin with. It is also what you get by choosing Import media on the opening screen.
- **Your choice wins.** Choosing a shape yourself (in New project, in Project settings, or with the Reshape buttons), opening a project or picking up a backup keeps that shape: media never changes it after that. Only the first video or picture decides, and only while the timeline is empty. Audio does not count.
- Close to a usual shape (within 2%), the project uses that shape's usual size, so a 4K phone clip makes an ordinary 1920 x 1080 or 1080 x 1920 project. Anything else, such as a 16:10 screen recording, keeps its own proportions with 1080 on the shorter side, at most 3840 on the longer, always in even numbers.

## 3.22 - 2026-10-01 - Choose a shape for a new project

- **Start a new project asks for its shape.** The opening screen's Start a new project opens a New project dialog: Widescreen 16:9 (1920 x 1080), Vertical 9:16 (1080 x 1920), Square 1:1 (1080 x 1080), Portrait 4:5 (1080 x 1350) or Classic 4:3 (1440 x 1080), each card saying what the shape is for. It also takes the name and frame rate. The cards are a real radio group: arrow keys move between them, and a double-click creates the project. Importing straight away still starts a widescreen project.
- **Project settings** has the same shapes in a Shape list above the width and height. Picking one fills the numbers in; typing your own shows Custom. (The Reshape buttons, which also refit every clip, are unchanged.)
- **Export** lists Portrait 4:5 and Classic 4:3 as well, and a custom canvas gets its own "This project" entry, so a project is never exported squeezed into a shape it is not.
- The shapes live in one table, `PROJECT_SHAPES`; the cards and the list are both built from it.

## 3.21 - 2026-10-01 - Shaky cam

- **Shaky cam** (Add > Effects - Looks): the picture below wanders, tips and trembles like a handheld camera. Three styles: **Handheld** (a gentle wobble), **Walking** (with a footstep bob) and **Earthquake** (fast and strong). How shaky sets the strength.
- It zooms in by just enough that the frame's edges never show, even at full strength; switch that off to let the edges show. The movement is a few slow waves that never line up, seeded per effect and worked out from the time, so the export matches the preview frame for frame and a split clip carries on the same shake.

## 3.20 - 2026-09-30 - Sound effects

- **Sound effects.** Add > Sound effects puts a sound at the playhead, in two groups. **Reactions** are SCRNCSTR's five recordings, the same mp3 files: Applause, Laugh track, Ta-da, Sad trombone and Rimshot. **Cues** are made by VIDEDTR's own code: Ding, Pop, Whoosh, Sparkle, Drumroll, Camera shutter and Countdown beeps.
- **Their own tracks.** Sounds go on SOUND FX tracks, never on your voice or music. A new sound uses the first sound effects track with room at the playhead; another one appears only when two sounds would overlap.
- Each is an ordinary audio clip: move, trim, fade and set its volume, and it is mixed into the export.
- **Built in.** Nothing is downloaded (the page still cannot open a network connection). The recordings travel inside index.html as base64 in a data-only `<script type="application/json">` block, which adds about 440 KB. Sounds sit in a Sound effects folder in the Media Pool, and a saved project makes them again when it opens instead of asking you to find them.
- Countdown beeps line up with the Countdown 3-2-1 effect when both start together.
- Help > About credits the five Freesound recordings (all CC0).

## 3.19 - 2026-09-29 - 3DEDTR joins the family

- **3DEDTR joins the family.** More apps and the splash's row of apps now include 3DEDTR (3dedtr.app), the new 3D modeling app with shape merging, ready for 3D printing, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js`.
- The splash's row now fits eight apps: the seven others on one line on a computer, and 4 + 3 on a phone (shared styles pasted in again from `_edtr-suite/suite-block.css`).

## 3.18 - 2026-09-29 - Spotlight, Magnifier and Moments

- **Three groups of effects.** The Add menu's effects come in three groups: Looks, Highlight and Moments.
- **Spotlight** (Highlight): dims, and can blur, everything outside an area you place on the preview, with a soft or hard edge and an ellipse or rectangle shape.
- **Magnifier** (Highlight): a zoomed-in lens like IMGEDTR's - round or rectangular, 1.5x to 5x, with a white ring. It can enlarge what is under it or another spot, joined to the lens by a thin line.
- **Moments, from SCRNCSTR:** Countdown 3-2-1 (a film-leader pre-roll), Confetti, Fireworks and Hearts. Each plays once from the start of its clip, and the export matches the preview frame for frame.
- **Blur the whole frame:** one button in the Inspector stretches a blur over the entire picture, and a blur's edges no longer darken at the border of the frame.

## 3.17 - 2026-09-28 - VCTREDTR joins the family

- **VCTREDTR joins the family.** More apps and the splash's row of apps now include VCTREDTR (vctredtr.app), the new vector drawing app with PowerPoint-style shape merging, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js`.
- The row of apps on the splash is now an even grid (shared styles pasted in again from `_edtr-suite/suite-block.css`), so the six others fit on one line on a computer, and 3 + 3 on a phone.

## 3.16 - 2026-09-27 - American spelling

- American spelling throughout: center (and centered), license, behavior,
  gray, canceled, labeled, recognize, organize, neighbor, honored, flavor,
  defense, artifact and the rest - in the interface, the Help panel, the
  changelog (this file too), the code comments and the code's own names
  (safeHexColor, exportCanceled, centerX and so on). Nothing a project file
  stores changed, so every project opens exactly as before.
- Left as it was: the shared SUITE block, which must stay identical in every
  app. Its only British spellings are in comments; change them in the master
  copy and paste it into every app when the family goes American.
- `aria-labelledby` keeps its spelling: it is the name of an HTML attribute,
  and the browser only recognizes it spelled that way.

## 3.15 - 2026-09-26 - Text, Color and Effects tracks; more transitions; + on every cut

- **Text tracks and Color tracks.** Two new kinds of track, each labeled on
  its track head (TEXT, COLOR), like Effects. `T` (Add > Text track) puts a
  caption on a Text track - a free one in front of the selection, or a new
  one there. `N` (Add > Color track) puts a black color clip on a Color
  track at the BACK of the picture, just above the audio: behind the footage
  it shows through any gap (a slate between scenes) and behind anything
  smaller on top (a title card). When footage above covers it, the message
  says so and how to bring it forward. A Text track holds only text and a
  Color track only color clips; both have the eye but no mute. Text and
  color clips already on video tracks in older projects stay where they are.
- **Blur is an effect.** Add > Effects > Blur (`B`) puts a blur region on an
  Effects track, above the selection as before. The Blur track kind is gone:
  an old project's Blur tracks open as Effects tracks with their blurs.
- **The Add menu** is three groups: New track (Video, Audio, Text, Color),
  Effects (Blur and the six from 3.13), and Transition at the nearest cut
  (all seven). It scrolls if the window is short.
- **Four new transitions.** Wipe and Push, each from the left, right, top or
  bottom (a new Direction menu under Transitions in the Inspector); Iris, a
  circle opening from the middle; and Zoom, the old shot zooming in as it
  fades into the new one. Like the cross dissolve they are centered on the
  cut and hold a frame when a clip has no footage to spare, and the moving
  ones ease in and out. They are for cuts only: an edge with nothing next to
  it still offers the dissolve and the two dips, since a wipe or a push needs
  something to wipe or push away.
- **A + on every cut.** Wherever two clips touch, a small round button sits
  on the join at the bottom of the track - "+" for a plain cut, the
  transition's own icon once it has one. It opens a menu of every transition
  and None, and "Length and direction..." goes to the Inspector. Keyboard:
  Tab to the button, Enter, arrows, Enter; Escape goes back to the button.
  It sits at the bottom edge so the clips' trim edges stay easy to grab, and
  is larger on a touch screen.
- **American spelling** in the interface: Color (the Inspector section, Fill
  color, Any color, key color, the Help text), and Gray for the swatch.
- Validation follows the new rules: each kind of track keeps only its own
  kinds of clip; a transition's direction is one of the four or "left".

## 3.14 - 2026-09-26 - Install, updates on the splash

- **Install VIDEDTR as an app.** An Install button appears in the top bar (on a narrow screen, Install VIDEDTR in the More menu) and **Install app** on the splash whenever the browser can install it. On iPhone and iPad the splash explains Share, then Add to Home Screen; in Safari on a Mac, File, then Add to Dock.
- **Check for updates on the splash**, using the same `findUpdate()` as the version dialog (the page's CSP forbids it from fetching, so the service worker asks). When there is a newer version, **Update now** loads it.
- Dave Ghidiu's name in the credits now links to his website, daveghidiu.com.
- Shared SUITE block moves to v4 (`SuiteInstall`, `SuiteUpdate`, the author link).

## 3.13 - 2026-09-26 - Effects: camcorder, VHS, old film and more

- **Effects tracks.** Add > Effects lists six effects. Each goes at the
  playhead, 5 seconds long, on an Effects track at the front (a new one, or
  the front one if it is already an Effects track with room). An effect works
  like a blur region, or an editor's adjustment layer: it changes everything
  painted on the tracks *below* its track, for as long as the effect clip
  lasts - one clip or a whole run of them. Drag the Effects track down to keep
  a caption above it untouched. The Inspector has an Effect section (choose
  the effect, then its settings), and Opacity & fades mixes it in and out.
  The eye on the track header switches the whole track off, for a quick
  before-and-after. Effects clips are a deep rose on the timeline.
- **Camcorder.** Four white corner brackets, a red REC light that blinks
  (half a second on, half off - or steady), REC, a battery, a running counter
  from 0:00:00 and a date stamp (today's date to begin with; type anything,
  or clear it to hide it). The counter carries on across a split.
- **VHS tape.** A softer, more saturated picture with its red and blue layers
  sliding apart; scan lines; tape noise; the ragged, sideways-shifted band
  along the bottom of every VHS picture; and, every now and then, a tracking
  glitch that tears a few horizontal bands sideways with a bright streak of
  noise. Strength and how often the glitches come are sliders. "PLAY ▶"
  shows for the first three seconds (it can be switched off).
- **Old film.** Sepia or black and white, flickering, weaving slightly in the
  gate, with scratches that linger a moment, dust, the odd hair, a vignette
  and grain.
- **Vignette** (darkness and softness), **Film grain** (strength), and
  **Letterbox**: 2.39:1, 2:1, 1.85:1, or pillars at the sides for 4:3 or a
  square.
- **Repeatable.** The grain, glitches, scratches and flicker come from a
  pseudo-random sequence seeded by the effect and the frame number, so a
  frame always looks the same: scrubbing shows the same glitch in the same
  place, and the exported file matches the preview frame for frame (checked:
  the REC light blinks on the same frames, and the VHS picture's average
  color matches within a few levels). Both halves of a split effect keep
  the same seed.
- Everything is sized in fractions of the frame, so an effect looks the same
  at every export size and in the small preview, and only the canvas's own
  drawing operations are used, so the graphics card does the work. An effect
  only ever touches the frame, never the margin you see when the preview is
  zoomed out.
- Saved in the project and validated on load: a known effect type, settings
  clamped to their ranges, the date stamp plain text of at most 24
  characters (drawn as pixels, never markup), effects only on Effects tracks
  and only effects on them.
- **Fixed:** a picture dropped on a blur track went onto it; blur and Effects
  tracks now refuse media. **Fixed:** text, color clips, blur regions and
  effects could not be stretched further left than where they started (the
  limit meant for the start of a video file); now they can, up to the clip
  before them.
- Menus that would run off the screen open upwards when there is more room
  above, and scroll inside themselves if they still do not fit. The Add menu
  needed it once it grew an Effects group.

## 3.12 - 2026-09-26 - A Media Pool built for bigger projects

- **Resizable.** Drag the Media Pool's right edge to make it wider or
  narrower. The handle is an 8px strip over the border (20px for a finger)
  that lights up when you point at it. It is also a proper keyboard control:
  Tab to it, then the arrow keys move it 16px (Shift: 64px), Home and End go
  to the narrowest and widest, Enter or a double-click puts it back to the
  standard width. Screen readers hear it as a separator with its width.
  The width is remembered in this browser, never narrower than 160px, and
  always squeezed so the preview keeps at least 360px - a width chosen on a
  big monitor does not crowd a laptop, and it comes back when the room does.
- **Folders are cards.** Each folder has a header row, and when it is open
  its contents sit under the header inside the same border, on a faintly
  tinted background with a colored stripe down the left. A folder inside a
  folder is a card inside that card, one step further in. Before, the tiles
  only had a thin line beside them and were the same size as everything
  else, so it was hard to tell what belonged to which folder.
- **Counts on every folder.** The header shows the files directly inside it
  and, if it has any, the folders directly inside it (an image icon and a
  folder icon, each with a number). The tooltip and the screen reader give
  the whole sentence, with the total: "12 files, 1 folder (16 files in all)".
  An open folder shows an open-folder icon.
- **Sticky folder headers.** Scroll through a folder and its header stays at
  the top of the pool until the folder has scrolled past; a folder inside it
  sticks just below, so the stuck headers read as a path. Plain CSS
  (`position: sticky`, offset by depth), on the desktop and in the phone's
  Media Pool sheet alike.
- **Smaller tiles in folders**, so a folder's contents fit two to a row in the
  standard-width pool (three on a phone), and read as "inside" rather than as
  big as everything else. Widen the pool for more to a row.
- With a folder selected, the drop zone says which folder Files... and
  Folder... will add to ("Adding to media / screenshots"), so importing into a
  folder is never an accident.

## 3.11.1 - 2026-09-26

- More apps and the splash now show each app's real icon, instead of a simple drawing on a colored square. The icons live in the shared block as `SUITE_MARKS` (data: URIs, so they work offline).

## 3.11 - 2026-09-26 - Splash, a calmer backup, credits, the family icon

- **The start-up screen is the shared splash:** Import media, Open a project or Start a new project, with the rest of the family underneath (each in its own color). The old opening dialog (`#dlg-start`) and its styles are gone. Media or a project arriving any other way closes it.
- **New backup rule.** Exporting the video or saving the project now clears the backup (`markBackupSafe()`), and a backup is only written when there are edits since then (`backupDirty`). So "Pick up where you left off" - and a new backup icon in the top bar - only appear after a crash or a closed tab, instead of on every launch.
- Closing the tab after an export or save no longer asks whether to leave.
- **Credits** in About: made by Dave Ghidiu with Claude, provided by FLX AI Hub and Finger Lakes Community College.
- **The icon joins the family look:** the same film strip and play button, now on a blue plate (`#0046ad`, VIDEDTR's color) with a light-blue frame, instead of a near-black one. The header mark, tab icon, home-screen icon, `icon-192.png` and `icon-512.png` are redrawn.
- Shared SUITE block moves to v3.

## 3.10 - 2026-09-26 - Color clips, Media Pool folders, a quieter toolbar

- **Color clips.** `N`, or Add > Color clip, puts a 5 second black card at
  the playhead, on the selected clip's track (or the active one), in the first
  free spot. The Inspector's new Fill color section has 16 ready-made colors
  - black, charcoal, gray, silver, white, cream, red, orange, yellow, green, a
  true chroma-key Green screen (`#00B140`), teal, blue, navy, purple, pink -
  and a picker for any other. The swatches are a radio group: one Tab stop,
  arrow keys to move, and each change is one undo step (a whole drag in the
  picker is one step too).
- A color clip has no file behind it. It is drawn with one `fillRect`, and to
  everything else it is a still picture exactly the size of the frame, so
  size, crop, shape, position, animation, drop shadow, opacity, fades and
  transitions all work on it unchanged. On the timeline it is a gray slate
  with a chip of its color. Saved and validated like text colors: only a
  literal `#rrggbb` is accepted, and one on an audio track is dropped. The
  Premiere / Resolve XML and the EDL list color clips as comments (every
  editor makes color mattes its own way; a gap shows black anyway).
- **Folders in the Media Pool.** The New folder button at the top of the pool
  makes one (inside the selected folder, if one is selected) with its name
  ready to type. Click a folder for its settings in the Inspector: name, which
  folder it is inside, how many files, New folder inside, Delete folder.
  Drag tiles or folders onto a folder to file them, or use the new Folder
  menu in a file's Inspector (the keyboard and touch way). Right and Left open
  and close a focused folder, F2 renames, Delete deletes. Deleting a folder
  never removes a file - what was in it moves up a level - and it is undoable.
  A folder cannot be moved inside itself. With a folder selected, Import puts
  new files into it.
- Folders live in the project (`folders` and `mediaFolders`), so they are
  saved, backed up and undone with everything else. A file keeps its id when
  it is reconnected, so reopening a project puts every file back in its
  folder. Validated on load: at most 500, names as plain text, and a parent
  that is missing or would make a loop puts the folder back at the top.
- **Import a whole folder.** Folder... in the Media Pool, `Shift + I`, or drop
  a folder anywhere on the pool (onto a folder row, and it goes into that
  folder). Each folder on disk that holds media becomes a pool folder; the one
  you chose opens, the ones inside it start closed. Hidden files and system
  clutter are skipped, other files are counted and left out, and importing
  the same folder again adds only what is new. Up to 1000 files at a time.
- **A project inside the folder.** If the folder has a `.vidproj` in it, you
  are asked: Open the project (it replaces the timeline, and its media is
  reconnected from that folder in one go) or Import the media only. Files are
  matched by where they sit in the folder and their size, so two files with
  the same name in different folders are told apart, and a renamed folder
  still matches. The project file now records each file's path inside an
  imported folder for this.
- Reconnect your media has a Choose folder... button, which searches the whole
  folder, subfolders included.
- **Toolbar.** The top bar is icons now, except Export, which keeps its word
  as the one button every visit ends on. Import is a folder with an arrow
  going in; Open project is a video file (two folders side by side read as
  the same command). The Inspector button moved to the family's group at the
  right - Inspector, Theme, Help, then Project settings as the cog - to match
  IMGEDTR and SNDEDTR. On a wide screen it now shows and hides the Inspector
  column (filled in while it is showing, and remembered in this browser); on
  a narrow one it opens the Inspector sheet as before. Split, Split all,
  Frame, Delete and Ripple delete are icons too, each with a short name for
  screen readers and its shortcut in the tooltip.
- **Tooltips for keyboard users.** Browsers show a button's tooltip on mouse
  hover only, never when you Tab to it, so an icon-only toolbar would have
  been a row of unlabeled pictures from the keyboard. Tabbing onto an
  icon-only button now shows its tooltip under it. Escape, a click, scrolling
  or moving on hides it.
- Undo keeps the clip you were editing selected (as long as it still exists),
  instead of dropping the Inspector back to "Select a clip".
- **Fixed:** a green-screened picture larger than 1920 pixels on its long side
  (4K video, most phone photos) drew wrongly once it also had a drop shadow.
  The keyer works on a scaled-down copy of such pictures, and the shadow path
  forgot to scale the crop rectangle to match. The plain and shadow paths now
  share one drawing function.
- Help > Keyboard shortcuts lists `N` and `Shift + I`.

## 3.9 - 2026-09-26 - Transitions

- **Three transitions: cross dissolve, dip to black, dip to white.** These
  are the ones nearly every edit uses; wipes, pushes and slides can come later
  if they are missed. `D` (or Add > Transition at nearest cut) puts a 1 second
  cross dissolve on the cut nearest the playhead, on the selected clip's track
  if one is selected. The Inspector has a new Transitions section with a Start
  row and an End row for the clip: pick a type and a length (0.1 to 5
  seconds). Undoable, saved in the `.vidproj` and the backup, validated on load.
- **Stored on the clip that comes in.** A transition on a cut lives on the
  second clip as `transitionIn`. An edge with nothing touching it (the first
  clip, the last clip, a clip after a gap) can have its own single-sided
  transition: dip to black or white fades from or to that color inside the
  clip, and a cross dissolve there fades from or to nothing, so a picture-in-
  picture clip dissolves in over whatever is underneath.
- **A cross dissolve is centered on the cut,** like Premiere and Resolve: half
  before, half after. Each clip plays on past its edge into the overlap. If a
  clip has no spare footage there (it was not trimmed), its first or last frame
  is held instead, and the Inspector warns about it. The two pictures are mixed
  additively, so a still background does not dim part-way through.
- A transition is shortened to fit: never longer than the shorter of the two
  clips, and a single-sided one never more than half its clip. The Inspector
  says when that happens. A transition replaces that edge's fade, so the two
  never stack. Moving a clip away from a cut turns its transition into a
  single-sided one; splitting a clip drops the transition at the new cut.
- On the timeline, transitions show as small wedges at the clip edges: dark
  for dip to black, light for dip to white, hatched for a dissolve.
- Picture only for now - sound still cuts at the edit, so use audio fades for
  a smooth sound change. Transitions are not written into the Premiere /
  Resolve XML or the EDL yet; those get plain cuts.
- Export reads both clips of a dissolve directly (the fast path) and matches
  the preview. Checked on solid colors to the exact pixel value (midpoint of
  red into blue is 127, 0, 127) and on real video for both the spare-footage
  and held-frame cases.
- Help > Keyboard shortcuts now lists `Shift + Delete` (ripple delete) and `D`.

## 3.8 - 2026-09-26 - Phone video orientation, and markers

- **Fixed: phone videos exported upside down.** A phone does not turn the
  picture when you hold it sideways or upside down; it records the sensor as
  it is and writes a "display matrix" in the MP4 saying how to turn it. The
  preview's `<video>` element obeys it. The fast export path (3.3 onwards)
  decodes with WebCodecs, which does not - so a clip recorded upside down came
  out upside down, and a portrait clip would have come out on its side and
  squashed. The matrix is now read from the track's `tkhd` box and each decoded
  frame is turned to match, through a small per-clip canvas (one extra GPU copy
  per frame, only for clips that need it). Checked for all four rotations: the
  export matches the preview pixel for pixel, and matches ffmpeg's own
  auto-rotated output.
- **Markers.** `M` or the new Marker button drops a flag at the playhead (on a
  frame that already has one, it opens that one instead). Click a flag to jump
  to it and read or edit its note - the note is kept however the dialog
  closes, Escape included. Drag a flag to move it; with a flag focused, the
  arrow keys nudge it a frame (Shift: ten) and Delete removes it. `[` and `]`
  jump to the previous and next marker. Flags with a note are filled in; empty
  ones are outlined; hovering shows the note. The status bar counts them.
- Markers belong to the timeline, not to a clip. They are saved in the
  `.vidproj` and the backup (validated on load: real times, plain-text notes up
  to 1000 characters, at most 500), undoable, used as snap points, and written
  into the Premiere / Resolve XML as sequence markers. Notes only ever reach
  the page as text, never as HTML.

## 3.7 - 2026-09-25 - Export format, explained

- **Chromebooks keep H.264.** The format is chosen automatically: MP4 with
  H.264 and AAC first, because it plays nearly everywhere and is encoded in
  hardware. When AAC's encoder fails - as it does on ChromeOS - the export used
  to fall through to WebM, which also swapped H.264 for VP9, encoded in
  software. Now only the sound changes: H.264 video with Opus audio, still in
  an MP4. Checked here that the muxer writes a valid, audible Opus-in-MP4 and
  that Chromium plays it; the H.264 half runs only on real hardware.
- **The dialog explains the choice.** There is no format menu because most of
  the options would fail on any given browser, so the note now says the format
  was picked automatically, and - when it had to settle for less than MP4 with
  H.264 and AAC - what it gave up and why. The "How long will it take?" note no
  longer names MP4, MOV and WebM: those are the files you import, but in an
  export dialog they read like output choices.

## 3.6 - 2026-09-25 - Timeline status bar and scrolling

- **Status bar** along the bottom of the timeline: project name, frame size,
  frame rate, clip count and length on the left; the **timeline zoom** on the
  right. Both zooms now sit bottom right of their panes. It is a row of its
  own rather than a floating pill like the preview's, so it never covers the
  bottom track. On a narrow screen the project line shortens with an ellipsis
  and the slider narrows; the zoom controls stay reachable.
- **Scrolling over the timeline** moves left and right (it did nothing before
  unless the tracks overflowed). **Shift + scroll** moves up and down through
  the tracks. **Ctrl / Cmd + scroll** or a trackpad pinch zooms.
- **Zoom holds its place.** Ctrl + scroll already zoomed, but from the left
  edge, so everything slid sideways and it looked like scrolling. The wheel
  now keeps the moment under the pointer still; the buttons, slider and + / -
  keep the playhead still (or the middle of the view, if the playhead is off
  screen). Wheel zoom is proportional, so a trackpad pinch is smooth and a
  mouse wheel notch is a clear step.

## 3.5 - 2026-09-25 - Export speed, second pass

- **No timers in the export loop.** It waited on `setTimeout` about 1.5 times
  per frame. Browsers stretch timers in any tab you are not looking at - to
  once a second, and after five minutes to once a minute - so a long export
  left running in the background could take hours. Every wait is now driven by
  the encoder's and decoder's own events, or by a MessageChannel message,
  neither of which is throttled. Measured: 1.49 timer waits per frame down to
  0.03 (the few left are one-off, during setup).
- **Getting each source frame is about 3x faster** (4.2ms to 1.4ms on the test
  clip). Feeding the decoder properly exposed a restart rule, dating from 3.3,
  that re-decoded from the previous keyframe on nearly every frame; the old
  timer-paced feeding had been too slow to trigger it.
- **iPhone clips.** The HEVC codec string is now built from the file's own
  configuration (it was a fixed Main-profile guess), and Dolby Vision (`dvh1`,
  the iPhone's HDR setting) is read as the HEVC underneath it.
- **H.264 level fitted to the export size.** Every H.264 option said level 4.0,
  which covers 1080p30 and nothing bigger; larger or faster exports could fall
  through to VP9, which Macs do not encode in hardware.
- **Export report.** Shown in the Export dialog after every export, with a
  Copy button: time split by stage, the encoder used and whether a hardware
  one is available, which clips were read directly and why any were not, and
  time spent in the background.
- **Screen Wake Lock** held while exporting, so a sleeping display does not
  hide the tab.

## 3.4 - 2026-09-24 - Family alignment

- **Help panel layout** now follows the rule every app in the family uses:
  Keyboard shortcuts first; About, Changelog and More apps last. VIDEDTR's own
  guide tabs (Getting started, Editing, View and export) sit between. The ?
  button and the ? key open it on Keyboard shortcuts.
- **Changelog tab** (new), fed from the table in `index.html`.
- **More apps tab** (new): the rest of the family - TXTEDTR, PDFEDTR, IMGEDTR,
  SNDEDTR, VIDEDTR, SCRNCSTR - with this app marked "You are here". It is the
  shared SUITE block, pasted identically into every app, so it needs no
  network. Clicking the logo opens it directly.
- **Inspector button** uses the family's sliders icon (three vertical sliders)
  instead of the horizontal one, matching SNDEDTR and IMGEDTR.
- **F1** opens the help panel as well as ?.
