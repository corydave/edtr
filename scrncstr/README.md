# SCRNCSTR

A screen and webcam recorder that runs entirely in the browser. No server, no
uploads, no analytics — recordings stream straight to a folder you pick.

Sibling to TXTEDTR; same conventions (single file, vanilla JS, no build step).

## Files

| File                  | Required | What it is                                        |
|-----------------------|----------|---------------------------------------------------|
| `index.html`          | yes      | The entire app. All CSS and JS inline.            |
| `scrncstr-icon.png`   | no       | 512×512 square PNG, transparent. Header mark + favicon. A drawn SVG mark stands in if absent. |
| `sfx-*.mp3`           | no       | Sound effects: `sfx-applause`, `sfx-laugh`, `sfx-trombone`, `sfx-celebrate`. Missing ones fall back to synthesis, or the button hides. |
| `manifest.webmanifest`| yes      | PWA metadata: name, icons, standalone display.    |
| `sw.js`               | yes      | Service worker, so it launches offline.           |
| `icon-192.png`        | yes      | Manifest icon, generated from the 512.            |
| `icon-maskable-512.png`| yes     | Padded, opaque variant. Android masks icons to a circle and would clip an edge-to-edge mark. |

## Deploy ritual

1. Bump `APP_VERSION` near the top of the `<script>` in `index.html`.
2. Upload `index.html`.

The version shows in the header badge and in About, and it rotates the service
worker cache — `index.html` registers the worker as `sw.js?v=<APP_VERSION>`, so
changing that one constant changes the worker's URL and forces a reinstall. One
edit, one upload. You never touch `sw.js`.

### Why the document is network-first

`sw.js` serves `index.html` from the **network first**, cache only as an offline
fallback. This is load-bearing, not a preference. Serving the document
cache-first deadlocks the whole scheme: the cached page carries the OLD
`APP_VERSION`, so it registers the OLD worker, so the version never changes, so
the cache never rotates — the app freezes at whichever version was cached first
and no amount of uploading fixes it. Verified by bumping the constant and
watching `scrncstr-1.1.0` become `scrncstr-1.2.0`.

Icons and the manifest stay cache-first; they only change when the version does,
and the install step refetches them with `cache: 'reload'`.

**Worth checking TXTEDTR for the same trap** if its worker serves `index.html`
from cache.

## Requirements

- Chrome or Edge, served over **https** or from `localhost`. `getDisplayMedia`
  and `getUserMedia` both refuse plain http.
- System audio capture needs Chrome 141+ on macOS 14.2+ (Apple did not allow
  third-party apps to capture system audio before 14.2).

## The three modes

- **Separate files** — clean screen recording + full-frame webcam recording, as
  two files. Two encoders. Place the webcam in your editor.
- **Combined** — one finished file with your face in it. Two sub-modes:
  - *Composite it in* — drawn onto the canvas as a circle / rounded rect /
    square, positioned from the in-page preview.
  - *Pop-out only* — no compositing. The Picture-in-Picture window is physically
    on screen, so the capture records it. Rectangular, but full quality, one
    encoder, and draggable during recording.
- **Screen only** — screen and narration, no camera.

## Audio routing

| Mode                | Mic goes to   | System audio goes to  |
|---------------------|---------------|-----------------------|
| Separate files      | webcam file   | screen file           |
| Combined (either)   | the one file  | the one file (mixed)  |
| Screen only         | screen file   | screen file (mixed)   |

Single-file modes have one audio track, so voice and system audio mix
permanently. "Save my mic as its own audio file" keeps a clean voice track.

## What you share — and note that it flips

- Every mode **except** pop-out: share a **single window**, so the app stays out
  of the shot.
- **Pop-out mode is the opposite** — it needs a **whole screen**. Share one
  window and the floating camera is not captured, so there is no face in the
  recording at all. The banner warns about this at record time.

## Controls

- **Hot spots** (Composite only) — six numbered dots on the preview, keys
  `1`–`6`. The overlay glides rather than jumps, so the move reads as
  deliberate in the recording. Hidden in Pop-out, because a Picture-in-Picture
  window's position cannot be set by script, and in Separate, where position is
  decided in the editor.
  **They also drop you out of full-frame** (v1.10.0). Asking for a corner while
  the webcam fills the screen can only mean "shrink it back down, over there" —
  there is no other reading. Before, the click moved a bubble nobody could see
  and the control looked dead. Both animations run at once and land together.
