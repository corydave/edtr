# 3DEDTR changelog

## 0.22.2 - 2026-10-22 - Two new apps in the family

- Two new apps in the family: TELEDTR, a teleprompter, and WHTBRDR, a whiteboard. Both are in the splash screen's row of apps and in Help > More apps.
- The shared SUITE block was pasted in again from `_edtr-suite`: TELEDTR and WHTBRDR in `SUITE_APPS` (TELEDTR with `ink`, the drawing colour for a light tile), their icons in `SUITE_MARKS`, and a 6 + 6 splash grid (4 + 4 + 4 on a phone).

## 0.22.1 - 2026-10-16 - Ready for EDTR Studio

- Ready for EDTR Studio (edtrapps.com/create/), one window with every app: inside the Studio, links to the other apps open them right there, Ctrl+Shift+1 to 9 switch apps (Ctrl+Shift+0 goes to the rail), and the splash leaves out its "More apps" row. On its own, nothing changes.
- The shared SUITE block gained its "EDTR STUDIO" section (`suiteInStudio()`).

## 0.22.0 - 2026-10-13 - Keyframes that keep a group's parts; layered exploded views

- **Parts too** (timeline, on by default, remembered in this browser as `settings.keyParts`): Add keyframe and Remove keyframe on a group now act on the group and every part inside it, at every level (`keyTargets`). Before, only the group was keyed, so parts moved inside it had no keyframes and sat in their last place for the whole animation - Dave's phone, with its app tiles pulled out at the end, showed them pulled out at the start too. Now a group can turn as a whole while its parts move apart or come together: exploding, or assembling a camera.
- **Back-filling:** a part getting its first keyframe inside a group that already has keyframes at other moments also gets keyframes at those moments, in the place it had before it was moved (`oldestPose`: its oldest pose in the undo history, only from steps where it was in the same group). A toast says how many parts this happened to.
- **Exploded view, Which way:** Out from the middle (as before), or **in layers** along Z (front and back), X (left and right) or Y (upwards). Parts whose middles are at the same depth (within 2% of the size along that direction, at least 0.25 mm) form one layer; layers are counted out from the middle one, which stays put, and the furthest goes the whole How far apart distance. Upwards counts from the bottom layer, which stays on the floor. Granularity is the group tree, as in CAD: a group's own parts move; a group inside it moves as one piece (explode that group too, for its parts).
- **Checked:** on the phone sample, App 1 pulled 40 mm forward and Lens 1 40 mm back at 4 s, then a keyframe on the Phone: at 0 s both are home, at 2 s halfway (with Smooth easing), at 4 s out - while the phone turns. A Z-layered exploded view puts the screen, tiles and front camera in front and the camera bar, lenses and rings behind. The animation, preset and group regressions pass.

## 0.21.0 - 2026-10-12 - A phone sample

- **Phone sample** on the splash (a fourth card, with a phone icon) and in the Tips section: `loadPhoneSample()` builds a made-up smartphone - deliberately no real brand's design - from 37 ordinary shapes in one group called Phone: a rounded extruded body (72 x 150 x 8 mm) with a bevelled edge, the screen glass, a front camera dot, 24 app tiles (a 4 x 5 grid and a dock), a camera bar on the back with two lenses in rings and a flash, two volume buttons and a side button, and a charging port. Every part is a normal shape with its own settings, so it can be picked (click the phone again), changed, moved apart or exported.
- It spins: an 8-second looping turntable laid on the group with `layerKeys` (two keyframes, Steady), and the timeline opens so Play is right there. One undo step takes it all away.

## 0.20.0 - 2026-10-12 - Made for fingers

- Number fields on a phone or tablet open a slider, not the keyboard: tap one and a small panel opens beside it with its name and value, a slider across a sensible range, and - and + buttons (hold to keep going). Tap the lit field again, or the keyboard button, to type an exact number. A slide is one step to undo. With a mouse, nothing changes. (Position runs 150 mm either way, Size from 1 to 300 mm, Turn from -180 to 180, and very wide boxes get an everyday range; the model changes as you slide.)
- The gizmo's arrows, rings and handles are bigger on a phone or tablet, so they are easier to catch with a finger.
- The shared SUITE block was pasted in again (new: the touch standard, `SUITE_TOUCH` and `suiteNumberPop()`).

## 0.19.1 - 2026-10-11 - The source, front and center

- **About starts with a "View the source on GitHub" button** (github.com/corydave/edtr), with a line on why: free and open source (MIT license), runs in your browser, keeps your files on your device, needs no sign-in, works offline.
- The shared SUITE block was pasted in again from `_edtr-suite` (new: `suiteSourceBox()`, drawn by `renderSuiteCredits()`).

## 0.19.0 - 2026-10-10 - A new splash

- **A picture of 3DEDTR in use across the top of the splash** - the same picture as on edtrapps.com, built into the app (as a data: URI), so it shows offline too. With it, the small icon beside the name goes, since the picture already shows it.
- **Every way to begin is a card with a picture:** a folder opening for Open (the icon everybody knows), and pictures of their own for the rest.
- **"Pick up where you left off" is smaller and quieter:** a slim row under the cards rather than the big first button. It still only appears when the last session ended without saving, and the app's main way to begin keeps the focus.
- **Links to edtrapps.com and GitHub** under the credits (on the splash and in About): "All the apps at edtrapps.com - Free and open source on GitHub (MIT license)".
- The splash is a little wider (760px) with the picture; on a phone the cards stack in one column. The shared SUITE block was pasted in again from `_edtr-suite`.

## 0.18.0 - 2026-10-10 - A tour of the features

- **Features, a new first tab in Help:** an animated tour of five of 3DEDTR's favorite features - Cut shapes to build, Build from simple shapes, Ready for 3D printing, Symmetry and Colors and finishes - each with a small looping drawing, a title and a sentence or two. Previous and Next, the dots, or the Left and Right arrow keys move between them; the animation has a pause button, and it starts paused when the device asks for less motion.
- **? or F1 and the Help button now open Help on Features.** Keyboard shortcuts is one tab over.
- **The splash has a "See what 3DEDTR can do" card** that opens the same tour over the splash.
- The shared SUITE block was pasted in again from `_edtr-suite` (new: `renderSuiteFeatures`, `suiteFeaturesOpen`, `suiteFeaturesCard` and their styles). The drawings are inline SVG with SVG's own animation tags, so they work offline and straight off a disk.

## 0.17.0 - 2026-10-08 - Symmetry, scatter, and Bevel, Knife and Linked

