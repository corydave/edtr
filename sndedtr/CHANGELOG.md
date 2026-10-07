# Changelog

All notable changes to SNDEDTR. Newest first.

The version number lives in two places and both must move together on a
release: `APP_VERSION` in `index.html` and `CACHE_VERSION` in `sw.js`.

## 0.7.5 - 2026-10-07 - DSKEDTR joins the family

- **DSKEDTR joins the family.** More apps and the splash's row of apps now include DSKEDTR (dskedtr.app), the new desktop publishing app: newsletters, flyers and booklets, with text that flows between boxes, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js`.
- The splash's row now fits nine apps: the eight others on one line on a computer, and 4 + 4 on a phone (shared styles pasted in again from `_edtr-suite/suite-block.css`).

## 0.7.4 - 2026-10-03 - Switched off, not broken

- An effect that is switched off no longer looks disabled. Its whole body was dimmed to 45% opacity, which reads as "unavailable" rather than "off" - the first question it drew was why the effects were greyed out - and it dropped the labels well below the contrast the rest of the app holds to (now 7.6:1 on a switched-off section, measured). The switch carries the state, and the section title goes quiet; the controls stay at full strength.
- Reaching for any control inside a switched-off effect now turns that effect on, the way a mixing desk does, and the status bar says so. Dragging a slider that does nothing is a dead end: you cannot tell whether the app is broken or whether you missed a step.

## 0.7.3 - 2026-10-03 - Links to the other apps

- Names of the other apps in Help (in the changelog, About and the guides) are now links that open that app. Each link opens in a new tab; this app's own name stays plain. Shared SUITE block: new `suiteLinkApps()` (called from `renderSuiteApps()`, so no app wiring needed).

## 0.7.2 - 2026-09-29 - 3DEDTR joins the family

- **3DEDTR joins the family.** More apps and the splash's row of apps now include 3DEDTR (3dedtr.app), the new 3D modeling app with shape merging, ready for 3D printing, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js`.
- The splash's row now fits eight apps: the seven others on one line on a computer, and 4 + 3 on a phone (shared styles pasted in again from `_edtr-suite/suite-block.css`).

## 0.7.1 - 2026-09-28 - VCTREDTR joins the family

- **VCTREDTR joins the family.** More apps and the splash's row of apps now include VCTREDTR (vctredtr.app), the new vector drawing app with PowerPoint-style shape merging, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js`.
- The row of apps on the splash is now an even grid (shared styles pasted in again from `_edtr-suite/suite-block.css`), so the six others fit on one line on a computer, and 3 + 3 on a phone.

## 0.7.0 - 2026-09-26

- **Installing:** the top-bar Install button now runs on the shared `SuiteInstall`, so it and the splash's new **Install app** share the browser's one-time install prompt. On iPhone and iPad the splash explains Share, then Add to Home Screen; in Safari on a Mac, File, then Add to Dock.
- **Check for updates on the splash.** The foot of the splash shows the version and asks the server whether a newer one is out; when there is, **Update now** loads it. The question goes through the service worker (`sw.js` now answers a `suite-check-update` message), which fetches `index.html` with `cache: 'no-store'` and reads its `APP_VERSION`. Nothing else is sent.
- Dave Ghidiu's name in the credits now links to his website, daveghidiu.com.
- Shared SUITE block moves to v4 (`SuiteInstall`, `SuiteUpdate`, the author link).
- `sw.js` CACHE_VERSION moves to 0.7.0 with it.

## 0.6.1 - 2026-09-26

- More apps and the splash now show each app's real icon, instead of a simple drawing on a coloured square. The icons live in the shared block as `SUITE_MARKS` (data: URIs, so they work offline).

## 0.6.0 - 2026-09-25

### Added
- Splash screen at start-up: Import audio, Record or Open a project, with the rest of the family underneath. Skipped when a file is opened straight into the app.
- Crash backups. The project, audio included, is kept in this browser while you work - the same bytes Save writes, built by the new `buildProjectBlob()`. Exporting or saving clears it, so a backup is only offered after a crash or a closed tab: "Pick up where you left off" on the splash, and a backup icon in the top bar. Audio makes it big, so it waits 8 seconds after the last change.
- Credits in About: made by Dave Ghidiu with Claude, provided by FLX AI Hub and Finger Lakes Community College.
- Its own colour: gray (`#4b5563`, 7.6:1 with white). The icon (the same bars, now on a gray plate), wordmark, Export and "Render and download" follow it; the wordmark uses a light gray (`#cbd1d9`) in dark mode. Selection, switches and pressed buttons stay blue on purpose - gray cannot show "on" against gray "off". `make-icons.py` now draws in gray and every PNG, `icon.svg` and the tab icon are redrawn.