- **Pause** — works in every mode. `MediaRecorder.pause()` genuinely omits the
  paused span: measured 2s + 4s paused + 2s producing a **4.25s** file, not 8s.
  Compositing stops while paused, and the timer excludes paused time. Two
  recorders pause within well under a millisecond of each other, so Separate
  mode does not drift.

## Sounds

**Filenames:** `sfx-<id>.<ext>` where id is one of `applause`, `trombone`,
`celebrate`, `laugh`, `rimshot`, and ext is any of `mp3`, `wav`, `m4a`, `ogg`.
Each extension is tried in that order, so downloads need no renaming. Reload
after adding one — sounds load once at startup.

**A file always wins over the synth.** The loader returns on the first
extension that both fetches and decodes, and never reaches the synth. Because
`mp3` is tried first, dropping in an mp3 supersedes a `wav` of the same name
without deleting anything — which is how the bundled set is shipped.

Since v1.9.0 the buttons are icon-only, so **"this one is synthesized" lives in
the tooltip**, not in a visible tag.

Three-step fallback, per sound:

1. **File present and decodes** → used as-is.
2. **File missing / 404 / undecodable / offline and uncached** → synthesized in
   Web Audio, *only* where synthesis is convincing. Trombone and celebrate are
   pitch-and-envelope shapes and sound fine; applause is passable; **laughter has
   no synth fallback** — there is no waveform trick for a human laugh.
3. **Neither** → the button hides itself. Never a dead control.

### The bundled sounds

Five CC0 sounds from Freesound, credited in the About dialog even though CC0
requires no attribution:

| Button | Sound | Author | Freesound |
|---|---|---|---|
| Applause | Concert audience applause 5 | thaighaudio | `/sounds/478415/` |
| Sad trombone | wah wah sad trombone | kirbydx | `/sounds/175409/` |
| Ta-da | Tada! | Yoshicakes77 | `/sounds/850021/` |
| Laugh track | Female crowd laughing | kikorurelas | `/sounds/767470/` |
| Rimshot | Baddum Tish – Comedy Rimshots – classic rim shot | OverlookHotelRecords | `/sounds/271208/` |

### Preparing a sound file (the recipe)

Raw freesound downloads are unusable as-is: the originals here totalled **23MB**
for 113 seconds of audio, including a 62-second rimshot file that turned out to
be the same hit recorded three times. The prepared set is **320KB**. Every one
of these steps mattered:

1. **Find the actual sound.** Dump a 100ms RMS envelope and read it:
   `ffmpeg -i in.wav -af "aformat=channel_layouts=mono,asetnsamples=4410,astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=-" -f null -`
   The rimshot's three takes are obvious as three identical decay curves.
   `silencedetect` found nothing useful — these files have no true silence.
2. **Trim to one take, and fade the tail.** A hard cut on a decaying cymbal is
   audible; 0.25s of `afade=t=out` is not.
3. **Match loudness, don't match peaks.** Peak normalisation cannot equalise
   this set: a rimshot is nearly all transient (I = −20 LUFS, TP = −1.8 dBTP), so
   it has no headroom to gain into and would sit 6dB under the applause forever.
   Measure with `loudnorm:print_format=json`, apply the difference to −16 LUFS as
   plain `volume`, and let a limiter catch what that pushes over.
4. **`alimiter` needs `level=disabled`.** By default it auto-levels its output,
   so *lowering* the ceiling *raises* the loudness. Lowering `limit` from 0.85 to
   0.66 made the applause 2dB **hotter**, which is the opposite of the intent.
5. **Leave ~2dB of headroom for the encoder.** mp3 reconstruction ringing pushes
   true peaks above the sample-peak ceiling the limiter enforced; a set limited
   to −1.4 dBFS came back measuring +0.5 dBTP.
6. `-c:a libmp3lame -b:a 128k -ar 44100 -ac 2`.

Two ffmpeg gotchas that cost time: **`print_format=json` is emitted at info
level**, so `-v error` hides the very numbers you asked for; and **ffmpeg
consumes stdin**, so an `ffmpeg` inside a `while read` loop eats the loop's own
input and the loop processes about one and a half files. `-nostdin`.

### The service worker caches only the winning extension