- **Symmetry** (the Inspector section is now *Symmetry, shrink, wall and smooth*): **Mirror** across X, Y and/or Z, or **Around** an axis with 2-64 copies (6 by default, round Y). The object keeps one piece - a half, a quarter, a slice - and the rest is made from copies of it through the object's own centre point. Edit the piece's points and every copy follows: one side of a hexagon, and all six change. Points on a cut stay on it as they move (Blender's Clipping), and for Around a point on one cut drags its partner on the other, so the copies always meet and the whole stays closed. Changing the number of copies or the mirrors re-cuts the whole; if the shape wasn't that symmetric (a 6-pointed star cut for 4 copies), it says how many edges are left open. **Off** keeps the whole shape as it looks now. Turning it on makes a shape a mesh (Undo brings the shape back). Saved in projects (`mods.sym`).
- **Pattern, On a surface** (scatter): copies of the picked object land at random spots on another object's surface - bigger faces get more - each standing up from the surface with its bottom resting on it. Options: only where it faces up, a random twist, sizes that vary (%), a lift (mm), keep them apart, and a shuffle number (the same number always gives the same scatter). Grouped as "<name> scatter". Sprinkles on a donut, in one click.
- **Edit mode:**
  - **Bevel (Ctrl+B)** cuts off the picked corners, each becoming a small new face (distance in the Inspector, default 1 mm). Works on the real edges, not the diagonals across square faces.
  - **Knife (K):** click where a cut starts and where it ends; the faces you can see between them are cut along that line (all of them with X-ray), and the new points are picked. **Cut across X / Y / Z** in the Inspector does a straight cut through the picked points' middle - the keyboard way.
  - **Linked (Ctrl+L):** picks every point joined to the picked ones.
- **Checked:** a 6-sided cylinder set to Around 6 keeps its exact volume and stays closed; its top raised and one corner pulled out (all six follow) stay closed; Mirror X + Z with Smooth 2 and a 1 mm wall is closed and survives a project save and reopen; 6 copies changed to 4 on a star warns about 28 open edges; 52 sprinkles scattered on a torus in one undo step; a box bevelled 4 mm at every corner is exactly 7914.67 mm³ and closed; knife and straight cuts leave boxes closed at 8000 mm³; axe finds nothing in the new Inspector parts.

## 0.16.0 - 2026-10-07 - Copy and paste; Extrude, Merge, Fill and loops

- **Copy, cut and paste objects:** Ctrl+C, Ctrl+X, Ctrl+V (Cmd on a Mac) with the 3D view or the Scene list focused. Each paste lands 10 mm further right than the last; after a cut, the first paste goes back to the same spot. A copied part of a group pastes back into that group (or, if the group is gone, into the scene where it was). Keyframes come along. Copying text in a box or the Help panel works as usual. The copies live in this tab only (not the computer's clipboard).
- **Extrude (E)**, as in Blender: faces with every corner picked are pulled out as a block with new side walls; with only edges picked (say the open rim of the icing), each edge grows a new strip. The new points are picked. With the pointer over the 3D view, E starts dragging them at once - click to keep, Escape to take the whole extrusion back (and your earlier picks). From the keyboard, E then the arrow keys.
- **Merge (M)** the picked points into one, at their middle; **Merge close points** (Inspector, with a distance, default 0.1 mm) joins points that almost touch - the picked ones, or all of them. Faces that fold flat are dropped.
- **Fill (Shift+F)**: a hole whose rim points are picked gets a lid (one face for 3 or 4 sides, a fan round a new middle point for more); otherwise three or four picked points get a new face, facing the camera.
- **Loops:** Alt+click an edge to pick the whole ring it lies on (round a torus's tube: 21 points; along it: 64). From the keyboard: pick two points side by side, then L. Loops follow four-sided pieces and stop at triangles and poles.
- **Inspector:** a new Edit mode section, *Extrude, merge and fill*, with all of these as buttons.
- **Checked:** a 20 mm box with its top extruded 5 mm is exactly 10,000 mm³ and closed; extruding in place then Merge close points gives back the same 12 points; Merge on the top makes an exact pyramid; an open-topped box extruded by its rim and Filled is closed again; the donut's half (bottom deleted) Filled is closed; Escape after E restores the points and picks; copy/cut/paste/undo and typing Ctrl+V in the Name box behave.

## 0.15.1 - 2026-10-07 - DSKEDTR joins the family

- **DSKEDTR joins the family.** More apps and the splash's row of apps now include DSKEDTR (dskedtr.app), the new desktop publishing app: newsletters, flyers and booklets, with text that flows between boxes, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js`.
- The splash's row now fits nine apps: the eight others on one line on a computer, and 4 + 4 on a phone (shared styles pasted in again from `_edtr-suite/suite-block.css`).

## 0.15.0 - 2026-10-07 - A handle for the Inspector sheet

The same grab handle as DSKEDTR 0.14.0, so the suite's phone sheets work alike.

- **Phones and tablets (820 px wide or less):** a grab handle (a short grip bar) at the top of the Inspector sheet. Drag it up or down to share the screen between the 3D view and the Inspector. The sheet keeps its own row in the layout (`grid-template-rows: minmax(0, 1fr) auto var(--sheet-h) 56px`), so the 3D view shrinks rather than being covered, and its ResizeObserver resizes the drawing and the camera's proportions as it goes.
- **Sizes:** it starts at a third of the screen (the old sheet took 46% of the area under the top bar). It is at least 120 px when open, and never so tall that the top bar, the tool rail, the status bar and timeline (when they show) and 120 px of the 3D view are lost. The height is remembered in this browser as a share of the screen (`settings.sheet` in `3dedtr-settings`), so it suits the phone turned either way, and it is worked out again when the window changes size.
- **Open and closed:** a tap on the handle opens or closes the sheet; dragging it nearly to the bottom closes it. Closed, only the handle stays (29 px), so it can be pulled up again. The Inspector button, Escape in the sheet and "Skip to the Inspector" work as before and stay in step. The sheet still starts closed and opens by itself after the first shape.
- **Keyboard and screen readers:** the handle is a `role="separator"` with `aria-valuenow` and `aria-valuetext` as a percent of the screen ("Inspector open, 33 percent of the screen" / "Inspector closed"). Up and Down change the height by 8% of the screen (Down below the shortest closes), Home closes, End makes it as tall as it goes, Enter or Space opens or closes; those keys never reach the app's shortcuts. Opening and closing are announced.
- **Desktop:** unchanged (the handle is hidden, so it is not in the Tab order).

## 0.14.0 - 2026-10-04 - Edit mode

The step of Blender's donut tutorial that makes the icing drip: editing an object's points.

- **Edit mode:** Tab in the 3D view (single-key shortcuts on), or **Edit points** in the Inspector. The object's points and edges show over it (a halo keeps them visible on dark and light objects); its selection box is hidden. Tab, **Done** or Escape (with no points picked) goes back. Picking anything else ends it.
- **Picking points:** click (Shift+click adds or takes away), a box (drag with the Select tool, or B then drag; Shift adds, Ctrl takes away), A / Alt+A, Ctrl+I, [ and ] (one point at a time, read out), and in the Inspector All, None, Others, More, Less and every point on one side of the middle (Bottom half, Top half, Left, Right, Back, Front). Points hidden behind the surface can't be clicked or boxed unless **X-ray** is on (Alt+Z), as in Blender.
- **Moving points:** the Move tool's arrows (they sit on the middle of the picked points), **G** to grab them with the pointer (X, Y or Z: one direction; click or Enter keeps it, Escape or a right-click cancels), the arrow keys and Page Up/Down, or the typed middle in the Inspector. Snap applies.
- **Proportional editing** (O, or the Inspector): points near the picked ones follow them, less the further away (Smooth, Round, Straight or Sharp falloff). **Reach** sets how far; while grabbing, the mouse wheel or Page Up/Down changes it and a circle shows it. This is how a drip is pulled down.
- **Deleting:** X or Delete removes the picked points and every face using them; Shift+Delete only the faces whose corners are all picked. The surface is left open (Wall makes it a solid again).
- **Undo-friendly:** each move or delete is one undo step; Undo and Redo keep you in Edit mode on the same object. Editing a shape's points turns it into a mesh (Undo brings the shape back). Shrink, Wall and Smooth stay on and are worked out again (live while dragging when quick).
- **Checked:** the icing recipe - a torus, Bottom half, Delete points (an open half-torus: 128 open edges), one point pulled down 6 steps with Proportional on, then Wall outward 1.5 mm and Smooth 2 - exports closed (0 open edges). Box select picks 2 front corners of a box from the front, 4 with X-ray; G, axis keys, Escape, the gizmo arrows and typed moves all move by the expected millimetres; axe finds nothing in light or dark.

## 0.13.0 - 2026-10-04 - Shrink onto

- **Shrink onto** (Blender's Shrinkwrap), the first setting in the Inspector section now called **Shrink, wall and smooth**: pick another object, and every point moves to the nearest point on its surface (found with three-mesh-bvh), then **Offset** mm out along that surface's direction. **Reach** (0 = every point) moves only points within that distance - the way to make just the inner edge of icing hug the donut.
- It follows: after any change (and Undo/Redo), an object whose own place, its target's place or shape, or its settings changed is wrapped again (`refreshWraps`, with a signature of all of those). It wraps the target as it is now, not frame by frame in an animation.
- **Order:** Shrink, then Wall, then Smooth - a sheet hugs the surface, then gets its thickness. On a closed shape it flattens it onto the surface (tested: a 12 mm sphere onto a 10 mm one, Offset 0.5, is 21 mm across; with a 1 mm Wall on top, exactly the shell volume, closed).
- **Projects** save the target by id (`mods.wrap: { target, offset, reach }`); opening a project gives every object a fresh id, so the target is matched up to its new one (and dropped if it isn't in the file).

## 0.12.0 - 2026-10-04 - Smooth and wall

A new Inspector section, **Smooth and wall**, for every shape and mesh: the next two steps of Blender's donut tutorial.

- **Smooth** (Off, 1, 2, 3), like Blender's Subdivision Surface: Catmull-Clark subdivision. The triangles are welded and put back into the four-sided pieces most shapes are made of (a flat triangle fan, such as a cylinder's lid, becomes one many-sided face), and quads much longer than the typical edge are cut into strips first, so a cylinder smooths into rounded ends instead of a streaky barrel. Each step makes about four times the triangles; past 1.5 million it stops and says so. Smoothed surfaces are shaded smooth.
- **Wall thickness** (mm) and **Grows** (Inward, Both ways, Outward), like Blender's Solidify with Even Thickness: a copy of the surface is moved along its normals (weighted by angle, and pushed further at corners so the wall is even), turned inside out, and joined to it along any open edge. A closed shape becomes a hollow shell (a 20 mm box with a 2 mm wall is exactly 20³ - 16³ = 3,904 mm³); an open one (a plane) becomes a solid sheet. Wall first, then Smooth, as in the tutorial.
- **Non-destructive:** the object keeps its own shape and settings (`userData.mods: { thick, dir, smooth }`; a mesh keeps its own triangles in `userData.base`), and is drawn - and merged, measured and exported - from a copy made with them. Saved in projects as `mods`, checked on opening. A picture on a smoothed or walled object is laid on again from the sides (box mapping).
- **Checked:** every result tested closed (watertight, consistently facing) in STL: hollow and outward boxes, smoothed sphere, torus, cylinder, text, a hollowed smoothed torus, a plane plate, and a smoothed Union mesh; undo, redo and project round trips keep the settings.

## 0.11.0 - 2026-10-04 - X-ray

- **X-ray** (Alt+Z, Blender's key, or the new button beside Wireframe in the top bar): every object is drawn see-through (40% solid), so what is behind or inside shows - the first step of following Blender's donut tutorial here. Objects that fade in an animation fade from that. Holes keep their own grey look.
- **View only:** it isn't saved in projects, PNG pictures and videos are made with everything solid, and the setting is remembered in this browser like Wireframe. Alt+Z works even with single-key shortcuts switched off, and not while typing in a box.
- **Tested** with the donut recipe that works today: a torus, a slightly thicker torus intersected with a box over its top half, then the donut subtracted from that (Keep originals) - an icing cap that hugs the donut, its inside visible in X-ray.

## 0.10.2 - 2026-10-03 - A switch for the built-in lights, and lighting saved with the scene

- **The sun button in the top bar** (after Clean view) switches the built-in lights on and off; Scene settings has the same switch as Built-in lights. Off, only the lights you add light the scene (with none, a message says the scene is dark and points at the bulb button); on again, it returns to the mood you had. It replaces the "Only my lights" mood from 0.10.0/0.10.1.
- **Lighting belongs to the scene.** Its mood and the switch are saved in the project (`lighting: { mood, on }`) and in undo steps, so a scene lit by one spot light opens dark-with-a-spot on any computer, and Undo puts the lighting back too. Changing the mood in Scene settings also makes it the mood new scenes start with; Settings' Lighting sets only that, without touching the open scene. Older projects open in your usual mood with the built-in lights on.

## 0.10.1 - 2026-10-03 - Every built-in light off, and links to the other apps

- **Only my lights** turns every built-in light off (the sky light stayed at 12%), so the lights you add are the only light in the scene. With none of your own switched on, Scene settings says the scene is dark, next to Add a light.
- **Links to the other apps:** their names in Help (the changelog, About and Getting started) open that app in a new tab; 3DEDTR's own name stays plain. Shared SUITE block: new `suiteLinkApps()`, called from `renderSuiteApps()`.

## 0.10.0 - 2026-10-02 - Lights, SVG import and tools for printing

**Lights**
- **Add a light** (the bulb button at the bottom of the tool rail, or Add a light... in Scene settings) adds a **spot light** up and to the front-right, aimed at the middle of the model. In the Inspector it can become a **bulb** (shines every way) or a **sun** (parallel light from far away), with **colour** (a picker, or Candle / Warm white / White / Daylight / Sunset), **brightness** (%), and for a spot its **beam width** and **soft edge**.
- **Aim it** with the Turn tool (E), the Turn boxes, or **Aim at** (the middle of everything, or any object). Its symbol in the view shows its beam (a cone for a spot, an arrow for a sun) and can be clicked; it is hidden in Clean view, pictures and videos.
- **Animate it** like anything else: keyframes move and aim it, and the **Dimmer** (0-100%, keyframed) fades it up or down.
- **Shadows:** up to 4 lights cast them (shadows are costly to draw), following the Shadows switch. A sun's shadow is fitted round the model every frame, so it stays sharp and never cut off.
- **Never part of the model:** a light is picked on its own; it is never merged, grouped, dropped to the floor, measured as a solid, or put in STL or OBJ. **GLB carries it** as a glTF light (KHR_lights_punctual), its moves included (the Khronos validator: 0 errors).
- **Lighting moods** for the built-in lights: **Product** (clean and even), **Dramatic** (dark, one strong side light), **Sunset** (warm and low, long shadows) and **Only my lights**, as well as Studio, Soft and Bright.
- Projects with lights are format 4 (an older 3DEDTR says it needs an update); projects without lights stay format 3.

**SVG import**
- **Open or drop an SVG** (from VCTREDTR, Inkscape, Illustrator, icon sets): a dialog shows a preview and what was found ("2 shapes with 1 hole"), with Width and Height (proportions kept) and Depth. It becomes an extruded shape with the Outline "Imported drawing": **holes stay holes**, and Bevel and the rest work as on any extruded shape. "Its own proportions" un-stretches it.
- **Read safely.** Scripts, pictures, embedded web pages, links to other files and XML entities are never used: the file is parsed as data, everything but shapes is removed first, `<use>` copies are expanded with a limit (a file that copies itself forever is refused), and only numbers are kept. The previews are drawn from those numbers, not from the file.
- White parts (a white background, or white drawn on top) can be left out; lines with no fill are left out unless that is all there is (then their insides are filled); text has to be turned into outlines first, and the dialog says so.

**For 3D printing**
- **Lay flat (L)**, a new button under the Scene list: turns an object onto its biggest flat outside face, on the floor, ready to slice.
- **Hole through a face (D)**: press it, then click a face - a round hole (3.2 mm, room for an M3 screw) goes in square to that face and right through, a millimetre out each side. Enter makes one straight down through the middle of the picked object. No turning a cylinder 90° for a keyring hole. The next hole is the size of a picked hole.
- **Rounded corners on drawn outlines:** the points list has a **Round** box: a sharp corner between two straight edges becomes a true circular arc of that radius (tested: a 20 mm square with 5 mm corners has exactly the area of a rounded square), instead of a smooth point that thins the wall.

**Keep in frame**
- **Exploded view, Camera orbit and Camera push-in** have a **Keep in frame** box (on for the first two). The camera steps back as the parts spread (keyframes added only when needed), an orbit stands back far enough to keep everything in view all the way round, and a push-in stops before anything leaves the picture. The fit is worked out from each corner of what is shown, for the view's shape.

**Keyboard and screen readers**
- **Measure between spots** (M, then Enter in the 3D view; or the button in Measure 1 to 2): pick an object and a spot on it (its middle, the middle of a side, or a corner) for each end; the distance is read out as you change them, and Show it in the view draws the same line as clicking.
- **The Scene list is a tree** for screen readers: each row says its level, its place among its neighbours, whether it is picked and whether a group is open.
- **Shorter Tab runs:** Alt+Page Down and Alt+Page Up jump between Inspector sections from anywhere in the Inspector; on a section heading, Up, Down, Home and End move between headings.
- The move and turn handles stand aside while Put on a face or Hole through a face waits for a click.

**GLB round trip**
- A glTF mesh node with parts under it comes back out of GLB export the same way (it used to become a group holding the mesh).
- A picture's offset (KHR_texture_transform) is kept, through projects too.
- Custom colours get a name in exported materials: "Blue satin", not "#2f6fd0 satin" (two blues: "Blue satin" and "Blue satin 2").

## 0.9.0 - 2026-10-01 - Animated GLB

**GLB carries the animation** (Export, then GLB, with **Animation** ticked - shown when something moves)
- **One clip, named after the project,** the length of the timeline's clip, with a track for each moving object: position, turn and scale (tracks that never change are left out).
- **Sampled at every frame** (plus just before and at each keyframe, so a "hold" jumps cleanly) and written as linear tracks. glTF's own in-between can't copy our easings or our angle-by-angle turns, so sampling is what makes it play exactly as it does here. Turns are written as quaternions kept on the same side from sample to sample, so a spin keeps spinning (tested: two whole turns over 4 s play back as 90° / 270° / 450°).
- **The camera** (tick Camera; on by default when the camera has keyframes): a camera node with the view's lens, and its moves when it has keyframes. glTF cameras look down their own -Z, as ours do.
- **Groups animate their parts** as here: each object's tracks are in its own group's space, in metres when the file is in metres.
- **Fades don't carry over:** glTF can't animate how solid something is, so a part that fades is written at its most solid. The summary says so.
- **The still pose** (the Pose list, now called "Still pose" for an animated GLB) is what other apps show when the clip isn't playing.
- **Checked** with the Khronos glTF Validator (0 errors, 0 warnings) and by playing the file back with three.js's own GLTFLoader and AnimationMixer: positions, turns and scales match the app at the same moments.

**Also**
- **GLB nodes are written as position, turn and scale (TRS), not a matrix.** Animation requires it, and the game-dev tester asked for it (engines read TRS directly).
- **Merging parts that have keyframes asks first** ("Merge animated parts? ... The merged solid is new, so it won't have any"). This was the second half of the timeline's release 2.

## 0.8.2 - 2026-10-01 - Fixes from the alpha round

Bug bounties to the educator (the video that stopped when the timeline note changed height), the designer (the tumbling turntable after Ungroup), the accessibility tester (the busy cover that wasn't modal) and the game dev (invisible props exported at frame 0).

**High**
- **Video export with the timeline showing.** The note under the timeline changed height during the export; the 3D view resized itself mid-video and the encoder refused the next frame ("sample size must remain constant"). The view's size is now locked while an export draws (video and PNG), and put back afterwards.
- **While a video is made, the rest of the page is inert** (no clicks, no Tab, hidden from screen readers): only Cancel can be pressed. The frame count is shown but spoken only at 25, 50 and 75 percent. Afterwards (or after Cancel) keyboard focus goes back to the 3D view - after any export, so Delete and the arrow keys work straight away.
- **Ungroup keeps spins.** Moving keyframes into another group's space used to write each turn the short way round, losing whole turns and flipping X/Z (a turntable part tumbled end over end). Turns are now written to follow on from the one before by the same steps (`eulerNear`, `rebaseKeys`). **A group's own keyframes are handed down** to its parts on Ungroup, so they move on screen exactly as before (with a keyframe every 10° where the group turns a lot, so an off-centre part still goes round in a circle).
- **Exports with animation:** STL, OBJ, GLB and PNG now have a **Pose** choice - where things are now (at the play head), at the start, or at the end of the clip - and the summary warns about parts that are faded out or shrunk to almost nothing at that moment, and says the GLB holds that pose only (animated GLB is still to come).

**Animation**
- **Undo brings back a change that wasn't kept** (moving the play head used to drop it for good): undo now returns to the moment the step was made, play head and all. The "not kept yet" warning has a **Keep it** button.
- **Stacked ready-made animations keep their own easing.** A keyframe can give one part of the motion (position, turn, scale, solid) its own easing; a preset sets it for the parts it changes and leaves the rest alone. A turntable on an exploded view now spins steadily (it used to freeze, then jump 72°), and the explode keeps its smooth start. Choosing the motion on the timeline sets it for the whole keyframe again.
- **Exploded view:** measured in the group (turning the group no longer changes the distances), a part straight below the middle stays on the floor (it used to sink through it, out of the picture), and holes go with the solid they overlap most instead of flying off as parts. With a group picked, the note says its parts move instead of "no keyframes".
- **The camera's "not kept yet" note** was wrong after turning the view by hand: the controls' glide ("damping") kept moving the view after the play head put it back. That glide is finished before the camera is placed.
- **A project whose clip starts with everything hidden** (a reveal) opens at the end of the clip, with a message, instead of on an empty scene.
- The shadow floor no longer hides what is under it (a "Rise up" reveal looked sliced off at the floor line).

**Shapes and text**
- **Bevels that would leak are held smaller.** A bevel bigger than a thin part (a narrow star point, a small rounded corner, a letter's thin stroke) folded over itself and left gaps. Each shape (and each letter) is checked after it is made and its bevel reduced until it is closed; the Inspector says "Bevel held at ... mm". Bevelled text (ą, ę) is now watertight, and letters with a smaller bevel line up front and back with the rest.
- **Smooth curved walls:** extrusions and text get smooth shading where faces meet at less than 35°, sharp edges elsewhere (and in GLB). Flat shading still shows every face.
- **Rounded rectangle corners are true quarter circles** (they were curves 0.24 mm outside a true radius).
- **Text: Smoothness** (0 = automatic; fewer pieces per curve for game props) and **Line spacing** (%). Typeface names are shorter, so they fit the list. A new Text opens its Shape section, where the words are typed.
- **A polygon or star says what Height makes it regular** (it is stretched to fill Width x Height).
- **Extruded shapes are named after their outline** ("Star 1", "Heart 2"), and the name follows the outline while it is still a made-up one.
- **A merge that ends in several loose pieces says so** (the middles of letters cut right through fall out: a Stencil typeface keeps them joined).
- Holes no longer count in a group's Size, or as sides to snap and line up to.

**Drawing pane**
- **Refuses outlines that can't be made:** a point touching another edge (a pinch) or a slit with no width, as well as crossings. A bow-tie is now called a crossing (not "points in a line").
- **Fit** (button, or F) shows the whole outline; typing a point out of sight fits the view. Coordinates you typed come back as typed (the drawing's position is kept), shown to 3 decimal places.
- A press within 12 pixels of a point picks it (a slightly-off double-click still makes it smooth). Ctrl+Enter uses the outline. Picking "Draw your own" with the keyboard no longer opens the pane on the way past (the Draw the outline... button does).
- Tabbing through the points table says which point is picked; a problem is said once (not again with every nudge).

**Accessibility and layout**
- F6 includes the timeline. The track's value text says "camera keyframe" when nothing is picked. K with the timeline hidden says "Timeline shown". A ready-made animation's message is spoken after its dialog closes. The preset choices have a name and a description, not one run-together label.
- Escape in the Text box no longer leaves the box and the 3D letters different.
- The timeline is never more than 45% of the window, so at 200% zoom the 3D view keeps its room.
- **Phones:** the timeline shows the play row and its note, with More for the rest; a › button slides the top bar to the buttons that don't fit (and ‹ back); narrow phones show the logo without the word, so four buttons fit.
- Small: the export file name starts as the project's name; .zip frames carry a real date; the OBJ hint mentions colours; a renamed group's hints follow the new name.

**Known, not fixed yet**
- Raised text with a bevel, sunk into a plate less deep than its bevel, can union with a few tiny slivers on the plate face (9-25 edges under 0.06 mm). Sink it deeper than the bevel, or use no bevel.
- From the alpha list, still to do: animated GLB, a true fillet (corner radius) for drawn points, lay-flat and through-hole helpers, "keep in frame" for camera moves, the Measure tool's keyboard route, the Scene list as a tree, the GLB round-trip leftovers.

## 0.8.1 - 2026-10-01 - Five more typefaces

- **New Typeface choices for Text:**
  - **Easy to read:** Atkinson Hyperlegible Next Bold (the Braille Institute's typeface for low-vision readers);
  - **Rounded:** Nunito ExtraBold;
  - **Tall and bold:** Anton;
  - **Script:** Pacifico;
  - **Stencil:** Big Shoulders Stencil Display ExtraBold. Its bridges keep the middles of O, A, B, D, P, R... joined on, so text cut right through a plate holds together (tested: a stencil O is two solids, an Inter O one ring).
- **All are SIL Open Font License 1.1 with no Reserved Font Names**, checked in both the package licences and the fonts' own name tables. They load only when a Text uses them, and the service worker keeps them for offline use. Every one extrudes watertight.
- **Fredoka and the original Atkinson Hyperlegible were swapped** for Nunito and Atkinson Hyperlegible Next: Fredoka has no Central European letters at all (ł, ő, č...), and Next is the Braille Institute's newer version.
- **Borrowed letters:** a letter a typeface doesn't have is drawn from Inter, at the same capital height, instead of "?". Atkinson Hyperlegible Next lacks Esperanto and Latvian letters (ĉ, ĝ, ŗ, ō...); most typefaces lack ĳ and ſ. Inter is fetched when it's first needed for this.
- `make-fonts.py` makes all eight, or just the ones named: `python3 make-fonts.py <folder> script stencil`.

## 0.8.0 - 2026-10-01 - Video export

**Video** (Export, then Video)
- **MP4, WebM or PNG frames.** MP4 uses H.264 where the browser can make it (Chrome, Edge, Safari); otherwise it uses VP9 and says that PowerPoint or QuickTime may not play it. WebM uses VP9 (or VP8). PNG frames come as a .zip of numbered pictures (`name-0001.png`...), stored rather than squeezed, for Premiere, Resolve, iMovie and the like.
- **Sizes:** the shape of the view (1080 high), 720p, 1080p (the default), square 1080, upright 1080 × 1920, or 4K.
- **Backgrounds:** as in the view, white, black, or see-through. See-through works for WebM (VP9 with alpha) and PNG frames; it isn't offered for MP4, which can't hold it.
- **Frame by frame:** each frame is drawn at the video's size and handed to the browser's video encoder (WebCodecs) before the next, so none are dropped, however slow the device. The busy cover counts the frames ("frame 45 of 150, about 6 s to go") and has a Cancel button, which gets keyboard focus. In a hidden tab it carries on with a timer.
- **It follows the camera's keyframes** when there are any, otherwise the view as you see it. Everything is put back afterwards: the view's size, the play head, the camera, the grid and handles.
- **The file is made on this device and downloaded;** nothing is uploaded. The summary in the dialog says the length, frames a second, frame count and size, and warns when nothing moves yet.
- **The video library** is Mediabunny 1.61.0 (Mozilla Public License 2.0), cut down to the parts used (220 KB instead of 690 KB) by `make-mediabunny.sh`, self-hosted in `engine/addons/mediabunny/`, loaded only when a video is first exported, and kept by the service worker for offline use. Its licence is in `engine/LICENSES.txt`.
- **Security policy:** `worker-src` now allows `blob:`, for the small helper Mediabunny makes from its own code to split out the see-through part of a transparent video. `connect-src` is unchanged, so nothing can be loaded from or sent to anywhere else.

**Fixes**
- **Ready-made animations at an odd moment:** a play head between round numbers (frame 41 of 30 a second is 1.3666... s) showed that long number and the browser refused it ("Please enter a valid value"). Times are now shown to 2 places. Every dialog's form has `novalidate`, because the app checks (and keeps inside their limits) its own numbers, so the browser never blocks a button. A preset ending a hair past the end of the clip counts as ending at the end, instead of making the clip longer.
- **On phones, dialog labels sit above their choices**, so Export's "Video" and "Everything shown" are no longer cut off.

## 0.7.0 - 2026-10-01 - Ready-made animations and an animated camera

**Ready-made animations** (Ready-made... on the timeline)
- **Six presets,** each with its own settings, plus when it starts, how long it takes and the motion (easing):
  - **Turntable:** the picked objects spin round on the spot - or, with several picked, together round their middle. Turns and direction.
  - **Reveal:** the picked objects fade, grow, rise up, drop in, or spin and grow - into view or out of it - one after another (in pick order) or all at once.
  - **Exploded view:** a group's parts (or the picked objects) move apart from their middle, by a share of the whole size; they can stay apart or come back after a pause.
  - **Cross-fade:** the first picked object fades out while the second fades in.
  - **Camera push-in:** the camera moves part of the way towards what it looks at.
  - **Camera orbit:** the camera circles what it looks at.
- **They only write keyframes** - ordinary ones, the same as Add keyframe - so the result can be changed on the timeline, and Undo takes it all away in one step.
- **They stack on top of motion that is already there:** a spin adds to the turns an object already makes, an explode adds to its positions, a push-in and an orbit together give a spiral in. (Each preset changes every one of the object's keyframes by however far along it is at that moment.)
- A preset that runs past the end makes the clip longer, and says so. Errors (Cross-fade without exactly two shapes, say) are shown in the dialog, which stays open.

**The camera can be animated**
- **With nothing picked, Add keyframe remembers the view** (where the camera stands and what it looks at); the button says "Add camera keyframe". Remove keyframe, Motion after it, dragging and Alt+arrows work on the camera's keyframe the same way.
- **The camera's keyframes are round dots** in their own lane, under the objects' diamonds.
- **Between keyframes the camera swings round the point it looks at** - its angle, distance and height are mixed separately - so it never cuts through the scene, and an orbit needs only two keyframes (a keyframe can carry whole extra turns).
- **Follow the camera** (on the timeline once the camera has keyframes): on, the view follows them, and turning it yourself is "not kept yet" like a moved object; off, look round freely while the keyframes stay.
- A project with camera keyframes opens on its first frame, without reframing the view.

## 0.6.0 - 2026-10-01 - Animation: the timeline and keyframes

**The timeline** (the film button in the top bar, or T)
- **A strip under the 3D view** with Play/Pause (Shift+Space), Back to the start, the time, and a track with one-second marks. The 3D view gets shorter to make room; Hide (X or T) puts it back.
- **Keyframes:** pick one or more objects and press **Add keyframe** (K). Each remembers its position, turn, scale and (for shapes and meshes) how solid it is, at the play head. Move the play head, change the object, add another, and Play glides it between them. Before the first keyframe an object waits at the first; after the last, at the last.
- **Kept on purpose, the Blender way.** Moving an object between keyframes only changes how it looks now. The note under the track says "Changed at 2.00 s but not kept yet" until you add a keyframe; moving the play head puts it back, with a message saying so. **Auto-key** (off by default) adds the keyframe by itself when you move, turn, resize or fade a picked object.
- **The diamonds** on the track are the picked objects' keyframes (other objects' show faintly). Click one to go to it; drag it to change its time. **Remove keyframe** (Shift+K, or Delete on the track) takes away the one under the play head.
- **Motion after it:** each keyframe sets how the motion goes to the next one - Smooth (ease in and out, the default), Steady, Speeds up (ease in), Slows down (ease out), or Waits, then jumps (hold).
- **Length** (0.5 to 600 s), **frames a second** (12, 24, 25, 30 or 60) and **Loop** are part of the project and of undo. Keyframes snap to whole frames; Pause stops on one. Shortening the clip past some keyframes says so.
- **From the keyboard:** the track is a slider for the play head. Arrows move a frame (Shift a second), Home/End go to the start and end, Page Up/Down jump between keyframes, Alt+arrows move the keyframe under the play head, Delete removes it, Space or Enter plays. In the 3D view, , and . step a frame. Every move says the time, and "keyframe" when there is one.

**How objects move**
- **Turns are worked out number by number**, not the shortest way round, so 0° to 360° is a whole spin. The Turn boxes now go up to 3600° (ten turns either way).
- **Solid goes down to 0%**, so an object can fade in from nothing. A nearly invisible object casts no shadow.
- **Groups animate their parts.** A part's own keyframes are measured in its group, like its Position boxes.
- **Duplicate, Pattern, Group and Ungroup keep each object's motion with it** (a copy moves the same way from its own place). Ungrouping a group that had keyframes of its own says that motion has gone. A merge or Join says the parts' keyframes don't carry over.
- **The Inspector** has an Animation section for an object with keyframes: when they are, Add keyframe, and Remove all keyframes.

**Under the hood**
- Keyframe lists are never changed in place, so undo steps share them safely. Moving the play head is not an undo step; undo puts things back as they are at the play head now.
- Projects are format 3 (`animation` and `keys`); 1 and 2 still open. Every keyframe is checked on opening (see README). A project with animation opens with the timeline showing.
- Messages float above the timeline instead of over its buttons. axe-core: 0 violations with the timeline open, light and dark.
- Still to come (release 2): animated GLB export, and a warning before joining animated parts.

## 0.5.2 - 2026-10-01 - Curves with the mouse

- **Fixed: double-clicking a point in the outline pane did nothing.** The drawing is redrawn on every press, and the pane holds on to the pointer while you drag, so the browser's own double-click landed on the drawing rather than the point. The pane now spots a second press on the same point within about half a second itself. That works for a double-tap on a touch screen too.
- **A wobble of a few pixels while clicking no longer counts as a drag**, so it can't spoil a double-click or add an empty undo step.
- **A Smooth button** in the pane's toolbar switches the picked point between smooth and sharp. It shows as pressed when the point is smooth, so curves are easy to find without knowing about double-click or the S key.

## 0.5.1 - 2026-10-01 - Draw your own outline

**The outline pane** (an extruded shape's Outline: "Draw your own")
- **Picking "Draw your own" opens a drawing pane**, and "Draw the outline..." in the Inspector opens it again later. It starts from a little house shape; Square, Triangle and Circle start again from those.
- **With a mouse or finger:** click to add a point. Click on (or near) a line and the point goes there; anywhere else, it joins the edge it stretches least, so the outline grows towards it rather than across itself. Drag a point to move it. Double-click it to make it smooth (the outline curves through it) or a sharp corner.
- **With the keyboard:** [ and ] (or Page Up/Down, Home, End) pick a point; the arrows move it one grid square, Shift five; Insert (or A) adds a point halfway along the next edge; Delete removes it; S makes it smooth or sharp; + and - zoom. Every move is announced ("Point 3 of 6: 10 mm across, 5 mm up, smooth").
- **The list of points** beside the drawing has labelled Across/Up boxes (in mm), a Smooth box and a Remove button for each point, for exact sizes.
- **Snap to grid** (on by default) rounds points to the grid squares. The grid's size follows the zoom (1, 2, 5, 10 mm...).
- **The shape in the 3D view follows as you draw.** "Use this outline" keeps it as one undo step. Cancel, Close or Escape put the shape back as it was. While the pane is open, Ctrl+Z and Ctrl+Y undo and redo inside it.
- **It won't keep an outline that crosses over itself** (a figure 8 has no clear inside, so it can't be made solid). The outline turns red and dashed, and a message says what to fix; "Use this outline" waits until it's fixed.
- **Width and Height** become the size the outline was drawn at; they still stretch it afterwards. Smoothness sets how finely the curves are cut into flat strips.
- **Smooth points use Catmull-Rom curves** (as Bezier curves), so the outline passes through every point you place.
- Drawn outlines come out watertight, with or without a bevel (tested: a house shape with a curve, and a circle).
- **Projects keep the points.** They are checked on opening: 3 to 100 points, every number inside its limits, and no crossing.

**Help**
- The Shortcuts tab has a "Drawing an outline" group, and Getting started mentions it.

## 0.5.0 - 2026-09-30 - Extruded text and shapes; the Scene grip; closed sections

**Extruded text** (the T button on the tool rail, or Shift+0)
- **Type one or more lines** in the Inspector (Enter starts a new line). Lines can be set left, centre or right.
- **Typefaces:** Inter (sans), Noto Serif (serif) and Zilla Slab (slab), all bold.
  - They ship in `engine/fonts/` and load the first time a Text needs one, so the app starts as fast as before and works offline. The service worker keeps them too.
  - All three are SIL Open Font License 1.1, with no Reserved Font Names. The conversion script is `make-fonts.py`, and the licences are in `engine/LICENSES.txt`.
- **Accented letters are included:** Latin-1 and Latin Extended-A (é, ñ, ü, ł, ő, ș, ž...), plus curly quotes, dashes, the ellipsis, € and ™. Any other character shows as "?", with no error.
- **Letter height is the height of a capital H**, in mm, so a 20 mm sign has 20 mm capitals. Depth includes the bevel. Letter spacing is a percentage of the letter height.
- **Bevel** rounds off the front and back edges, cutting in from the outline so the letters keep their size. It is held to 6% of the letter height so thin strokes survive.
- **Each letter goes through the merge clean-up**, which welds corners a hair apart. Unbevelled text in all three typefaces comes out watertight. A bevel on a few letters with ogoneks (ą, ę) can still overlap itself in places; slicers repair that, and the hint says so.
- **Text stays editable:** retyping, or changing the typeface or size, rebuilds it. It is saved in projects as words, not triangles.
- **It is a solid like any other.** It can be grouped, patterned, coloured and given a picture. Make it a hole and join it with a plate to engrave it (tested: watertight).

**Extruded shapes** (the star button on the tool rail)
- **Outlines:** star, heart, arrow, polygon, rounded rectangle, ring and cross, each pushed out into a solid.
- **Settings:** Width, Height and Depth (the outline fills the Width x Height exactly), plus an optional bevel.
- Only the settings an outline uses are shown: Points for stars and polygons, Inner size for stars, rings and crosses, Corner radius for rounded rectangles.
- Every outline comes out watertight, and they are named "Shape 1", "Shape 2"...

**The Inspector**
- **The Scene pane has a resize grip**, the same as IMGEDTR's. It sits between the Scene list and the action buttons.
  - Drag it, or focus it and use Up/Down (Shift for bigger steps) or Home/End.
  - Double-click or Enter goes back to automatic. The height is remembered in this browser.
  - Screen readers hear it as a separator with its height. On phones and tablets, where the Inspector sheet scrolls as a whole, it is hidden.
- **Every section starts closed.** A section you open stays open while you pick other objects ("Shape" stays open from a box to a sphere), until you close it or reload the app.

**Small things**
- The Turn tool's tooltip says "Turn (rotate)", and Getting started says "turn (rotate)", so it is found by either word.
- On a 1280 x 720 screen the tool rail fits all 17 buttons without scrolling.
- Getting started covers text and extruded shapes.

## 0.4.3 - 2026-09-30 - Space to slide, and guide lines

- **Hold Space and drag to slide the view**, the same as IMGEDTR and VCTREDTR (and Photoshop and Figma).
  - It works in the 3D view only. Space still presses buttons and Scene-list rows, and does nothing while you type.
  - While Space is held, the move, turn and resize handles stand aside, so a drag that starts on a handle slides the view too. A Space-click picks nothing.
  - Right-drag, Ctrl/Cmd/Shift-drag and two-finger drags still slide the view, as before. (Ctrl-drag was three.js's default, not a 3D-modelling standard: 3D apps disagree on this.)
- **Guide lines while snapping.** Dragging an object with Snap on has made its sides and middle stick to other objects' sides and middles since 0.4.0; now you can see it happen.
  - A dashed line shows the shared side or middle, running through both objects.
  - The line is coloured by axis, like the handles, the grid and SketchUp's guides: red where X lines up, green for heights (Y), blue for Z. A single suite red would look like the X axis here.
  - The lines go when you let go, and Clean view hides them.

## 0.4.2 - 2026-09-30 - Fixes from the fifth test round

- **Fixed: a bored part joined onto a flat face left that face missing inside the bore.** This happened with a standoff (a post with a screw hole) on a plate, or a block with a through-hole standing on a plate. The mesh had 96 open edges, and the volume came out 6.5 to 16.7 mm³ low. It also happened with a plain Subtract followed by Union, and in 0.4.0. The merge clean-up (`repairMesh`) now:
  - **Welds corners that are a hair apart** (closer than a hundred-thousandth of the model's size) before anything else, so a sliver between two near-identical corners no longer leaves a gap when it is removed.
  - **Patches flat gaps of any size.** A ring of open edges that lies flat, like the missing floor of a bore, is filled whatever its size; other gaps are filled only when small (up to 64 edges).
  - **Leaves zero-area rings to the T-junction fix** instead of patching them with flat triangles, which the tidy-up then removed again.
  - **Repeats the T-junction fix and the tidy-up** until nothing changes, and closes T-junctions once more at the very end.
  - The designer's test parts all come out closed at their hand-calculated volumes: the standoff on a plate, the block with a through-hole, the block sunk into a plate, and the full enclosure (26,749.86 mm³, which also lost its 3-edge crack on the rim).
- **A rounded cylinder resized along one side only stays round.** Its Radius follows the side you changed, and a message says so. Before, it became an oval and the bevel stretched with it.
- **P then Enter looks straight down from 9 points under the part** (the middle, the corners and the middles of the sides) and lands on the highest thing found. A part hanging over an edge, or sitting over an existing hole, now lands on the plate instead of the floor.
- **Phones and tablets:** Put on a face closes the Inspector sheet itself, so the whole view is free to tap, and closing the sheet no longer cancels it. The banner sits at the bottom of the view, clear of the view buttons. On desktop it sits at the top left, clear of them too.
- **The Put on a face button is shown pressed** while it is waiting for a click.
- **Clearer messages:**
  - When only some parts of a Join had a picture, the message says so and explains why there is none on the result.
  - "Round edges can be at most half the smallest side, so it is held just under 10 mm."
  - A pattern of a pattern is called a grid ("Peg grid", not "Peg pattern pattern").

## 0.4.1 - 2026-09-30 - Fixes from the fourth test round

**Holes and Join**
- **Fixed: holes went into GLB files as solid parts.** The Export summary said they were left out, but GLB export didn't check. They are left out now.
- **Join into one solid joins each inner group first**, with its own holes. So a hole only cuts the parts of its own group, as in Tinkercad. The designer's standoffs no longer disappear.
- A group made only of holes counts as holes one level up.
- **Cleaner cuts:** all the cutters (and holes) are joined into one first, then cut out in one go. Cutting them one at a time re-sliced the same faces again and again, and a hole taller than its plate left gaps.
  - A 25-hole pegboard with holes taller than the plate went from 98 open edges to 0, and from 12,642 to 9,712 triangles.
- A part that is too small to measure against a big one is now refused with the right message ("the overlap is too small to measure"), not "do not overlap".

**Rounded edges**
- **Rounding steps 1 on a box is a true chamfer:** 6 faces, 12 flat bevels and 8 corner triangles. A 20 mm cube with a 3 mm chamfer is exactly 7,064 mm³. The rounded-box shape with one step still had a corner at 45° on every edge.
- **Resizing a rounded box or cylinder keeps the rounding the same size.** The Size boxes and the Resize tool change its Width, Height and Depth (or Radius) instead of its scale, which squashed a 3 mm rounding to 12 mm along the stretched side.
- Too big a rounding now says what it is held at ("at most half the smallest side").

**Placing**
- **Put on a face:**
  - A face that lines up with the grid gives its exact height. A ray-worked click point could be 64.99994 instead of 65, which then stopped a Join from closing.
  - Holes are ignored: you can't stand on one, and one poking out underneath doesn't lift the part.
  - The message names the part you clicked, not its group.
- **The keyboard way into Put on a face:** Enter drops the selection onto whatever is straight below it, or onto the floor.
- **Touch screens:** there is a Cancel button in the banner, and pressing the button again stops it.
- **Leaving the 3D view** (Tab, or a click elsewhere) cancels Put on a face, so Enter can't do something else by surprise.
- **Holes are left out** when lining up, Put next to, Measure 1 to 2 and Drop to floor.
- **Measure 1 to 2 updates** after Put next to and Line up.
- **Enter** in the 3D view goes into a group (its first part), and **Shift+Enter** goes back out.

**Pictures and materials**
- **A merge or Join keeps a picture only if every solid part had the same one.** One part's bricks were spread over the whole roof. It says when it drops the pictures.
- **Imported material names are kept** ("Steel", "Rust Red"), and exported under that name until you change the look. So "satin" no longer piles up on each round trip.
- With **Imports keep their place** on, a multi-part import keeps the file's own origin as its group's origin.

**Keyboard and screen readers**
- **Focus stays on the Inspector button or box you used** when the Inspector is rebuilt (Hole, Right of, the Size boxes...). Ctrl+Z from a number box comes back to that box.
- After a group, a pattern or an undo, focus moves to the row of what is picked.
- The same words shown and announced are read out once, not twice.
- Patterns are grouped and named in one go ("Peg pattern"), with one message. A circle pattern's copies show friendly turn angles.

**Small things**
- Colour dots in the Scene list are round, so white ones don't look like empty checkboxes.
- Group arrows are bigger on touch screens.
- Disabled merge buttons say why they are disabled.
- The crash-backup message counts the parts inside groups.
- Opening a file no longer also says "Framed the selection".

## 0.4.0 - 2026-09-30 - Groups, holes, placing, patterns, rounded edges, pictures

**Groups**
- **Group (Ctrl+G) and Ungroup (Ctrl+Shift+G).** A group moves, turns, resizes, hides and is named as one, and its parts keep their own shapes and colours. Nothing is merged.
- **Clicking a part of a group** picks the whole group; clicking again picks just that part. Once you are inside a group, clicks pick its parts.
- **The Scene list shows each group's parts** indented under it. The arrow button (or Right and Left on the keyboard) opens and closes a group.
- **The group's Inspector** has Ungroup, Pick the parts, and **Join into one solid**, which merges all the parts and cuts out any holes.
- **Groups are saved in projects** (format version 2; version 1 files still open) and **written into GLB files as nodes**.
- **Opening a GLB or glTF keeps its groups** and each part's own position, turn and scale, so a prop's pivot stays where the file put it.
- A model with several parts opens as one group, named after the file.
- Merge works on objects at the same level. Inside a group, the result stays in the group.

**Hole mode**
- **Kind: Solid or Hole** (in the Inspector, for one object or several). A hole is see-through grey.
- **Any merge cuts the holes out of the solids.** So does Join into one solid on a group, which is how Tinkercad does it.
- Holes are left out of exports, and the Export dialog says so.

**Placing things exactly**
- **Put next to, in pick order:** with two or more objects picked, number 2 goes to the right of, left of, on top of, under, in front of or behind number 1, number 3 goes against number 2, and so on, with a gap you choose.
- **Put on a face** (P, or the button under the Scene list). Click a face of another object, and the selection moves against it, centred on the point you clicked.
- **The Measure tool** (M, on the tool rail) measures between two clicked points. Points near a corner snap to it. It shows the distance and how far apart the points are along X, Y and Z. Escape clears it.
- **Measure 1 to 2:** with two objects picked, the Inspector shows the gaps between them on each axis, and the distance from middle to middle. This works from the keyboard.
- **Snap to other objects:** while moving with Snap on, an object's sides and middle stick to other objects' sides and middles when they come within 8 pixels.

**Patterns**
- **Pattern (repeat)** in the Inspector makes copies in a line (with a step in X, Y and Z) or round a circle (a centre, an angle to fill, and whether the copies turn with the circle). The copies can be grouped. It takes one undo step.

**Rounded edges**
- **Boxes and cylinders have Round edges (mm) and Rounding steps.** Rounding steps 1 gives a flat bevel (a chamfer). Rounded shapes stay editable, and they merge and print closed.

**Pictures on surfaces (textures)**
- **Add a picture** (PNG, JPEG or WebP) to any object in the Look section, and set how many times it repeats across and up.
- **Pictures are redrawn at most 1024 px across.** Only the pixels are kept, so the camera and place details in a photo never reach the project.
- Pictures are saved in projects, and each one is checked and redrawn again when a project opens.
- Pictures are exported in GLB. GLB and glTF files bring their pictures in.
- Number 1's picture goes onto a merge result.

**Fixes from the third test round**
- **Fixed: a second GLB export shrank a merged object 1000 times.** It still looked right on screen, but the next STL came out 0.04 mm. The export now keeps its own list of copies and never scales the live mesh.
- **Fixed: the left, bottom and back resize handles grew the object the wrong way.** The side opposite the handle you grab now stays put.
- **Fixed: dragging a resize handle past the far side turned the object inside out** (a negative scale), which broke its exports and merges. The size now stops at its smallest.
- **Resizing several objects** now snaps to whole mm and grows from one side, like one object. The "Group resize step" setting is gone.
- **Fixed: a multicolour object painted one colour still exported its old colours** (in COLOR_0 and OBJ).
- **Fixed: pressing F while the view was changing** left the camera part-way. It now frames from where the view is going.
- **Fixed: Clean view showed the handles again** after adding or picking an object.
- **Fixed: "Skip to the Inspector" on phones and tablets** now opens the Inspector sheet first.
- **Tidier merges.** Flat and doubled triangles are removed, and small holes of up to 64 edges are patched. The testers' chest (a box plus a flush-ended cylinder) and lamp (unions with a sphere) now come out closed. Corners in the same place get exactly the same numbers, for strict CAD checks.
- OBJ export writes texture coordinates (`vt`), and 3DEDTR reads the `# Units: metres` line of its own OBJs, so they come back full size. There is no false "That is big" for a 5 m model in mm.
- **Copies are named after the original** ("Log 2", not "Cylinder 2").
- Save project suggests the name typed in Export.
- A merge keeps number 1's bottom-centre origin.
- The GLB scene is named after the project (it was "AuxScene").
- The multicolour hint is tied to the Colour box for screen readers.
- The Flat view button is called "Flat view", so it can't be confused with Shading > Flat.
- The Settings hints are tied to their checkboxes.

## 0.3.1 - 2026-09-30 (running) - Clean view

- **Clean view** (C, or the eye button in the top bar) hides the grid and its axis lines, the move, turn and resize handles, the selection outlines, the X-Y-Z label and the "add a shape" hint, so you can just look at the model. The selection and settings stay as they were; press C again to bring everything back.

## 0.3.0 - 2026-09-29 - Colours through merges, flat view, one-sided resize

The next fixes from the testers' list.

**Colour**
- **Union keeps each part's colour.** A brown trunk and a green top stay brown and green after merging. Subtract and Intersect paint the cut walls in the kept object's colour. The object remembers its colours as a colour per corner.
- **Picking a colour paints the whole object** one colour; Undo brings the part colours back. The Inspector says when an object keeps its parts' colours.
- **Colours and texture coordinates (uv) travel everywhere:** through merges, projects (.3dedtr), GLB (COLOR_0 and TEXCOORD_0) and imports. A model with more than 200 parts is still joined into one, but now keeps each part's colour.
- **OBJ export writes colours** after each corner ("v x y z r g b"), which Blender, MeshLab and 3DEDTR read. It is 3DEDTR's own small OBJ writer, since three.js's leaves colours out. Object names keep their spaces.
- **GLB materials are shared and named:** objects that look the same share one material, called after its look ("Red satin", "Multicolour matte").

**Viewing and sizing**
- **Flat view** (the Flat button, or 5): an orthographic camera with no perspective, so parallel edges stay parallel, for checking alignment. Front, Side, Top, Corner, F, zoom (+/-, scroll) and picking all work in it.
- **Resize from one side:** the Resize tool's handles grow an object towards the handle, and the left, bottom and back sides stay put, as in Tinkercad. Settings can switch back to growing from the middle. (Turned objects still grow from their middle.)
- **A turned object shows how much room it takes up on the grid** under its Size ("On the grid it takes up 42.43 × 20 × 42.43 mm").
- **The camera reframes after a merge** whose result grows past the edge of the view.

**Origins and imports**
- **Shapes can have their origin at the bottom centre** (Shape section, "Origin: Middle | Bottom centre"), like meshes. The shape stays where it is on screen, and the setting is saved in projects.
- **Imports can keep the positions in their file** (Settings: "Imports keep their place"), instead of landing in the middle of the view.

**Small things**
- Enter in the Name box keeps the name and goes back to the 3D view.
- A new shape that steps aside to avoid another says so ("Placed beside Box 1 so they don't overlap").
- A second skip link, "Skip to the Inspector".
- Tablets (600 to 820 px wide) keep a slim status bar with the selection and its size. On phones and tablets, messages show below the view buttons, clear of the Inspector sheet.

## 0.2.1 - 2026-09-29 - Fixes from the second test round

The five testers re-ran their round-1 work on 0.2.0. This fixes what 0.2.0 broke or left rough.

- **Fixed: Subtract refused real small cuts** in big parts (a 1 mm cube out of a 100 mm block, a 5 mm notch in a 1 m cube) as "nothing was cut". It now refuses only when no cutter reaches the object, or the volume does not change at all (to a billionth). The message counts only the cutters that touch ("1 object cut out of Lid (1 did not touch it)").
- **Watertight merges.** Merge results now close their T-junctions (where a corner of one face sits on the middle of another's edge). The testers' flush-cut clip, box-minus-cylinder and flush-union phone stand now all export with 0 open edges.
- **Big scenes fit.** The camera can pull back to 80 m (it stopped at 6 m), and its near and far limits follow the zoom, so a 15 m fence fits and F frames it.
- **Pick several by keyboard:** the arrow keys only move through the Scene list; Enter or Space picks and un-picks.
- **Undo and redo keep the selection** of a merge, a delete or a copy.
- **Ctrl+Z / Ctrl+Y straight after typing a number** undo in the app, not in the box. **Escape in an Inspector box puts the last value back.**
- **Group turns** show friendly angles too (Y 135, not X 180 / Y 45 / Z 180).
- **Values kept inside their limits say so** (a 0.05 mm slot silently became 0.1 mm).
- File names: a typed ".3dedtr" is not doubled, and runs of dashes and spaces are tidied. The Save dialog shows "type a name" on the box itself (aria-invalid).
- glTF names keep their spaces ("Snow bottom", not "Snow_bottom"). No "very big" hint on a glTF already converted from metres, and no double full stop.
- Phones: messages appear at the top of the view, clear of the Inspector sheet. Focus lands on the 3D view after the splash closes (any way) and after opening a file.

## 0.2.0 - 2026-09-29 - Fixes from the test panel

Five testers - a maker, a teacher, a game developer, a product designer and a keyboard-only user - used 0.1.1 end to end. This release fixes what they found.

**Merge Shapes**
- **Clean, closed results.** Merging now uses three-bvh-csg's CDT clipping. Shapes that touch exactly (a cutter as long as the block, a peg standing on a floor) used to turn into thousands of sliver triangles and a mesh with gaps: a flush-cut clip went from 27,961 triangles with 6,331 broken edges to 414 and 6, and a peg on a floor from 1,833 triangles with 815 to 170 with none. Merging is also faster (16 chained merges: 2.1 s to 0.4 s).
- **Subtract says when nothing was cut** (the objects don't overlap) instead of quietly making an identical copy. The messages count correctly ("1 object cut out of Walls").
- **The result keeps the kept object's name.**

**Sizes and placing**
- **Fixed:** after changing a shape's Width, Height or Depth, typing a Size used the old size (Width 60, then Size 80, gave 240 mm).
- **Objects on the floor stay on the floor** when they get taller or shorter - in the Inspector, with Reset scale, or with the Resize tool.
- **Resizing one object with Snap on keeps its size to whole move steps** (1 mm by default), instead of 0.1x jumps. Groups still use the group resize step.
- **Turn boxes** show the angle you turned to after going past 90 degrees (Y 135, not X 180 / Y 45 / Z 180).
- A hint says Size is measured along a turned object's own sides.

**Export and import**
- **GLB is in metres**, the glTF standard, with the numbers baked into the mesh and node positions, so models are the right size in Godot, Unity and Blender. OBJ can be exported in metres too (mm by default). A new Units choice in Export.
- **Flat shading carries across** into STL, OBJ and GLB (each triangle gets its own face direction).
- **The STL summary** warns about anything below the floor (below the print bed) and says whether every solid is closed (watertight).
- **glTF and GLB are converted from metres to mm on the way in.** GLBs made by 3DEDTR 0.1 were in mm, so they come in 1000 times too big: the new "mm → metres" button fixes that.
- **Made in other units?** One-click cm, inches and metres to mm (and back) in the Inspector, for one object or a whole group.
- **Origin to bottom centre** for meshes, for game props that should stand on their pivot.
- Up to 200 imported parts stay separate (was 32). White OBJ parts get a colour from the palette.

**Saving**
- **Save project asks for a name** (so a class doesn't end up with twenty-five files called 3dedtr.3dedtr), opening a project remembers it, and Export starts with the same name.
- A crash backup is found even if the app is reopened within 30 seconds of the crash (it looks again once the old tab has stopped "breathing").

**Keyboard and accessibility**
- Focus stays in place after Merge, Delete and Undo: it lands on the result's row in the Scene list, never back at the top of the page.
- **F6 / Shift+F6** jump between the tool rail, the 3D view, the Scene list, the Inspector and the top bar.
- Escape in an Inspector box goes back to the 3D view (it no longer clears the selection from inside the Inspector). On a phone, Escape closes the Inspector sheet.
- Ctrl+D works straight after typing a number. Renaming takes the first keys you type. The Export and Save dialogs open on their name box.
- The Help panels scroll with the keyboard (axe: scrollable-region-focusable).
- Colour swatches have names, show which one is on, and are announced.
- Forced colours (Windows High Contrast): the swatches and colour dots keep their colours, and pressed, picked and selected states show as outlines.
- The 3D view's description only mentions single-key shortcuts while they are on.

**Phones, tablets and small laptops**
- The Inspector button says "Inspector", and the Inspector opens by itself after the first shape.
- Getting started covers naming, undo, saving and reopening, and touch gestures.
- At 1280 x 720 every rail button fits.
- Pick several starts a fresh selection, so the first object you tap is number 1, and turns itself off after a merge.

**Also**
- The grid grows with the scene (up to 20 m, with metre lines) and the move step goes up to 1000 mm.
- The triangle count shows only what is visible, plus the selection's share.
- Undo remembers 300 steps (was 100).
- Framing (F) fits tall, narrow windows.

## 0.1.1 - 2026-09-29

- **Recovers from a bad upload by itself.** If the 3D engine fails to load, the page now throws away its saved copy of the engine, so Reload fetches fresh files instead of the broken ones. The "did not load" card also shows the browser's own error, which names the file that failed.
- **The offline copy only keeps whole engine files.** The service worker checks each one before saving it (a JavaScript file over 4 KB that ends in its export list), so an empty or cut-off file, or an error page, is never saved.
- More apps and the splash now list all eight apps in every app in the family.
- README: upload, then purge Cloudflare, then test.

## 0.1.0 - 2026-09-29

First release.

**Building**
- Nine shapes on the tool rail: box, sphere, cylinder, cone, pyramid (3 to 12 sides), wedge, torus, capsule and plane. Each one stays editable: its size and smoothness can be changed in the Inspector at any time. Shift+1 to Shift+9 add them from the keyboard.
- A new shape lands on the floor where the camera is looking, and steps aside if something is already there.
- Move (W), Turn (E) and Resize (R) tools with drag handles. With several objects picked, the handles move them all together.
- The Inspector takes exact numbers: position, turn in degrees, size in millimetres (with Keep proportions), plus Drop to floor, Middle of grid, Reset turn and Reset scale.
- Snap (the magnet) moves, turns and resizes in steps you set in Settings: 1 mm, 15° and 0.1 by default. Hold Alt (Option) to move freely.
- Look: colour (with quick swatches), finish (Matte, Satin, Glossy, Metal), how solid it is, and smooth or flat shading.

**Merge Shapes**
- Union, Subtract and Intersect, in pick order: the first object picked is kept, gives the result its look, and is what Subtract cuts into. Numbers in the Scene list show the order.
- Keep originals hides the pieces instead of deleting them.
- Line up with number 1: left, centre, right, bottom, middle, top, back and front edges, and Drop all to floor.

**Files**
- Open STL, OBJ, glTF and GLB models (drag and drop works too), and save and reopen .3dedtr projects. Every file is checked before anything is added or replaced, and a glTF that points at other files or web addresses is refused.
- Export STL (turned Z-up for 3D printers), OBJ, GLB (keeps colours and finishes) and PNG pictures (up to 3x the view, optionally see-through). Export everything shown, or just the selection.

**Viewing**
- Drag to turn the view, right-drag to slide, scroll to zoom; Front, Side, Top and Corner views (1 to 4); Frame (F); grid (G); wireframe (Shift+W); three lighting moods and shadows.

**Keyboard and screen readers**
- Arrow keys move the selection the way they point on screen (Shift for ten times as far), Page Up/Down move it up and down, End drops it to the floor, [ and ] pick the previous or next object, Alt+arrows turn the view.
- The Scene list works with Up/Down (Shift to add), Home/End, F2 to rename and H to hide.
- Single-key shortcuts can be switched off in Settings.

**Family features**
- The family's splash (New scene, Try the example, Open a file), crash backups with the backup icon, help panel (Keyboard shortcuts, Getting started, About, Changelog, More apps), Install button and update check. Works offline once installed.
- The 3D engine (three.js r186, three-mesh-bvh 0.9.15, three-bvh-csg 0.0.18, all MIT) ships in the app's engine folder, so the page loads no code from any other server.
