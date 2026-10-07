# DSKEDTR changelog

## 0.13.0 - 2026-10-07

- **Inspector button** in the top bar (three sliders, before Theme and
  Help, as in the other apps): hides or shows the right-hand column, so
  the page gets the room. A dot on it means something is picked while it
  is hidden. Remembered in this browser. The Accessibility button opens it
  again when needed.
- **Opacity** for pictures, shapes and lines: Look, Opacity (5 to 100%).
  It is see-through on the desk, in the PNG and in the PDF.
- **Drop shadows** for pictures, shapes and lines: Look, Drop shadow, with
  how far across and down, softness, strength and colour. A shadow falls
  the same way however the object is turned. In the PDF the object stays
  sharp and its shadow is a soft picture underneath (PDF has no blur).
- **Pictures in any shape:** Picture, Frame shape, "Choose a shape..." opens
  the Shapes gallery (without the lines) and cuts the picture to a heart, a
  star, a shield or any other closed shape. Crop and Fill still work; clicks
  outside the shape miss it; text wrap follows it.
- **Rounded corners for pictures** are now in Picture, beside the frame
  shape (they were hidden under Look).
- **Locking**, easier to find: a Lock button in Arrange and Ctrl+Shift+L
  (Cmd+Shift+L), as well as the padlock in Layers. Clicking a locked thing on
  the page now says how to unlock it, and clicking something that belongs
  to a master page says where to change it. Layers has "Unlock everything on
  this page" when anything there is locked.
- Project files are now version 7.

## 0.12.1 - 2026-10-06

- The Units, grid and guides panel now hangs from the arrow that opens it
  (beside Guides in the top bar), like any menu, instead of sitting over
  the right-hand column. It stays inside the window, and on a phone it
  follows the arrow when the top bar scrolls sideways. It still stays open
  while you drag guides; the arrow, its X or Escape closes it.

## 0.12.0 - 2026-10-06

- **Master pages:** things that show on many pages at once, like a
  masthead, a footer or page numbers. The new Master pages button (under
  the page buttons, beside the filmstrip) lists the masters instead of the
  pages; edit one like any page, with a banner saying which. The add, copy
  and delete buttons work on masters while they show. A master's things
  are drawn behind each page's own, print on every page that uses it, and
  can only be changed on the master.
- **Which pages use which master:** in Document (nothing picked), "Master
  page for page 3", with "Use it for every page". A new page uses the same
  master as the page before it. The filmstrip marks each page with its
  master. A master can hand **even pages** to another master (Master page,
  "On even pages, use"), for left- and right-hand pages.
- **Page numbers:** in a text box, Insert, Page number (or Ctrl+Alt+Shift+N,
  Cmd+Option+Shift+N on a Mac) and Number of pages. On a master they show
  as #; each page shows its own number, as real text in the PDF. Master
  page, "Add a page number" puts a footer box with one at the bottom.
- **"Continued on page 3" and "Continued from page 2":** two choices in
  Text flow for a text box whose story runs onto another page. The line
  appears only when the text really does come from, or go on to, a box on
  another page, in the Caption style in italics, and keeps its page number
  right as pages move.
- The sample newsletter has Master A, with a footer rule and "Page 1 of 2",
  and its main story says where it continues.
- Text never flows between a master and a page; master text is reached
  with Tab only while that master is showing; the Accessibility checker
  checks masters' pictures and shapes for alt text too.
- Project files are now version 6.

## 0.11.0 - 2026-10-06

- **115 shapes, in sections like Publisher's** (the Shapes tool, U, then U
  again or a second click for the gallery): Recently used, Lines, Basic
  shapes, Block arrows, Flowchart, Callouts, Stars and banners, Shields and
  Signs and symbols. The gallery is a grid of small pictures; the name of
  the one under the pointer or focus shows below it (and every button is
  named for screen readers). Arrow keys move around it (up and down by
  rows, across sections), Home and End jump to the ends.
- **The nine shields from VCTREDTR**, with exactly the same outlines:
  Classic, Heater, Pointed, Round, Arched, Dipped, Notched, Peaked and
  Scalloped.
- **New lines:** Arrow line and Double arrow line (drawn from where the
  drag starts to where it ends; Shift for 45 degrees), plus curves, an arc,
  an elbow, a wavy line, a zigzag, brackets and braces (outline only).