`sw.js` used to precache all five ids × all four extensions, on the reasoning
that missing ones fail harmlessly under `allSettled`. That is true, but it means
a folder holding **both** an mp3 and the wav it replaced caches both — 23MB of
superseded audio pinned offline for sounds the app will never reach for. It now
mirrors the app's own `SFX_EXTS` order and stops at the first extension that
answers.

### Where sounds land

Sounds ride with your **microphone**, because they are part of your performance:

| Mode          | Sounds go into            |
|---------------|---------------------------|
| Combined      | the combined file         |
| Separate      | the **webcam** file (with your voice) — the screen file keeps clean system audio |
| Screen only   | the screen file           |
| Mic sidecar   | **never** — that file exists to be a clean voice track |

They reach the file through a single `GainNode` bus connected to each recorder's
`MediaStreamAudioDestinationNode`. Verified by recording that graph with no
microphone attached: silence measured RMS 0.0, the sound measured 0.123.

One consequence worth knowing: **a file that carries sounds can no longer take
the single-source shortcut** of cloning the track, because a bare clone has no
graph to inject into. It goes through the mixer even with one input.

### Hearing them

Sounds always go into the recording. Whether you hear them:

- **Before recording** — always, so you can test.
- **While recording** — only with "Play sounds out loud" ticked, and then
  **use headphones**: on speakers your microphone re-records the sound through
  the room and you get a doubled, hollow copy.

## Overlay controls (Composite only)

Drawn onto the canvas I composite, which is why none of these exist in Pop-out,
Separate or Screen-only — those record the raw screen capture, where there is no
frame of mine to draw on.

| Control | Key | Notes |
|---|---|---|
| Full-frame webcam | `0` | Interpolates the overlay's rect toward the full frame — same code path as the bubble, not a special case. Ring fades out as it takes over. |
| Countdown (film leader) | `l` | Half a second of flat black, then the cinema academy leader: crosshairs, a ringed circle, a hand sweeping one full turn per numeral, 3-2-1. 2.9s in all. **Opaque** — see below. |
| Confetti | `c` | 150 particles in frame-fractions, so a burst looks the same at any capture resolution. Culled below `y = 1.15`; an empty array means the draw loop skips it entirely. |
| Webcam out of the recording | `k` | Keeps your face out of the file while you keep seeing it — the mirror of Blank screen. **Does not touch the camera.** Drops out of full-frame. **Not** a substitute for Screen-only mode. |
| Fireworks | `f` | Five staggered shells. Shell and spark share one array, told apart by `kind`; a shell replaces itself with ~45 sparks at its burst height. |
| Hearts | `h` | 28 hearts rise from below the frame, swaying, fading out over the top fifth. Bezier path, no image asset. |
| Blank screen | `b` | Covers the screen layer only — face, watermark and timer stay visible. No text is drawn on it. |
| Show timer on screen | — | Off by default. Reads `elapsedMs()`, the same clock as the control bar, so it stops on pause instead of drifting. |

**Why Camera off cannot replace the mode picker.** The mode is not a view, it
is the recorder graph. Separate mode builds *two* `MediaRecorder`s writing two
files; Combined builds a canvas compositor; Screen-only never calls
`getUserMedia` at all, so no permission is asked and no camera light ever comes
on. Those are decided before the first byte is written and cannot be changed
mid-take — a live toggle cannot retroactively decide not to have written a
webcam file. It also cannot un-mix audio: single-file modes bake the mic in.
Camera off is a *performance* control, and it only exists in Combined-composite
mode because that is the only mode with a canvas to omit the face from.

**It must not touch the camera.** The first version (v1.12.0) disabled the
video tracks. That did keep the face out of the file — and also blacked out the
pop-out window and every other preview, so you were recording blind. The camera
now keeps running and the compositor simply stops drawing it.

**That makes it the one place the preview is deliberately not the recording**,
which matters because the whole app is built on those being identical. So the
DOM bubble changes job. Normally it carries `.ghost`: a transparent drag target
whose own `<video>` is `visibility: hidden`, because the canvas underneath is
already drawing your face. With the webcam hidden there is nothing on the canvas
to see, so the bubble drops `.ghost`, shows its own live video, and takes
`.cam-hidden` — dashed border, dimmed, and a `::after` reading **not recorded**.
The two classes are mutually exclusive and `applyCamHiddenStyle()` owns both.

Two details that bit:

- **Clearing the flag between takes is not enough.** The bubble keeps whichever
  classes it was left with, so a new take would open with a dashed "not
  recorded" overlay over a webcam that was very much being recorded.
