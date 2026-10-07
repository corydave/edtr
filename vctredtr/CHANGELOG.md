# VCTREDTR Changelog

Newest first. The short form of each entry also lives in the `CHANGELOG` table inside `index.html` (shown in the app's Help > Changelog tab). Add new releases to both.

## 0.11.3 - 2026-10-03 - Links to the other apps

- Names of the other apps in Help (in the changelog, About and the guides) are now links that open that app. Each link opens in a new tab; this app's own name stays plain. Shared SUITE block: new `suiteLinkApps()` (called from `renderSuiteApps()`, so no app wiring needed).

## 0.11.2 - 2026-09-30 - A quieter "o", and a guard for installing

- **Opened from a file, the version badge shows a small "o"** (for offline) instead of the word "offline", so nobody wonders why this app says offline when no other app in the family does. Hovering it explains.
- **`build-offline.py` now refuses to make an `index.html` that could not be installed:** it checks that the manifest link, the icon links and the service worker are all there. (The one-file editions made on 2026-09-30 before 0.10.1, as `vctredtr-offline.html`, had the manifest taken out, which is why a copy made from one of them cannot be installed.)

## 0.11.1 - 2026-09-30 - GAMEDTR on pause

- **GAMEDTR is out of the More apps list and the splash for now,** so the family is back to eight apps (the shared block pasted in again from `_edtr-suite`, the same copy the other apps carry: splash 620px wide, 4 + 3 on a phone).

## 0.11.0 - 2026-09-30 - Curved text, more shapes, repeats, outlines and pictures

- **Curved text.** A **Curve** slider in the Text section, -100 to 100: above 0 bends the words into an arch, below 0 into a smile, and 100 takes them all the way round a circle (badges, seals, a word round a logo). Each line follows the same circle, like rings. Letter spacing works with it. It shows on the canvas, in PNG and SVG exports (each letter placed and turned, so any app shows it the same), and **Turn into shapes** and **Merge Shapes** keep the curve exactly. While you type, the words show straight.
- **More shapes: the Shapes tool (U),** after the Shield on the tool rail, with twelve: heart, arrow, double arrow, chevron, speech bubble, speech box, cloud, lightning bolt, crescent moon, cross, ribbon banner and map pin. It works like the Shield: click the button for the gallery, and the button shows the one you picked; a click draws one in its natural proportions, a drag stretches it, Shift+drag keeps its proportions; the Inspector swaps a drawn one for another. Shapes are named after what they are ("Heart 1").
- **Repeat around a centre,** a new Inspector section for anything picked: **Copies** (2 to 72), **Distance** from the selection to the circle's centre (it starts at the selection's larger side), and **Turn copies** (face out, like petals, or stay upright). The selection stays at 12 o'clock and the copies go round from it, all picked afterwards, so Union makes a flower, a sunburst or a gear in one press. One undo step.
- **Outline to shape,** in the Outline section: a line, a pencil squiggle or any outline becomes a filled shape of exactly the same look, ends and corners included (round, square or flat ends; round, sharp or flat corners). A filled shape with an outline keeps its inside, with the outline as a separate shape on top. Dashes become one solid band.
  - **Merge Shapes now takes lines too:** it turns them into shapes first, like text, in the same undo step.
- **Pictures.** Open, drop or paste a PNG, JPEG, WebP or GIF (a screenshot, say) to place it on the artboard.
  - **Clip to top shape** (in Align and arrange): pick the picture (or anything) and a shape or text on top of it, and the rest shows only inside that shape - a photo inside a circle, a shield or a word. It becomes one group; **Unclip** (or Ungroup) takes it apart and gives the shape its colours back.
  - To trace a picture: lower its opacity, lock it, and draw over it with the Pen.
  - Privacy: every picture is redrawn onto a fresh canvas before it goes in, which leaves behind the hidden details photos carry (camera, date, GPS location). Big pictures are shrunk to 2048 px across so projects stay a sensible size. Photos are kept as JPEG, pictures with see-through parts as PNG.
  - A project may only contain pictures stored inside it; one that points at a file or website elsewhere is refused.