- **Arrowheads on any line:** Look, Arrowheads: none, at the end, at the
  start, or both. They grow with the line's thickness and print in the
  PDF and PNG.
- New basic shapes (trapezoid, heptagon to dodecagon, pie, teardrop, arch,
  half frame, L-shape, plaque, snipped and folded corners, cylinder, cube,
  ring, "no" sign, smiley face), block arrows (four directions, up-down,
  four-way, notched, striped, pentagon, bent and U-turn), 25 flowchart
  shapes, more callouts (square, pointing left, thought bubble), more
  stars (4 to 32 points, an explosion) and banners (wave, double wave),
  and symbols (sun, check mark, X mark, house, gear).
- A click without a drag makes a shape at its own proportions, fitting a
  1.5 inch square, so a bracket comes out tall and thin.
- A line from the gallery can be picked by clicking on the line itself.
- Recently used shapes are remembered in this browser only.
- Project files are now version 5 (lines can have arrowheads).

## 0.10.0 - 2026-10-06

Phase 2 begins: text wrap.

- **Text wrap** for any picture, shape or line: pick it, open Text wrap in
  the Inspector, and choose how text goes around it:
  - **No wrap** (as before): text runs over or under it.
  - **Around its box.**
  - **Tight**, around its shape: an ellipse, a star, a merged shape, or,
    for a **PNG with a see-through background, around what shows** (the
    see-through part is left out). A JPEG photo has no see-through parts,
    so tight follows its frame.
  - **Above and below only**: nothing beside it.
  - **Distance from the text**, in the units you use (1/8 inch to start).
- A line goes on the wider side of what it wraps around, never on both
  sides at once (easier to read), and needs room for about six letters;
  where there isn't, or a word would have to be cut in two, the text
  carries on below.
- Picked objects show their wrap: a dashed outline (traced, for a PNG)
  with a pale band as wide as the distance.
- A wrap never pushes text out of a box that sits entirely on top of it,
  so a coloured panel can wrap the column beside it and still hold its
  own text.
- Works with turned text boxes, linked boxes, undo, copy and paste, saved
  projects (now version 4), the PDF and the PNG.