- **The watchdog had to learn the difference between hidden and broken.** In
  v1.12.0 the bubble was hidden outright, measured 0×0, tripped "bubble
  collapsed to zero" and forced the diagnostics panel open — shouting about the
  button you just pressed. `state.camHidden` is checked first and reports
  nothing. The panel now says *webcam not in the recording*.

The caption is positioned with `bottom: 15%`, not pixels: at the very bottom of
a **circle** bubble the disc has narrowed to nothing, so a pixel offset put the
text outside the visible shape and under the resize grip.

### The film leader is the odd one out, deliberately

**`LEADER_LEAD_MS = 500` is a handle for the edit, not a delay.** The first
half-second is dead flat black — no crosshairs, no dial, no grain, one single
colour across the whole frame. That makes it trivially findable when scrubbing a
long take, and it gives you somewhere to put a cut or a cross-fade that is not
already mid-animation. The test asserts the handle is exactly one colour, which
is a stronger claim than "it looks black" and is what stops a later change from
quietly drawing grain over it.

Timing splits into `LEADER_LEAD_MS + LEADER_COUNT_MS`, and the numeral maths
works off `t - LEADER_LEAD_MS`. Anything reading elapsed time against the
numerals needs that offset — the tests do.

It breaks two rules the other effects follow, and both breaks are the point:

- **It is opaque.** Covering the frame is what a leader *is*, and it is what
  makes the thing read as intentional rather than as an overlay that leaked into
  the video. The first version used an `.87` scrim and the webcam ghosted
  through as a faint green smudge beside the dial — 13% of a bright face is
  still visibly a face. The test now allows *no* green cast at all, rather than
  the perceptual brightness threshold that a visible ghost had already passed.
- **It has no particle array.** The whole animation is a pure function of
  elapsed time, so there is nothing to cull and nothing to reset but the start
  timestamp. That also makes it the easiest thing here to test: back-date
  `state.leader.startedAt` and you render an honest frame from any instant.

Which mattered, because **racing the wall clock does not work in these tests.**
A full-stage Playwright screenshot costs a few hundred milliseconds, so waiting
850ms between reads actually landed 1700ms in and read "1" where the test
expected "2" — twice, in two different places. Pin the clock; do not sleep
against it.

A second press restarts rather than being ignored — someone pressing it twice
wants the countdown to begin again, not to be told it is already running.

Every particle effect obeys the same contract: **positions are fractions of the
frame** (so a burst looks identical at any capture resolution), particles are
culled the moment they leave, and an empty array means the draw loop skips the
effect entirely — an idle recording costs nothing.

Three tuning lessons, all learned by watching it rather than reading it:

- **The ticker runs at 30fps, so every velocity is per-33ms.** Both new effects
  were first tuned by eye against no particular frame rate and came out absurdly
  slow — a shell took two seconds to climb, and hearts were still drifting
  thirty seconds later, which meant the next take could inherit them.
- **A firework must burst in the middle band, not at the ceiling.** Bursting at
  `y = 0.16` throws the top third of the sphere clean out of frame. `burstAt` is
  `0.30–0.52`.
- **A spark drawn as a dot is dust.** Each one is drawn as a streak from its
  previous point to its current one, in three passes under `globalCompositeOperation
  = 'lighter'` — a wide dim halo, the coloured streak, then a white-hot head —
  and holds full brightness for the first half of its life before falling away.
  Fading from frame one made the burst look like it had already happened.

The presenter's own timer in the control bar is always present in every mode —
"show timer on screen" only controls whether it is *burned into the recording*.

## Logo / watermark (Composite only)

Three sources, so it is useful before you supply anything:

| Source | Needs a file? | Notes |
|---|---|---|
| Text badge | no | Type a line — name, URL, course code. Drawn as a pill. |
| `builtin:scrncstr` | no | Inline SVG, the app's own mark. |
| `builtin:rec` | no | Inline SVG, a REC badge. |
| Upload | your PNG/SVG | Stored as a Blob in **IndexedDB**, never uploaded anywhere. 4MB cap, non-images rejected. |

Corner, size (% of frame width) and opacity are all adjustable, and there is a
DOM twin on the preview stage driven by the same state and margins as the canvas
draw — so the preview does not lie about the output.

**Drawn after the webcam**, deliberately: a watermark that disappears the moment
you cut to full-frame camera is not a watermark. The consequence is that a logo
and the webcam bubble in the same corner will overlap, with the logo on top.