## 0.5.1 - 2026-09-24

### Changed
- The help panel has tabs: Keyboard shortcuts, About, Changelog and More apps -
  the same four, in the same order, as every app in the family. The Changelog
  tab reads a short `CHANGELOG` table in `index.html`, so a release now goes in
  both places.
- More apps lists the rest of the family (TXTEDTR, PDFEDTR, IMGEDTR, SNDEDTR,
  VIDEDTR, SCRNCSTR). It is the shared SUITE block, pasted identically into
  every app, so it needs no network. Clicking the logo opens it directly.
- The effects panel button is now called the Inspector, the name the other
  apps use for it. Its sliders icon is the family's Inspector icon.
- The sun, moon and help icons are the family's shared drawings.
- `F1` opens the help panel as well as `?`.
- The theme button stays on phones instead of being hidden. The top bar
  tightens below 420px so it still fits on one row.

### Fixed
- Shortcut keys fired behind open dialogs: pressing an arrow in the help panel
  also nudged the playhead, and Space could start playback under a dialog.
  App shortcuts now stand down while any dialog is open.

## 0.5.0 - 2026-09-24

### Changed
- Colour is now how you find your way around a project. Each track owns one of
  ten colours: its header wears it outright, its clips are solid blocks of it
  with the waveform drawn on top in white, and its lane carries a wash of it so
  an empty stretch still says whose row it is.
- Every colour was chosen by measurement rather than by eye. White clears 4.6:1
  on a clip so the waveform stays crisp, each colour clears 3:1 against the lane
  behind it in both themes so a clip always reads as a block, and the darker
  shade that carries the track name and clip label takes white text at 7:1 or
  better - the AAA floor for small text. Measured worst case across all ten:
  7.02:1.
- The selected clip is marked with a white ring inside the block, which reads on
  every one of the ten colours in either theme. The playhead glows while audio
  is playing.
- Clip names moved to the bottom of the clip. They were at the top, colliding
  with the fade handle as soon as a clip had any fade on it.
- The track colour swatch is gone; the whole header is the swatch now.

### Fixed
- Track name fields were picking up the generic text-input styling instead of
  their own. An attribute selector like `input[type="text"]` outranks a plain
  class, so `.track-name` had been quietly losing that argument - invisible
  while headers were grey, obvious the moment they were coloured.

## 0.4.1 - 2026-09-22

### Changed
- On a phone the effects panel is now the bottom half of the screen rather than
  a sheet floating over the timeline. Each half scrolls on its own: tracks in
  the top half, settings in the bottom, and nothing is hidden behind anything.
- Trimmed the chrome on small screens to pay for that half: the master meters,
  the transport clock, the theme toggle and three status readouts are hidden,
  and below 520px the wordmark gives way to the logo alone. Top bar 121px down
  to 42px; total chrome 277px down to 153px, which leaves the timeline a usable
  179px with the panel open instead of 55px.
- Shorter track lanes on a phone (84px rather than 108px), so more than one
  track fits in the space that is left.
- Wider track header column on a phone, so the FX and remove buttons stop being
  pushed off the edge.

### Fixed
- A long status message could make the whole page wider than the screen. Flex
  items will not shrink below their own content unless told they may, so the
  message was setting the width of the page - and on a phone that also pushed
  the layout past the width the mobile styles are written for, quietly turning
  them off. The message now wraps instead.

## 0.4.0 - 2026-09-22

### Added
- Background noise removal. Select a patch of room tone, press Learn, then
  reduce a clip. It measures how loud each frequency is in the noise and
  subtracts that much across the whole clip, so unlike the gate it keeps
  working while someone is talking.
- Ripple delete: removes the selected range and slides everything after it back
  to close the gap. Acts on every track, so a second microphone or a music bed
  stays in step. `Shift+Delete`.
- Fade handles in the top corners of every clip. Drag one inwards to set that
  end's fade; the handle sits where the fade reaches.