- Fixed: fields with units in their labels (Rounded corners, Distance,
  column Gap, Page setup's Width and Height) showed the label broken over
  three lines.

## 0.9.0 - 2026-10-06

- **Nine more fonts, built in** (all free, SIL Open Font License), each
  with bold and italics unless noted: Andika (made for beginning readers),
  Lexend (made for easy reading; no italics), Comfortaa (rounded; no
  italics), Comic Neue (casual), Literata (serif for long reading),
  Fraunces (headline serif), Zilla Slab (friendly slab), Archivo Black
  (big, blocky headlines; one weight) and Atkinson Hyperlegible Mono.
  Atkinson Hyperlegible stays the default. Pick one for a paragraph style
  (Paragraph, Font, with a sample line) or for any words (Characters,
  Font). Fonts load the first time they are used, so the app still starts
  quickly. A font without bold or italics uses the nearest style it has,
  and Characters says so.
- **Your own fonts:** add .ttf, .otf or .woff files (Document, "Add font
  files...", the end of either font list, or drop them on the page). They
  are grouped into families by the name inside them and saved inside the
  project, so it opens the same anywhere. Each file is checked first (a
  real font, at most 15 MB, 40 per document); WOFF2 and font collections
  can't be read yet, and DSKEDTR says so. Remove one from Document: words
  using it go back to Atkinson Hyperlegible (one undo step).
- **Font licences are respected in PDFs.** A font file says whether it may
  be put inside documents. One that says no is drawn as shapes in the PDF
  instead of being embedded, and both the font list and the Accessibility
  checker warn that its text can't be selected, searched or read aloud
  there.
- The checker suggests a reading font when Body or Caption text is in a
  headline font (Archivo Black).
- Project files are now version 3 (they can carry fonts). Older versions
  of DSKEDTR will refuse them; this version opens the older ones.
- The one-file app is about 3.1 MB now (the fonts are about 0.8 MB of it).

## 0.8.0 - 2026-10-06

Milestone 6, the last of phase 1: formatting inside a paragraph.

- **Bold, italic and underline** for any words: Ctrl+B, Ctrl+I, Ctrl+U
  (Cmd on a Mac), or the new **Characters** section of the Inspector while
  typing. With nothing highlighted, they set how the next letters you type
  look. Bold off in a heading makes words NOT bold there. Italics are the
  real Atkinson Hyperlegible italics, not slanted letters.
- **Colour and size** for any words, in Characters, with the contrast
  against white paper shown right there. A line grows to fit its biggest
  letters. "Style's" puts the paragraph style's colour back.
- **Links:** highlight words, press Ctrl+K (or use Characters), type an
  address and press Enter. "flcc.edu" becomes https://flcc.edu and an
  email address becomes a mailto: link; anything that isn't a web, email
  or phone address is refused. Links are always underlined (so they never
  rely on colour alone), and in the PDF they can be clicked, with the
  link's words as the description screen readers announce.
- **Kerning by hand:** with the cursor between two letters, Alt+Left /
  Right (Ctrl+Cmd+Left / Right on a Mac, where Option+arrows move by word)
  closes up or opens the gap, by 1/100 of the letters' size (Shift: five
  times as much). With words highlighted, it spaces all their letters. The
  Kerning field in Characters takes exact numbers.
- **Clear formatting** (Ctrl+backslash, or the button): back to the paragraph
  style. Links stay.
- Formatting comes along when copying words inside a story, when copying
  and pasting text boxes, in undo, saved projects, the PDF, the PNG and the
  page thumbnails. The sample newsletter now has bold dates and days and
  an italic phrase.
- The Accessibility checker measures the contrast of each colour on a line
  separately, warns about links whose words don't say where they go
  ("click here"), suggests words instead of bare web addresses, and warns
  about formatted words under 9 pt.
- Project files are now version 2. Older versions of DSKEDTR will refuse
  them (rather than quietly losing the formatting); this version opens the
  older ones.
- The PDF only includes the fonts the document uses.
- Fixed: the alignment buttons in Paragraph didn't show which one was
  chosen. Small buttons that are on (alignment, Bold) are now emerald with
  a ring.
- Fixed: pasting a single copied text box showed an error in the browser
  console (the Inspector looked at the new text before it was laid out).

## 0.7.2 - 2026-10-06

- **Preview (the eye in the top bar, or W):** see the page as it will
  print. Guides, the grid, margins, box edges, handles and the cursor are
  hidden, and so is everything outside the page: whatever waits in the
  staging area, and any part hanging off an edge. Preview is for looking,
  so a click or drag on the page slides the view instead of moving things;
  Page Up / Page Down, zooming and undo still work. W, Escape, the
  banner's "Back to editing" button, picking a tool or starting to type
  all go back to editing. It works alongside the colour vision preview.

## 0.7.1 - 2026-10-06

- **The staging area:** the grey around the page is now somewhere to keep
  things. Drag anything off the page (a spare photo, a heading you're not
  sure about) and it stays there, visible and editable, on that page's
  desk. Things out there are never printed or exported, never read by
  screen readers, and the Accessibility checker leaves them alone (it just
  mentions, as a tip, what is waiting out there). Something half on the
  page still prints its half, and the checker still says it runs off the
  page. Rulers, zooming and Fit page all measure from the page as before.
  On a touch screen, one finger on an empty spot in the staging area still
  slides the view.
- **Ctrl+Shift+drag copies too** (Cmd+Shift on a Mac), in a straight line,
  as in PowerPoint. Ctrl+drag still copies freely.
- **Space to slide the page is steady now.** Holding Space made the browser
  scroll a screenful with each repeat of the key, which caused the jitter
  and the jump after letting go. And Space now works in the middle of a
  drag: hold it while moving something and the view slides along, with
  the thing still under the pointer, to carry it a long way.
- Fixed: after moving, resizing or turning something with the mouse, the
  crash backup and the Accessibility checker didn't update until the next
  other change.

## 0.7.0 - 2026-10-06

- **More shapes:** a Shapes tool (U) on the rail with 24 shapes: triangle,
  right triangle, diamond, parallelogram, pentagon, hexagon, octagon, half
  circle, star, seal, burst, heart, arrow, double arrow, chevron, speech
  bubble, speech box, cloud, lightning bolt, crescent moon, cross, ribbon
  banner, map pin and border frame (many the same drawings as VCTREDTR's).
  The button shows the shape it draws; press it (or U) again for the
  gallery, which works with the arrow keys. Drag on the page to draw one
  (Shift keeps it in proportion), click for one at its natural shape, or
  press Enter for one in the middle. Each fills, outlines, turns, resizes,
  merges, exports and takes alt text like any shape.
- **Rounded corners** for rectangles and rectangular picture frames
  (Rounded corners, in Look), in the units you picked. Merge Shapes, the
  PDF and PNG keep them.
- **Copy, cut and paste:** Ctrl+C, Ctrl+X and Ctrl+V (Cmd on a Mac) for what
  is picked: text boxes (with their text), shapes, lines and pictures,
  groups kept together. Pasting on the same page puts the copy a little
  down and to the right (further each time); on another page, in the same
  place. It even pastes into another document opened in the same tab,
  pictures included. Copied text boxes put their text on the clipboard
  too, for other apps. Text copied from another app pastes as a new text
  box in the middle of the page. While typing in a text box, Ctrl+C and
  Ctrl+V work on the text as always.
- **Ctrl+drag copies** (Cmd+drag on a Mac): the original stays put and a
  copy moves, as one undo step. A Ctrl+click without a drag still picks one
  object inside a group, as before. (Alt stays "no snapping for this drag".)
- Fixed: changing a shape's fill, outline or outline width in Look showed an
  error and didn’t redraw the page until the next change.

## 0.6.1 - 2026-10-06

- **Guides find the middle.** A guide dragged near the middle of the page
  catches it from further away, and while you drag, a pink line with a
  label says what it lines up with: "Middle of the page", "Middle of the
  margins", "Margin" or "Page edge". Shapes and boxes you move get the same
  labels. The middle of the margins is a new snapping point too (it differs
  from the page's middle when the margins aren't even). Alt (Option) still
  gives a free drag.
- **Quick guides** in the units, grid and guides panel: Middle, Thirds,
  Quarters, Tri-fold (the page's width in three equal panels) and Half-fold.
  Each adds to the guides you have, never doubling one, and is one undo step.
- **Zooming zooms the page, not the web page:** Ctrl (Cmd on a Mac) + scroll
  wheel and a trackpad pinch zoom the page around the pointer, in every
  browser (Safari's own trackpad gestures included). Plain scrolling still
  scrolls. The browser's own zoom still works everywhere else.
- **Touch screens:** two fingers pinch to zoom and slide to move around. One
  finger on the page draws, moves and picks things (before, the browser
  could take a one-finger drag as scrolling and stop it halfway); one finger
  on the grey around the page slides it. A second finger landing undoes
  whatever the first had started, so a pinch never moves anything.

## 0.6.0 - 2026-10-06 (phase 1, milestone 5: accessibility tools and type)

- **Centimetres.** A Units choice for every measurement in DSKEDTR:
  inches, centimetres, millimetres or points. It is in Page setup and in
  the units, grid and guides panel (the arrow beside Guides). The rulers,
  the Inspector's position and size, Page setup, margins, guides and column
  gaps all follow it; switching converts any number you were typing. It
  starts in inches for US English and in centimetres everywhere else, and
  is remembered in this browser. (Documents still store points, so nothing
  in a document changes when you switch.)
- **Styles: how each role looks.** While typing, the Paragraph section shows
  the style of the paragraph's role (Heading 1, Heading 2, Body, Caption):
  size, weight, line spacing, letter spacing, kerning on or off, space
  before and after, alignment (left, centre, right, justified) and colour.
  A change applies to every paragraph with that role in the document, and
  only changes its look, never what it means to a screen reader. Each style
  shows its contrast on white paper as you pick a colour. Reset this style
  puts it back. Styles are saved in projects (and checked when opened), and
  the PDF follows them exactly, letter for letter.
- **The Accessibility tab**, beside the Inspector, and a top-bar button that
  shows how many problems there are. It checks again by itself a moment
  after every change, and lists, most serious first: a missing document
  title; pictures and shapes without alt text; low contrast, measured from
  the page itself (so text over shapes and photos is checked too) against
  WCAG's 4.5:1, or 3:1 for large text; text that doesn't fit; text under 9
  pt; justified text (a tip); missing or skipped headings (tips); pictures
  that will print blurry; things running off the page; and empty picture
  frames (a tip). Each has a "Go to it" or "Fix" button that goes to the
  page, picks the object and opens the right Inspector field.
- **See the page as someone else does:** red-blind, green-blind, blue-blind,
  no colour, or blurred (low vision). It is a preview on the desk only,
  with a banner and a Stop button; exports never change.
- **Export's "Before you share it" list** is now the checker's list (its
  problems, not its tips).
- **The units, grid and guides panel no longer gets in the way:** on a wide
  screen it sits over the right-hand column, and it stays open while you
  drag guides on the page; its X, the arrow or Escape closes it.
- Fixed: on phones, the filmstrip and the side panel could slide under the
  page; now the whole window scrolls and each part keeps its full height.
- Not yet: styles for words inside a paragraph (bold or a colour for one
  word) and kerning between two chosen letters. Both need the text to
  carry formatting per letter, which is the next big change to the text
  engine.

## 0.5.1 - 2026-10-06

- **Rulers, grid, guides and snapping are in the top bar** now, since they
  are about the whole document, not what is picked. Four toggle buttons
  (filled when on): Rulers, Grid, Guides and Snap. The small arrow beside
  Guides opens a panel with the grid's spacing (1/8, 1/4, 1/2 or 1 inch, 5
  mm or 1 cm) and everything the Guides section of the Inspector had (add a
  guide, exact positions, column guides, Remove all). That section is gone
  from the Inspector.
- **Rulers** along the top and left of the page, in inches from the page's
  top-left corner. They mark where the pointer is and the extent of what is
  picked. **Drag out of a ruler onto the page to make a guide** (from the
  top ruler an across guide, from the left one an up-and-down guide); let
  go off the page and no guide is made.
- **A grid** on the page (never printed), with a darker line every inch (or
  cm). With Snap on, things and guides snap to the grid, unless a page edge,
  margin, guide or other object is even closer.
- **Snap** is one switch for all snapping (it was always on before, and the
  Guides section had its own "Snap to guides"). Alt (Option) while
  dragging still gives one free drag.
- Keys: Alt+Shift+R rulers, Ctrl+' grid, Ctrl+; guides, Ctrl+Shift+; snap.
- These four are view settings, remembered in this browser, not part of the
  document: switching them is no longer an undo step, and they no longer
  count as unsaved work. The guides themselves are still saved with the
  document. (Projects saved by 0.5.0 still open; their old show/snap
  settings are simply ignored.)

## 0.5.0 - 2026-10-06 (phase 1, milestone 4: files and the suite)

- **Save project** (the disk button, Ctrl+Shift+S): the whole document in a
  .dskedtr file, pictures inside, so it opens again exactly as it was.
  **Open** (the folder button, Ctrl+O, or drop the file anywhere in the
  window) brings it back. Opening is careful: the file is read as data and
  the document rebuilt from it field by field, keeping only what DSKEDTR
  knows and checking every number, colour, name and piece of text; each
  picture must really be a JPEG or PNG, at most 8000 pixels a side (checked
  before it is decoded), that decodes, or it is left out.
- **Export** (the green button, Ctrl+S): a PDF of every page, or a PNG
  picture of the page showing (96, 150 or 300 pixels per inch). The PDF has
  each page at its real size, text as real text in the document's own font
  (embedded, so it can be selected, searched and copied, with every letter
  exactly where the page shows it), shapes and merged shapes as sharp
  outlines, pictures at full resolution, and the document's title and
  language. Before you export, the Export box points out text that doesn't
  fit, pictures or shapes still missing alt text, and a missing title. Not
  yet: a tagged PDF (headings, reading order and alt text for screen
  readers inside the PDF); that is planned.
- **New document** (the page-with-a-plus button): an empty Letter page. It
  asks first when there is unsaved work.
- **The splash** when DSKEDTR opens, as in the other apps: New document,
  Pick a size (opens Page setup), Open a project, or Explore the sample,
  with the rest of the family underneath.
- **Crash backups:** while there is unsaved work, a copy is kept in this
  browser a few seconds after each change. Saving or exporting removes it.
  If the tab closes some other way (a crash, a closed laptop), the next
  start offers "Pick up where you left off", and a backup button appears in
  the top bar. A backup is opened with the same checks as any file.
- **The full help panel:** Keyboard shortcuts, Getting started (a newsletter
  from start to finish), About (privacy, the libraries and their licences,
  credits), Changelog and More apps. The DSKEDTR mark in the top bar opens
  More apps; the version shows beside the name.
- **Install as an app** (the Install button, when the browser offers it),
  with its own icons; it then opens with no internet. Installed, a .dskedtr
  file can be opened with DSKEDTR from the computer's files. The splash
  checks for a newer version.
- Messages now show on screen too (they were only read out to screen
  readers): a picture that can't be added, a file that can't be opened,
  "Saved...". Page setup says what is wrong inside its own box.
- Fixed: Page setup would not apply A4, A5 or a custom size whose inches
  aren't a multiple of 1/8 (the browser's own check refused them without
  saying why). Named sizes are now also kept exactly (A4 is 595.28 x 841.89
  points, not rounded through inches).
- DSKEDTR is in the shared block's list of apps, marked as not shown yet,
  so the other apps don't list it until it is ready.

## 0.4.1 - 2026-10-06

- **The sample now has pictures** (page 2), so pictures can be tried without
  adding a file: an original illustration of the outdoor concert (drawn by
  the app itself as it starts, so nothing is downloaded and the one-file
  edition stays one file), with its alt text and a place in the reading
  order; and an empty round frame with an outline, a placeholder for "Book
  fair photo (to come)". Double-click the illustration to crop it; pick it
  to try Fill, Show it all, Centre, the size slider and the frame shape.
- Fixed: an empty ellipse frame's cross ran past its edge; it now stops at
  the ellipse.

## 0.4.0 - 2026-10-06 (phase 1, milestone 3: pictures and Merge Shapes)

- **Pictures.** A Picture tool on the rail (F): click on the page to add a
  picture there, or drag to draw a frame first. Pictures can also be
  dropped on the page (dropped on a frame, they fill it) or pasted (a paste
  fills a picked empty frame, otherwise it adds a new picture). From the
  keyboard: pick the tool, then Enter. JPEG, PNG, GIF, WebP, AVIF and BMP,
  up to 40 MB.
- **Privacy:** every picture is decoded and redrawn as it comes in, and only
  the redrawn copy is kept, so hidden data in the file (a phone photo's GPS
  location, camera details) is left behind. Nothing leaves the browser.
  Huge pictures are kept at most 4000 pixels on the long side.
- **Alt text, right away.** A small "Describe this picture" box opens the
  moment a picture lands: Save, It's decoration, or Later (the Meaning
  heading keeps saying "needs alt text" until it has some). A picture with
  alt text joins the page's reading order.
- **Picture frames,** rectangle or ellipse. An empty frame is a pale
  placeholder with a cross that never prints; double-click it (or Enter)
  to choose its picture.
- **Cropping:** double-click a picture (or Enter, or the Crop button). The
  whole picture shows faintly around the frame: drag to move it inside the
  frame, drag its corners to size it, arrow keys to nudge; Escape or Enter
  when done. Buttons: Fill frame, Show it all, Centre, and a size slider.
  Resizing a frame keeps a filled or fitted picture filling or fitting it.
- **A blurry-print warning** when a picture will print under 150 pixels per
  inch at its size, on the Picture heading too. New pictures start no
  bigger than 3 inches and never below 150 pixels per inch.
- **Replace picture** keeps the frame, its place and shape, then asks you
  to check the alt text still fits.
- **Merge Shapes:** Union, Combine, Fragment, Intersect and Subtract, as in
  PowerPoint and VCTREDTR (same icons and Alt+Shift+U/C/F/I/S shortcuts,
  same Paper.js engine), in Arrange. Rectangles, ellipses and earlier
  merged shapes can be merged; the first one picked gives its look (each
  Fragment piece takes the look of the shape on top there). The result is
  a merged shape you can move, resize, turn, fill, outline, merge again and
  give alt text. Clicks only pick it where it really is, not in the empty
  corners of its box.
- The one-file edition now carries Paper.js too (0.67 MB).

Known limits:

- Pictures aren't saved anywhere yet: project files and backups come in
  milestone 4.
- Text doesn't wrap around pictures yet (phase 2).
- Shaped picture frames (a photo in a star) didn't make this milestone.

## 0.3.2 - 2026-10-06

- **Undo and Redo in the top bar,** where VCTREDTR, IMGEDTR and 3DEDTR have
  them, greyed out when there is nothing to undo or redo. Pressing them
  with the mouse keeps the cursor in the story you were typing in.
- The zoom buttons' tooltips now show their real shortcuts (Ctrl/Cmd + =,
  -, 0), and zoom sits next to Undo and Redo on the left.