## The preview IS the canvas (Composite mode)

In Composite mode the preview video is fed by `canvas.captureStream(15)` — it
shows the frame being recorded rather than a reconstruction of it. Two
consequences:

- **Confetti, the burned-in timer, the logo and the full-frame zoom all appear
  in the preview for free**, and cannot drift from the output.
- **It fixed an intermittent black preview.** Previously `#screenPreview` and
  the hidden `#compScreen` both consumed the same screen `MediaStream`, and one
  could go black while the other kept decoding — recording fine, preview dead.
  Only `#compScreen` touches that stream now.

The compositor therefore starts when you enter the arrange screen, not at record
time. The DOM bubble becomes a transparent drag target (class `ghost`) that
outlines itself on hover, since the canvas already draws the webcam; the DOM
logo twin is suppressed for the same reason.

## Spotlight — PARKED (`SPOTLIGHT_ENABLED = false`)

> Did not work in practice and is hidden as of v1.7.1. The code is intact and
> gated behind one flag near the top of the script — flip it to `true` to bring
> back the button, controls, `s` shortcut, drag placement and the canvas draw.
> Restoring settings also forces `spotlight.on = false` while parked, so a
> settings blob saved while it was enabled cannot leave anyone dimmed with no
> control to switch it off.

What it was meant to do (Composite only):

Dims the frame except a feathered circle. Drawn **before** the webcam, logo and
timer, so those stay bright — only the screen is dimmed.

Two modes, chosen by the browser, not by you:

| Mode | When | How you aim it |
|---|---|---|
| **Follow** | `'oncapturedmousechange' in CaptureController.prototype` | Tracks your real cursor over the captured surface, via a `CaptureController` passed to `getDisplayMedia`. |
| **Manual** | otherwise | Drag the preview. The preview *is* the composited frame, so a point there is that point in the recording. |

The button label reports which you got. As of Chrome 141 the API is **not**
shipped, so manual is what you will see — but the follow path is wired and was
verified against a shimmed API, so it lights up by itself when Chrome ships it.

Implementation notes: the dim-with-a-hole is rendered on a **scratch canvas**
and composited in, because `destination-out` on the main canvas would erase the
video underneath rather than just the dim. The scratch is rebuilt only when the
geometry changes, so a stationary spotlight costs one `drawImage` per frame.
A controller is only created when it can actually be used — it also governs
focus behaviour, so the default is left alone otherwise.

## Control layout (v1.17.0)

Three rows under the preview, all Composite-only except sounds. Every row is
`icon on the left, then a bordered cluster of icon-only buttons` — the leading
icon (`.ctl-lead`) names the row, so no button needs a caption and each row
stays one line tall however many controls arrive later:

1. **Camera** (lucide `camera`) — shape (circle / rounded / square), then
   **keep the webcam out of the recording** (lucide `ban`), a rule, then
   full-frame webcam and pop-out camera. One cluster because they are all
   "where and how does my face appear"; the rule separates *how it looks* from
   *where it lives*.

**The two rules line up because the layout says so, not by coincidence.** Two
things make that true:

- Every control sits on the same **46px pitch** (40px wide, 6px gap).
  `.ctl-cluster .shapes` is a nested flex box and had its own 4px gap, putting
  the three shapes on a 44px pitch and landing the camera rule 4px left of the
  effects one. Its gap must match the cluster's.
- Each half of a cluster is wrapped in **`.ctl-side`**, and the leading half has
  `min-width: calc(var(--ctl-slots) * var(--ctl-pitch) - 6px)` — four slots,
  178px. Before that, alignment only worked because both sides happened to hold
  four buttons; moving Blank screen across the rule would have pulled the
  effects rule 46px left. A side with more than four buttons simply grows, and
  then the rules need `--ctl-slots` raised to match.
2. **Effects** (lucide `sparkles`) — Countdown, Confetti, Fireworks, Hearts, a
   rule, then Blank screen, Logo and Timer. **The rule separates momentary from
   persistent**: everything left of it fires once, everything right of it stays
   on until clicked again. Blank screen moved across in v1.15.0 — it is a
   toggle, and sitting with the bursts it read as another thing that fires once.
3. **Sound effects** (lucide `volume-2`) — Applause, Sad trombone, Ta-da, Laugh
   track, Rimshot. Shown in every mode, since sounds go through the audio mix
   rather than the canvas.

