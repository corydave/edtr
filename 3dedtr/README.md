# 3DEDTR

A 3D modeling app that runs entirely in the browser. Build models from basic shapes, merge them (**Union**, **Subtract**, **Intersect**) and export them for 3D printing. Part of the TXTEDTR / PDFEDTR / IMGEDTR / SNDEDTR / VIDEDTR / SCRNCSTR / VCTREDTR family. Its family colour is bronze, `#7a4100` (8.1:1 with white text); in dark mode, text in the app colour uses `#f0b46e`.

## Files

| File | What it is |
|---|---|
| `index.html` | The whole app: HTML, CSS and JavaScript in one file |
| `engine/` | The 3D engine: unmodified copies of three.js r186 and its helpers, plus three-mesh-bvh and three-bvh-csg for Merge Shapes. Licences in `engine/LICENSES.txt`. Upload the folder with the app. |
| `sw.js` | Service worker: offline support, and it keeps a copy of the engine |
| `manifest.webmanifest` | Makes the app installable, and lets the installed app open `.stl`, `.obj`, `.gltf`, `.glb` and `.3dedtr` files |
| `icon-192.png`, `icon-512.png`, `icon-maskable-512.png`, `apple-touch-icon.png`, `favicon-32.png` | App icons, drawn by `make-icons.py` |
| `icon.svg` | The mark as an SVG (the same drawing as the top bar and the shared block's `SUITE_MARKS`) |
| `make-icons.py` | Redraws every PNG icon: `python3 make-icons.py` (needs Pillow) |
| `make-mediabunny.sh` | Rebuilds `engine/addons/mediabunny/mediabunny-3dedtr.min.js` (the video library) from npm: `sh make-mediabunny.sh` (needs Node.js). Only needed to update it; not for the server. |
| `make-fonts.py` | Makes `engine/fonts/*.json` (the Text shape's typefaces) from the fontsource .woff files: `python3 make-fonts.py <folder>` (needs fonttools and skia-pathops). Only needed to change the fonts or their characters. |
| `CHANGELOG.md` | Long-form release notes |

## The 3D engine

The engine is **self-hosted** in `engine/`, not loaded from a CDN, so the page's security policy can be `script-src 'self'` with no outside server at all. An import map in `index.html` points `three`, `three/addons/`, `three-mesh-bvh` and `three-bvh-csg` at those files.

| Package | Version | Files |
|---|---|---|
| three | 0.186.1 (r186) | `build/three.module.js`, `build/three.core.js`, and from `examples/jsm/`: OrbitControls, TransformControls, STLExporter, OBJExporter, GLTFExporter, STLLoader, OBJLoader, GLTFLoader, BufferGeometryUtils, SkeletonUtils, RoundedBoxGeometry, FontLoader, SVGLoader (under `engine/addons/`, same sub-folders; `geometries/RoundedBoxGeometry.js` is new in 0.4.0, so upload that folder too) |
| three-mesh-bvh | 0.9.15 | `build/index.module.js` as `three-mesh-bvh.module.js` |
| three-bvh-csg | 0.0.18 | `build/index.module.js` as `three-bvh-csg.module.js` |
| mediabunny | 1.61.0 (MPL-2.0) | Only the parts video export uses (Output, MP4 and WebM formats, BufferTarget, CanvasSource, codec checks), bundled by `make-mediabunny.sh` as `addons/mediabunny/mediabunny-3dedtr.min.js` (220 KB). Loaded only when a video is exported. |

To upgrade: replace the files (same names), update the versions here, in the About tab and in `engine/LICENSES.txt`, and change `ENGINE_CACHE` in `sw.js` so browsers download the new engine.

**Uploading the engine (and Cloudflare).** daveghidiu.com sits behind Cloudflare, which keeps its own copies of `.js` files. Upload the whole folder first, then **purge the cache at Cloudflare**, and only then open the app. If you open it while files are still uploading, Cloudflare (and your browser) can keep a half-finished file and go on serving it after the upload is done.

The app protects itself from the rest: the service worker only saves an engine file that arrived whole (a JavaScript file over 4 KB ending in its `export { ... }` list), and if the engine fails to load, the page throws away its saved engine copies, so Reload fetches fresh ones. The "did not load" card shows the browser's own error, which names the file that failed.

## Fonts (the Text shape)

Eight typefaces, all SIL Open Font License 1.1 with no Reserved Font Names (a converted copy may be shared), from fontsource 5.3.0, converted to three.js "typeface" JSON by `make-fonts.py`:

| File | Typeface | Shown as |
|---|---|---|
| `sans.json` | Inter Bold | Sans |
| `serif.json` | Noto Serif Bold | Serif |
| `slab.json` | Zilla Slab Bold | Slab |
| `legible.json` | Atkinson Hyperlegible Next Bold | Easy to read |
| `rounded.json` | Nunito ExtraBold | Rounded |
| `display.json` | Anton | Tall and bold |
| `script.json` | Pacifico | Script |
| `stencil.json` | Big Shoulders Stencil Display ExtraBold | Stencil (its bridges keep letter middles attached, for cut-through signs) |

Each holds Latin, Latin-1 and Latin Extended-A where the typeface has them (105-250 KB) and is fetched the first time a Text needs it. A letter a typeface lacks (Atkinson Hyperlegible Next has no Esperanto or Latvian letters such as ĉ, ŗ; most lack ĳ and ſ) is drawn from Inter at the same capital height; a letter neither has shows as "?". Upload the `engine/fonts` folder with the rest of the engine (and purge Cloudflare). To add a typeface: put its fontsource .woff files in a folder, add a line to FONTS in `make-fonts.py`, run `python3 make-fonts.py <folder> <key>`, add the key to the Typeface list in `index.html` and to `ENGINE_FILES` in `sw.js`, and add its copyright line to `engine/LICENSES.txt`. Check the licence first: a font with a Reserved Font Name can't be converted and kept under its name.

## Lights

The bulb button on the tool rail adds a **spot light**, aimed at the middle of the model. In the Inspector it can become a **bulb** (point light) or a **sun** (directional), with colour, brightness (100% is about the studio light; a spot or bulb fades with the square of the distance, as real lights do), beam width and soft edge (spot), and shadows. Aim it with the Turn tool (E), the Turn boxes, or **Aim at**.

- A light is an item in the Scene list (`userData.type: 'light'`): an Object3D holding the three.js light, which shines down the item's own -Z. Its symbol is drawn in `helperGroup`, so Clean view, PNG and video leave it out. It is picked alone (never merged, grouped, measured as a solid, dropped to the floor, or put in STL or OBJ).
- **Keyframes:** position and turn move and aim it; the **Dimmer** (keyframed like "how solid") fades it.
- **Shadows:** at most 4 lights cast them (`MAX_SHADOW_LIGHTS`); a sun's shadow area is fitted round the model before every drawing (`fitSunShadows`). The Shadows switch covers them all.
- **GLB** carries lights as `KHR_lights_punctual` (spot cones and colour included; a spot or bulb's intensity is divided by 1,000,000 in a metre file, so it looks the same). Their position and turn animate with the rest; the dimmer can't (glTF has no way to animate brightness without another extension).
- **Scene lighting is saved with the scene** (`lighting: { mood, on }` in the project, and in undo steps): the built-in lights' mood (Studio, Soft, Bright, Product, Dramatic, Sunset) and whether they are on. The **sun button in the top bar** (or Built-in lights in Scene settings) switches every built-in light off, leaving only the lights you add, and back on to the same mood. Settings' Lighting is only the mood a new scene starts with; a project from before 0.10.2 opens in it, built-in lights on.

## SVG import

Open (or drop) an `.svg`: a dialog previews it, with its width, height (proportions kept) and depth, and it becomes an extruded shape whose Outline is "Imported drawing", holes kept (`params.art`: `{ aspect, shapes: [[outline, hole...], ...] }`, each ring a flat list of x, y numbers from -1 to 1). Made for VCTREDTR's SVG export, and works with Inkscape, Illustrator and icon sets.

- **Read safely:** the text is parsed as XML (DOMParser runs no scripts and loads nothing); a file with XML entities is refused; everything but shapes, groups, `defs`, `symbol`, `use` and `style` is removed (scripts, pictures, foreignObject, links, text, filters), as are event attributes and any `href` that isn't `#id` and CSS `@import`/`url()`; `<use>` copies are expanded by 3DEDTR, refusing ones that copy themselves and stopping past 20,000 pieces. three.js's SVGLoader then reads the cleaned file; only numbers are kept, and the previews are drawn from those numbers.
- **What comes in:** filled shapes, with fill-rule holes. White parts (a background, or white drawn on top) can be left out. Lines with no fill are left out, unless that is all there is. Text must be turned into outlines first.
- **Size:** from the SVG's own width and viewBox (mm, cm, in, pt, px at 96 a inch); anything under 2 mm or over 400 mm starts at 50 mm across.
- **Limits:** 5 MB, 8,000 points (simplified with Douglas-Peucker until it fits), 400 shapes.

## For 3D printing

- **Lay flat (L):** turns each picked object so its biggest outside flat face (one with nothing sticking out past it) is on the floor.
- **Hole through a face (D):** click a face; a 3.2 mm round Hole goes in square to that face, right through the object plus 1 mm each side. Enter instead makes one straight down through the middle of the picked object. The next hole takes the size of a picked hole.
- **Rounded corners on drawn outlines:** a sharp point between two straight edges can have a Round radius (the points list's Round box): a true circular arc (`roundedPieces`), held to half of each edge.

## Smooth and wall

The Inspector's **Smooth and wall** section works on any shape or mesh, without changing it: the object is drawn from a copy made with its settings (`applyMods`), in `userData.mods: { wrap?: { target, offset, reach }, thick, dir: 'in' | 'mid' | 'out', smooth: 0-3 }`. A mesh keeps its own triangles in `userData.base`; projects save the base and `mods`.

- **Wall thickness** (`solidify`): weld, then move a copy of the surface along angle-weighted normals (further at corners, for an even wall), flip it, and bridge any open edges. Closed shapes become hollow shells; open ones solid sheets.
- **Shrink onto** (`wrapPoints`, first): each point to the nearest point on the target object's surface (a `MeshBVH` of its world-space copy) plus `offset` along its face direction, only within `reach` mm when set. `refreshWraps()` (called in `afterChange`) re-wraps when either object, or the settings, changed. Projects remap the target id.
- **Smooth** (`smoothStep`, Catmull-Clark): weld, rebuild quads from triangle pairs (`quadsOf`) and flat fans (`mergeFans`), cut long quads into strips (`evenOut`), then subdivide. Stops before 1.5 million triangles.

## Edit mode

Tab in the 3D view (with single-key shortcuts on), or **Edit points** in the Inspector, edits the points of one shape or mesh (section 9d of the script). Its own triangles (`userData.base` for a mesh; a shape is built fresh without its mods) are welded into shared points (`weldGeometry` → `edit.w = { pos, col, tris }`) and drawn over it as `LineSegments` and `Points` (with a background-coloured halo) in `editGroup`, which follows the object every frame.

- **Picking:** `editPointAt` (within 12 px), `editBoxSelect` (Shift adds, Ctrl/Alt removes), All / None / Others / More / Less / one side of the middle. Points hidden behind the surface are left out (`editVisible`: a `MeshBVH` ray from the point towards the camera) unless X-ray is on.
- **Moving:** `editStartMove` records every point and how much it follows (1 when picked; with Proportional editing, `falloff()` of the distance to the nearest picked point within the reach), then `editApplyMove(d)` moves them by a world distance turned into the object's own space. Used by the gizmo (on `editPivot`, the middle of the picked points), G (a plane facing the camera; X/Y/Z keep one direction; snap applies), the arrow keys and the typed middle.
- **Keeping it:** `editCommit` writes the points back as the object's own triangles (a shape becomes a mesh), rebuilds Shrink/Wall/Smooth, and commits one undo step. Undo/Redo re-attach to the same object by id (`reattachEdit`), keeping the picked points when the count matches.
- **Deleting:** points and every face using them, or just faces whose corners are all picked (then unused points go). The surface is left open - Wall makes it printable again.
- **Building (0.16.0):** every tool hands new `{ pos, col, tris }` to `editReplace`, which drops unused points, renumbers and commits one undo step.
  - `editExtrude`: faces with every corner picked are copied onto new points and joined to the old ones by side walls along the region's border (each wall wound to match the faces on both sides); with no whole face, picked edges (open ones first) each grow a strip. E with the pointer over the view starts a grab flagged `extrude` (no Proportional pull), and cancelling it undoes the extrusion and puts the picks back.
  - `editMergeCentre` (M) and `editMergeClose` (a grid of boxes as wide as the distance, then union-find); `editMergeFinish` drops faces that fold to a line and pairs of faces on the same three points.
  - `editFill` (Shift+F): picked open edges are chained into rims; a rim of 3 or 4 gets one face, a longer one a fan round a new middle point. Otherwise 3 or 4 picked points make a face, ordered round their middle and turned towards the camera.
  - Loops (`editLoopFrom`): the triangles are put back into quads with `quadsOf` (as Smooth does); from an edge, the walk goes straight on through every point with exactly four edges, to the one edge that shares no piece with the incoming one. Alt+click picks the visible edge nearest the pointer (`editLoopClick`); L uses two picked neighbours.
- **More tools (0.17.0):** `editSelectLinked` (Ctrl+L, a flood fill over `edit.nb`); `editBevel` (Ctrl+B: on the faces from `quadsOf`, each picked corner becomes two points on its edges, `bevel` mm along, at most 45% of the edge; the new face at each point is its cap edges chained into a ring and fanned - a 20 mm box with 4 mm bevels is exactly 8000 - 8 x 4³/6 mm³); `editCutPlane(plane, keep)` splits every crossed face along a plane in the object's own space and also splits the faces beside each cut edge, so nothing cracks; the Knife (K, `knifeClick`) makes that plane from two screen clicks and the camera, keeping faces whose middle is between the clicks and can be seen (all of them with X-ray); `editCutAcross` cuts straight across X, Y or Z through the picked points' middle.
- **Copy and paste (objects):** `copySelection` keeps `describe()` of each picked object with its group's id and its world and local matrices (`clip`, in this tab only); `pasteClip` makes fresh ids, puts each copy back in its group if that group still exists (otherwise into the scene at its world place), moves it 10 mm per paste and carries its keyframes along (`keysFollow`). Only from the 3D view or the Scene list, so copying text elsewhere is untouched.

## Keyframes and groups

`addKeyframes` keys `keyTargets(selection)`: with `settings.keyParts` (Parts too, on the timeline, default on) that is every picked object plus every part of every picked group, at every level. Parts keep their own keyframes in their group's space, so the group's motion (a turntable) and the parts' motion (an explode) add up. A part keyed for the first time while an ancestor has keyframes at other moments is back-filled there with `oldestPose(id, parentId)`, its oldest pose in the undo history within the same group. The Exploded view preset's Which way field spreads parts out from the middle, or in layers along X, Y or Z (layers by middle depth, ranked outwards from the middle layer).

## Samples

The splash offers **Try the example** (`loadExample`: a box and a cylinder, picked, ready to Subtract) and, since 0.21.0, **Phone sample** (`loadPhoneSample`): a generic smartphone built from descriptors with `createItem` - 37 shapes in a group, with an 8-second turntable on the group. Both are also buttons in Tips.

## Symmetry

`mods.sym` is `{ kind: 'mirror', x, y, z }` or `{ kind: 'around', count, axis }`, applied first in `applyMods` (`applySymmetry`): points within a hair of a cut are put on it, faces lying in a cut are left out, the piece is copied (mirror images with their faces reversed), and points on the cuts are joined (`closeGroups`, union-find in a grid). `setSymmetry` makes the object's triangles whole with the old symmetry, then cuts them to the new piece (`clipToPlane`, planes through the object's origin from `symPlanes`), so a shape becomes a mesh holding one piece; it warns when the copies' cuts don't match (`weldedOpenEdges` before and after). In Edit mode, `editSeamPoints` keeps moved points on their cut (on the axis: along it), and for Around moves each first-cut point's partner on the second cut with it, turned by one slice.

## Pattern: On a surface

`scatterOnSurface`: the target's world triangles (only those facing up, when asked) are picked by area with a seeded random maker (`seededRandom`, mulberry32), a random point in each; copies keep the object's own turn and scale, then vary in size, twist round their own up, have their up turned to the face's direction and their bottom (`localBox`) set on the surface plus the lift. "Keep them apart" refuses spots closer than 0.6 x the object's width. Grouped as "<name> scatter" by default; one undo step.

## Animated GLB

With **Animation** ticked (Export, GLB), the file holds one animation clip: for each moving object, its position, turn (quaternion) and scale, sampled at every frame of the clip plus just before and at each keyframe, as linear tracks on that object's node (in its group's space; in metres when the file is). The camera can be included as a camera node, with its moves. How solid an object is can't be animated in core glTF, so fading parts are written at their most solid. Nodes are always written as TRS (translation, rotation, scale). Checked with the Khronos glTF Validator and three.js's GLTFLoader + AnimationMixer.

## Video export

Export, then **Video**. The clip (its length and frames a second are on the timeline) is drawn **one frame at a time** at the size asked for, and each frame goes to the browser's own video encoder (WebCodecs) through Mediabunny, which packs the frames into the file. Every frame is drawn and handed over before the next, so nothing is dropped on a slow device: it just takes longer. A progress count and Cancel show while it works. Nothing is uploaded.

- **Kinds:** MP4 (H.264 where the browser can make it - Chrome, Edge and Safari can; otherwise VP9, with a message that PowerPoint or QuickTime may not play it), WebM (VP9 or VP8), or **PNG frames** in a .zip (stored, not squeezed; at most 3,600 frames), for video editors.
- **Sizes:** the view's shape at 1080 high, 1280 × 720, 1920 × 1080, 1080 × 1080, 1080 × 1920 (upright) or 3840 × 2160. The camera keeps its up-and-down view, so a wider shape shows more at the sides.
- **Background:** as in the view, white, black, or **see-through** (WebM and PNG frames). A see-through WebM stores the see-through part separately (VP9 alpha), as browsers and editors expect; Mediabunny does that in a small helper (a worker), which is why the security policy allows `worker-src blob:`. It still can't load or send anything elsewhere.
- **The camera:** the video follows the camera's keyframes when there are any (even with Follow the camera off), otherwise it uses the view as you see it. Holes, the grid, handles and outlines are left out, as in PNG.
- Upload `engine/addons/mediabunny/` with the rest of the engine (then purge Cloudflare). The service worker keeps it, so video export works offline too.

## Units and directions

- 1 unit = 1 mm. One grid square is 10 mm; the stronger lines are every 50 mm. The grid grows for bigger scenes (2 m, then 20 m with lines every 100 mm and 1 m).
- **GLB is exported in metres** (the glTF standard), baked into the mesh and node positions. OBJ is mm unless Units says metres. glTF and GLB are read as metres and converted to mm.
- Y is up, as in three.js and most 3D apps. **STL export turns the model so Z is up** (the "Z is up" box in Export, on by default), because 3D printers and slicers expect that. STL import turns it back. OBJ and GLB stay Y-up, which is their convention.

## Project files (.3dedtr)

- **Save project** (Ctrl+Shift+S) keeps everything editable. The file is JSON (format version 3, or 4 when it has lights, so an older 3DEDTR says it needs an update instead of failing):
  - each object's name, kind, shape settings, position, turn, scale and look;
  - whether it is a hole;
  - its picture and repeat.
- **Animation** (format 3): `animation: { length, fps, loop, camera }` at the top (`camera`: the camera's keyframes, `{ t, p, g, e, spin }` - where it stands, the point it looks at, the easing, and whole extra turns), and and `keys` on any object or group: a list of `{ t, p, r, s, o, e }` (time in seconds, position, turn in radians, scale, how solid 0-1 for shapes and meshes, and the easing after it: `smooth`, `linear`, `in`, `out` or `hold`). Positions are local, like the Position boxes (in the group, for a part).
- **A group** is an entry with `type: "group"`, its own position, turn and scale, and its parts in `children`.
- **A merged or imported object's triangles** are stored as base64: positions, normals, uv, colours and an optional index.
- **Pictures** are stored once, in `textures`, as PNG, JPEG or WebP `data:` URLs of 3DEDTR's own redrawn copy.
- **Opening** checks every value before anything is replaced:
  - the format name and version (1 to 4 open);
  - lights (`type: "light"`, only at the top level, 16 at most): kind, `#rrggbb` colour, numbers inside their limits;
  - an imported drawing (`params.art`): 400 shapes and 8,000 points at most, every number from -1 to 1;
  - a drawn outline's points may have a 4th number, a sharp corner's Round radius (0 to 1,000 mm);
  - the kind of each object: only the known shapes (including `text` and `profile`), `mesh` and `group`;
  - shape settings by kind: numbers inside their limits, Text's words cleaned of control characters (500 at most), and choices (typeface, outline, line alignment) only from the known list;
  - a drawn outline (`params.outline`): 3 to 100 `[across, up, smooth]` points, each number from -1 to 1, that don't cross over themselves, pinch or double back. Anything else falls back to the default outline. `params.at` is where its middle was in the drawing pane (two numbers);
  - keyframes may carry `ce`: easings for single parts of the motion (`p`, `r`, `s`, `o`), only from the known list;
  - numbers are inside their limits, and colours are `#rrggbb`;
  - for meshes, the data lengths match and every index points at a corner that exists;
  - camera keyframes: the same checks for time and easing, positions inside the usual limits, and `spin` a whole number from -100 to 100;
  - keyframes: times from 0 to 600 s, the same number checks as positions, turns and scales, solid from 0 to 1, easings only from the known list, 20,000 keyframes at most; two at the same moment keep the later one. The clip is 0.5 to 600 s at 12, 24, 25, 30 or 60 frames a second;
  - groups are no more than 16 deep;
  - each picture is a `data:image/png|jpeg|webp;base64` URL under 16 MB. It is decoded by the browser and drawn again before use.
- Ids from the file are never used, and unknown fields are ignored.
- Limits: 150 MB per file, 2,000 objects (groups included), 3,000,000 triangles.

## Opening 3D models

- **STL** (binary or text), **OBJ**, **glTF** and **GLB**. An import is added to the scene, standing on the floor in the middle of the view.
- A glTF or GLB may only carry its data inside itself. One that points at other files or web addresses is refused before it is loaded (and the security policy would block the request anyway). Compressed glTF (Draco, meshopt) is not supported yet and is refused with a message.
- Shapes, colours, finishes and pictures (with their repeat and offset) come in. Animation, cameras and lights are left out.
- **SVG drawings** too: see SVG import.
- A glTF mesh node with other nodes under it comes in as a group holding that mesh and its parts; GLB export turns it back into one mesh node with its parts under it (while it is still as imported).
- **glTF and GLB keep their groups** and each part's own position, turn and scale (its pivot).
- A model with several parts comes in as one group, named after the file.
- A model with more than 200 parts is joined into one object, which keeps each part's colour.
- 3DEDTR's own OBJ files say their units on the first lines (`# Units: metres`), and it reads that back.

## Merge Shapes

Merging is done by three-bvh-csg, with `useCDTClipping` on. That gives closed (watertight) results and no sliver triangles when faces touch exactly, which the default splitter did not (tested in 0.2.0).

- **Before merging:** each object's position, turn and scale are baked into a copy of its triangles, so every piece is in the same frame.
- **The order:** the solids are merged first, in pick order. Then every **hole** is subtracted, whatever the kind of merge.
- **The result** is a new `mesh` object. It takes the first solid's look and goes where that object was, inside its group if it was in one. The originals are removed, or hidden with **Keep originals**.
- **Join into one solid** (a group's Inspector) does the same with all of the group's shown parts. Each group inside is joined first, with its own holes, so a hole only cuts its own group; a group of only holes counts as holes one level up. The result takes the group's place and name.
- **Cutting:** all the cutters (and all the holes) are joined into one brush first, then cut out in one go. Cutting one at a time re-sliced the same faces and left gaps (tested in 0.4.1).
- **Planes** have no inside, and are left out.
- **Tidying afterwards (`repairMesh`):** flat and doubled triangles are removed and T-junctions are closed. Holes of up to 64 edges are patched. Corners within a millionth of the model's size get exactly the same numbers.

## Colours

Each object has one colour, except a mesh made by Union from differently coloured parts (or imported with colours): it keeps a colour per corner (the `color` attribute, flagged `vertexColors` on the object and in projects). Picking a colour paints it one colour again. Merges carry `position`, `normal`, `uv` and `color`; shapes without a colour list or uv get them filled in first, so every brush has the same data.

## Phones and tablets

At 820 px wide or less the tool rail moves under the 3D view and the Inspector becomes a sheet between them, in its own grid row (`.app.sheet-open`: `minmax(0, 1fr) auto var(--sheet-h) 56px`), so the 3D view shrinks rather than being covered; tablets (600 px and up) keep a slim status bar. The **grab handle** at the top of the sheet (the same as DSKEDTR's) resizes it: drag it, or use Up/Down/Home/End/Enter on it (a `role="separator"`). It starts at a third of the screen, stays at least 120 px and always leaves the top bar, rail and 120 px of the view; a tap, or a drag nearly to the bottom, closes it to just the handle. The height is saved as a share of the screen in `settings.sheet` (`wireSheetHandle`, `applySheet`).

## Keyboard and screen readers

- The 3D view is a focusable `role="application"` region, so screen readers pass the arrow keys through. Arrow keys move the selection along the grid axis closest to "right" and "forward" on screen, Page Up/Down move it up and down, End drops it to the floor, Alt+arrows turn the view, + and - zoom.
- The Scene list is the keyboard way to pick objects: Up/Down (Shift to add), Home/End, Right/Left to open and close a group, F2 to rename, H to hide. It is an ARIA `tree` (each row a `treeitem` with its level, position and whether it is picked or open); the eye and arrow buttons are hidden from screen readers, as H and the arrows do the same.
- **Inspector:** Alt+Page Down / Alt+Page Up jump to the next or previous section heading from anywhere in it; on a heading, Up/Down/Home/End move between headings.
- **Measuring without a mouse:** in the Measure tool, Enter (or Measure between spots... in Measure 1 to 2) opens a dialog: an object and a spot on it (its middle, the middle of a side, or a corner of its box) for each end, the distance read out as it changes, and Show it in the view.
- Single-key shortcuts (W, 1, [ ...) can be switched off in Settings (WCAG 2.1.4).
- **Edit mode by keyboard:** Tab (single keys on) enters and leaves it from the 3D view - Shift+Tab and F6 still leave the 3D view, and with single keys off Tab moves focus as usual (no trap). [ and ] pick one point at a time and say where it is; the arrow keys and Page Up/Down move the picked points; the Inspector picks by side and moves by typed numbers. The banner, the status bar and the live region say how many points are picked.
- **X-ray** (Alt+Z, or the button beside Wireframe) draws every object see-through (`XRAY_SEE`, 40%) through `setSeeThrough()`, which every change of how solid something is goes through; `holdXray()` leaves it out while a PNG or video is drawn. It's a browser setting (`settings.xray`), not part of the project.
- Changes made in the Inspector never rebuild the Inspector, so Tab moves from box to box without losing its place.
- **The timeline** is a region under the 3D view. Its track is one `role="slider"` control for the play head (aria-valuetext says "1.50 s of 5.00 s, keyframe"): arrows move a frame (Shift a second), Page Up/Down jump between keyframes, Alt+arrows move the keyframe, Delete removes it, Space or Enter plays. The note under it is a status region that says when a change is not kept yet. Playback never starts by itself.
- **The outline pane** ("Draw your own") is a modal dialog. The drawing is a focusable `role="application"` SVG: [ and ] pick a point, arrows move it, Insert/Delete add and remove, S toggles smooth. The same points are a table of labelled number boxes, and the pane has its own live region (the app's announcer is hidden behind a modal). Smooth points are round dots and sharp corners squares, so the difference doesn't rely on colour.

## Known gaps (later versions)

- Edit mode has no edge bevel with rounded segments or edge slide yet, and loops need four-sided pieces (they stop at triangles and poles)
- A shell (hollow) tool, and compressed glTF
- Overlapping shapes in an imported SVG stay overlapping solids (Merge, or Join, cleans them)
- Raised bevelled text sunk into a plate less deep than its bevel leaves tiny slivers when merged (a CSG limit): sink it at least as deep as the bevel, or use bevel 0
- Dragging rows in the Scene list to reorder them or move them into a group
- The gizmo moves in world directions only (no "local" mode yet)
- See the project doc `3DEDTR-persona-findings.md` for the full list from the 0.1.1 test panel