- Fixed: deleting a text box (with Delete or the Arrange button) failed
  part-way in 0.2.0 to 0.3.1 when naming it for screen readers: the box was
  gone but an error stopped the announcement.

## 0.3.1 - 2026-10-06 (a tidier Inspector, and guides)

- **Every Inspector section folds,** and they **start folded**: you see a
  short list of headings and open what you need. Sections you open stay
  open next time (remembered in this browser), as in 3DEDTR. Headings are
  full-width buttons 44 px tall, easy to hit with a finger. On a heading,
  Up/Down/Home/End move between headings; Alt+Page Down / Alt+Page Up jump
  between headings from anywhere in the Inspector.
- **Folded headings still warn:** Story says "doesn't fit" and Meaning says
  "needs alt text" right on the heading.
- **Arrange is compact:** small captioned groups of icon buttons, split by
  thin rules. Align (six icons in one row, with "Align to" beside its
  label), Space evenly and Order side by side, then Group and Copy and
  remove. Every icon has a name for screen readers and a tooltip with its
  shortcut.
- **Look and Meaning** are now two sections, so alt text has its own place.
- **Guides:** lines to line things up against, the same on every page and
  never printed (teal). Add one up-and-down or across, or add column guides
  inside the margins (choose the number of columns and the gap). Type an
  exact position in the Guides list, remove one with its X button, or drag
  a guide on the page with the Select tool (drag it off the page to remove
  it). Objects snap to guides; "Show guides" and "Snap to guides" turn them
  off. The sample has guides at its column edges. Undo covers all of it.