- Echo, reverb and distortion, per track. Echo and reverb are sends with a mix
  control; the reverb builds its own impulse response rather than shipping one.
- Zoom slider in the toolbar, on a logarithmic scale, replacing the plus and
  minus buttons. Keyboard `+` and `-` still work.

### Fixed
- Dragging a clip did nothing on a phone. Two separate causes: the clips had no
  `touch-action`, so the browser claimed every drag for scrolling and cancelled
  the pointer events; and the effects panel, which is a fixed sheet across the
  bottom on small screens, was open by default and covering the timeline.
  Clips now opt out of browser gesture handling, the panel starts closed on
  phones and has its own close button, and the empty lane still pans.
- Export could scroll out of reach on a narrow window. The toolbar now scrolls
  everything except Export, which stays pinned.

### Changed
- The version number sits beside the wordmark again.
- The record button is labelled "Record" rather than being a bare red circle.
- Trim grips and fade handles grow when the pointing device is a finger.

## 0.3.0 - 2026-09-20

### Added
- Volume envelopes. Each track carries a line across the timeline that sets its
  volume over time, for ducking music under a voice or pulling down a single
  loud moment. Press `E` or the Envelope button, then click a lane to add a
  point, drag to move it, double-click to remove it. The same envelope appears
  in the side panel as a list of points, so it can be built from the keyboard.
- Master bus section in the panel: output level, and a look-ahead limiter that
  holds the finished mix under a ceiling so an export cannot clip. The limiter
  delays the audio by 5 ms and uses a sliding minimum over that window, so the
  gain has arrived before the peak does.
- Project save and load. A `.sndedtr` file holds the arrangement, every setting
  and the audio itself. `Ctrl+S` and `Ctrl+O`.
- Opus export, in an Ogg container written by hand - the browser can encode
  Opus but cannot package it.
- Loudness matching on export, measured the way broadcasters measure it
  (ITU-R BS.1770 integrated LUFS, gated). Choose -14, -16 or -19 LUFS and the
  mix is measured, adjusted and rendered again at the right level.
- `make-icons.py` in the project folder: redraws every PNG icon from one set of
  shapes, so the mark only has to be edited in one place.

### Changed
- Tracks now run into a master bus rather than straight into the output.

## 0.2.0 - 2026-09-19

### Added
- Brand mark beside the wordmark, built on the same dark plate, inset border
  and accent blue as the VIDEDTR mark, so the two apps read as a set. Drawn
  inline in the page and reused as the favicon.
- Installable web app: `manifest.webmanifest`, `sw.js` and a full icon set.
  Served over https the app installs, opens in its own window and runs with no
  network at all.
- Install button in the top bar, shown only when the browser offers
  installation (`beforeinstallprompt`).
- Audio file handling: once installed, `.wav`, `.mp3`, `.m4a`, `.ogg`, `.opus`,
  `.flac` and `.aac` files can be opened straight into SNDEDTR from the desktop.
- Collapsible sections in the effects panel, all closed on load. The title
  button opens the section and the switch turns the effect on, so either can be
  used without the other. A dot beside a collapsed title marks an effect that
  is switched on.
- Install notes in the help dialog.

### Changed
- Version number moved from beside the wordmark to the right-hand end of the
  top bar.
- Wordmark now uses the accent colour, matching VIDEDTR.
- `sndedtr.html` renamed to `index.html`.

## 0.1.0 - 2026-09-19

First build.

### Added
- Multitrack timeline with canvas waveforms, zoom from 0.5 to 12,000 pixels per
  second, snapping to clip edges and the playhead, and drag and drop import.
- Non-destructive clips: split, trim from either end, drag in time and between
  tracks, all backed by 60 levels of undo.
- Fades drawn into the waveform and scheduled as real gain automation;
  normalize by peak measurement into clip gain rather than rewritten samples.
- Per-track effects, adjustable while playing: noise gate (AudioWorklet), hum
  removal at 50 or 60 Hz with harmonics, three-band EQ, compressor.
- Microphone recording with the browser's own echo cancellation, noise
  suppression and automatic gain control switched off.
- Offline render to 16-bit and 24-bit WAV, and to MP3 through an encoder that
  is fetched only if MP3 is chosen.
- Full keyboard operation, focusable clip elements over the canvas for screen
  readers, light and dark themes, responsive to phone width.