With the captions gone, **the tooltip is the only label**, so it has to say what
the control *does*, not what it is called: "Crops the webcam to a circle", not
"Circle". Toggles flip their tooltip to the reverse action when on. Every
`title` is mirrored to `aria-label`, because a screen reader gets nothing from
an icon.

Two consequences worth knowing before editing:

- `setBtnLabel(id, text, title)` no longer has a `.ibtn-label` span to write
  into on these buttons, so its `text` argument is inert and the `title` is the
  whole job. It is still safe to call — the span lookup is guarded.
- **A synthesized sound used to admit it with a visible `synth` tag.** That tag
  is gone; `paintSoundboard` appends "(synthesized)" to the tooltip instead.
  Reaching for `.sfx-tag` now returns `null`.

**Pop Out is a real toggle** as of v1.9.0. It had `title` and `aria-label` but
no `aria-pressed`, so `#liveControls button[aria-pressed="true"]` never matched
and it refused to stay illuminated — it looked broken while working fine.
`setPipLabels` now derives the state from `document.pictureInPictureElement`
rather than trusting its caller's wording, and `#pipCam` listens for
`enterpictureinpicture` / `leavepictureinpicture` so closing the floating window
from its own control (or having the OS take it) un-illuminates the button. The
lesson generalises: **an icon-only toggle's entire visible state is
`aria-pressed`.** Forget the attribute and the CSS has nothing to hook, with no
error anywhere.

`Back` sits bottom-left under the diagnostics with an arrow; `Start recording`
is bottom-right. The recording bar is `position: fixed` while recording, with a
spacer reserving its height — note it floats within *this window*, not above
other applications.

**Reset position lost its button** but kept its job: it is on the `r` key. It is
the escape hatch for geometry restored from a bad save, which once left the
overlay invisible.

**Blank screen** covers the screen layer only — face, watermark and timer stay
visible, so the recording reads as deliberate rather than dead. Always resets
between takes.

It used to letter *screen hidden* across the middle of the frame. That is a
caption for the viewer of a recording that is deliberately showing them nothing,
and it sat exactly where a face or a slide lands when the screen comes back. The
lit button and the diagnostics line are for the presenter; **the recording does
not need narrating.**

## The burnt-in timer

`formatClock(ms)` is shared by the control-bar timer and the canvas overlay, so
a long recording cannot show `90:00` in one place and `1:30:00` in the other. It
rolls into `H:MM:SS` past an hour.

Two fixes worth remembering (v1.10.0):

- **`elapsedMs()` returned the epoch before the first take.** `startedAt` is `0`
  on the arrange stage, and `Date.now() - 0` is ~1.79e12 ms — which the overlay
  rendered, correctly and uselessly, as **`29806737:49`**. It now returns `0`
  when `startedAt` is falsy, so the arrange stage previews a real `00:00`.
  The general shape: *a duration computed from an uninitialised start time is
  not a small wrong number, it is a timestamp.*
- **The pill twitched on every digit.** Proportional digits meant `00:11` and
  `00:08` measured differently, so the box resized once a second. It now uses a
  monospace stack and measures a same-length template of `8`s. Text is centred
  off the box with `textBaseline: 'middle'` rather than positioned by a padding
  guess, and the corner radius is half the height, so it is a true pill.

## Dialog behaviour (the help panel)

Since 1.18.0 there is one dialog, `#helpDlg`, with four tabs - Keyboard
shortcuts, About, Changelog, More apps - in the same order as every app in the
family. It replaced the separate `#keysDlg` and `#aboutDlg`, and the header's
keyboard and `?` icons became a single `?` at the right-hand end, beside a new
theme toggle. The tab strip lives inside the sticky `.dlg-head`, so it stays
reachable however far down a tab you scroll. `openHelp(tabId)` is the one way
in; the notes below still hold for it.

Three closes — a sticky **X**, a click on the backdrop, and `Escape` (free from
native `<dialog>`) — and no footer button. Three things are worth knowing:

- **The dialog used to open already scrolled down.** Not a scroll bug:
  `showModal()` moves focus to the first focusable descendant and the browser
  scrolls it into view, and the only focusable thing was *Close* in the footer.
  The X is now first in the DOM, which fixes the cause; `openDialog()` also
  resets `scrollTop` for whatever focusable element gets added above it later.