- Clicking on the page takes focus out of an Inspector field, so Ctrl+Z
  and Delete act on the page.

## 0.3.0 - 2026-10-06 (phase 1, milestone 2: pages and layers)

- **Pages.** One page at a time on the desk, with a **filmstrip** along the
  bottom: live thumbnails, page numbers, and a red dot on any page with
  text that doesn't fit. Click a thumbnail, or use Left/Right in the strip
  (Home/End for the ends); Alt+Left/Right or drag moves a page. Buttons add
  a page after this one, duplicate it (text boxes keep the text they show,
  unlinked) or delete it. Page Up/Page Down on the page go back and forth.
- **Stories run across pages.** The sample's main story now continues on
  page 2. Typing or arrowing past the end of a box follows the text onto
  the next page, and "to p. 2" / "from p. 1" labels mark the jumps. Boxes
  on any page can be linked (the "Continues in" list names the page).
- **Page Setup** (Inspector, with nothing picked): size (Letter, Legal,
  Tabloid, Half Letter, A4, A5 or custom), orientation and margins, for
  every page. When the size changes, everything **stays where it is**,
  lined up to the corner, edge or centre you pick in a 3 by 3 grid. Or
  choose to stretch boxes and shapes to fit (text keeps its size). It says
  how many objects ended up partly off the page.