- **Several lines of text export properly** in SVG now, one line under another. (Before, the lines ran together into one.)
- **The More apps list and the splash include GAMEDTR,** the ninth app (the shared block pasted in again from `_edtr-suite`).

## 0.10.1 - 2026-09-30 - The one-file edition becomes the main one

- **`index.html` is now the one-file edition** (the drawing engine, opentype.js and every font inside) and is what vctredtr.app serves. On the website it installs, opens offline and checks for updates as before; copied to a USB stick or opened from a file it works with no internet at all, and says "offline" beside its version.
- **The edition that loads its parts from the internet is now `index-online.html`,** and it is the source: edit it, then run `build-offline.py` to make `index.html`. (Before, the one-file edition was `vctredtr-offline.html`.)
- The service worker keeps each page under its own name, so opening one edition never replaces the stored copy of the other.

## 0.10.0 - 2026-09-30 - Letter spacing, and a calmer Inspector

- **Letter spacing** for text: a slider in the Text section, as a percentage of the font size (like Figma), so it grows with the text. The slider runs from -20 (letters squeezed together) to 100 (spread out); the number box takes -50 to 200. 0 is normal.
  - It shows everywhere: on the canvas, in the typing box while you edit, in PNG and SVG exports (as SVG's `letter-spacing`) and in the SVG code view.
  - **Turn into shapes** and **Merge Shapes** keep it: the letter outlines are laid out with the same gaps.
  - It is saved with the text in projects, and undo, copy and paste keep it.
  - Browsers that can space canvas letters themselves (Chrome, Edge, newer Safari and Firefox) do; older ones get each letter placed by the app, so it works there too.
- **The Inspector's sections start closed,** so there is less to take in at once: just the headings (Merge Shapes, Position and size, Fill, Outline...). Open the ones you use and they stay open, from one shape to the next and the next time you open the app (remembered in this browser).

## 0.9.0 - 2026-09-30 - Merge text with shapes, Pad contents, and an offline edition

- **Merge text with shapes,** the heart of most logos. Pick some text and one or more shapes and press any Merge Shapes button: the text is turned into shapes first (each letter's real outline, holes and all), then merged, as PowerPoint does it. Cut a word out of a shield, join letters to a star, fragment a word into pieces. It is one undo step, and if the merge leaves nothing, the text is put back.
  - **Turn into shapes** (a button in the Text section, or Ctrl+Shift+O) does just the first part: the text becomes a shape called "Text 1 shapes" with the same colour, gradient and outline, ready for Edit points or for use in any other app.
  - The letters come from the font files, read by **opentype.js** (pinned and fingerprint-checked like Paper.js, and only downloaded the first time). So it works with the 27 **included** fonts; the five built into the computer (Sans, Serif, Mono, Rounded, Impact) cannot be read by a web page, and the app says so. Rockwell turns into Arvo, its stand-in.
  - **New text now starts in Montserrat** (bold), one of the included fonts, instead of the computer's own Sans, so it looks the same everywhere and can always be merged.
  - The fonts are now `.woff` files instead of `.woff2` (opentype.js cannot read WOFF2). They are saved for offline use again, once.
- **Pad contents,** in the Artboard section (as in IMGEDTR): the artboard becomes the size of the drawing plus the same margin on every side. The margin box beside it starts at 10 px, can be anything from 0 to 2000, and is remembered. Outlines count, so a thick outline is not cut off. Enter in the box pads straight away.
- **An offline edition:** `vctredtr-offline.html`, the whole app in one file (about 2 MB) with the drawing engine, opentype.js and every font inside. It runs from a USB stick, an email attachment or a double-click, with no internet at all, and exports still carry their fonts. `build-offline.py` makes it from `index.html` (run it after each change, as with PDFEDTR). It shows "offline" beside the version, and its rule book allows no outside addresses.
- **On a phone, the top bar fades** at whichever edge has more buttons past it (Export, Help and Settings are off to the right at first), so it is clear it swipes sideways.

## 0.8.1 - 2026-09-29 - 3DEDTR joins the family

- **3DEDTR joins the family.** More apps and the splash's row of apps now include 3DEDTR (3dedtr.app), the new 3D modeling app with shape merging, ready for 3D printing, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js`.
- The splash's row now fits eight apps: the seven others on one line on a computer, and 4 + 3 on a phone (shared styles pasted in again from `_edtr-suite/suite-block.css`).

## 0.8.0 - 2026-09-29 - Many more fonts

- **27 new fonts**, so the Font box now has 32, grouped:
  - **Built into this computer** (as before): Sans, Serif, Mono, Rounded, Impact.
  - **Sans serif:** Atkinson Hyperlegible, Montserrat, Poppins, Comfortaa, Fredoka, Oswald, Anton, Bebas Neue.
  - **Serif:** Playfair Display, Merriweather, Abril Fatface.
  - **Slab serif:** Rockwell, Arvo, Coustard, Alfa Slab One, Holtwood One SC.
  - **Display:** Bangers, Bungee, Luckiest Guy, Righteous, Lobster, Press Start 2P.
  - **Handwriting and marker:** Permanent Marker, Pacifico, Caveat, Dancing Script, Indie Flower.
  - **Monospace:** Space Mono.
- **A sample line** under the Font box shows the text's own words (or a sample sentence) in the chosen font. Arrowing through the fonts updates it and the drawing as you go.
- **The fonts ship with the app,** in a new `fonts/` folder (about 1 MB): free, open-licence fonts from the Google Fonts collection, with every licence in `fonts/LICENSES.txt`. They load from the app's own address, so no font service learns who is drawing what, and they are saved for offline use when the app installs, in a store that app updates leave alone.
- **Exports keep the fonts.** PNG export, Copy as PNG (and Ctrl+C into Slides) and exported SVG files carry the fonts their text uses, so the text looks the same on any computer. The SVG code view leaves them out, to stay short.
- **Rockwell** is a paid font, so it cannot ship with the app. Macs and Microsoft Office have it; on other computers Arvo, a close free cousin, shows instead (the Inspector says so when Rockwell is picked).
- **Bold is real or off.** Fonts with only one weight (Anton, Bangers, Bungee and others) switch the Bold box off, with a note, rather than letting the browser fake a bold by smearing the letters. Coustard's bold is its extra-heavy 900.
- Text is measured again once its font arrives, so its selection box fits the real letters.

## 0.7.0 - 2026-09-29 - Drag layers into a new order

- **Drag to reorder** in the Layers list. Each row now starts with a dotted grip: press it and drag, and a violet line shows where the row will land. With a mouse or pen, dragging the name works too (a click still picks it, because the drag only starts after the pointer moves a few pixels). On a phone or tablet, use the grip; a finger on the name still scrolls the list.
- **Picked rows move together:** drag one picked row and every picked shape comes along, keeping their order. Dragging a row that is not picked moves just that one and leaves your selection (and its pick order for Merge Shapes) alone.
- Near the top or bottom edge the list scrolls, Escape cancels a drag, and each drop is one undo step. The top of the list is drawn on top, so dropping a row higher brings the shape forward. Alt+Up/Down on a row still does the same from the keyboard.

## 0.6.0 - 2026-09-29 - Shields

- **A Shield tool** (D), on the tool rail after the Star, with nine styles: Classic, Heater, Pointed, Round, Arched, Dipped, Notched, Peaked and Scalloped.
- **Click the shield button** and a flyout of the styles opens beside it (above it on a phone), like PowerPoint's shape gallery. Pick one and it closes; the rail button then shows the style you picked, and a small corner triangle says there is more inside. From the keyboard: Enter on the button opens it, the arrow keys move between styles, Enter picks, Escape closes. D picks the Shield tool; D again opens the styles.
- **Drawing:** a click drops a shield in its natural proportions (about 5 wide to 6 tall); a drag stretches it; Shift+drag keeps its proportions.
- **Shields stay live:** with a shield selected, the Inspector's Shield section shows the same styles, and picking one swaps the outline while keeping its size and place (one undo step). Editing its points or merging it makes it a plain path, like the other shapes. Shields merge like any filled shape: a star subtracted from a shield makes a badge.
- A style name read from a project file is checked against the app's own list; anything it does not know opens as Classic.

## 0.5.0 - 2026-09-28 - Proportional corners, Pick several in the Inspector, no invisible shapes

- **Corner handles keep the proportions.** Dragging a corner scales the shape evenly, so a square stays square and a perfect hexagon stays perfect. Side, top and bottom handles stretch in one direction. Hold **Shift** on a corner to stretch freely (the opposite of before). Alt still resizes from the middle.
- **Pick several in the Inspector.** A **Pick several** button now sits on the Layers heading (shown once there are two or more shapes), with a hint while it is on: tap rows to add them, tap again to take one out. It is the same setting as the two-squares button on the tool rail, so on a phone you can build a selection without leaving the Inspector.
- **No more invisible shapes.** New shapes still follow the last look you picked, but if that look has no fill and no outline, a new shape would be invisible: it was there, but you could not see it. Now it gets its fill back, and a message says why. With nothing selected, the Inspector's Fill section warns about it too. An outline-only style still makes outline-only shapes.
- **Family:** the row of apps on the splash is an even grid (six on one line on a computer, 3 + 3 on a phone), from the shared styles. PDFEDTR 1.7, IMGEDTR 1.10.1, SNDEDTR 0.7.1, VIDEDTR 3.17 and SCRNCSTR 1.20.1 now carry the shared block with VCTREDTR in it, and TXTEDTR 1.13 lists it in More apps.

## 0.4.0 - 2026-09-28 - Copying that works on a Mac and in Slides, and a resizable Layers pane

- **Fixed: Ctrl+drag did not copy on a Mac.** On a Mac, Ctrl+click is the system's right-click, so the browser reports the right mouse button, and 0.3.0 ignored anything but the left button. Ctrl+click is now read as a normal click with Ctrl held. (0.3.0 was only tested on Linux, where this does not happen; the tests now also run as a Mac browser.)
- **Option+drag copies too** (Alt+drag on Windows and Chromebook), the usual Mac way in Keynote, Figma and Illustrator. A plain Option+click just picks the shape. Alt still means "move without snapping" when you press it after a drag has started; an Alt-dragged copy still snaps onto the original's corners, for tiling.
- **Ctrl+C copies a picture.** Before, it put SVG code on the clipboard, so Google Slides pasted the code as text. Now the clipboard gets a see-through PNG of the selection at 2x, the same as Copy as PNG.
  - Pasting back into VCTREDTR still gives editable shapes with every detail: the app remembers the exact size of the picture it made, and a pasted picture of that size is taken to be its own.
  - **Ctrl+Alt+C** copies the SVG code instead (the selection, or the whole drawing with nothing selected).
  - Browsers that cannot put a picture on the clipboard get the SVG code, with a message saying so.
- **Resizable Layers pane**, the same grip as IMGEDTR: drag the handle under the layer list, or focus it and use Up/Down (Shift for bigger steps), Home/End. Double-click or Enter goes back to automatic. The height is saved in this browser.

## 0.3.0 - 2026-09-28 - Ctrl+drag to copy, and a wigglier Pencil

- **Ctrl+drag copies** (Cmd+drag on a Mac), like PowerPoint: press Ctrl on a shape and drag, and a copy comes with the pointer while the original stays where it was.
  - If the shape is part of the selection, the whole selection is copied; otherwise just that shape.
  - A Ctrl+click that does not move still adds the shape to the selection or takes it out, as before. (The app waits for the first movement to tell the two apart.)
  - The copy and the move are one undo step. Escape during the drag cancels both.
  - The originals' corners count for corner snapping, so a Ctrl+dragged perfect hexagon locks onto the one it came from: tiling is click, then Ctrl+drag, Ctrl+drag...
- **Pencil options** (the Pencil tool, B, was already the freehand tool; it now says so in its tooltip). While it is picked, the Inspector shows:
  - **Smoothing**, 0 to 100 (default 25, the old fixed amount). It is how far, in screen pixels (0 to 10), the finished curve may drift from your hand. 0 keeps every wiggle and squiggle exactly as drawn.
  - **Close loops**: on (the default, as before), ending near where you started makes a closed, filled shape; off, it always stays a line.
  - Both are saved in this browser's settings.

## 0.2.0 - 2026-09-28 - Perfect shapes, and tiles that fit together

- **A click makes a perfect shape.** With a shape tool, a click on the canvas (or Enter, from the keyboard) now makes a square, a circle, or a polygon or star with every side the same length and every corner the same angle. Before, polygons and stars were stretched to fill a square box, so a hexagon's sides were not equal. A hexagon dropped this way has six 108 px sides and six 120° corners.
- **Dragging is unchanged:** a drag stretches the shape to the box ("all bets are off"). **Shift+drag** keeps it perfect.
- **Perfect stays perfect.** Changing a perfect polygon's sides or a star's points keeps it perfect, with the same centre and size. Resizing with Shift on a corner keeps it perfect too. Stretching it (different amounts across and down) turns "perfect" off, the Inspector says so, and **Make regular** puts it back.
- **Corner snapping, for tessellating.** While you move shapes, each of their corners is checked against every other shape's corners; one that comes within a few screen pixels locks on exactly, and a pink ring shows where. Two perfect hexagons dropped side by side share an edge exactly: no gap, no overlap. Corner snapping wins over the edge-and-middle guides; Alt moves freely, and Settings > Snap to guides turns both off. The other corners are sorted into a grid when a drag starts, so it stays quick with many shapes.
- Stored as `regular: true` in a polygon's or star's `data.shape`. Older drawings open as stretched shapes, so nothing changes shape by itself; press Make regular on any you want perfect.

## 0.1.1 - 2026-09-28 - Moving shapes, and picking several on touch screens

- **Fixed: dragging a shape did not move it.** Every drag to move failed (on any screen, whether or not shapes overlapped), because the code asked Paper.js's Rectangle for a `translate` method it does not have. Resizing, turning and box-picking were not affected. The tests for 0.1.0 moved shapes by calling the code directly instead of dragging, which is why they missed it; the tests now drag with a mouse and with touch.
- **Pick several** (new toggle on the tool rail, after Edit points; shortcut M): the touch-screen way to Shift+click.
  - While it is on, each tap adds a shape to the selection or takes it out, on the canvas and in the Layers list, in Select and in Edit points.
  - A tap on empty canvas keeps what you picked (so a stray tap does not lose them); dragging a box on empty canvas adds what it touches.
  - It switches itself off after a merge.
- The Merge Shapes hint (and the Help tab) explains Pick several on phones and tablets instead of Shift+click.

## 0.1.0 - 2026-09-28 - First build

- **Merge Shapes**, the reason the app exists, like PowerPoint's feature of the same name:
  - **Union** joins shapes into one outline. **Combine** joins them but cuts out where they overlap. **Fragment** breaks them into separate pieces at every overlap. **Intersect** keeps only the part where they all overlap. **Subtract** keeps the first shape and cuts the others out of it.
  - Pick order matters: click the first shape, then Shift+click the others. The first shape gives the result its look. Numbered badges on the canvas and in the Layers list show the order.
  - One difference from PowerPoint: Fragment pieces keep the colour each piece already showed (the top shape at that spot), so the picture looks the same and the pieces can be pulled apart.
  - Five buttons at the top of the Inspector (each with a picture of its result), Alt+Shift+U / C / F / I / S, and a Merge Shapes tab in Help that explains each one.
  - Works on filled shapes (rectangles, ellipses, polygons, stars, closed pen and pencil shapes, and earlier merges). Lines, text and groups are left out, and the toast says so.
- **Tools:** Select (V), Edit points (A), Rectangle (R, with rounded corners), Ellipse (O), Polygon (Y, 3-24 sides), Star (S, 3-40 points and an inner size), Line (L), Pen (P: click for corners, drag for curves, click the first point to close), Pencil (B: freehand, smoothed; ending where you started makes a closed shape), Text (T), Eyedropper (I: copy one shape's look to the selection, or to new shapes) and Hand (H).
  - A click with a shape tool drops a shape of a set size; Shift keeps it square, Alt draws from the middle. Enter on the canvas adds one in the middle of the view, so drawing works from the keyboard.
  - Rectangles, polygons and stars stay "live": their corners, sides and points can be changed in the Inspector until their points are edited or they are merged.
- **Edit points:** drag points and curve handles (smooth points keep their handles in line; Alt breaks them), double-click the outline to add a point, Alt+click or double-click a point to switch smooth/corner, Delete removes points, arrow keys move them, drag a box to pick several.
- **Select:** move, resize from 8 handles (Shift keeps proportions, Alt from the middle), turn (Shift: 15-degree steps), drag a box to pick, Shift/Ctrl+click to add. Smart guides snap to the artboard and other shapes (pink lines); Alt moves freely. Optional grid and grid snap in Settings.
- **Inspector:** Layers list (show/hide, lock, rename with F2 or a double-click, Up/Down to move between rows, Alt+Up/Down to change the order), an action bar (duplicate, order, group/ungroup, delete), and fold-open sections: Merge Shapes, Position and size (X, Y, W, H with an optional proportion lock, rotation, turn 90°, flip), Shape, Text, Fill (solid, linear or radial gradient, opacity), Outline (colour, thickness, solid/dashed/dotted, ends, corners), and Align and arrange (align, space out evenly, group). With nothing selected it shows the artboard and the style for new shapes.
- **Colour picker:** the same picker as IMGEDTR (saturation/brightness square, hue strip, Hex/RGB/CMYK boxes, eyedropper in Chrome and Edge), plus the family's quick swatches.
- **Artboard:** New drawing starts at 16:9, 1920 x 1080, see-through. Pick a size offers slide, square, app icon, social, portrait, letter and banner sizes. Fit to drawing trims the artboard to what is drawn.
- **Export:** PNG at 1x to 4x (see-through unless the artboard has a background) or SVG, of the whole artboard or just the selection. A title and description go into the SVG for screen readers, and Copy as alt text copies them for a PNG. **Copy as PNG** (Ctrl+Shift+C) puts the selection, or the whole artboard, on the clipboard at 2x, ready to paste into Google Slides or PowerPoint.
- **SVG code view** (the </> button, Ctrl+Shift+K): the code behind the drawing, updating as you draw, with Copy code.
- **Files:** open SVG files (cleaned by an allow-list first), paste SVG code, save and open `.vctredtr` projects (checked before opening), copy and paste shapes (the clipboard also gets them as SVG code).
- **Family standard:** splash with New / Pick a size / Open and the rest of the family, crash backups (offered only after a session that ended without an export or save), the backup icon, Help with Keyboard shortcuts (each can be switched off), Merge Shapes, About, Changelog and More apps tabs, theme button, Inspector button, Install button and update check, installable and offline.
- **Accessibility:** zero automated WCAG 2.2 AA issues (axe-core) on the splash, the editor, Help and Export, in light and dark themes. The whole workflow works from the keyboard.