- **`.dlg-head` is `position: sticky`**, so the X is reachable from anywhere in
  a long dialog rather than only from the point you opened it at.
- **A backdrop click is detected by the pointer's position, not by
  `e.target === dlg`.** The target test is the usual trick and it works because
  the dialog has no padding, but with `overflow: auto` a click on the
  *scrollbar* also targets the dialog element — and closing the dialog when
  someone grabs its scrollbar is infuriating. Comparing the click against
  `getBoundingClientRect()` cannot make that mistake.

## The sound meter

A progress bar and a countdown sit to the right of the sound row, and each
button's tooltip carries its length (`Applause · 6.8s`). Sounds go live into the
recording, so timing one against what you are saying was guesswork otherwise.

- **It is driven from `performance.now()` against the buffer's own duration**,
  not from the `AudioBufferSourceNode`. `onended` can only tell you it is over,
  which is not the question being asked.
- **Overlapping sounds: whichever finishes last owns the bar.** Otherwise
  hitting a 1.4s rimshot during 6.8s of applause would snap the bar back to
  zero and count down to a finish that had not happened.
- **When a sound ends the bar empties but the length stays on screen.** "That
  was 6.8s" is the thing you wanted for next time; blanking it throws away the
  only answer the meter ever gives you.
- It is `aria-hidden`: `playSfx` already announces, and a bar counting down
  would be noise to a screen reader.

## Keyboard shortcuts dialog

(Now the Keyboard shortcuts tab of the help panel - see above. The header
button is the `?` at the right; the recording bar's keyboard button and the
`?`/`F1` keys open the panel on this tab.)

Two ways in, and the second one exists because of the first. A `keyboard` icon
sits next to the `?` in the header, and `?` opens it from anywhere — but **the
floating recording bar sits on top of the header during a take**, so the header
button is literally unclickable exactly when you most want the shortcut list.
There is now a matching button in the orange bar itself.

`verify_reckeys.js` asserts that overlap with `elementFromPoint` rather than
taking it on trust, so the reason the second button exists is written down as a
test.

**How it right-aligns without a second layout.** `.rec-keys` carries
`margin-left: auto`, which looks like it should fight the `flex: 1` spacer that
already pushes Pause right. It does not, and the order of operations is why:
flex grow resolves **before** auto margins, so on a single line the spacer eats
all the free space, nothing is left for the auto margin to absorb, and the
button simply trails Stop recording. When the bar wraps, the spacer stays up on
line one — line two holds only Stop recording and this button — so free space
exists again and the auto margin carries it to the right edge, landing it
directly under Pause. One declaration, correct in both layouts.

Its vertical padding is 8px where the other bar buttons use the base 11px: its
content is a 23px icon rather than a ~17px line of text, so equal padding left
it 2px taller than Pause and Stop and visibly proud of the row. The test now
asserts all three heights match.

 Worth knowing: the live-stage key handler bails early with
`if ($('hotspots').hidden) return;`, so `?` is handled **above** that guard —
it is the one key in there that is not about the webcam overlay. Below the
guard it would only have worked in Combined mode, which is the one place users
least need to be told what the keys are.

The dialog states its own scope in a box at the top, because most of the keys
genuinely do nothing outside Combined mode and a list that silently lies is
worse than no list.

## A missing tag that looked like a spacing bug

Worth its own heading, because the symptom was three steps from the cause.

The v1.10.0 edit that reordered the effects row consumed the cluster's closing
`</div>` and never put it back. Nothing broke: the parser recovered by letting
the *row's* `</div>` close the cluster instead, so `<p class="hint">` ended up
inside the row, the row became the last element child of `#liveControls`, and
`.ctl-row:last-child { margin-bottom: 0 }` matched it. The gap above the sound
row vanished. Reported, reasonably, as "the spacing is too small".

Two things follow:

- **Check tag balance after any patch that brackets a region by find-index.**
  `src[i:j]` silently swallows whatever closing tags sit inside it. A one-line
  count of `<div` versus `</div>` against the previous version catches it. (The
  count is not zero-sum here — a JS template string contributes one unmatched
  `<div`, so compare the *delta* to the last known-good file, not to zero.)
- **A CSS rule that keys off document position is a tripwire for malformed
  markup.** `:last-child` did exactly what it was told; the markup lied to it.

`verify_ui113.js` now asserts the structure directly — the hint is a direct
child of `#liveControls`, the effects row contains exactly `[lead, cluster]`,
and all three row gaps are equal — so this cannot come back silently.