- **Layers list** (an ARIA tree, front-most first): Up/Down pick, Right/Left
  open and close groups, F2 or double-click renames, H hides, L locks,
  Delete deletes, Alt+Up/Down moves forward and backward, Enter types in a
  text box. Eye and lock buttons for the mouse. This is the keyboard way to
  reach every object.
- **Groups:** Ctrl/Cmd+G and Ctrl/Cmd+Shift+G (and buttons in Arrange).
  Clicking any member picks the group; Ctrl/Cmd+click picks just one.
  Align and Space evenly treat a group as one object. The sample's sidebar
  is a group.
- **Hide and lock.** Hidden objects aren't drawn or read; locked ones can't
  be picked on the page or moved, but their text can still be edited.
- **Rotation:** a rotate handle above a picked object (Shift: 15 degree
  steps) and a Rotation field. Turned text boxes still take clicks,
  selection and typing; resizing a turned object moves the edges the way
  they look.
- **Reading order per page,** with the heading naming the page. A story is
  read on the page where it starts. Tab moves through the stories page by
  page.
- The Layers and Reading order sections fold away and stay folded.

Known limits:

- Lines don't rotate (drag their ends instead).
- Resizing several objects at once when some are turned is approximate.
- Grouping is one level deep (no groups inside groups).

