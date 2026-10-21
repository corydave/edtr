# ANIMEDTR changelog

## 0.24.0 - 2026-10-21

**Rigging: posing figures** (Dave's picks, after seeing StykAnimate go open
source: both stick figures and figures made of groups; the limb bends with
pins; saved poses plus ready-made ones. StykAnimate is GPL-3.0, so only its
ideas were used, none of its code).

- **Pose mode:** pick a figure and press **J** (or **Pose** on the quick
  bar, in the Inspector's new **Pose** section, or in the right-click
  menu). Every joint shows a dot, each bone a thin line, and the ends of
  the limbs (hands, feet, the head) an orange dot. **J** or **Escape**
  when done.
- **Drag a hand and the arm bends:** drag any part and the joints of its
  limb turn so the point you hold follows the pointer: a hand bends the
  elbow and the shoulder, a foot the knee and the hip. The body stays
  put: a limb starts where a joint holds more than one (the body holds
  the head and both arms). Out of reach, the limb points straight at the
  pointer. **Shift** + drag turns just the joint you hold. Dragging a
  joint's dot (an elbow, a knee) turns the joint above it. Dragging the
  hips (the dot where the legs join), or a part of the figure itself (the
  robot's body), moves the whole figure.
- **Pins:** double-click a part, or tick **Pinned** beside its joint, and
  its end stays where it is on the stage while you pose the rest (a
  square on the stage shows it). Pin both feet and drag the hips down,
  and the knees bend.
- **Kept at once, as keyframes:** the first change at a frame gives the
  figure and every joint a keyframe there (holding where they were), so a
  pose is always whole. Move the play head and pose again to animate.
  One drag, one key press or one pose is one undo step.
- **The keyboard:** in Pose mode, **N** and **Shift+N** pick a joint (it
  is read out, with how far it is turned and whether it is pinned),
  **Left** and **Right** turn it (Shift: 10 degrees), and with the whole
  figure picked the **arrows** move it (pins hold). The Pose section also
  lists every joint with its turn as a number, and its Pinned box.
- **The stick figure (Y,** a new button on the tool rail): ten joints
  (Body, Head, Left and Right upper arm, forearm, thigh and shin), each a
  group with its pivot on the joint, so it is an ordinary group you can
  recolour, resize, give a shadow or open up. "Left" is the left of the
  screen as it faces you.
- **Poses:** **Put a pose here** puts a pose on the figure at the play
  head; each joint turns the short way to it. A stick figure has Stand,
  Wave, Walk (step 1 and 2), Run, Jump, Sit and Cheer. **Save this pose**
  keeps the figure's pose by name in the lesson (joints by their names),
  for any keyframe of any figure whose joints have the same names; saving
  a name again updates it. **Delete a saved pose** removes one.
- **Any figure of groups inside groups** poses the same way: the robot,
  or a drawing from Inkscape or VCTREDTR (whose rotation centres already
  come in as pivots).
- **A new template, Posing a figure (rigging):** a stick figure walks in,
  waves, crouches and jumps for joy, cheers and lands, with a marker and a
  description for each part.

## 0.23.0 - 2026-10-21

**Pictures: crop, shape and border; drop shadows on anything** (Dave's
picks: crop by dragging on the stage; rounded and circle shapes; shadow
presets you can fine-tune; shadows on everything, not just pictures).

- **Crop on the stage, like PowerPoint:** pick a picture and press **C**
  (or **Crop** on the quick bar, in the Inspector's Look, or in the
  right-click menu). Its handles become eight crop bars, on the sides and
  the corners. Drag one in and that side is cut off: the box shrinks with
  it and the picture stays exactly where it was. The parts cut off show
  faintly, with a dashed line round the whole picture, while you crop.
  Dragged back to within a few pixels of the picture's own edge, a side
  snaps to it (Alt: no snapping).
- **Slide the picture under its box:** in Crop mode, drag inside the
  picture, or use the arrow keys (1%, Shift: 10%), to choose which part
  shows. It never goes past the picture's own edge. **C**, **Enter** or
  **Escape** ends Crop mode; it says how the picture is cropped.
- **By the numbers:** Look has **Cut off (% of the picture)**: Left, Right,
  Top and Bottom, and **Reset crop**. At least 5% always shows each way.
  A crop is the picture's own, the same at every keyframe: when you crop,
  every keyframe's box shrinks to match and moves so the picture stays
  put, so a picture that moves, grows and turns keeps doing so, cropped
  the same way all through. **Fit the box to the picture** now keeps the
  crop's shape. **Replace picture** starts the new picture uncropped.
- **Shape and border:** a picture's **Shape** is Rectangle, Rounded
  rectangle (its **Corners**, 24 to start) or Oval or circle (a circle in a
  square box). **Border** draws an outline round that shape, in any colour
  and width.
- **Drop shadows on anything:** pictures, shapes, lines, text and groups
  have a new **Shadow** section. Start from **Soft**, **Close** or
  **Lifted**, then change its colour, **Strength**, **Softness**,
  **Distance** and which way it **Falls** (eight directions); changing a
  number makes it **Your own**. It falls the same way however the thing
  is turned, as if the light stays put, and fades with it. With several
  things picked, **Arrange** has a Shadow for all of them at once.
- **In the lesson:** cropping, shapes and shadows are SVG clip paths and
  filters set as attributes, so the exported lesson's strict Content
  Security Policy (no inline styles) is kept. A picture's name for a
  screen reader is unchanged; the border and shadow are not read.
- **Fixed:** a part of the Inspector that redraws itself (such as the
  shadow's numbers appearing) now starts its fields with their values,
  and keeps focus on the field you were in.

## 0.22.1 - 2026-10-16

- Ready for EDTR Studio (edtrapps.com/create/), one window with every app: inside the Studio, links to the other apps open them right there, Ctrl+Shift+1 to 9 switch apps (Ctrl+Shift+0 goes to the rail), and the splash leaves out its "More apps" row. On its own, nothing changes.
- The shared SUITE block gained its "EDTR STUDIO" section (`suiteInStudio()`).

## 0.22.0 - 2026-10-15

**Shape tweens: morphing** (Dave's pick, like Flash's shape tween; both
ways in; the second shape becomes the end).

- **Morph one shape into another:** pick two shapes (rectangles, ellipses
  or outlines) and choose **Morph Square into Oval** (or the other way
  round) from the right-click menu or **Arrange** in the Inspector. The
  first turns into the second over a second from the play head: its
  outline, place, size and colour all blend. The second shape is used up
  for the end (behaviours that pointed at it go too); **Undo** brings it
  back in one step.
- **Morph into a shape...:** pick one shape and choose it from **Motion**
  in the Inspector or the right-click menu. The Shapes gallery opens in a
  dialog (filled shapes for a filled shape, lines for a line); pick one and
  the shape becomes it, in the same place and at the same size. Escape
  changes nothing.
- **It is all keyframes:** a keyframe can now have an outline of its own.
  At a keyframe, **Edit points** changes the outline there; between two
  keyframes the outline is worked out for you, so there are no points to
  edit (it says to go to a keyframe). A keyframe added half-way through a
  morph keeps the shape it has there, so nothing jumps. The Motion table
  marks a keyframe that has its own outline.
- **How it blends:** both outlines are walked round at the same pace and
  matched point for point (turned to the best starting point, and the same
  way round), so a square becomes a star without twisting. An outline in
  two pieces morphing into one in one piece grows the extra piece from a
  dot. Rectangles and ellipses become outlines first, as **Turn into an
  outline** does.
- **Safe and small:** a keyframe's outline is checked like any outline
  (path data only, and not too long) when a lesson is opened.
- **A new template, A butterfly's life (morphing):** one shape becomes an
  egg on a leaf, a caterpillar, a chrysalis, then a butterfly that flaps
  away, with a label and a marker for each stage.

## 0.21.0 - 2026-10-15

**Effects: motion presets and text effects** (Dave's pick for a bigger
build; presets make real keyframes; several things can go one after
another; all four text effects).

- **The gallery:** pick one thing or several and press **E** (or **Add an
  effect...** on the quick bar, at the top of the Motion section, or in the
  right-click menu). Twenty-four effects in four groups, each a card with a
  little picture that plays while you point at it or move to it with the
  keyboard (not when the device asks for less motion). The arrow keys move
  between them, Enter adds the one you are on, Escape adds nothing.
- **Entrances** (the thing appears at the play head): Fade in, Fly in (from
  the side you pick), Rise up, Zoom in, Pop (springs out a little too big,
  then settles), Bounce in, Spin in.
- **Emphasis:** Pulse, Wiggle, Shake, Hop, Spin, Blink (twice a second at
  most, gently: never a flash) and Colour flash (to the colour you pick and
  back).
- **Exits** (the thing leaves once it is gone): Fade out, Fly out, Sink,
  Zoom out, Pop out, Spin out.
- **Real keyframes:** an effect is written as ordinary keyframes from the
  play head, which you can then nudge, retime or delete like any others,
  and Undo takes it back in one step. Sizes change round the pivot (so a
  Pulse round a hinge grows from the hinge). Keyframes already in its way
  make way for it (it says how many); after a Spin, later keyframes are a
  whole turn on too, so it never spins back. A lesson too short for it
  grows to fit.
- **How long, which way, which colour:** each effect starts with a sensible
  length (0.6 s in and out, 1 s for emphasis; text by how much there is to
  show: about 25 letters, 3 words or 1.5 lines a second), and you can type
  your own.
- **One after another:** with several things picked, they go top to bottom
  (left to right along a row) with a gap between them (0.3 s at first):
  bullet points fly in one by one with a single click.
- **Text effects:** **Typewriter** (letter by letter, with a cursor if you
  like), **Word by word**, **Line by line** and **Highlight sweep** (a
  marker-pen highlight behind the words, in the colour you pick). Text
  boxes have two new values that animate like anything else, **Shown (%)**
  and **Highlight (%)**, in their Look section, with **Shows by** (letters,
  words or lines), the cursor, and the highlight colour. The lines stay
  where they will be as the words appear, and a screen reader always has
  all of the words.
- **A new template, Bullet points (effects):** states of matter, with a
  title that types itself, points that fly in one after another, a
  highlight sweep, and a star that pops in and pulses. All of it was made
  with effects.
- In the project file, values gain `reveal` and `hl` (0 to 1), and text
  boxes `revealBy`, `revealCursor` and `hlColour`. Lessons made before show
  everything and highlight nothing, as they always did.

## 0.20.0 - 2026-10-15

**Masks** (Dave's pick: mask groups, like Illustrator's clipping masks;
hard edges, with a Soft edge option).

- **Make a mask:** pick a shape and the things that should show through
  it, then **Make a mask** (the Inspector's Arrange section, or the
  right-click menu). They become a group (Mask 1) whose **front-most part
  is the window**: everything else in the group shows only where the
  window is. Everything outside it is cut away.
- **The window animates like anything else.** Move it for a torch beam
  sweeping a dark scene, grow it from nothing for a reveal, slide it for a
  wipe across a diagram, fade it to fade what shows. Any kind of part can
  be the window: a shape, an outline, text (words you see the picture
  through), a picture, even a group. Its colour does not matter; how
  see-through it is does.
- **Soft edge** (the Inspector's new **Mask** section) feathers the window,
  so a spotlight fades out gently (0 is a clean cut). The section also
  picks which part is the window, and **Release mask** makes it an
  ordinary group again (the window shows as itself). Any group can become
  a mask there, with its front part as the window.
- **While you work inside a mask group** (double-click it), its mask is
  off, so every part shows in full; a dashed line shows the window's edge.
  Leave the group and the mask is back. On the stage the window shows
  faintly, so it can be seen and picked, and its dashed edge shows whenever
  the group is picked.
- **Copy, paste and duplicate** keep the mask (the copy looks through its
  own copy of the window). Deleting the window, or ungrouping, ends the
  mask.
- **Screen readers** never read the window (it only shapes what shows);
  the other parts are read as in any group, and a named mask group is read
  as one picture, as before.
- **Everywhere a lesson goes:** the exported lesson, SCORM, the video, the
  GIF and the picture of a frame all show the mask, using SVG's own
  `<mask>` (with each stage on a page given its own ids, so a template's
  card and the stage never mix theirs up).
- **A new template, A torch in the deep (masks):** a dark sea that shows
  only through a round torch beam with a soft edge, which sweeps across to
  find fish, a crab and a treasure chest.
- In the project file a mask group has `maskBy` (its window's id) and
  `maskSoft`. A window that is not one of the group's own parts is ignored.

## 0.19.1 - 2026-10-15

**Inkscape's rotation centres become pivots** (Dave: work on the Inkscape
rotations, the first thing 0.19.0 left out).

- In Inkscape, the rotation centre is the little cross you can drag when
  something is in rotate mode. When it has been moved, Inkscape keeps it in
  the file (`inkscape:transform-center-x` and `-y`: how far it is from the
  middle of the thing's box, in the file's own units, with y counted
  upwards). ANIMEDTR now reads it when an SVG comes in as shapes, and makes
  it that part's **pivot**: an arm whose centre sits on its shoulder swings
  from the shoulder here too.
- It works for **groups** (an arm group, a head group), **shapes**,
  **text** (turned text too), and **the drawing as a whole** (when the
  drawing is one group in Inkscape, its centre becomes the drawing's
  pivot). A group that holds just one shape passes its centre to that
  shape.
- **Nothing moves:** each part is drawn exactly where it was without the
  centres; only what it turns round changes. The message after bringing a
  drawing in says how many parts kept one.
- **Safe to read:** only two plain numbers of a sensible size are taken
  from each part (anything else is ignored), and they reach the drawing
  engine as numbers ANIMEDTR writes itself.
- Drawings from VCTREDTR, Illustrator and the rest have no such centres,
  so their parts turn round their middles, as before. ("As one picture"
  has a single pivot, the middle.)

## 0.19.0 - 2026-10-15

**Pivot points** (Dave's pick for the next build: one pivot for each
object, not animated; it is for turning and resizing; a Pivot button and a
key to drag it on the stage, with a picker and numbers in the Inspector).

- **What it is:** the point something turns (and resizes) round, Flash's
  transformation point. It starts in the middle, so nothing changes until
  you move it. Put an arm's pivot on its shoulder and the arm swings from
  the shoulder; a hand's on its wrist and it waves from the wrist; a door's
  on its hinge. Each object has one pivot, the same at every keyframe.
- **On the stage:** the picked object shows its pivot as a small dot.
  Press **Q** (Flash's Free Transform key), or the new **Pivot** button on
  the quick bar, and the dot can be dragged. It snaps to the corners, the
  middles of the edges and the middle (hold Alt for no snapping). The
  **arrow keys** move it 1% of the object's size (Shift: 10%), and it says
  where it is ("Pivot at its top left"). Q or Escape when done.
- **In the Inspector** (Position and size): a 3 by 3 picker (nine radio
  buttons; the arrow keys move between them), **Across** and **Down** in
  percent (the pivot may sit outside the object, up to four times its size
  away, like the top of a pendulum's string), and a button that does what
  Q does.
- **Moving the pivot never moves the object:** at every keyframe (and in
  a change not kept yet) X and Y change so that it is drawn exactly where
  it was. Only the turning between keyframes changes, which is the point.
- **Resizing round the pivot** (Dave: turning and resizing, like Flash):
  typing **W or H** grows or shrinks it from its pivot (from the middle,
  unless you moved the pivot), and so does **Alt + dragging a corner**.
  Dragging a corner without Alt still keeps the opposite corner where it
  is. Older lessons look exactly as they did: a size change between two
  keyframes was already kept as numbers at each keyframe, and those numbers
  are not touched.
- **The turn knob** turns things round the pivot. **Along a motion path**,
  the pivot is what travels along the path (a paper plane can fly by its
  nose).
- **Groups** turn round their own pivot, and the parts inside round
  theirs. Ungrouping keeps each part where it is drawn.
- **A new template, A waving robot (pivots):** a robot of groups inside
  groups. Its arm swings up from the shoulder, the hand (a group inside the
  arm) waves from the wrist, and the head tilts from the neck, on a loop.
- In the project file each object has `pivot: [across, down]` (shares of
  its box). Projects and lessons without one turn round the middle, as
  before. The Features tour's Start from a template card now says thirteen.

## 0.18.1 - 2026-10-15

**The tour plays the real thing** (Dave: swap some of the tour's drawings
for the templates that really pop, like the bouncing ball and Click to
reveal).

- **Animate with keyframes** (now first) plays the bouncing ball template:
  the ball drops, stretches, squashes and bounces across the toy world.
- **Interactive, with no code** (second) plays Click to reveal (neon): the
  scanner types its question, a pointer presses Show the answer, and
  eleven Earths line up across Jupiter.
- **Start from a template** is a new card with the water cycle playing all
  the way round. It takes the place of Save, open, pick up again.
- Draw paths, Lessons everyone can use and One file that works anywhere
  are unchanged.
- **How:** the lesson's own runtime drew each template frame by frame, and
  every change was written down as SVG animation tags, so the tour still
  needs no script, works offline, and pauses (or shows its best still
  frame when the device asks for less motion) like every other card.
  The soft colour fades are shrunk to small pictures, and a straight-line
  stretch of movement keeps only its ends, so the three come to about
  250 KB. They keep the templates' own colours in light and dark mode.
  The tool that makes them is `_edtr-suite/features-src/captures/animedtr-capture.js`.

## 0.18.0 - 2026-10-15

**Groups inside groups** (Dave's pick for the next build: "as deep as you
like", up to 10; SVG drawings keep their nesting; not inside clips yet).

- **Ctrl+G now works anywhere:** on the stage, or inside a group (the new
  group goes inside it). A group can hold groups, up to ten deep: a body,
  its arm, the arm's hand, the hand's fingers. Each level animates on its
  own, and everything inside follows (the finger turns with the hand, the
  hand swings with the arm). The eleventh level is refused, and the
  status line says why.
- **Finding your way:** a click on the stage picks the thing on the stage;
  inside a group, a click picks what is in that group (even if you
  clicked something deep inside it). Double-click, or Enter, goes one
  level in, with the part you double-clicked picked; Escape goes one level
  out, with the group you left picked; a click outside goes back out to
  wherever it is. It says where you are: "Inside Hand group, in Arm group,
  in Body group". The layers tree shows every level, indented, as before.
- **Ungroup** puts the parts in the group around it (or on the stage),
  where they are now. **Copy, Duplicate, Delete and Move to layer** take
  everything inside, however deep. Pasting a group while inside another
  puts it inside (or a level further out, if it would go too deep).
- **For screen readers:** a group with a name (or a button, or decoration)
  speaks for everything inside it, however deep; otherwise its parts are
  read where they are, in the order they are drawn.
- **SVG drawings** (0.15.0) now keep their own groups inside the drawing's
  group (VCTREDTR's layers: a head, the arms, the legs), up to the depth
  limit. A group holding just one thing is not kept; the thing takes its
  name ("Wing"). So the "a group for each of its groups" choice is gone:
  one group now does both. Inside a group, a drawing goes in as a group of
  its own.
- **Opening a lesson** checks the groups: none more than ten deep, no loops
  (a group inside itself), parts on the layer of the group at the top.
- **Fixed:** double-clicking a group, a clip or a text box with a mouse did
  nothing (the stage holds on to the pointer while it is pressed, so the
  double-click seemed to land on the stage itself). Enter always worked;
  now both do.
- **Not yet:** groups inside clips. Things learners drag, and answers to
  questions, still have to be on their own (not in a group); grouping
  them says so.

## 0.17.0 - 2026-10-14

**MP4 video** (the second of the night's two builds: started only once
0.16.0 passed every check).

- **Export, Video, Format: MP4 or WebM.** MP4 (picked first when this
  browser can make it) is the one that plays everywhere: PowerPoint and
  Keynote, phones, QuickTime, Kaltura and most video tools. WebM stays:
  smaller, for browsers, Brightspace and YouTube. The captions file
  (.vtt) comes with either.
- **Inside:** H.264 pictures in "constrained baseline" (every player reads
  it, and it has no frames that point forward, so they are stored in the
  order they show), at the level the size and speed need (3.1 for
  1280x720, 4.0 for 1920x1080, up to 5.1 for 4K), and AAC sound at 48 kHz.
  ANIMEDTR writes the MP4 itself (writeMp4: the ISO base media format, a
  tree of four-letter boxes), with the index first ("fast start"), so it
  starts playing before it has all arrived. No libraries.
- **The dialog says what this browser can do,** a moment after it opens:
  - no H.264 encoder (Chromium on Linux, for one): MP4 is greyed out and
    WebM is picked (and if MP4 was picked anyway, a WebM is made, and the
    message says so);
  - H.264 but no AAC encoder: the note warns that the sound will be Opus
    (browsers and VLC play it; PowerPoint and QuickTime may not);
  - Chrome and Edge on Windows and on a Mac have both.
- **Checked with ffmpeg** (this workspace's Chromium has no H.264 encoder,
  so the boxes were tested with H.264 and AAC made by ffmpeg, then put in
  an MP4 by writeMp4): ffprobe reads every field, ffmpeg decodes it with
  no errors, every picture is the same as the original frame by frame,
  the sound is the same sample by sample, keyframes are listed, and it is
  laid out ftyp, moov, mdat; at 24, 30 and 60 frames a second, with and
  without sound. The whole way through this browser's own encoders (VP9
  and Opus in an MP4, as a stand-in) a lesson came out with every frame,
  its length and its sound.
- **To know:** the AAC encoder adds a sliver of quiet at the very start of
  the sound (about 1/40 of a second), which is not trimmed. Not tried in
  Safari, nor with a real H.264 encoder (Chrome on a Mac will be the first).

## 0.16.0 - 2026-10-14

**Questions, with the answers checked for you** (Dave: "do all four... or
is it best to do just one or two?": this is the first of the two builds
for the night; the choices below were made while Dave slept, to be
changed in the morning if he likes).

- **The Lesson's new Questions section.** Each question has a name, the
  points a right answer earns (added to a variable: the Score, made if
  there is none, so the score reaches an LMS), **One try** or **Until
  right**, and with one try **After a wrong answer, show the right one**.
  Each has its own two cards of actions: **When it is answered right**
  and **When it is answered wrong** (a sound, a Say, Go to a marker...).
  The lesson can also act **When every question is answered** (once).
- **Add a question** makes a working starter on the stage (all ordinary
  objects, to change as you like), in the next of three columns, so three
  starters sit side by side:
  - **Multiple choice:** a question and three answer buttons (Whale is
    right). Any object on its own can be an answer: pick it, then its
    **Question** section: **An answer to** (which question) and **The right
    answer**. Tick more than one right, and any of them counts.
  - **Click the right spot:** a picture placeholder and three **spots**:
    shapes learners cannot see (only their focus ring, and their tick or
    cross once picked), dashed orange while you edit. Lay them over the
    parts of a picture. A screen reader reads each spot's name, so name
    it by where it is, not by whether it is right (the check says so).
  - **Type the answer:** a question, an **Answer box** and a Check button.
    The box is a real text box in the lesson: Enter checks it (so does
    any button with "Check the answers"). It takes a list of **accepted
    answers**, one a line; capitals, extra spaces and a full stop at the
    end do not matter. A number can be **off by** a little (3.14 within
    0.01), and "3,14" (a decimal comma) and "1,500" (a thousands comma) are
    read the usual ways. With one try and "show the right one", a wrong
    answer shows the answer in the message strip.
- **In the lesson:** a right answer gets a white tick on green, a wrong
  one a white cross on red, the right one (shown after a wrong one) a
  green tick on white; colour is never the only sign. "Right!", "Not
  right. Try again." and "Not right. The right answer: Whale." are read
  out. Answers stay in the Tab order once their question is done, named
  with how it went ("Shark, your answer, not right"), and say "this
  question is answered already". Restart puts everything back. The text
  version explains how to answer. Answer boxes keep their place in a
  reading order of your own (Tab goes to them in order).
- **Safety:** what learners type is only ever compared as words: never
  put in the page as markup, never run (tested with an `<img onerror>`).
  The box has no spelling help (it would give answers away), and a phone
  shows number keys when the answers are numbers.
- **Checks:** an Answer box needs a name (what to type: Needed); a
  question with no answers, no right answer ticked, a box that takes no
  answers, or a spot named "Correct" are warnings.
- **For an LMS:** "Out of" counts what questions earn.
- **New template: Check your understanding**: all three kinds on one
  screen (a mammal, the part of a plant that takes in water, the gas
  plants take in), with sounds, a score line, and "All three answered"
  when done. Set up for an LMS, out of 3. Thirteen templates now.
- **Reduce motion:** a button whose action is plain Play (like Step by
  step's Next step) now goes straight to where the lesson would stop
  next, without the movement, as "Go to marker and play" already did.
- **Fixed:** text that a behaviour shows was read out with "{Score}" as
  typed instead of the number. It now reads what it shows.
- **Not tested here:** Safari and Firefox (only Chromium is in this
  workspace). The Answer box is an HTML text box inside the SVG (a
  foreignObject); Safari has had bugs with those in the past, so it is
  worth one try there.

## 0.15.0 - 2026-10-14

**SVG drawings come in as shapes** (Dave picked this as the next build: it
was in the plan from the start, "SVG drawings brought in from VCTREDTR",
and had not been built).

- **Three ways in:** the Picture tool (F), a drop on the stage, or a
  paste: an SVG file, or SVG code as text (VCTREDTR's **Copy SVG code**).
- **The dialog** shows the drawing, says what it found ("7 shapes and 2
  text boxes") and what changed on the way in, and asks how to bring it in:
  - **As one group of shapes** (the usual): move the whole drawing, or open
    the group to animate any shape in it.
  - **A group for each of its groups** (when it has two or more, such as a
    character's head, arms and legs from VCTREDTR's layers): each one can
    be animated on its own.
  - **As one picture:** flat, like a PNG. Always possible, and the only
    choice when there are more than 200 shapes (or no room in the lesson).
  - Inside a group or a clip (which cannot hold groups), the shapes go
    straight in.
  The preview is drawn from ANIMEDTR's own numbers, never from the file.
- **What comes across:** every shape becomes an outline with its fill,
  outline colour and width, and see-through-ness (a group's opacity
  included); a shape with no fill becomes a line. Transforms (move, turn,
  stretch, skew), circles, polygons and arcs are worked into the points.
  An outline drawn at twice the size keeps twice the width. Text becomes a
  text box in ANIMEDTR's fonts (so it is read aloud), lines kept. Names come
  from the drawing (VCTREDTR's, Illustrator's data-name, Inkscape's labels;
  VCTREDTR's added " 1" is taken off), and the drawing's title and
  description become its words for screen readers.
- **What changes:** gradients become their average colour; dashed lines
  become solid; pictures, masks, clipping, filters, patterns and animation
  inside the drawing are left out. The dialog lists them.
- **"Non-zero" fills** (SVG's usual rule, where overlapping pieces of one
  shape stay filled) are untangled with Paper.js, so they look the same
  with ANIMEDTR's even-odd rule. Checked: drawn both ways, imports differ
  from the original in under 1% of pixels (a VCTREDTR export, nested
  transforms with skew and arcs, an icon set's stroke-only icon).
- **Safety, from the ground up** (the suite's SVG rules):
  - over 10 MB, a compressed .svgz, or any XML entity: refused before
    reading;
  - DOMParser reads it as data, then a clean copy keeps only drawing
    elements and a fixed list of attributes, every value checked (no
    scripts, "on..." handlers, links, outside pictures, stylesheets that
    import, or url()s that leave the file);
  - <style> classes are applied by ANIMEDTR itself (simple rules only);
  - <use> copies are expanded here, only the ones that show, at most 8
    deep and 20,000 elements in all, so a "billion copies" file stops in
    about a second;
  - nothing from the file is ever put in the page, and the copy is never
    attached to it.
  Tested with a hostile file (onload, script, foreignObject, javascript:
  links, outside pictures and stylesheets, a self-copying <use>): nothing
  ran and nothing was fetched.
- **Accessibility check:** a drawing of shapes with no words must have
  them (as a picture must); one with text gets a tip. When the file has
  no title, focus goes straight to Read aloud as.

## 0.14.1 - 2026-10-14

**Step by step, fixed** (Dave: "Add a 'Back' button, and double check
the logic").

- **Back.** Every step after the first has a **Back** button (labelled
  for screen readers with where it goes: "Back to step 2"). It goes to the
  step before and waits there. It hides for the half second while the
  next step builds, so it never jumps somewhere unexpected mid-build.
  **Start again** moved to the left, so the reading order (Start again,
  then Back) matches what is seen.
- **Next step moves one step, every time.** In 0.14.0 each Next step
  button used "Go to marker and play" on the next step's marker: that
  jumped straight to the next step and then played on, past it, to the
  one after (a step went by on its own). Now there is one Next step
  button for every step, and its action is plain **Play**: from the
  "Pause here" marker it is waiting at, it builds the next step and stops
  at the next marker. One button also means keyboard focus never has to
  move.
- **Why it only happened sometimes: a player bug, now fixed for every
  lesson.** The browser's time for a frame can be a touch earlier than
  the moment Play is pressed, which put the play head one frame back.
  Playing from a "Pause here" marker, it then met that same marker again
  and stopped there, so Play (or a button that plays) sometimes did
  nothing. That race is also why the template sometimes worked. The play
  head never goes backwards now (in lessons and in the editor).


**The rest of phase 3** (Dave: "Let's go with the rest of Phase 3!").

- **Colour schemes, as in DSKEDTR.** A lesson has six colours that go
  together, each with a job (DSKEDTR's six: Text, Main, Accent 1, Accent
  2, Pale, Light). The **Colour scheme** button (the Lesson section of the
  Inspector, nothing picked) opens a card for each scheme, showing this
  frame in its colours; pick one and the whole lesson is recoloured in
  one undo step: everything in the old scheme's colours, and lighter or
  darker shades of them (DSKEDTR's colour mapper, the same way), takes
  the new scheme's. That covers the stage's background, every object's
  colour and outline in every keyframe, the inside of clips, and colours
  that behaviours Set. White, black, pictures and your own colours stay.
  Fourteen schemes: **Studio** (ANIMEDTR's own, its usual colours, so
  older lessons start in it) and DSKEDTR's thirteen. Or change any of the
  six to make it your own, with a warning when text would be hard to read
  (DSKEDTR's four checks). **Every colour field** offers the six as
  swatches (one Tab stop, arrows along it), and new text, rectangles,
  ellipses and outlines start in Text, Main, Accent 1 and Accent 2.
- **Animated GIFs come in as flipbooks.** Add a GIF that moves (the
  Picture tool, a drop, a paste) and ANIMEDTR asks: **As a flipbook** (it
  moves) or **Just its first picture**. A flipbook gets one page for each
  of the GIF's pictures (at most 120: more are thinned out evenly), each
  showing for the GIF's own speed on average, and it keeps moving while
  the lesson waits, as a GIF does (one that plays once, plays once).
  Pictures over 960 pixels are scaled down. Its own decoder follows
  IMGEDTR's GIF spec on hostile files: the size is checked before anything
  is made (4000 a side at most, and a memory budget for all the pictures),
  at most 1000 pictures are read, the LZW decoder checks its code size,
  never grows its table past 4096, never writes past a picture's box and
  stops at the data's end, and a cut-off file keeps the pictures that were
  whole (and says so). Transparency, interlacing and all three disposal
  methods are handled.
- **Three more templates:**
  - **Step by step (process):** the scientific method as a flowchart that
    builds one step at a time and waits at each, with a card of words
    for each step and a Next step button. It is in the Studio scheme's own
    colours, so another scheme recolours all of it.
  - **Flip cards:** three vocabulary cards (Photosynthesis, Habitat,
    Predator). Activate a card to turn it over; again to turn it back.
  - **Match them (drag and drop):** four animals to their habitats, as a
    test: they stay wherever they are dropped until **Check my answers**;
    right ones score (with a chime), wrong ones slide back (with a bonk),
    and all four matched brings a fanfare. Set up for an LMS (out of 4),
    in the Meadow scheme.
- **Getting started (Help) says how to put a lesson in Brightspace:** as
  a page (Upload / Create, Upload Files), as a SCORM package with a grade
  item (Upload / Create, New SCORM Object / xAPI Object), or as a video
  with its captions (Video or Audio, then Advanced Editing, Closed
  Captions, Upload). Menu names can differ a little between colleges, and
  it says so.

## 0.13.0 - 2026-10-14

**More ways out** (phase 3 begins, Dave: "multiple modality exports").
Export now starts with **What to make**, and each choice shows its own
settings; the main button says what it makes.

- **Lesson** (one HTML file): as before.
- **For an LMS (SCORM 1.2 package, a .zip)**, for Brightspace, Moodle,
  Canvas or Blackboard: imsmanifest.xml and the lesson. Inside an LMS the
  lesson finds the LMS's SCORM API on the windows around it and:
  - marks itself "incomplete" when it opens;
  - sends its **score** as it changes (one variable, picked in Export,
    out of a number ANIMEDTR works out from what its behaviours add);
  - reports **"completed"** when the learner reaches the end or the last
    marker, or a behaviour runs the new action **Mark the lesson complete
    (for an LMS)**; with a **pass mark**, "passed" or "failed" instead (the
    manifest carries it as the mastery score);
  - sends how long it was open, and says goodbye, when the page closes.
  Only those values are sent; nothing about the learner is read. Outside
  an LMS (or as a plain lesson) it works as usual and sends nothing. The
  LMS settings are saved with the lesson; the quiz (out of 3) and Sort
  these (out of 6) templates come set up.
- **Video (WebM)**: VP9 video with Opus sound, full or half size, made with
  the browser's own video encoder (WebCodecs), frame by frame (it takes
  about as long as the lesson, often less), and
  written into a WebM file by ANIMEDTR itself (with cue points, so players
  can jump about). Beside it, a **.vtt captions file** from the captions of
  the sounds on the timeline, for Brightspace, YouTube or any player. The
  video plays straight through, the way the lesson plays before anyone
  clicks: behaviours do not run, nothing waits at a marker, things hidden
  at the start stay hidden, and only sounds on the timeline are heard.
  Browsers without WebCodecs (older Safari) are told so.
- **Animated GIF**: 320, 480, 640 or full width; 8 to 25 frames a second;
  plays over and over, once, or 3 times (the dialog notes WCAG 2.2.2: a
  GIF has no pause button); optional dithering for smoother gradients.
  One palette for the whole GIF (median cut, so no colour flicker), and
  each frame holds only the part that changed, with unchanged pixels
  see-through, so it stays small. The encoder is ANIMEDTR's own, written
  for beginners, and can grow into the family's planned GIF block.
- **Picture of this frame (PNG)**: as before, now one of the choices.
- A video or GIF shows a **progress bar** while it is made, and **Cancel
  becomes Stop** (Escape stops it too).
- Needed items still stop a lesson or an LMS package (learners use those),
  but not a video, GIF or picture.

## 0.12.0 - 2026-10-14

**Sounds**, the last of phase 2 (Dave's picks: a timeline track as well
as a Play a sound action, and captions in a strip under the stage).

- **Adding one:** Sounds, in the Lesson Inspector (nothing picked): Add a
  sound takes an MP3, WAV, Ogg, M4A (AAC) or WebM audio file, up to 15 MB
  (SNDEDTR's exports work). It is checked by its first bytes, never its
  name, played far enough to know how long it is, and kept inside the
  lesson (like pictures, outside the undo history). A sound over 5 seconds
  comes in as Speech, a shorter one as a Sound effect; Music is the third
  kind. Each has a name, a Listen button and a Delete button (which takes
  out its places on the timeline and the actions that play it, one undo
  step).
- **The timeline's Sounds row** (it shows once the lesson has a sound):
  "On the timeline here" starts a sound at the play head, as a block as
  long as the sound. Drag the block to move it, click it to see it in the
  Inspector, or type its frame there (the keyboard's way). Inserting,
  removing and changing frames a second move it along. A sound on the
  timeline follows the play head like Flash's stream sounds: Play starts
  it (part way through, if the play head is part way in), Pause pauses
  it, a jump catches it up, and while the lesson waits at a "pause here"
  marker it plays on to its end. Playing in the editor plays it too.
- **From a behaviour:** two new actions, **Play a sound** and **Stop all
  sounds**: a click, a right or wrong drop, a marker, a key.
- **Captions** (WCAG 1.2.2): speech needs its words, and Export asks for
  them; an effect gets a short note such as [a bell rings] (Accessibility
  reminds you). One line per caption; a line can start with its time
  ("0:12 Then the rain comes"), and lines without one share the time by
  how long they are. In a lesson, captions show white on black in a strip
  under the stage while the sound plays, and in full (without the times)
  in the text version.
- **In the player:** a **Sound** button (off and on: WCAG 1.4.2) and a
  **Captions** button, both on to start. Browsers only play sound after a
  click or a key, so a lesson that plays by itself starts silent until
  then (sound on the timeline catches up at once); Accessibility suggests
  starting paused when speech begins in the first two seconds.
- **Files:** saved projects keep each sound as its own file (sounds/ in
  the .animedtr file), checked again on opening; backups keep them too.
  An exported lesson carries only the sounds it plays, and its safety
  rules allow sound from inside the file only (media-src data:).
- **Templates:** the bouncing ball boings at each landing (one sound,
  four times on the timeline); Sort these chimes for a right drop, bonks
  for a wrong one and plays a fanfare when all six are sorted. Every one
  is made from numbers inside ANIMEDTR (a short WAV written on the spot),
  so no one's recording is in them.

## 0.11.0 - 2026-10-14

**Drag and drop** (sort these, match these), the second half of quizzes.
Dave's pick: the author decides, per draggable, between instant feedback
and a test that is checked later.

- **The Drag and drop section** of the Inspector, for anything on its own
  (not a part of a group; a group itself is fine):
  - **Learners can drag it**, with **Its right places** ticked below (none
    ticked: any place is right);
  - **It is a place to drop things** (it needs a name learners will hear:
    Export asks for one).
- **Instant (the usual):** dropped on a right place, it stays there for
  good (it is no longer a button) and its new card **When it is dropped on
  a right place** runs. On a wrong place, it slides back home and **When it
  is dropped on a wrong place** runs. Dropped on no place, it just goes
  back. Ticking "Learners can drag it" moves any "When it is activated"
  actions into the right-place card, and says so.
- **A test:** tick **Wrong drops stay where they land**. Then it stays on
  whichever place it is dropped, and the new action **Check the answers**
  (on a Check button, say) keeps the right ones, sends the rest back, and
  runs each one's card. It says how many were right.
- **When everything is in a right place**, a new card for the whole
  lesson, runs once every draggable is (until the lesson restarts).
- **Places line things up** in rows from their top-left corner (or in the
  middle, when only one fits).
- **Everyone can do it** (WCAG 2.1.1 and 2.5.7):
  - drag with a mouse, a pen or a finger (the page does not scroll under
    it), and the places show dashed rings while something is carried;
  - or tap the item and then tap the place, with no dragging at all;
  - or with the keyboard: Tab to it ("Mars, draggable item"), Space or
    Enter picks it up, the arrow keys or Tab choose a place (it shows
    there, with a solid ring), Space or Enter drops it, Escape puts it
    back. Every step is said ("Over Rocky planets, 1 of 2"). After a right
    drop, the keyboard moves on to the next thing to place.
  - The text version explains all three ways.
- **Checks:** Export wants a name for every place; Accessibility flags a
  draggable with nowhere to go, and one stacked behind its place (it would
  be hidden once dropped there).
- **A new template, Sort these (drag and drop):** six planets into Rocky
  planets and Gas giants, "Sorted: {Score} of 6", a hint for each wrong
  drop, and a cheer when all six are sorted.
- **Fixed:** in a lesson, a focused group showed a focus ring round each of
  its parts as well as round itself.

## 0.10.0 - 2026-10-14

**A score, and variables** (Dave's pick: quizzes in two builds, score and
variables first, then drag and drop in 0.11.0; scores show as {Score} in
text).

- **Variables** (the Lesson Inspector, nothing picked): numbers the lesson
  keeps while it plays. Each has a name (letters, digits and spaces; Score
  and score are the same name) and a whole number to start from. Every one
  goes back to its starting number when the lesson restarts. Up to 20.
- **Change a variable**, a new action for any card: Score, add 1 / take
  away 1 / set it to 0.
- **If a variable is...**, another: If Score is at least 3, then these
  actions, otherwise those (is, is not, is more than, is at least, is less
  than, is at most). Its Then and Otherwise lists sit inside the card, set
  in; they can hold any action but another If (one level keeps it easy to
  read).
- **{Score} in any text box or Say** shows the number: "You got {Score}
  out of 3". In the editor it shows the starting number. **Show a
  variable...**, under a text box's Text, puts it in at the cursor (and
  makes Score if there is no variable yet). Renaming a variable renames
  every {Name} in the lesson with it, so nothing breaks. Deleting one takes
  out the actions that used it (one undo step, and it says how many).
- **Read out as it changes:** a text box on screen that shows a variable
  is read out when its number changes ("Score: 2 of 3"), the way a status
  message should be (WCAG 4.1.3).
- **Quiz with a score** replaces the one-question Multiple choice template:
  three science questions, a score at the top, a Say after each answer,
  and a marker behaviour at the end with an If (three out of three:
  "Perfect score!"; otherwise "Have another go"). Try again sets Score to 0.
- **Focus in lessons:** when the button you are on leaves the screen (you
  answered, and the next question took its place), the keyboard moves to
  the first button now on screen in the reading order, instead of back to
  Play.
- **Checks:** Accessibility flags text showing {a name} that is not a
  variable (it would show just as typed); Export checks that every Change
  and If has a variable, and that every If has something to do.

All of it is data from fixed lists, like every behaviour: a lesson still
never holds code, and an imported lesson can only name variables it has.

## 0.9.0 - 2026-10-14

**Fonts** (Dave: "when does font selection come in?" - it had slipped
since milestone 1). A text box's Look section now has:

- **Font**: ten free families, the same files DSKEDTR carries (all SIL
  Open Font License 1.1): Atkinson Hyperlegible (the default), Andika,
  Lexend, Comfortaa, Comic Neue, Literata, Fraunces, Zilla Slab, Archivo
  Black and Atkinson Hyperlegible Mono, plus **Device font** (the
  computer's own, which adds nothing to a lesson but looks a little
  different on each device). The line under the menu is written in the
  font, with what it is good for.
- **Italic** (Lexend, Comfortaa and Archivo Black have no italics of their
  own, so the browser slants them) and **Line spacing** (1.25 as before;
  1.5 is roomy, for long passages).
- Several text boxes picked (Ctrl+A for all of them): a **Text** section
  changes their font, bold, italic and spacing together, one undo step.
- New text uses the font you picked last (when a lesson opens, the font
  of its first text box).

The fonts are inside the app (about 840 KB, so index.html is now about
1.9 MB): they work offline and nothing is ever fetched. An **exported
lesson carries only the fonts its text uses** - about 20 KB for each
style - as @font-face rules inside its one fingerprinted style block (the
safety rules already allowed fonts written into the file, and nothing
else), with the fonts' licence beside them as plain text. A lesson in the
device font carries none. **Save a picture of this frame** puts the fonts
inside the picture too.

Text is wrapped with its real font: a browser only unpacks a font when
something first uses it, so the runtime asks for it, and once it has
arrived works the lines out again (editor, lessons and template pictures).

Older lessons open in Atkinson Hyperlegible (they used the device font), so
their lines may break a little differently. Pick Device font to go back.

The neon planet template types its question in Atkinson Hyperlegible Mono:
every letter is the same width there, so the typing cursor stops right
after the question on every computer (it measured the device font before).

## 0.8.1 - 2026-10-14

**A quick-action pill** (Dave: edit a flipbook "without going deep into the
Inspector"). Picking something floats a small bar just above it, as in
DSKEDTR, with the action you most likely want next:

- a flipbook: **Edit flipbook**; a clip: **Edit clip**;
- a group: **Work on its parts**; an outline: **Edit points**;
- several things that can be one: **Make a clip**;
- and always **Duplicate** and **Delete**.

It sits above what is picked, clear of the turn handle (below it when there
is no room), stays inside the stage area, and has finger-sized buttons on a
touch screen. It hides while dragging, playing, drawing and editing points.
From the keyboard, Alt+F10 jumps to it, Left and Right move along it, and
Escape goes back to the stage. (A double-click, Enter on the stage, and the
menu still edit a flipbook too.)

## 0.8.0 - 2026-10-14

**Clips** (Dave's pick for 0.8.0, with flipbooks). A clip is a little
animation of its own - a spinning gear, a blinking arrow, a character's
wave - that you can use on the stage as often as you like. Edit the clip,
and every use of it changes.

- **Make a clip (F8**, the menu, or Arrange in the Inspector): the picked
  objects become a clip, and one use of it takes their place. It looks
  exactly the same: the clip starts where their animation started and plays
  once, holding its last frame, as they did.
- **Edit a clip:** Enter on the stage, a double-click, or Edit clip. The
  stage and the timeline become the clip's own (its own size, length and
  layers), with a bar at the top of the stage saying where you are
  (Lesson > Clip 1). Escape, or Lesson in that bar, goes back. Undo works
  inside a clip too.
- **Each use plays its own way** (the Inspector's Clip section): round and
  round, once (then it holds its last frame), or holding one frame; from
  any of its frames ("Starts at clip frame"); and it can **keep moving while
  the lesson waits** at a marker, so an arrow can keep blinking while the
  lesson waits for a click. In a lesson, the Play/Pause button shows Pause
  while anything moves and stops it all (WCAG 2.2.2); with "reduce motion"
  on, such clips hold still.
- **Make it its own clip** gives one use a copy of the clip, so editing it
  changes just that one. Duplicating a use (Ctrl+D) makes another use of
  the same clip.
- A clip holds shapes, outlines, text and pictures (not groups or other
  clips). Its parts are not read one by one: the use is read by its name,
  which Make a clip fills in from the words in it.
- The Lesson Inspector's new **Clips** section lists them: Edit, Use it,
  and Delete (for a clip nobody uses). Copying a use into another lesson
  brings its clip along.

**Flipbooks.** A flipbook is a clip drawn page by page. **New flipbook**
(the Clips section, or the menu with nothing picked) puts one on the stage
and opens it with the Pencil. Whatever you draw goes on the page you are
on, and onion skin shows the page before (blue) and after (green) faintly.
The bar at the top turns pages (or comma and full stop), adds a page, copies
this page (to change it a little) and deletes it; Frames per drawing (2 is
"on twos") sets how long each page shows. Back on the stage it plays round
and round and keeps moving while the lesson waits.

**The Pencil (B)** draws freehand, smoothed when you let go (Paper.js's
simplify, as in VCTREDTR), in the colour, width and smoothing set in its
bar at the top of the stage. Each stroke is a line whose points you can
edit (A).

**A new template, Clips and a flipbook:** a hand-drawn stick figure (a
flipbook of eight drawings) walks across a park while three gears - one
clip, used three times at different sizes - turn in the corner.

Also: on a phone the ten tools sit a little closer, so all of them fit; a
line's onion skin is drawn as a line (it was filled in).

## 0.7.1 - 2026-10-14

**Merge shapes**, as in VCTREDTR (and PowerPoint). Pick two or more filled
shapes - rectangles, ellipses, gallery shapes or Pen outlines - and:

- **Union** joins them into one outline;
- **Combine** joins them, but cuts out where they overlap;
- **Fragment** breaks them into pieces wherever they overlap, each piece in
  the colour it showed (the top shape's at that spot);
- **Intersect** keeps only the part where they all overlap;
- **Subtract** keeps the first shape you picked and cuts the others out.

They are in the Inspector when two or more filled shapes are picked, in the
menu (Shift+F10), and on the keys Alt+Shift+U, C, F, I and S. The shapes are
merged as they look at the play head (turned, stretched, inside a group or
not); the result is one outline that takes the first shape's look, layer,
place in the stacking order and timing, and goes where it was. Curves stay
curves, so the result has sensible points to edit (A). Lines, text, pictures
and groups are left out (and the announcement says how many). Keyframes and
behaviours of the merged shapes are not carried over; Undo brings the shapes
back in one step.

The engine is Paper.js 0.12.18 (MIT licence), the very same file VCTREDTR
carries, inside the page: it works offline and makes no requests. The build
checks it against the official file's fingerprint. Only the editor uses it;
exported lessons never contain it.

**Fixed: drift when editing the points of a turning outline.** After an
edit, an outline's box was fitted tightly round its points, which moved the
box's middle; between two keyframes where the outline turns, that move was
blended in a straight line while the outline turned round it, so the shape
drifted (45 degrees: 3 points; a full spin: as far as the point moved). An
outline that turns between its keyframes now grows its box evenly round the
middle it already had, so nothing drifts at all. (Its box can be a little
bigger than the shape on one side.) Outlines that do not turn keep a tight
box. 0.7.0's changelog put the cause as "turning and resizing"; resizing
alone never drifted.

**Phone: the timeline folds while the Inspector is open.** Opening the
Inspector sheet folds the timeline to its controls (the play buttons, the
frame and Add keyframe), so the stage keeps its room; closing it gives the
timeline back the height you chose. If you make the timeline taller while
the sheet is open, that height is kept.

## 0.7.0 - 2026-10-13

Phase 2 begins (Dave's pick: the pen tool and motion paths first).

**The Pen (P)** draws your own outlines point by point, the way VCTREDTR's
Pen does: click for a corner, drag for a smooth curve (Shift keeps it to
45 degrees), click the first point again to close the shape. Enter,
Escape or a double-click ends an open line, and Backspace takes back the
last point. From the keyboard alone, Enter on the stage adds a straight
line, ready to shape.

**Edit points (A, or double-click an outline)** shows its points:

- drag a point, or a curve handle (a smooth point keeps its handles in
  line; Alt lets them go their own ways);
- Shift+click, or a box dragged on empty stage, picks several points;
- Alt+click or a double-click on a point switches it between a corner
  and a smooth curve; a double-click on the outline adds a point;
- Delete removes the picked points;
- from the keyboard: N and Shift+N pick the next or previous point (it is
  read out: "Point 3 of 8: X 540, Y 220, smooth") and the arrow keys
  move it (Shift: 10 points);
- the Inspector's new **Points** section lists the points; for the
  picked one it has X and Y, Smooth curve, Add a point after it and
  Delete, plus Closed shape and Reverse for the outline.

Every gallery shape is an outline too. **Turn into an outline** (Look, or
the menu) makes a rectangle or an ellipse one.

**Motion paths.** Between two keyframes, anything on the stage can follow
an outline instead of a straight line (Motion, Along a path), and can
**turn with the path** or **go the other way**. Pick an outline and one
other thing, and **Move ... along ...** does it in one step (two seconds
from the play head). The keyframes at either end stay on the path when
you move or reshape it, the editor draws the path dotted while the thing
following it is picked, and the timeline shows that stretch dotted.

**Guides.** Anything can be a guide (Timing): it shows dashed while you
edit and is left out of the lesson (and out of the checker, the reading
order and the PNG export). A path that something follows becomes one.

**Custom curves.** "Custom curve" joins the eases: shape the motion
between two keyframes by dragging two handles on a little graph, typing
their numbers (each handle is a group of Across and Up), or starting from
Overshoot, Wind up, Both, Snappy or Gentle. It works like CSS
cubic-bezier().

**A new template, Along a path:** a paper plane flies a loop the loop,
turning as it goes, with a trail of puffs behind it. Click the plane to
fly it again.

Underneath: the runtime now reads any SVG path data into points and
curves (lines, curves, quadratic curves and arcs, absolute or relative)
and writes it back, so exported lessons follow paths exactly as the
editor does. Not in this build: Merge Shapes (VCTREDTR's union, subtract
and so on), which stays on the phase 2 list.

## 0.6.3 - 2026-10-13

**The click-to-reveal template is redone** in a neon 1980s cyberpunk
style (Dave's idea). The art is all original:

- a starry purple sky (one star in four twinkles slowly), a pink haze on
  the horizon, and wireframe mountains in neon pink and cyan;
- a grid floor that rushes toward you: each line across is worked out in
  perspective and jumps back to the horizon when it reaches the bottom;
- scanlines and dark corners like an old screen (they sit under the
  words and buttons, so they never block a click);
- Jupiter as a glowing neon planet with wavy belts, a drifting Great Red
  Spot, a night side and a rim light; a tiny Earth drawn to the same
  scale.

The lesson plays a short intro: a "planet scanner" panel switches on and
the question types itself in, with a blinking cursor (slowly: three
changes a second at most). It waits at the Question marker. Show the
answer goes to the Answer marker: the answer is on screen at once (so
it is there with reduced motion too), then a scan line sweeps Jupiter,
target brackets lock on, Earth glides to Jupiter's middle, and ten more
Earths pop up beside it, 11 across. The sizes fade in (Jupiter about
139,820 km wide, Earth about 12,742 km), and Ask again goes back to the
question. Markers: Start, Question, Answer, Eleven Earths.

## 0.6.2 - 2026-10-13

**The bouncing ball template is redone** in a rounded, polished toy-world
style, inspired by the backgrounds of late-80s platform games. The art is
all original (no copied pictures or characters):

- outlined pastel hills shaped like tall rounded columns, each with a
  soft shine and a few dimples, in front of a pale far ridge of bumps;
- puffy clouds that drift slowly, a floating platform, two round bushes,
  and a grassy ledge with a scalloped edge over striped sandy soil.

The ball is glossy and bounces like real gravity: it speeds up as it
falls and slows as it rises, and each bounce is lower than the last. It
stretches just before it lands, squashes flat on the ground with two puffs
of dust (bigger for a harder landing), and its shadow shrinks and fades as
it rises. Then it rolls to a stop. The shine stays at the top left (it
comes from the light, so it does not spin with the ball). The ball is a
button: click it, or Enter, to drop it again. Markers: Start, Bouncing,
At rest.

## 0.6.1 - 2026-10-13

**The water cycle is the flagship demo** (Dave: "make it as impressive as
you can"). It is the first template now, and the splash's picture shows
it open. About 17 seconds in five steps; the lesson waits at the end of
each, and Next and Back step through:

- the intro: the title and caption card fade in, the sun rises from
  orange to yellow behind a glowing halo, and two gulls glide across;
- **Evaporation**: the halo pulses, shimmering lines of warm air and
  puffs of vapour rise from the sea and fade;
- **Condensation**: the puffs drift together and swell into a cloud;
- **Precipitation**: the cloud darkens and moves over the mountains,
  rain falls onto the slopes (each drop lands on the ridge below it),
  snowflakes drift onto the peaks, and there is one flash of lightning
  (well inside the flashing limit);
- **Collection**: a river fades in down the mountain and drops of water
  run along it to the sea, while the cloud whitens and drifts back;
- **Around again**: the whole cycle is drawn as a loop of four arrows
  with its four labels, and the caption invites a click. This is the
  still frame.

Waves drift on the sea the whole time. The sun, the sea, the cloud and
the mountains are buttons that each say one more fact. The reading order
is set (the title, the caption, the four buttons, then the labels), every
marker has its description for the text version, and the checker finds
nothing to fix.

**The labelled diagram is now a cartoon plant** in a hand-drawn
web-cartoon style (Dave asked for a Homestar Runner feel): thick wobbly
black outlines, flat loud colours, a lumpy cloud, a smug sun that bobs,
pebbles in the soil, wiggly roots, and a flower with a face that sways,
looks shiftily from side to side and blinks, on a two-second loop.
Point at a part, tap it or Tab to it, and a speech bubble with a
wisecracking label pops up ("STEM: carries water up from the roots. A
plant elevator."). Click the flower and it says "Hey! Easy on the
petals." It is all original: no characters, names or lines from the show.

**How they are made.** Only ANIMEDTR's own material: shapes, text,
pictures, groups (the cartoon's flower, sun and roots each move as one)
and outlines, animated with keyframes, lifespans, markers and
behaviours. Two things are made in code when the template opens: the
hand-drawn outlines (the mountains, the river, the wobbly cartoon shapes)
and three soft pictures (the sky's and the sea's colour fades and the
sun's glow). They open in the editor like anything else (move, resize,
recolour, animate them), but the editor cannot draw a free outline of
its own yet: that is the pen tool, in phase 2.

**Fixed: text on the stage of an exported lesson picked up the text
version panel's styles.** The SVG text and the panel shared a class name
(`ani-text`), so every text box on the stage carried the panel's
`overflow: auto` (and an accessibility checker could mistake it for a
scrolling box). Stage text is now `ani-words`.

**The contrast check** now skips text while it fades in or out (a moment
in passing, not how it is read), and measures hidden text together with
whatever the same behaviour shows with it, such as a speech bubble.

## 0.6.0 - 2026-10-13 (milestone 5: accessibility tools and templates)

**The Accessibility tab**, beside the Inspector (DSKEDTR's pattern), and
a checker button in the top bar with a count of the things to fix. It
checks again by itself a moment after every change and lists, most
serious first, each with a Go to it button that picks the object, moves
the play head to where the problem shows and opens the Inspector there:

- **Needed** (Export waits for these): buttons with no name, pictures
  with no words and not marked as decoration, actions that point at
  nothing, an invalid language, and **flashing**: anything that changes
  brightness by 10% or more back and forth more than three times in one
  second (WCAG 2.3.1), on an object big enough to matter.
- **Fix**: **low contrast**, measured, not guessed: the stage is drawn
  without its text at the moments each text box is on stage (when it
  appears, at its keyframes, at markers), and the colour really behind
  the words is read from that drawing, so text over a shape or a picture
  is checked too (4.5:1, or 3:1 for text 24 px and up, or 18.7 px bold);
  text under 18 px at the stage's size; buttons smaller than 24 by 24
  (WCAG 2.5.8); a key used by two behaviours; things hidden at the start
  that no behaviour shows; things outside the stage the whole time.
- **Tip**: markers without descriptions, no still frame, no text
  version, and a busy lesson (six or more things read) still in the
  automatic reading order.

The tab also says what it cannot check (whether names make sense, what
behaviours do while the lesson runs) and suggests trying the lesson in
Preview with a keyboard and a screen reader.

**Reading order** (nothing picked, Lesson, Reading order): every text
box, named picture and button in the order a screen reader reads them,
with Up and Down buttons. Automatic is the drawing order (the bottom
layer first); moving anything makes the order your own, and "Back to
automatic" undoes that. In the lesson, the stage reads its objects in
that order (`aria-owns`), and Tab and Shift+Tab move through the buttons
in it, whatever order they are drawn in, then on to the player bar as
before. A click still goes to whatever is under the pointer.

**See it as others do.** The Accessibility tab can show the stage as
people with red-blind (protanopia), green-blind (deuteranopia) or
blue-blind (tritanopia) colour vision see it, or with no colour at all.
A badge on the stage says it is on. Only in ANIMEDTR: never in a lesson.

**Templates.** The top bar's Templates button (it replaces the sample
button) and the splash's Templates card open a choice of six, each with
a picture: A moving thing, Labelled diagram (point at, tap or Tab to a
part of a plant to see its label; its reading order puts each label
after its part), Click to reveal, Multiple choice (each answer jumps to
a "Correct" or "Try again" marker with a button back), Process steps (the
water cycle: each step plays, then the lesson waits), and the sample.
Each is a finished, accessible lesson, with nothing for the checker to
flag, ready to change into your own.

**On a phone, the Inspector is a sheet** along the bottom with a grab
handle, like the rest of the family: drag it to share the screen with
the stage, tap it to open or close it, and from the keyboard Up and Down
change its height, Home closes it and Enter opens or closes it. Its
height is remembered. The Accessibility tab lives in the same sheet.

**Lessons: a switch for letter and number keys.** A correction to 0.4.0:
a lesson that listens for single letters or digits (like the sample's
B) needs a way to turn them off, because they can clash with a screen
reader's own keys and with speech input (WCAG 2.1.4, level A). The
lesson's text version now has a "Letter and number keys: on/off" button.
Arrow keys are not affected.

**Checked on a Chromebook-sized screen** (1366 x 768) with the keyboard
alone: the splash fits, New, a rectangle from the keyboard, no
scrolling, and room for the stage and the timeline.

## 0.5.1 - 2026-10-13

**ANIMEDTR is gold** (Dave's pick, after seeing gold and fuchsia side by
side: "a bit more yellow", so it stays clear of 3DEDTR's bronze). The
main colour is `#655800`, the yellowest gold that still carries white
text at 7:1 like every app in the family (7.1:1); in dark mode the app's
text and buttons use a bright gold, `#fde047` (13.2:1 on the dark
panels). The icon, the top bar's mark, the wordmark, Export and the
other main buttons, pressed buttons, focus rings, the timeline's
on-stage bars, the splash and the Features tour all follow it, and the
splash picture was taken again. The PNG icons were redrawn
(`make-icons.py`), and the manifest and the shared SUITE block carry the
new colour. Colours inside lessons (the sample's answer text, new
shapes) are lesson content and did not change.

## 0.5.0 - 2026-10-13 (milestone 4: files, export and the suite shell)

**Project files.** Save (the disk button, or Ctrl+Shift+S) keeps the
whole lesson in one `.animedtr` file to keep editing later: stage,
layers, objects, keyframes, markers, behaviours and pictures. Open (the
folder button, or Ctrl+O), or drop one anywhere on ANIMEDTR, to carry on.
The file is a zip like DSKEDTR's (`mimetype` first, `project.json`, then
`pictures/<id>.jpg|png`), so any zip tool can look inside one. The file
is named after the lesson's title, or the name it was opened with.

**Opening trusts nothing in the file.** Every position and size in the
zip is checked, at most 2,000 entries, nothing unpacks past the size it
claims (a "zip bomb" stops at once), every file is checked against its
CRC, locked entries are refused in plain words, and the names inside are
only looked up, never used as paths. The lesson goes through the same
whitelist the exported lesson uses. Every picture must really decode as
a PNG, JPEG or WebP; one carrying anything else (a phone photo's GPS
location, a text note) is redrawn, which drops it, and ANIMEDTR's own
pictures are kept byte for byte. A file from a newer ANIMEDTR says to
update. Problems show in a small dialog that says what went wrong.

**New, Open and the sample ask before replacing unsaved work:** Save it
first, Go ahead without saving, or Keep working on this one.

**Crash backups** (the family's SuiteBackup). A few seconds after each
change the lesson is copied into this browser's own storage, pictures
as Blobs. Saving or exporting deletes the copy. A copy still there at
the next start means the last session ended some other way, and only
then does ANIMEDTR mention it: "Pick up where you left off" on the
splash, and the backup icon in the top bar (Restore, Discard, Not now).
A restored backup goes through the same checks as a file, and opens as
unsaved work. Backups never leave the computer.

**The family's welcome screen.** New lesson, Open a project and the
sample lesson as cards, a picture of ANIMEDTR in use across the top, the
"See what ANIMEDTR can do" tour, the rest of the family, the credits,
the version with its update check and Install. Escape leaves an empty
lesson. A file opened from the computer skips it.

**The family's help panel.** Features (an animated tour of five
favorite features), Keyboard shortcuts, Getting started, About (with the
"View the source on GitHub" button and the credits), Changelog and More
apps. Left and Right move between the tabs. The Help button, ? and F1
open it on Features; the logo opens it on More apps.

**A picture of this frame.** The Export dialog can also save the stage
at the play head as a PNG the size of the stage, for slides or a
handout. It is drawn by the lesson's own runtime, without the picked
box or focus rings.

**Install ANIMEDTR as an app** (Chrome and Edge show an Install button
in the top bar; Safari's way is on the splash). Installed, it opens with
no internet, and double-clicking an `.animedtr` file opens it here. It
checks for a newer version when the splash opens. New beside index.html:
`manifest.webmanifest`, `sw.js` (network first for the page, as in every
app, with the suite's update check), the PNG icons and `make-icons.py`.

**Numbers with a finger.** On a touch screen a tap on a number opens the
family's slider panel instead of the keyboard (a second tap types). X
and Y slide across the stage, width and height up to the stage's size,
turn from -180 to 180. Opacity keeps typing, since it has its own slider.

**Shared SUITE block.** ANIMEDTR is in `SUITE_APPS` (with `listed:
false`, so the other apps don't list it yet) and `SUITE_MARKS`. Fixed in
the block while pasting it: the About tab's credits showed the author's
web address as plain text ("Made by https://daveghidiu.com/") instead of
his name as a link. The master copy in `_edtr-suite` has the fix; the
other apps get it at their next paste.

## 0.4.1 - 2026-10-13

**ANMEDTR is now ANIMEDTR** (Dave's call). The name changes everywhere:
the app, its exported lessons ("Made with ANIMEDTR"), the project format
(`animedtr-project`, and `.animedtr` files when saving arrives in 0.5.0)
and the folder. Nothing had been saved in the old format yet, so nothing
needs converting. Settings saved under the old name (the timeline's
height, open sections, theme) carry over by themselves.

**Opacity has a slider** beside its number (Dave: trying it on Opacity
first). Slide it and watch the object fade, or type the number: each
follows the other. One slide is one undo step. From the keyboard the
slider takes the arrow keys, Page Up and Page Down, Home and End, and a
screen reader hears its value as "80 %".

## 0.4.0 - 2026-10-13 (milestone 3: behaviours)

**Objects can do things.** Pick an object and open Behaviour in the
Inspector. Two triggers: when someone activates it (a click, a tap, or
Enter or Space) and when someone points at it or focuses it (a tap on a
touch screen). Each holds a list of actions that run in order. An object
with a behaviour becomes a real button in the lesson, so the keyboard and
screen readers reach it with Tab.

**The actions:** go to a marker and play, go to a marker and pause, play,
pause, show, hide or toggle an object, set a property (opacity, fill, x,
y or turn) at once or as a glide of up to 5 seconds, open a web page
(https, http or mailto only, always in a new tab that cannot reach back to
the lesson) and say something (the words appear in a strip under the
lesson until the next message or until it is closed, and are read out).

**Pointing is undone by leaving.** What a point or focus behaviour
changes goes back the moment the pointer leaves, focus moves on or
Escape is pressed, so a label that pops up never gets stuck on screen and
never needs the mouse to get rid of (WCAG 1.4.13). On a touch screen a
tap shows it and a second tap puts it back.

**The lesson has behaviours too** (nothing picked, Lesson, Behaviours):
when it starts (and when Restart is pressed), when the play head reaches
a marker, and when someone presses a key. Keys are letters, digits and
arrows only, never with Ctrl, Alt or Cmd, and never keys people need to
move around. The text version lists every key ("Press B to..."), so
everyone can find them.

**The sample uses it.** Press B in "How does a ball move?" to show the
answer and bounce the ball.

**Checks know about behaviours.** The lesson check flags actions that
point at a deleted marker or object, a web address that is not allowed
and empty words to say, and offers to fix them. Deleting an object, a
layer or a marker also removes the actions that used it (undo brings them
back). Copy and paste keeps a pasted group's behaviours pointing at its
own copies.

**Safe by design.** Every behaviour is checked again by the lesson itself
when it loads, the exported page's security rules still block everything
it does not need, and links are checked to the letter before they open.
Preview now lets a link open its new tab.

**Small things.** The "add a behaviour" choice has its own line in the
Inspector so its words are never cut off. Reduced motion makes glides
happen at once.

## 0.3.0 - 2026-10-13 (milestone 2: the timeline)

**The timeline keeps its height** (Dave: opening and closing groups used
to resize it). Its height is yours: a drag bar on its top edge sets it,
and it is remembered in this browser. Rows scroll inside it, and the ruler
and the markers row stay in sight while they do. On the bar from the
keyboard (it is a separator, like the suite's phone sheet handle): Up and
Down change it by 24 pixels (Shift: 96), Home makes it smallest, End as
tall as it goes (the stage always keeps some room), Enter or Space fold it
to just its controls and back. Double-click the bar for the usual height.
The bar looks and works like the splitter in IMGEDTR's Inspector: a slim
line between the stage and the timeline with a small grip in the middle
that lights up in the app's colour.

**Zoom and scroll the timeline.** The three buttons under the layers list
(or Ctrl + wheel on the frames) zoom it across; Fit shows the whole
lesson. Zoomed in, a scroll bar appears under the lanes (Shift + wheel or
a sideways wheel slides it), the ruler labels every 1, 2, 5, 10... seconds
as there is room, and the view slides by itself to keep the play head in
sight, so the keyboard never loses it.

**Lifespans you can drag.** The picked object's "on stage" bar has grips
at its ends: drag the left one to change when it appears, the right one
for when it leaves (to the last frame: it stays to the end), or the middle
to slide the whole thing in time, keyframes and all (never past the start
or the end). From the keyboard: [ and ] make the picked objects appear or
leave at the play head (Timing in the Inspector has the numbers too).

**Frames.** On the timeline, = inserts a frame after the play head and -
removes the one at it (Shift: a whole second). Everything later slides,
the lesson gets longer or shorter, and keyframes in removed frames go
(unless it is an object's only one). Markers can be dragged along the
markers row (a click still opens one in the Inspector).

**Copy and paste a keyframe.** With the timeline focused, Ctrl+C copies
how the picked object is at the play head and Ctrl+V pastes it as a
keyframe on the picked objects at the play head (an object with none yet
gets one at its start too, so it glides).

**Onion skin** (the three circles on the timeline): faint copies of the
picked objects (or of everything that moves, with nothing picked) 4, 8
and 12 frames before (blue) and after (green), at 24 frames a second.

**The Frames menu** (the ... button, or a right-click on the frames, or
the Menu key there): keyframes, copy and paste, appears and leaves here,
insert and remove, markers, onion skin. Loop is now a toggle button and
Remove keyframe an icon, so the controls fit on one line.

**Fixed:** a drag on the timeline could stop part way if an earlier drag
had picked some of the timeline's text (the browser started its own
drag-and-drop). The timeline's text can no longer be picked. Opening or
closing a row in the tree now redraws at once, so quick key presses never
act on the old rows.

**Checked with Playwright:** 29 new checks (the height never changing by
itself, the bar by keyboard and pointer, remembered height, zoom, follow,
fit, lifespans' ends and middle, sliding a keyed object, [ and ], insert
and remove, a marker drag, keyframe copy and paste, onion skin, the menu)
plus the 0.1 (43) and 0.2 (56) checks, axe on the editor: no violations.

## 0.2.0 - 2026-10-13 (milestone 1: stage and objects, with layers and groups)

**Layers.** The timeline's left column is now a layers tree (an ARIA
tree, suite standard): each layer opens to show its objects, front first,
and a group opens to show its parts. Up/Down move and pick (Shift adds),
Right/Left open and close, F2 renames, H hides a layer while editing, L
locks it, Alt+Up/Down moves forward or back, Delete deletes, Enter goes to
the stage. The eye and lock on each layer row are for the mouse. A closed
layer's lane shows all its keyframes faintly. The + beside "Layers" adds
one above the picked layer; new things go on the picked layer (marked with
a dot). Hidden and locked only matter while editing: a lesson shows every
layer. The sample now has Background, Ball and Words layers.

**Groups (one level).** Ctrl+G groups the picked objects; Ctrl+Shift+G
ungroups. A group has its own keyframes, and its parts keep theirs inside
it, so a car can drive while its wheels turn. Resizing a group scales its
parts. Double-click a group, or press Enter on the stage, to work on its
parts; Escape or a click outside leaves it. Ungrouping keeps each part
where it is at the play head (a group's own motion is dropped, with a
warning; Undo brings it back). In a lesson, a named group is read as one
picture (or one button, if it has a behaviour); an unnamed group lets its
parts speak.

**Drawing and picking**
- Drawing tools: click Rectangle, Ellipse, Text or a shape, then drag on
  the stage (Shift: a square or circle). A click without a drag makes one
  at the usual size. R, O, T arm the tools; from the keyboard, Enter or
  Space on a tool button, or Enter on the stage with a tool armed, adds
  one in the middle of the view.
- The shapes gallery (U): 91 outlines from DSKEDTR's gallery (VCTREDTR's
  shields among them) in eight sections, with arrow keys between them.
  Line shapes (curves, brackets, braces, zigzags) are drawn with a line.
- Pictures (F, a drop, or a paste from another app): PNG, JPEG, WebP or
  GIF (the first frame). Each is decoded by the browser and redrawn, which
  drops hidden data such as GPS, saved as JPEG (or PNG when it has
  see-through parts), at most 2400 pixels a side. The "Read aloud as" field
  is focused at once; Export needs words or "Decoration". Replace picture
  and "Fit the box to the picture" are in Look.
- Several at once: Shift-click (stage or tree), or drag a box on empty
  stage. Picked objects are always side by side (all on the stage, or all
  in one group). K, arrows, Delete, copy and duplicate work on all of them.
- Snapping (the magnet in the top bar): edges and middles snap to the
  stage's (or the group's) and to other objects', with pink guides. Alt
  turns it off for one drag.
- Line up and space out: in the Inspector (Line up), with the stage when
  one object is picked, with each other (or the stage) when several are.
- Copy, cut, paste and duplicate (Ctrl+C, X, V, D); Ctrl+A picks
  everything; Ctrl+] and Ctrl+[ bring forward and send back; "Move to
  layer" in Arrange.
- Zoom and pan: Ctrl+wheel or a pinch zooms round the pointer; the wheel,
  Space+drag or one finger on empty stage slides; Ctrl+= and Ctrl+- zoom,
  Ctrl+0 fits, Ctrl+1 is 100%; the zoom bar sits in the stage's corner.
- Finger-sized handles on touch screens (the suite's numbers: 15 px,
  caught from 22 px away, the turn knob 48 px up; the nearest one wins).
- A context menu: right-click, a long press, Shift+F10 or the Menu key,
  on the stage and in the tree (layers have their own). Everything in it
  is also in the Inspector or a shortcut.

**Fixed on the way:** renaming in the tree could lose the name if the
timeline redrew while you typed.

**Checked with Playwright:** the 0.1 checks (43) and 56 new ones (layers
tree keys, locking, drawing, the gallery, pictures including a fake one,
grouping and ungrouping, inside a group, snapping and Alt, copy and paste,
the menu, zoom, and an exported lesson with a picture, a gallery shape and
a group as its button), plus axe on the editor (light and dark) and the
lesson: no violations, no CSP problems, no requests.

**Not yet:** project files and crash backups (milestone 4), bundled fonts,
SVG import from VCTREDTR, groups inside groups, lines with arrowheads.

## 0.1.0 - 2026-10-13 (phase 0: the first working pass)

The spike from the spec (`ANIMEDTR-SPEC.md` in the Teaching Apps project):
the whole loop from drawing to an exported, accessible lesson, built on
one shared renderer.

**One model, two players.** `index.html` has three script blocks. The
first (`id="aniRuntime"`) reads, checks, draws and plays a lesson. The
editor draws its stage with it, and Export copies it word for word into
every lesson, so a lesson plays exactly as the editor showed it. Preview
(W) is the exported file itself, in a sandboxed frame.

**Editor**
- Rectangles, ellipses and text boxes (R, O, T), added in the middle of
  the stage. Move, resize (corners; Shift keeps the shape) and turn (the
  knob above; Shift for 15 degree steps), also when turned. Arrow keys
  move the picked object (Shift: 10).
- Timeline: markers, then one lane per object (top first), showing when
  it is on stage, its keyframes and its tweens (dashed when it waits).
  The frames are one keyboard slider (the suite's pattern): arrows,
  Shift+arrows, Home/End, Page Up/Down between keyframes (markers when
  nothing is picked), Alt+arrows move a keyframe, Delete removes it,
  Space plays. Drag a keyframe to retime it; click a marker to edit it.
- Keyframes the 3DEDTR way: K keeps the picked object's look here. On a
  keyframe, changes go into it. Between keyframes they are "not kept yet"
  until K or "Keep for the whole lesson". An object with no keyframes just
  moves, and K then makes it glide from where it was (two keyframes).
- What animates: X, Y, width, height, turn, opacity and colour. Easing per
  keyframe: Steady, Speeds up, Slows down, Smooth, Waits then jumps.
- Inspector (sections start closed and remember being opened): Position
  and size, Look, Timing (appears, leaves, hidden at the start), Motion
  (the keyframes as a table: the text version of the timeline), Behaviour,
  Access ("Read aloud as"), Arrange. With nothing picked: the lesson's
  title, language and text version intro; the stage's size, background,
  frames a second (changing it keeps every timing in seconds), length,
  autoplay, loop and still frame; the markers.
- Behaviours: "when someone activates it" (click, tap, Enter or Space,
  always together), in order: go to a marker and play or pause, play,
  pause, show, hide, show or hide an object.
- Markers (M): a name, a frame, "Pause here" and a description.
- Undo and redo, theme toggle, Help (getting started, shortcuts, about),
  F6 between areas, a phone layout (rail along the bottom, the Inspector
  over the stage).

**Exported lessons (one .html file)**
- A player bar that is always there: Play/Pause, Restart, Back and Next
  (marker to marker), and a Text version built from the intro and the
  markers' descriptions (also shown when JavaScript is off).
- Objects with behaviours are buttons with a name; named shapes are
  pictures; text is real text; the rest is decoration. A thick two-tone
  focus ring. If the focused object leaves the stage, focus moves to Play.
- Text a behaviour reveals is read out when it appears.
- Reduce motion: opens paused on the still frame; Back and Next step.
- Its own Content Security Policy: no network at all, and only the
  runtime and the player's styles may run, by their SHA-256 fingerprints.
  The lesson's data sits in a JSON script with every `<` escaped, and is
  checked again by `cleanProject` before it plays.

**Checked with Playwright:** 43 checks on the editor and an exported
lesson (keyframes, pending changes, keyboard timeline, export blocking,
Preview, Tab and Enter on a button, announcements, reduced motion, no
requests, no CSP violations), and axe (WCAG 2.2 AA and best practice) on
the editor in light and dark and on the lesson: no violations.

**Not yet** (later milestones in the spec): project files and crash
backups, the suite block (splash, Features, Changelog, More apps,
installing), pictures and the shapes gallery, layers, snapping, more
triggers (pointed at or focused, keys, frames), the Accessibility tab,
templates, bundled fonts (text uses the system font, so wrapping can
differ slightly between computers).