## Gotchas worth remembering (all learned the hard way)

- **Never release and immediately re-acquire the same macOS camera.** You get a
  track that reports `readyState: "live"` and never delivers a frame — a black
  preview with no error. The code adopts the setup preview's existing track
  instead. Matching must use `track.getSettings().deviceId`, not a remembered
  dropdown value, which goes stale when device labels refresh after permission.
- **Fake camera devices never reproduce that**, so headless tests pass while the
  real app shows nothing.
- **`requestAnimationFrame` is suspended when the page is backgrounded.** A
  canvas compositor driven by rAF silently freezes the recording on its last
  frame the moment you minimise the window. The draw loop runs off a Web Worker
  timer, which is exempt.
- **An absolutely-positioned element sized only by JS collapses to 0×0** if that
  JS bails out. `#bubble` has a CSS size floor and retries a zero measurement.
- **`overflow:hidden` used to shape an element clips its own drag handles.** The
  resize grip is a sibling of the bubble, not a child.
- **`hidden` is an HTML IDL property; `SVGElement` does not have it.**
  `svg.hidden = false` silently does nothing. Wrap SVGs in a span to toggle.
- **Keep every shape class in one list** (`SHAPE_CLASSES`) so switching away
  from a shape cannot leave a stale class behind.
- Test **transitions**, not just states. Several bugs here only existed on the
  way *back* from a mode.
- **A cache-first service worker for the document freezes your version forever.**
  See "Why the document is network-first" above.
- **Absolutely-positioned siblings paint in DOM order.** Hot-spot dots needed an
  explicit `z-index` or the overlay buried whichever dot it was parked on,
  making it unclickable.
- **A patch script that validates anchors one at a time can lose every earlier
  edit** when a later one fails before the write. Validate all anchors first,
  then write — the `ok` lines otherwise report intent, not saved changes.
- **`Promise.allSettled` in the worker install is what lets optional files be
    optional.** The three absent `sfx-*.mp3` files do not block activation.
- **A pixel test is only as good as its classifier.** The confetti test reported
  "no confetti found" because several confetti colours are blue or green, and the
  detector classified them as screen or camera. The feature was fine. Prefer
  injecting a known particle at a known coordinate and probing exactly there.
- **Anything in `init()` that READS restored state must run after
  `loadSettings()`.** The logo decode and the overlay-button paint were both
  placed before it and silently used defaults — the logo source was still
  `'none'`, so nothing decoded and *no error was raised either*. A silent
  no-op is harder to spot than a thrown one.
- **Never close the `AudioContext` between recordings.** Closing it left the
  sound-effect `GainNode` belonging to a dead context, so the *next* recording
  threw "cannot connect to an AudioNode belonging to a different audio context"
  and silently never started. One context lives for the page; just
  `disconnect()` the bus. **Found only by a test that recorded twice** — every
  earlier test used one recording per browser context.
- **Test repetition, not just the happy path.** Two of the nastiest bugs here
  (this one, and the poisoned `localStorage`) only appear on the second run.
- **`destination-out` erases everything below it on that canvas**, not just the
  layer you meant. Composite such effects from a scratch canvas.
- **Don't block keyboard shortcuts on every `<input>`.** A focused range slider
  has no use for letter keys, so blocking there meant that after nudging a
  slider, `s` and `c` silently did nothing. Block on what *consumes* the key.
- **`textContent` on an icon button deletes its icon.** Toggling state on the
  new Lucide buttons wiped their SVGs. Text-bearing icon buttons now carry a
  `.ibtn-label` span that state updates write to; icon-only buttons keep their
  state in `aria-pressed` plus `title`/`aria-label`.
- **Chromium ships without AAC; Chrome has it.** An `.m4a` fetches fine (200) and
  then fails `decodeAudioData` in a Chromium test build —
  `canPlayType('audio/mp4; codecs="mp4a.40.2"')` returns `""`. Not a bug, but it
  means m4a support cannot be proven in this test environment.
- **Don't derive filenames from display labels.** The "not available" hint built
  `sfx-<lastWordOfLabel>.mp3`, so "Laugh track" told you to add `sfx-track.mp3`.
  Build paths from ids.
- Web fonts are deliberately not cached — they are cross-origin and would be
  stored as opaque responses. Offline, type falls back to the system stack.