## 0.2.0 - 2026-10-06 (phase 1, milestone 1: objects)

- **Inspector no longer jumps.** The lines that change length (the box
  note, the story line, "All the text fits") always keep room for two lines.
- **Tools on the rail**, with VCTREDTR's letters: Select (V), Text box (T),
  Rectangle (R), Ellipse (O), Line (L). Reading order moved to N.
- **Draw** text boxes, rectangles, ellipses and lines by dragging (Shift:
  square, circle, 45 degree line). A click without a drag makes a
  default-size one. From the keyboard: pick a tool, then Enter on the page
  adds one in the middle. A new text box starts typing at once.
- **Select tool:** click to pick, Shift+click to add or remove, drag on
  empty page to pick everything the box touches, Ctrl/Cmd+A for all. Drag
  to move (Shift: straight), drag a handle to resize (Shift on a corner:
  keep the shape), drag a line's ends. Arrow keys move 1 pt (Shift: 10 pt).
  Double-click a text box (or Enter) to type in it; Escape while typing
  picks the box.
- **Snapping** to the page edges and centre, the margins and other objects'
  edges and centres, with pink guide lines. Hold Alt to turn it off for one
  drag.
- **Linking text boxes:** click a box's out-port (the square on its right
  edge), then click an empty box. Or use "Continues in" in the Inspector,
  which also works from the keyboard. "Stop the flow here" ends a chain;
  the text after it returns to the overflow.
