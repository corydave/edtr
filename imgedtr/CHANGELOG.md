# IMGEDTR Changelog

Newest first. The short form of each entry also lives in the `CHANGELOG` table inside `index.html` (shown in the app's Info > Changelog tab). Add new releases to both.

## 1.17.0 - 2026-10-10 - A new splash

- **A picture of IMGEDTR in use across the top of the splash** - the same picture as on edtrapps.com, built into the app (as a data: URI), so it shows offline too. With it, the small icon beside the name goes, since the picture already shows it.
- **Every way to begin is a card with a picture:** a folder opening for Open (the icon everybody knows), and pictures of their own for the rest.
- **"Pick up where you left off" is smaller and quieter:** a slim row under the cards rather than the big first button. It still only appears when the last session ended without saving, and the app's main way to begin keeps the focus.
- **Links to edtrapps.com and GitHub** under the credits (on the splash and in About): "All the apps at edtrapps.com - Free and open source on GitHub (MIT license)".
- The splash is a little wider (760px) with the picture; on a phone the cards stack in one column. The shared SUITE block was pasted in again from `_edtr-suite`.

## 1.16.0 - 2026-10-10 - A tour of the features

- **Features, a new first tab in Help:** an animated tour of five of IMGEDTR's favorite features - Hide private info, Spotlight one row, Numbered click steps, Show where to click and Magic wand: fill and recolor - each with a small looping drawing, a title and a sentence or two. Previous and Next, the dots, or the Left and Right arrow keys move between them; the animation has a pause button, and it starts paused when the device asks for less motion.
- **? or F1 and the Help button now open Help on Features.** Keyboard shortcuts is one tab over.
- **The splash has a "See what IMGEDTR can do" card** that opens the same tour over the splash.
- The shared SUITE block was pasted in again from `_edtr-suite` (new: `renderSuiteFeatures`, `suiteFeaturesOpen`, `suiteFeaturesCard` and their styles). The drawings are inline SVG with SVG's own animation tags, so they work offline and straight off a disk.

## 1.15.0 - 2026-10-07 - Make a headshot

- **New: Make a headshot**, a guided screen for profile photos. Start it from the splash ("Make a headshot") or the start screen ("Headshot"), and pick a photo (iPhone HEIC photos work too).
  1. **Frame the face.** Drag the photo to put the face in the middle; the Zoom slider (100% to 500%), the mouse wheel or a trackpad pinch zooms in. On the canvas, the arrow keys move the photo (Shift: ten times further) and + and - zoom. Portrait photos start near the top, where faces usually are. **Choose a different photo** (or drop or paste one) swaps the photo and keeps the style.
  2. **Style.** Circle or Square (Square has a Corners slider), a Border with its colour, and a Shadow with a Softness slider.
  3. **Background.** None (see-through corners, the default), White, or a colour. A tip says to choose White if a website shows the corners black.
  4. **Size and save.** 400, 800 (default) or 1024 pixels square. **Download PNG** (always PNG, so the corners can be see-through; named after the photo, for example *portrait-headshot.png*) and **Copy image**.
- **The shadow is never cut off.** The photo shrinks by a margin worked out from the shadow (1.5 x its softness plus how far it falls), so the whole blur fits inside the square. Nobody has to set the margin by hand.
- **Simple screen.** The tool rail, the Layers list and the layer action bar are hidden, and only the shortcuts that make sense still work (undo, redo, zoom, open, export, save project, copy image, help). On a phone the Inspector sheet opens by itself.
- **Open in full editor** goes back to normal IMGEDTR with nothing lost: the headshot is one ordinary image layer (its crop is the framing, its corner radius the circle, plus its border and shadow) on a square canvas, so every tool, Undo and Save project work on it.
- **Your style is remembered** for the next headshot (in IMGEDTR's settings in this browser; every value is checked when it is read back). Changing the size scales the border and shadow with it, so the look stays the same.
- Undo and Redo cover every headshot change, and the panel always shows what is really in the picture.

## 1.14.1 - 2026-10-07 - DSKEDTR joins the family

- **DSKEDTR joins the family.** More apps and the splash's row of apps now include DSKEDTR (dskedtr.app), the new desktop publishing app: newsletters, flyers and booklets, with text that flows between boxes, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js`.
- The splash's row now fits nine apps: the eight others on one line on a computer, and 4 + 4 on a phone (shared styles pasted in again from `_edtr-suite/suite-block.css`).

## 1.14.0 - 2026-10-07 - A grab handle for the phone Inspector

- **Phones and narrow windows: the Inspector sheet has a grab handle** along its top edge, the same as DSKEDTR's.
  - **Drag it up or down** to share the screen between the picture and the Inspector. The picture's area shrinks and the picture re-fits; the sheet never covers it.
  - **Tap it** to open or close the sheet. **Drag it nearly to the bottom** to close it. A closed sheet leaves just the handle showing (above the tool rail), so it can be tapped or pulled up again. The Inspector button in the top bar still opens and closes it, and the two stay in step. The sheet still starts closed.
  - **It starts with its top two thirds of the way down the screen.** It is never shorter than 120 px when open, and never so tall that the top bar, the tool rail and at least 140 px of picture are lost.
  - **Keyboard:** the handle is a separator. Up and Down change the height by about 8% of the screen (Down below the shortest closes it), Home closes, End makes it as tall as it goes, Enter or Space opens or closes it. Screen readers hear "Inspector open, 33 percent of the screen" or "Inspector closed".
  - **The height is remembered** in this browser (in IMGEDTR's settings), as a share of the screen, so it still fits after the phone is turned.
- The picture is redrawn straight away when its area changes size, so it no longer flickers while the sheet moves.
- Wide screens are unchanged: the handle only exists in the phone layout.

## 1.13.0 - 2026-10-07 - Fill and Recolor with the magic wand

- **The magic wand has an Action switch: Erase, Fill or Recolor.** Tolerance and Contiguous work for all three.
  - **Fill** is a paint bucket: the clicked area becomes one flat colour (Fill color, which starts as your annotation colour).
  - **Recolor** changes the clicked colour to a new one but keeps its shading, so lighter and darker parts stay lighter and darker. With Contiguous off, one click changes every area of that colour, such as both blue parts of the accessibility logo.
  - **Alt (Option)+click** with Fill or Recolor puts the original colours back in the clicked area.
- **No fringe.** A logo's edge pixels are blends (half blue, half white, say), and a plain bucket fill leaves them in the old colour. The wand grows the area by 2 px and changes each of those edge pixels by how much of the clicked colour it holds. It works that out by following the line from the clicked colour through the pixel's colour to the edge of the RGB cube. Pure neighbours (the white) are untouched. See-through-ness is never changed, so soft edges on transparent backgrounds stay soft.
- **Nothing destructive.** Like erasing, each click is saved as a small recipe in the layer's new `paint` list and replayed in order onto a copy of the picture. **Clear all color changes** (in the wand's panel and the picture's properties) brings back the exact original, and undo works per click.
  - Erasing sits on top of colour changes, and a Restore brush brings back the recoloured pixels.
  - Erase clicks with the wand now read the recoloured picture.
- **Soft edge for Fill works in every browser, Safari included.** It's done in plain JavaScript, not the browser's blur filter. (Erase's soft edge still uses the blur filter, so it stays sharp in Safari.) Recolor needs no soft edge; it blends by itself.
- Colour-change recipes in project files are checked when a project opens: known kinds, real numbers, and a proper #rrggbb colour. Anything malformed is dropped.

## 1.12.1 - 2026-10-03 - Links to the other apps

- Names of the other apps in Help (in the changelog, About and the guides) are now links that open that app. Each link opens in a new tab; this app's own name stays plain. Shared SUITE block: new `suiteLinkApps()` (called from `renderSuiteApps()`, so no app wiring needed).

## 1.12.0 - 2026-10-02 - Drag a copy, resize from the center, tidy-ups

- **Ctrl+drag a layer to drag a copy** (Cmd on a Mac). The original stays where it was, and you drop the copy wherever you like. **Ctrl+Shift+drag** keeps the copy moving in a straight line, across or down.
  - The copy is made on the first real movement. A plain Ctrl+click without dragging still adds or removes a layer from the selection, as before.
  - Pressing a layer that is already selected copies the whole selection. Pressing one that isn't copies just that layer, or its group.
  - Copy and move are one undo step.
  - On a Mac, Ctrl+click on the canvas no longer opens the right-click menu (a real right-click still does).
- **Ctrl while dragging a resize handle resizes from the center:** the opposite side moves the same amount. **Ctrl+Shift** grows or shrinks all four sides evenly, keeping the proportions. This also works on several selected layers or a group, scaling from their middle.
- **Resize handles snap** to the canvas edges and center and to other layers' edges and centers, with the same pink guides as moving. Hold Alt (Option) to resize freely. This is for layers that aren't turned; a turned layer's sides aren't straight across or down, so it doesn't snap.
- **Pad contents changed:** it now fits the canvas to everything on it with a 10 px margin all round, in one click. It used to add 10 px to each side and needed Fit contents first. For a different margin, use Canvas size... (padding, then Fit now).
- **The New canvas and Settings dialogs use IMGEDTR's color picker,** the same one as the properties panel, instead of the system one. The picker now opens inside a dialog when it's called from one, so it shows on top.
- Help's shortcut list gains rows for the four new drag combinations.

## 1.11.1 - 2026-09-29 - 3DEDTR joins the family

- **3DEDTR joins the family.** More apps and the splash's row of apps now include 3DEDTR (3dedtr.app), the new 3D modeling app with shape merging, ready for 3D printing, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js`.
- The splash's row now fits eight apps: the seven others on one line on a computer, and 4 + 3 on a phone (shared styles pasted in again from `_edtr-suite/suite-block.css`).

## 1.11.0 - 2026-09-29 - Magic wand

- **Magic wand (W)**, under the Eraser in the tool rail. Click an area of one color on a picture and it is erased - the white behind a logo, a flat background behind a screenshot.
  - **Tolerance** (0-100, default 20): how different a color may be and still be picked. Red, green, blue and see-through-ness are compared separately; the biggest difference counts.
  - **Contiguous** (on by default): only pixels touching the clicked area. Turn it off to pick every matching pixel in the picture, such as the white inside the letters "o" and "e".
  - **Soft edge** (0-8 px, default 1): blurs the cut edge so it is not jagged. Not available in Safari, which cannot blur inside a canvas; there the edge is sharp.
  - **Restore** mode, or **Alt (Option)+click**, brings the clicked area back.
- **Built on the eraser.** A wand click becomes part of the picture's eraser mask, so it mixes with brush erasing and Restore, flips and crops with the picture, and **Clear all erasing** undoes it.
- **Small projects.** Only the click is saved (point, tolerance, contiguous, soft edge), not the pixels. The original picture never changes, so the same click always picks the same area. Wand clicks in project files are checked when a project opens; malformed ones are dropped.
- The flood fill only looks inside the part of the picture that is shown (its crop).
- Help's shortcut list now calls Shift+E "Eraser tool" (it said "(images)", from before pen and highlighter could be erased).

## 1.10.1 - 2026-09-28 - VCTREDTR joins the family

- **VCTREDTR joins the family.** More apps and the splash's row of apps now include VCTREDTR (vctredtr.app), the new vector drawing app with PowerPoint-style shape merging, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js`.
- The row of apps on the splash is now an even grid (shared styles pasted in again from `_edtr-suite/suite-block.css`), so the six others fit on one line on a computer, and 3 + 3 on a phone.

## 1.10.0 - 2026-09-28 - Perfect shapes, more line ends, a real color picker

- **Clicking with a shape drops a perfect one.** Rectangle becomes a 160 px square and ellipse a 160 px circle. Shapes from the panel come out in their regular proportions (an even hexagon, an equilateral triangle); the speech bubble, arrow, pin and ribbon keep their usual look. Enter on the canvas does the same. Dragging still draws any size.
- **Resizing shapes** (rectangle, ellipse and every panel shape):
  - Corner handles keep the current proportions.
  - Side and top/bottom handles stretch freely.
  - Shift snaps to the perfect shape from any handle.
- **More line ends.** Lines and arrows now have **Start** and **End** rows, each with five choices: none, closed arrowhead, open arrowhead, closed circle and open circle. The line stops short of each end shape, so nothing shows through. Stored as `startCap` / `endCap`; older projects' `headStart` / `headEnd` still work, and unknown values in a file fall back to them.
- **New color picker** for every color in the properties panel and the canvas background (the square button before the swatches):
  - A saturation/brightness square (arrow keys, Shift for bigger steps) and a hue strip.
  - Boxes to type the color as **Hex** (the default), **RGB** (0-255) or **CMYK** (%). The format you choose is remembered.
  - An **eyedropper** in browsers that have one (Chrome and Edge).
  - Escape, clicking elsewhere or tabbing away closes it.
  - CMYK uses the simple screen formula, which is fine for matching a brand guide's numbers but not a colour-managed print conversion.

  The round swatches stay as one-click favourites. The New canvas and Settings dialogs still use the system picker.

## 1.9.0 - 2026-09-27 - Copy and paste layers

- **Ctrl+C / Ctrl+X / Ctrl+V (Cmd on a Mac) work on any layer.** Before, the keyboard only pasted pictures from the system clipboard. There was no copy for layers at all, only the Duplicate button (Ctrl+D).
  - Copies images, shapes, text, step markers (a pasted step becomes the next number), cursors, spotlights, redactions, magnifiers, several layers at once, or a whole group (pasted as a new group).
  - Each paste is nudged 20 px further down and right than the last, so repeated pastes fan out. Copies go just above the originals, or on top when the originals are gone.
  - Pictures come along in memory, so layers can be pasted into a different document opened later in the same tab.
  - Undo works as usual. Cut is copy + delete.
- **Whichever you copied last wins.** Copying layers replaces the system clipboard with a short note ("IMGEDTR layers..."). If you copy a screenshot afterwards, Ctrl+V pastes the screenshot. The layer data itself stays inside IMGEDTR: it is never read back from the clipboard, so nothing another app puts there is trusted as layer data.
- The toolbar **Paste** button also pastes copied layers when there is no picture on the clipboard.
- Typing in a text box or a field still copies and pastes text as normal.
- The shortcuts appear in Help > Keyboard shortcuts, with on/off switches like the rest.

## 1.8.0 - 2026-09-27 - Erase pen and highlighter, tidier choice buttons

- **The eraser works on pen and highlighter strokes**, not just images. Start a stroke on the ink to erase it; start on a photo next to it and the photo is erased, as before. The eraser checks the actual line, not the stroke's box. Restore brings ink back, and Alt swaps Erase and Restore, just as on images.
- **How it works:** a stroke is a list of points, not pixels, so it keeps its own list of eraser strokes and is drawn through a mask (stroke, then soft dabs cut out, then onto the canvas). The highlighter still multiplies over what is below. Eraser points are stored as fractions of the layer's box, like the stroke's own points. The gaps move, resize, rotate and flip with the stroke. Color, thickness and opacity stay editable, and **Clear all erasing** (in the pen or highlighter properties) restores the whole stroke.
- **Choice buttons fill their row.** Erase | Restore, Circle | Square, Solid | Pixelate and the other button rows now share the width of the properties column evenly, instead of leaving an empty stretch after the last button.
- **Safer project files:** when a project opens, eraser strokes on images, pens and highlighters are checked (known modes and shapes, real numbers, point pairs). Anything malformed is dropped, so a damaged file cannot break drawing.
- The tool rail tooltip now says "Eraser" rather than "Eraser for images".

## 1.7.1 - 2026-09-27 - Spotlighting more than one thing

- **Fixed: a second spotlight hole could hide the first.** Drawing a hole with no spotlight *selected* (the usual case once the first hole is done) made a whole new spotlight layer. That layer dimmed everything outside its own hole, including the first hole. Now a new hole joins the selected spotlight, or else the top visible, unlocked spotlight on the canvas. A new spotlight is only made when there is none. The same goes for pressing Enter on the canvas with the Spotlight tool.
- **Two spotlight layers now work together.** Each spotlight also cuts out the holes of every other visible spotlight, with each hole keeping its own spotlight's feather. Older projects that already have two spotlights look right now too. Where two spotlights overlap outside the holes, their dimming adds up (darker). For an even dim, keep every hole in one spotlight, which is now what happens by default.
- The Spotlight tool's hint now explains that more holes join the same spotlight.

## 1.7.0 - 2026-09-27 - Regular shapes, Pad contents, opacity in the layer bar

- **Regular shapes with Shift.** Holding Shift while drawing or resizing a shape keeps its *regular* proportions, not a square. A hexagon comes out with six even sides, so it turns in 60 degree steps and tiles like a honeycomb. The same goes for the triangle and warning sign (equilateral), pentagon and star (width = 2 sin 72 degrees : 1 + cos 36 degrees), and the square-bodied diamond, octagon and badge. Other shapes keep their usual proportions with Shift.
- **Make regular** button in the properties of those shapes. It keeps the center and width and fixes the height.
- Shape outlines now shrink the drawing by the same amount across and down, so a shape's proportions always match its box. A regular hexagon stays regular at any thickness.
- **Pad contents** (next to Fit contents) adds 10 px of canvas on every side; each click adds 10 more. **Fit contents, then Pad contents** gives an exact 10 px margin. The canvas tools grid now has an even ten buttons.
- **Opacity in the layer action bar.** A new % button, before Delete, shows the current opacity ("Mixed" if the selected layers differ). It opens a small panel with a horizontal slider and a number box (5-100%):
  - Arrow keys change either control. Enter in the number box applies and closes. Escape closes.
  - It applies to one layer, a multi-selection or a whole group.
  - It is turned off for locked layers, redactions (never see-through) and spotlights (their Strength does this).
  - The per-type Opacity sliders are gone from layer properties. The "new layer style" panel for a tool still has one, because there is no layer yet.

## 1.6.0 - 2026-09-27 - Shapes panel, resizable Layers pane, tool tooltips

- **Shapes panel.** The Rectangle and Ellipse buttons are now one **Shapes** button (shortcut **U**). It opens a panel of 22 shapes in three groups:
  - **Basic:** rectangle, ellipse, triangle, right triangle, diamond, pentagon, hexagon, octagon (stop sign).
  - **Symbols:** star, heart, check mark, X mark, plus, pound / hash sign, no sign (prohibited), warning sign.
  - **Callouts and awards:** speech bubble, block arrow, location pin, light bulb, award ribbon, badge / seal.

  The button shows the shape you picked last. **R** and **E** still choose the rectangle and ellipse straight away. In the panel, the arrow keys move between shapes, Enter picks one, and Escape closes it.
- **New shape layer type** (`shape`, with a `kind`). Each drawing is one SVG path in a 100 x 100 box. That path draws the canvas, the button picture and the click area, so the three always match. Clicking an unfilled shape only picks it on its outline, like rectangles do.
- **Signs start with their usual colors:** red no sign, yellow warning sign with a dark "!", blue award ribbon, green check, red X. The # sign uses your annotation color. Changing a sign's colors does not change the style of the next ordinary shape.
- **Shape properties:** a Shape menu that turns one shape into another, Flip horiz. / Flip vert. (for the speech bubble's tail or the right triangle), plus the outline, thickness and fill that rectangles have. Flipping the whole canvas mirrors shapes too.
- **Resizable Layers pane.** A grip under the layer list: drag it, or focus it and use Up/Down (Shift for bigger steps) and Home/End. Double-click it or press Enter to go back to automatic. The height is saved in settings and squeezed to fit when the window is smaller. It works in the phone's bottom sheet too.
- **Tool rail tooltips.** The slow browser tooltips are replaced with a shared bubble showing the tool and its shortcut. It appears after a short pause on hover, and straight away on keyboard focus. Escape hides it; touch never triggers it. The buttons also get `aria-keyshortcuts`. Shortcuts switched off in Help are not shown. The Shapes panel buttons use the same tooltips.
- Projects with an unknown shape kind open it as a star instead of failing.
- Fixed: the 1.5.0 update had rewritten the old 0.3.0 changelog note about the magnifier. History now says what 0.3.0 shipped (a round bubble).

## 1.5.0 - 2026-09-27 - Rectangular magnifier

- **Magnifier shape:** a new **Shape** switch (Circle / Rect) in the magnifier's properties. Pick it with the Magnifier tool active to set the shape for the next magnifier, or with a magnifier selected to change that one. The choice is remembered for the next one.
- **Rect** has a **Corners** slider (0 to 200) for rounded corners, and resizes freely (a circle still keeps its width and height equal). A new rectangle starts wider than it is tall, which suits a line of text or a toolbar.
- The outline around the spot being magnified, and the leader line's start and end points, follow the shape.
- Switching a rectangle back to a circle makes it square around its center, using the shorter side.
- Projects save the shape and corner size. Older projects, and anything unexpected in a file, open as round magnifiers.

## 1.4.0 - 2026-09-26 - Install, updates

- **Install IMGEDTR as an app.** An Install button appears in the top bar, and **Install app** on the splash, whenever the browser can install it (Chrome, Edge and friends, desktop and Android). On iPhone and iPad the splash explains Share, then Add to Home Screen; in Safari on a Mac, File, then Add to Dock.
- **Check for updates on the splash.** The foot of the splash shows the version and asks the server whether a newer one is out; when there is, **Update now** loads it. The question goes through the service worker (`sw.js` now answers a `suite-check-update` message), which fetches `index.html` with `cache: 'no-store'` and reads its `APP_VERSION`. Nothing else is sent.
- Dave Ghidiu's name in the credits now links to his website, daveghidiu.com.
- Shared SUITE block moves to v4 (`SuiteInstall`, `SuiteUpdate`, the author link).

## 1.3.1 - 2026-09-26 - Real icons in the family row

- More apps and the splash now show each app's real icon, instead of a simple drawing on a coloured square. The icons live in the shared block as `SUITE_MARKS` (data: URIs, so they work offline).

## 1.3.0 - 2026-09-26 - Splash, crash backups, credits, its own colour

- **Splash screen** at start-up: Open an image, Paste from clipboard or Blank canvas, with the rest of the family underneath. Skipped when a file is opened straight into the app (dropped, pasted, or from the desktop).
- **Crash backups.** While you edit, the document and its pictures are kept in this browser (IndexedDB). Exporting, copying the image or saving a project clears the backup, so one is only offered after a crash or a closed tab: as "Pick up where you left off" on the splash, and as a backup icon in the top bar (Restore / Discard / Not now). Restoring goes through the same checks as opening a project file.
- **Credits** in About: made by Dave Ghidiu with Claude, provided by FLX AI Hub and Finger Lakes Community College.
- **Its own colour: green** (`#305305`, 8.9:1 with white). The icon, wordmark, Export and the other main buttons, selection and focus all follow it; dark mode uses a lighter green (`#9bd66b`). `icon-192.png`, `icon-512.png` and the manifest's theme colour are redrawn to match.
- Shared SUITE block moves to v3 (each app's tile in its own colour).

## 1.2.1 - 2026-09-26 - Inspector sheet on phones

- **Phones and narrow windows:** the inspector (layers and properties) now opens as a sheet across the bottom of the screen, just above the tool rail, instead of a drawer sliding in from the right over the picture. The canvas shrinks to the top part and re-fits the picture, so you can see it while you change it. The sheet scrolls on its own.
- If you have zoomed or panned by hand, opening or closing the sheet keeps the same spot in the middle of the view instead of re-fitting.

## 1.2.0 - 2026-09-25 - Snapping and smart guides

- **Smart guides:** while you drag a layer (or a multi-selection or group), its edges and center snap to the canvas edges and center, and to the edges and centers of other visible layers. Pink guide lines show what it lined up with, and disappear when you let go.
- **Move freely:** hold Alt (Option on a Mac) while dragging to skip snapping for that move, or turn snapping off in Settings > "Snap to guides while moving". Shift still keeps a move straight across or down; snapping then works along that line only.
- Fixed: Shift or Ctrl/Cmd+pressing a layer and dragging now moves the selection (it only toggled the selection before). A Shift+click without dragging still adds or removes that layer.

## 1.1.1 - 2026-09-24 - Family alignment

- **More apps:** a fourth tab in the help panel lists the rest of the family (TXTEDTR, PDFEDTR, IMGEDTR, SNDEDTR, VIDEDTR, SCRNCSTR), with this app marked "You are here". Clicking the logo opens it directly. The list is the shared SUITE block, identical in every app.
- **Inspector button:** the family's sliders icon, placed before the theme button, shows or hides the layers and properties column on a wide screen. The phone drawer button uses the same icon and name.
- **Help button:** the family's ? icon replaces the "i" icon. F1 opens the panel as well as ?.
- The header cluster now follows the family order: Inspector, Theme, Help, Settings.

## 1.1.0 - 2026-09-24 - Phase 5: Multi-select and groups

- **Select several layers:** Shift or Ctrl/Cmd+click on the canvas or in the layer list; Shift+click a range in the list (Shift+Arrow from the keyboard); drag a box on empty canvas (it picks layers fully inside the box, so a full-size screenshot underneath is not grabbed); Ctrl/Cmd+A selects every visible, unlocked layer.
- **Work on them together:** drag to move; corner handles resize everything evenly (so text never squashes); the top handle turns them around their shared center (Shift = 15 degree steps). Nudge, duplicate, arrange (front/forward/backward/back) and delete all apply to the whole selection. One opacity slider sets them all.
- **Groups:** Ctrl/Cmd+G groups the selection; Ctrl/Cmd+Shift+G ungroups. A group is a folder in the layer list with a fold arrow, member count, show/hide and lock for all members, and rename (double-click, F2, or the Name field). Left/Right arrow keys fold and unfold from the keyboard.
  - Clicking any member on the canvas picks the whole group; double-click a member to edit it on its own (Escape leaves the group). Picking a member in the list does the same.
  - Drag a layer between two members (or just under an open group's header) to add it to the group; drag it anywhere else to take it out. Groups move as one block.
  - Bring forward/backward on one member keeps it inside its group. Duplicating a whole group makes a new group.
  - Groups are saved in projects; a group left with fewer than two members dissolves on its own.
- **Align and distribute:** align to each other (left, centers, right, top, middles, bottom), align to the canvas (also offered for a single layer), and space three or more layers evenly across or down.
- **Change:** dragging on empty canvas now draws a selection box instead of panning. Pan with Space+drag, the middle mouse button, scrolling, or two fingers on a touch screen.
- Fixed while testing: pressing Enter to finish renaming a group also folded it.
- Fixed: reopening a saved project added empty settings that were not in the file; projects now come back exactly as saved.

## 1.0.0 - 2026-09-24 - Phase 4b: Finishing touches

- **Canvas background, simplified:** the separate Transparent checkbox and Background swatches are now one Background row under Canvas tools. The first swatch (checkerboard with a red slash) means none/transparent, which is the default for pasted images. The background fills in behind every layer - for example the see-through corners of a tilted screenshot.
- **Image adjustments:** Brightness, Contrast and Saturation (-100 to 100) in Image properties > Adjust, with Reset adjustments. They use the browser's built-in filters where available and the same formulas pixel by pixel in Safari. Adjustments tilt, crop and erase along with the picture.
- **Alt text:** a field in the Export dialog, saved with the document. "Draft from text layers" starts a description from your text layers and steps; "Copy alt text" puts it on the clipboard for Brightspace's image description field. A gentle tip shows while it is empty.
- **Projects (.imgedtr):** Save project (header button or Ctrl+Shift+S) writes the document and its pictures to one file; open it with Open, drag-and-drop, or (in the installed app) "Open with". Everything stays editable - layers, crops, erasing, tilt, showcase, alt text. Undo history is not saved.
  - Opening treats the file like one from a stranger: every value is checked (layer types, numbers, colors, text lengths, picture format - PNG/JPEG/WebP only), prototype-pollution keys are refused, and nothing replaces the current canvas unless the whole file passes. Six kinds of broken or hostile files were tested and all are rejected with a clear message.
  - Saving a project that contains Redact layers asks first, because a project keeps the original pixels under each redaction. Exported images stay flattened.
  - Opening a project over unsaved work asks first.
- **Accessibility pass:** axe-core (WCAG 2.2 AA + best practices) reports zero issues across the start screen, canvas, image, step and spotlight panels, and the export and info dialogs, in light and dark themes. Fixes: the wordmark is now the page's level-1 heading, the tool rail is a named navigation landmark, and toolbar roles that promised arrow-key navigation were replaced with plain groups. A keyboard-only walkthrough (create, nudge, type, reorder, undo, delete, export) passes.
- The manifest now also registers .imgedtr files for the installed app.

## 0.4.0 - 2026-09-24 - Phase 4a: Tilt and Showcase

- **Perspective tilt for image layers** (Image properties > Perspective tilt): Left/right and Up/down, -60 to 60 degrees, on top of the normal rotation. Crop, erasing, rounded corners, border and shadow all tilt with the picture. The tilted picture is fitted inside the layer's box, so handles and selection behave as before. Reset tilt puts it flat again.
- The eraser works on tilted images - strokes are mapped back through the perspective onto the flat picture.
- Flipping a tilted image (or the whole canvas) mirrors its tilt too.
- **Showcase export** (Export dialog > Showcase): tilt left/right, tilt up/down and rotate the whole canvas - annotations included - round its corners, and place it on a gradient (two colors + angle), solid or transparent background with padding and a drop shadow. Live preview, presets (Table, Left, Right, Flat) and Reset. The size note shows the final size.
- Showcase settings are saved with the document and are part of undo/redo. While Showcase is on, Copy image copies the showcased version.
- Perspective is drawn with a small, commented per-pixel "homography" warp with bilinear sampling and soft edges - no WebGL, still zero dependencies. Results are cached, so only changed settings are redrawn.

## 0.3.1 - 2026-09-24 - Staging area, step numbers, circle holes

- **Staging area:** anything hanging off the canvas is now drawn around it, faded, instead of disappearing. You can click, move and edit it there. Only the canvas itself is exported. (Spotlights are the exception - they only ever cover the canvas.)
- **Step numbers you can type:** a Number field moves a step to that spot in the series; the other steps shift up or down to make room, so there are never duplicates or gaps. Earlier/Later still nudge one place at a time.
- **First number:** a series can start at any number (for example 5, when continuing from an earlier screenshot). Saved with the document, applies to every step, works with letters too (5 = E).
- **Circle spotlight holes:** Circle joins Ellipse and Rect. Circles stay round while drawing and resizing; switching an ellipse to Circle keeps its center. The hole shape can also be picked before drawing, in the Spotlight tool's panel.

## 0.3.0 - 2026-09-24 - Phase 3: Teaching tools

- **Step markers (N):** click to drop numbered circles; the tool stays on so you can place several in a row. Numbers follow the order you placed them (not the layer order), renumber automatically when one is deleted, and can be moved Earlier/Later. Styles: 1 2 3, A B C or a b c; color, number color, size and an optional white ring.
- **Cursor stamps (C):** 13 original vector cursors - arrow pointer, link hand, open hand, closed hand, I-beam, move, four resize directions, crosshair, not-allowed and a click burst. Default 64 px, fill `#0046ad` with a white outline and soft shadow, all adjustable. The cursor's tip lands exactly where you click.
- **Spotlight (S):** drag out holes (ellipse or rounded rectangle); everything outside is dimmed (color + strength) and/or blurred, with an adjustable feather. With a spotlight selected, new holes join it; Delete removes just the selected hole. Clicks on the dimmed area pass through to the layers below. New spotlights slot in just above the top image, so annotations drawn on top stay bright. Blur uses the canvas filter where available and a shrink-and-grow fallback in Safari.
- **Redact (X):** solid box (safest) or pixelate with blocks of at least 8 px, each a true average of its pixels. Always fully opaque; exports are flattened, so hidden details are not in the file.
- **Magnifier (M):** press on the spot to enlarge and drag to where the round bubble goes (a plain click places it up and to the right). Zoom 1.2x to 8x, border color and width, leader line, shadow. The bubble redraws the real layers zoomed in, so it stays sharp. A small handle moves the magnified spot.
- **Layer action bar:** duplicate, bring to front, forward, backward, send to back and delete now sit in a bar between the Layers list and Properties, greyed out when nothing is selected.
- Whole-canvas operations (crop, canvas size, resize, rotate, flip, fit) carry spotlight holes and magnifier spots along correctly.

## 0.2.1 - 2026-09-24 - Panel and layer list polish

- Layers panel moved above the properties panel, with a capped height, so the list stays put while properties change.
- Drag and drop to reorder layers: grab the grip (mouse or touch) or the layer name (mouse or pen). A blue line shows the drop spot, the list scrolls near its edges, and it is one undo step. Alt+Up/Down still reorders from the keyboard.
- App mark (picture frame with an orange pencil) beside the wordmark; icon-192.png and icon-512.png regenerated to match (512 is full-bleed, so it also works as a maskable icon).
- Removed the "This layer is locked" notice that pushed the properties panel down.
- Fixed: while a layer name had keyboard focus, the layer list swallowed every key, so Ctrl+Z and tool shortcuts did nothing.
- Fixed: pressed buttons (such as a locked padlock) turned light grey on hover, hiding their white icon.

## 0.2.0 - 2026-09-24 - Phase 2: Image tools

- Crop tool (K) for the whole canvas: drag the handles or draw a new box, aspect presets (Free, Original, 1:1, 4:3, 16:9, 3:2), portrait/landscape swap, exact width/height, rule-of-thirds guides. Enter applies, Escape cancels, arrow keys move the box.
- Per-layer crop for images (double-click an image, press Enter on it, or use Crop image). Works on rotated and flipped images, and is non-destructive: Reset crop brings the whole picture back.
- Eraser (Shift+E) for image layers: circle or square brush, size and feather, with a live outline. Restore mode (or hold Alt/Option) paints erased pixels back. Strokes are stored as points, so every stroke can be undone and nothing is ever destroyed. "Clear all erasing" removes it all.
- Image layer styling: rounded corners, border (thickness and color), drop shadow (softness, distance, strength). The last style used carries over to the next image you add to the canvas.
- Image layer actions: flip horizontal/vertical, original size (1 image pixel = 1 canvas pixel), reset crop.
- Canvas tools (shown when nothing is selected): canvas size with a 9-point anchor and padding presets, fit to contents, resize by percent or pixels, halve size, rotate left/right, flip horizontal/vertical. Text stays readable when the canvas is flipped.

## 0.1.0 - 2026-09-24 - Phase 1: Foundation

- Start screen with Paste, Open (or drag-and-drop) and Blank canvas (size presets, background color or transparent).
- Opening or pasting into the empty app sizes the canvas to the image; later images arrive as new layers, centered and scaled to fit.
- iPhone HEIC/HEIF photos convert to PNG on the device. Safari's built-in decoder is used when available; otherwise the `heic-to` 1.5.2 library (libheif in WebAssembly) loads on first use from jsDelivr, pinned with a Subresource Integrity hash, and is cached for offline use.
- Images over 8000 px on a side are scaled down on load, with a notice. Files over 150 MB are refused.
- Every layer can be moved, resized and rotated (rotate handle with Shift for 15-degree steps, plus a numeric angle). Resizing works correctly on rotated layers.
- Layer list: select, reorder (buttons, `[` `]`, Alt+Up/Down), show/hide, lock, rename (double-click or F2), duplicate, delete.
- Tools: arrow, line, rectangle, ellipse, text, pen, highlighter. Clicking without dragging places a sensible default (a click with the arrow tool points the arrow at that spot).
- Text layers: multi-line, four font styles, size, bold, italic, alignment, color, optional background box with padding. Double-click to edit in place; resizing scales the font.
- Properties panel: position, size, rotation and style for the selected layer; the last style used becomes the default for the next layer of that type.
- Undo/redo (200 steps), zoom and pan (buttons, Ctrl+scroll, trackpad pinch, two-finger touch pinch, Space+drag).
- Export PNG, JPEG or WebP with quality and scale; copy to clipboard. Metadata (including GPS) is always stripped.
- Keyboard: every tool and action has a shortcut, each can be switched off in Info > Keyboard shortcuts; Enter on the canvas inserts the current shape for keyboard-only use.
- Light/dark themes, responsive phone layout, installable PWA with offline support, Content-Security-Policy that blocks the page from sending data anywhere.