- **Arrange:** align edges, centres and middles (to the selection, the
  margins or the page), space three or more evenly, to front, forward,
  backward, to back, duplicate (Ctrl/Cmd+D), delete. Deleting a box in a
  chain keeps its text in the story.
- **Shapes and lines** have fill, outline colour (picker or hex code) and
  outline width. Each is either decoration (screen readers skip it) or has
  alt text; one with alt text joins the reading order.
- **Document title and language** in the Inspector when nothing is picked.
- **Margin guides** (blue, never printed).
- Undo and redo cover all of it.

Known limits:

- No rotation yet.
- From the keyboard, objects are picked by Escape from a story's text or
  Ctrl/Cmd+A. The layers list (next milestone) will reach any object.
- Ports and handles can crowd each other on very small boxes.

## 0.1.0 - 2026-10-06 (phase 0: the text engine test)

The first piece of DSKEDTR: a one-page test of the text engine, before the
rest of the app is built on it.

- **Text that flows between linked boxes.** The sample newsletter's main
  story runs through two linked text boxes. Our own line breaking, using the
  font's real letter widths and kerning (opentype.js), decides what fits.
- **Overflow mark.** When a story doesn't fit, its last box turns red with a
  red "+" mark, the Inspector says how many words are left over, and screen
  readers hear it once.
- **Typing through a real, invisible text box.** Each story lives in a
  hidden textarea, so typing, accents, other-language input (IMEs), copy
  and paste, Select All, word-by-word moves and screen readers all use the
  browser's own text handling. The page draws the result as vector shapes.
- **Cursor and selection drawn on the page:** click, Shift+click, drag,
  double-click a word, triple-click a paragraph. Up/Down, Home/End and Page
  Up/Down follow the lines on the page, across boxes, remembering the
  column. Cmd+Left/Right on a Mac go to the line's ends.
- **Paragraph roles:** Heading 1, Heading 2, Body, Caption, from the
  Inspector or Ctrl+Alt (Cmd+Option) + 1 / 2 / 0 / 9. Enter after a heading
  starts a Body paragraph; Enter at the start of a heading keeps both as
  headings.
- **Reading order for page 1.** Automatic (top to bottom, then left to
  right) until changed. Change it in the Inspector list (Up/Down to pick,
  Alt+Up/Down to move, drag, or the Move buttons) or with the Reading order
  tool (click items on the page in order). Tab moves between stories in
  reading order. Decoration (the rule and the sidebar background) is listed
  as not read.
- **Undo and redo** for typing (grouped), roles, reading order and box
  sizes: Ctrl/Cmd+Z, Ctrl/Cmd+Shift+Z, Ctrl+Y, and the browser's Edit menu.
- **Box position and size** in the Inspector, in inches, for testing the
  flow.
- Zoom, Space+drag to slide the page, light and dark mode, a short Help
  (? or F1), phone layout.
- Two editions, like VCTREDTR: `index-online.html` (the source) and
  `index.html`, the one-file edition made by `build-offline.py`.

Known limits in this test:

- Letters the font doesn't have (Japanese, emoji) show as empty boxes. A
  fallback font is needed later.
- No spell check marks: the browser can only draw them in a visible text
  box. Spell check needs its own word list later.
- Copy and paste are plain text. The right-click menu on the page is the
  browser's, so it can't paste into a story.
- Layout is redone in full on every keystroke (about 16 ms for this page in
  testing). Fine for a page; a long newsletter will need layout that only
  redoes what changed.
- A heading can be left alone at the bottom of a box (no "keep with next"
  yet).
