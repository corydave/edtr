# WHTBRDR - changelog

## 0.4.2 - 2026-10-20 - PDF words, celebrations, and copying pages

- **Highlights quote the PDF words under them:** "Yellow highlight on: the mitochondria is the powerhouse", in the layers list, "Picked: ...", and what screen readers hear. A word counts when the highlight covers at least half its letters. The quote is worked out from where the highlight is (never stored), so moving a highlight to other words changes it.
- **Shift snaps a highlight to a line of text:** with the highlighter, hold Shift over a PDF's words and the stroke runs straight along that line, as tall as its letters, from the word it started on to the word under the pointer (either way). Off the text, Shift draws a straight line as before.
- **Screen readers hear a PDF page's words** (the board's description, up to 4,000 characters), as well as what is drawn on it. A page with no text says it may be a scan.
- **How it reads the words:** pdf.js gives text in runs (a few words in one font) with where each starts and how wide it is; WHTBRDR shares each run's width out among its letters. Close enough to tell which words a highlight covers. Text from a PDF is only ever shown as plain text, and capped in length.
- **Celebrate, in Present mode:** SCRNCSTR's confetti, fireworks and hearts (the same colors and physics, scaled to the real time between frames so fast screens don't speed them up), from a Celebrate button on the floating bar (a small menu), or Shift+C, Shift+F and Shift+H (plain F and H were taken: full screen and the highlighter). With the device's reduced-motion setting on, each is shown as a still picture that fades away over a second and a half. Fireworks stay small sparks, staggered, never a flash of the whole screen.
- **The magnifying glass zooms further:** from 2 times (where it starts, and never less, as Dave asked) up to 8. The mouse wheel or a trackpad pinch, + and - (with or without Ctrl, instead of the browser's zoom), or two fingers swiping up or spreading; Ctrl+0 goes back to 2. The glass shows its zoom ("3x") for a moment while it changes. (Two fingers not yet tried on a real phone or tablet: phone testing is on hold.)
- **Copy, cut and paste pages** (from the wings, as in DSKEDTR): Ctrl+C, X and V with the keyboard in the filmstrip, the page pill's new Copy, Cut and Paste, and the right-click menu. Pasted pages (fresh copies, marks and backgrounds and all) go after the page on show and are picked. Cut asks nothing (the pages are on the clipboard, and undo brings them back). The copies stay in this tab, since PDF pages and pictures point at files only this tab holds. A picture on the computer's clipboard, pasted with the keyboard in the filmstrip, becomes a page.
- **Fixed:** the Layers section's count ("4 marks") now follows every change; after drawing on a page it said "0 marks" until the Inspector was drawn again.

## 0.4.1 - 2026-10-20 - The page pill

- **The page pill, from DSKEDTR:** click or tap a page in the filmstrip and a small pill of buttons floats just above it: **Move left, Move right | Present from this page, Open a PDF or pictures after this page, Duplicate | Delete** (in the warning color). The same look as DSKEDTR's: round 34px buttons (42px on a touch screen), 20px icons, thin separators, a soft shadow; it stays centered over the page on show and inside the filmstrip's width.
- **It acts on every picked page** and says so: "Duplicate 3 pages", and the pill itself is named "Pages 2 to 4 picked". A button that can't act right now (the first page can't move left, the only page can't be deleted) is grayed but stays in reach, so the arrow keys don't skip over it.
- **From the keyboard:** coming into the filmstrip opens the pill; Tab from the pages reaches it (one Tab stop); Left, Right, Home and End move along it; Escape closes it and puts the keyboard back on the page (a second Escape then lets go of the extra picked pages, as before). It closes on a click anywhere off the filmstrip, or when the keyboard leaves it, but not while "Delete page 3?" or a file chooser is open.
- **The filmstrip's side** keeps just the + (add a page after this one); its copy, move and delete buttons moved into the pill, as in DSKEDTR. The right-click menu on a page gained **Present from this page** and **Open a PDF or pictures after this page**.
- **"Copy this page" is now "Duplicate this page"** (still Ctrl+Shift+D), DSKEDTR's word, so "copy" stays free for the clipboard if pages get copy and paste later.

## 0.4.0 - 2026-10-20 - Open PDFs and pictures

- **Open** (Ctrl+O, the new folder button in the top bar, or "Open a PDF or pictures" on the splash): every page of a PDF becomes a page of the same size, with the PDF under everything you draw, so it can't be picked, moved or erased by accident. A picture becomes a page the size of the picture (as its background picture, so it can still be faded). New pages go in after the page on show; on a board that is still one blank page, they take its place. One undo step either way.
- **Drop** a PDF on the board or the filmstrip to open it the same way. A picture dropped on the filmstrip becomes a page where it lands; dropped on the board, it is still a picture you can move. Several files at once work too.
- **Sharp at any zoom:** pdf.js paints the whole page (2048 pixels on its long side), and when you zoom in past that, it paints just the part on screen again at your screen's own sharpness, a moment after zooming stops. The filmstrip gets small copies, nearest pages first (200 pages took under 4 seconds in testing).
- **A PDF page in the Inspector:** its file, its page number and size (read only: a PDF page keeps the PDF's size), Turn the page (a quarter at a time; what you drew stays put) and Clear the page. Lines or a grid from Background can go over it. "Make every page this size" leaves PDF pages alone.
- **Password-locked PDFs** ask for the password in a dialog ("That password didn't open..." when it is wrong). It goes straight to pdf.js and is never kept: the field is emptied at once.
- **Office files** (Word, PowerPoint, Excel, Pages, Keynote, Numbers, OpenDocument) open a "Save it as a PDF first" dialog with the steps for that program and for Google's, and a button to open the PDF. It says why: converting it here would mean sending it to a server.
- **Turned away, with a reason:** a damaged PDF, a file that is neither a PDF nor a picture, a PDF over 100 MB. A PDF page bigger than 100 inches is shrunk to fit. The board's 500-page limit applies, and the toast says how many pages were left out.
- **Two editions,** the suite's way, as in PDFEDTR: `index-online.html` is now the source (edit it), and fetches pdf.js 5.7.284 from jsDelivr with SRI fingerprints the first time a PDF is opened. `build-offline.py` makes `index.html`, the edition the site serves, with pdf.js packed inside (gzip, then base64, about 700 KB) from `vendor/`; it checks the files against the same fingerprints first, and the page checks them again before unpacking. The offline edition makes no network call at all.
- **Security:** the CSP adds `blob:` to script-src and worker-src (pdf.js runs from a blob: address the page makes itself, after the fingerprint check; worker-src keeps `'self'` for the service worker). The online edition's connect-src adds `https://cdn.jsdelivr.net`, and the build takes it out again. PDF JavaScript never runs, links in a PDF can't be clicked, and pictures inside a PDF are limited to 60 megapixels.
- The help panel: Ctrl+O in the shortcuts, a Getting started step for opening, the About tab says which edition is running and credits pdf.js. "What is coming" was months out of date (it still listed the filmstrip and Present mode); it now names what is actually next.
- `sw.js` keeps the online edition under its own name, so visiting it never replaces the offline page the installed app opens with.
- `_edtr-suite/paste_whtbrdr_bar.py` now pastes the bar into `index-online.html`; run `build-offline.py` after it.

## 0.3.4 - 2026-10-20 - Step numbers, units, and a gentler Escape

- **Step numbers** (N, or the new Step tool on the rail, below Stamp): numbered discs, as in IMGEDTR, that count on from page to page. N puts one in the middle of the board (picked, so the arrow keys move it); with the tool, a click puts one where you click. Their color is one of the five pen colors in the pill (blue at first), sized S / M / L; they stay round and upright.
- **The numbering:** all the steps make one run, page by page. Delete a step and the gap closes; move or copy a page and everything after renumbers (a copied page with steps 4 to 6 becomes 7 to 9). Any step can **start new numbering**, from any number, in 1 2 3, A B C or a b c; a copied page keeps its restart, so a copied "lesson 2" page still starts at 1.
- **For a picked step:** type its number (it moves to that place among the steps on its page), Earlier and Later, Start new numbering here (with Start at and Style), number color, white ring and size, and a line saying what it continues from ("Continues from step 6 on page 2"). Copies take the next numbers.
- **Descriptions:** each step is "Step 3"; words added in the Description field come after the live number ("Step 3: click Submit"). The filmstrip says which steps each page has ("Page 2: Steps 4 to 7").
- **Units:** inches, centimeters, millimeters or points, one choice at the top of the Page section ("Measure in", also in Position and size) for every measurement: page size, position and size, background spacing, the grid's squares. The first choice follows your browser's language. With centimeters or millimeters, a new board starts on A4, and new backgrounds and grids use 5 mm dots and squares (1 cm for large graph paper).
- **Present mode, Escape:** from any tool it goes back to the Pointer first; with the Pointer, it stops. In Chrome and Edge, Escape no longer drops out of full screen on the way (hold it down to leave full screen). **F**, or the new Full screen button on the bar, goes in and out of full screen while presenting.
- **Fixed:** picking "Custom size" for the page now shows its width and height.

## 0.3.3 - 2026-10-20 - Backgrounds and the coordinate grid

- **Backgrounds** (Inspector, with nothing picked): dots, small lines (college ruled), large lines with a red margin line (wide ruled), and small or large graph paper. Each has its own line color and spacing (in inches or millimeters).
- **The coordinate grid,** for graphing: all four quadrants or the first only, the square's size, what a square is worth (0.5, 2, 10...), a number every so many squares, numbers on the axes and axes with arrows (each can be turned off), and the origin wherever you want it (counted in squares). It sits on top of any background.
- **The background picture:** choose one (checked and redrawn like every picture, so hidden data such as GPS is left out), then fit, fill or center it and fade it from 0 to 90%. A picture already on the page becomes the background with "Make it the background" in its Inspector.
- **On every page:** each of the three has "Put it on every page", and a new page takes the background, grid and picture of the page on show.
- None of them are marks: they can't be picked, moved or erased, so drawing (and erasing) on top never disturbs them. They show in the filmstrip, in Present mode and in its magnifying glass, and screen readers hear them in the page's description ("under it, graph paper, a coordinate grid").
- The help panel's tour has a fifth feature, "A graph in one tap".

## 0.3.2 - 2026-10-20 - Present mode

- **Start:** the Present button in the top bar (from the page on show), F5 (from the first page) or Shift+F5 (from this page). The page fills the screen on black, using the browser's full screen where it is allowed. **Escape** stops, back on the page you ended on (leaving the browser's full screen stops too).
- **Moving:** Right, Down, Space, Page Down or Enter go forward; Left, Up, Page Up or Backspace go back; Home and End jump to the ends. Clicker remotes work (they send Page Up and Page Down). A number and then Enter goes to that page (the number keys still pick colors on the way, and Enter puts the tool back). With the Pointer, a click on the page goes forward, and the mouse wheel moves one page per turn.
- **The floating bar** (bottom center; it fades when the mouse is still, and the mouse arrow hides with it): the Pointer, the five pens, S / M / L, the four highlighters, the eraser, the **laser pointer** (K, a glowing dot with a fading tail in the pen's color), the **spotlight** (S, everything dark but a circle around the mouse), the **magnifying glass** (M; + and - zoom it from 1.5 to 5 times; it redraws the page larger, so it stays sharp), **disappearing ink** (strokes fade after a few seconds and are never kept), undo, the page before and after, and Stop. It is one Tab stop, and the arrow keys move along it.
- **B or W** turns the screen black or white, as in PowerPoint ("." and "," too); any key or a click brings the page back.
- **Ink while presenting is real ink.** When you stop, if anything changed, WHTBRDR asks whether to keep it or take it all away; either way is one undo step.
- **Screen readers** hear each page's number and title ("Page 4 of 12: The water cycle"), and the board lists what is on the page in reading order.
- The help panel's tour has a fourth feature, "Present, and keep drawing", and the keyboard list has the presenting keys.

## 0.3.1 - 2026-10-19 - Install it, and a splash

- **Installable:** Install in the top bar (shown only when the browser allows it) or at the foot of the splash gives WHTBRDR its own window and icon. It opens with no network: `sw.js` keeps the page and the icons (never your boards). With a network, each launch loads the newest version, and the splash checks for updates (Update now when there is one). On iPhone and iPad the splash says how to add it to the Home Screen.
- **The splash** at start-up, the family's: a picture of WHTBRDR in use, then **New board** (the page as it is, ready to draw on), **Pick a page size**, **Draw on a picture**, the "See what WHTBRDR can do" tour, the other apps and the credits. A picture pasted or dropped on the splash closes it and goes onto the page. Escape or the X goes straight to the board.
- **Icons:** `icon.svg` and a full set of PNGs (192, 512, a maskable 512 for phones that crop, Apple's 180, a 32 favicon), drawn by `make-icons.py` from the same numbers. `whtbrdr-thumb.webp` is the hub picture, for when WHTBRDR is listed.
- **Next:** Present mode (0.3.2), pulled forward from milestone 6.

## 0.3.0 - 2026-10-19 - Pages

- **The filmstrip** along the bottom shows every page, numbered, with a small live copy of what is drawn on it. The page on show has a thick outline (and "on show" for screen readers); other picked pages a dashed one and a tick.
- **Add a page:** the + button, Ctrl/Cmd+Enter, or the + that shows between pages under the mouse. A new page takes the size and color of the page on show.
- **Copy pages** (Ctrl/Cmd+Shift+D), marks, groups and descriptions and all; the copies go right after. **Move pages** with the arrow buttons, Alt+Left and Alt+Right, or by dragging. **Delete pages** with the button or Delete; it asks first when they have marks, and undo brings them back. A board keeps at least one page.
- **Pick several pages** with Ctrl/Cmd+click, Shift+click or Shift and the arrow keys, to copy, move or delete them together. Right-click a page for the same choices (Shift+F10 or the Menu key from the keyboard).
- **Getting around:** the filmstrip is one Tab stop (the arrow keys go page to page, Home and End to the ends, Enter back to the board), Page Up and Page Down work from the board, and F6 now stops at the filmstrip too. Undo and redo show the page the change was on.
- **Inspector:** "Make every page this size" and "Make every page this color" when there is more than one page.
- **Phones:** the filmstrip folds behind a Pages button in the top bar (not yet checked on a phone).
- **Fixed:** renaming a row in the layers list could stop after the first letter, when the Inspector happened to be redrawn just then (0.2.4).

## 0.2.4 - 2026-10-19 - Describe it, list it, line it up

- **Descriptions (alt text):** every mark gets a description as it is made: "Red arrow pointing right", "Yellow highlight", "Text: Read page 4", "Sticky note: check this date", "Picture: diagram.png". Text and sticky notes follow their own words. The Inspector's **Description** field (at the top of what is picked) replaces it; the reset button puts the written one back. A whole group can have a description of its own, which copy and paste carry along. The description is the mark's name everywhere: the layers list, "Picked: ...", Tab, the menus.
- **Decorative:** a switch for marks that carry no meaning; screen readers skip them (and exports will, later). Typed descriptions are cleaned to one plain line of at most 250 characters and only ever shown as text.
- **The layers list** (an Inspector section, open it once and it stays open): one row per mark, top first, with a color dot; groups open with Right and close with Left, nested as grouped. Highlights sit in a band of their own at the bottom, as they are drawn under the ink. Up and Down pick, Space adds, F2 (or a double-click) describes, H hides, L locks, Alt+Up and Alt+Down move, Delete removes, Enter types in a text or note. The eye and padlock on each row do the same with the mouse, and rows can be dragged among their neighbors.
- **Hide:** a hidden mark isn't drawn and can't be clicked, boxed, erased or reached by Tab or Ctrl/Cmd+A; the layers list brings it back.
- **Snapping:** moving, resizing, dragging a line's end and drawing a shape snap to the page's edges and middle and to other marks' edges and middles, with a pink guide line. Hold Alt to skip it, or switch it off in the Select tool's settings.
- **Line up** (Inspector): align left edges, centers, right edges, tops, middles or bottoms, to each other or to the page (one mark lines up with the page), and space three or more evenly across or down. A group counts as one.
- **Order:** Bring forward and Send backward now step past a mark of the same kind: a highlight past the next highlight, ink past the next ink (each kind is drawn on its own layer, so a step past the other kind showed no change).

## 0.2.3 - 2026-10-19 - Copy, arrange, group and lock

- **Copy, cut, paste, duplicate** (Ctrl/Cmd+C, X, V, D). Copies stay inside WHTBRDR: the computer's clipboard only gets a short note ("WHTBRDR: 2 rectangles") with a one-off code, and Paste brings the marks back only while that note is still there, so pasting can never read outside text or data into a board. A copied picture from anywhere still pastes in as a picture (0.2.2). Each paste lands a little further down and to the right; copied groups paste as new groups of their own.
- **Order:** bring to front or forward, send backward or to the back (Ctrl/Cmd+] and Ctrl/Cmd+[, with Shift for all the way). Highlights stay under the ink, as always.
- **Groups** (Ctrl/Cmd+G, Ctrl/Cmd+Shift+G): a click on any part picks the whole group, and it moves, resizes, turns, copies and deletes as one. Groups can hold groups. Double-click a group to work inside it (a faint dashed frame shows which group); Escape or a click outside steps back out. Ctrl/Cmd+A and the selection box pick only within the group you are in. Tab treats a group as one stop.
- **Lock** (Ctrl/Cmd+Shift+L): a locked mark ignores clicks, drags, the selection box, Ctrl/Cmd+A and the eraser, so you can draw right over it. Tab and a right-click still reach it (it shows a gray dotted frame with no handles), and the page's menu has "Unlock all on this page".
- **The right-click menu** (also Shift+F10 or the Menu key with the board focused): Cut, Copy, Paste, Duplicate, Delete, the four order moves, Group, Ungroup, Work inside the group, Lock, and Type in it or Its own size where they fit. Arrow keys, Home and End move through it; Escape closes it and puts focus back. A long press on a touch screen stays the selection box.
- **Inspector:** Duplicate, and an Arrange row (Front, Forward, Backward, Back, Group, Ungroup, Lock). Something locked shows only Unlock and Let go.
- The help panel lists the new keys.

## 0.2.2 - 2026-10-19 - Pictures and stamps

- **Pictures:** I (or the Picture button), paste (Ctrl/Cmd+V), or drop files on the board. PNG, JPEG, GIF (its first frame) and WebP, recognized by their first bytes, under 30 MB and 60 megapixels (read from the file's header before it is opened). Every picture is redrawn on the way in, so hidden data such as GPS and camera details is left out, and kept at most 4096 pixels on its long side. They come in no bigger than 60% of the page, picked; "Its own size" puts one back to its size. Pictures are kept apart from the undo list, so undo never copies their bytes.
- **Stamps (G):** PDFEDTR's green check and red X, plus an orange star and a blue question mark. Pick one in the pill (S / M / L size it) and click; Enter puts one in the middle. They stay square; their color can be set for new ones (Inspector, with the tool) or changed on picked ones, and a picked stamp can be switched to another.
- **Eraser:** leaves pictures alone (they have Delete), takes stamps away whole.
- **Phones:** the four shapes fold into one Shapes button (the four sit in the pill while one is in use), separators go, and Picture moves to the top bar, so every tool fits on the rail without scrolling.
- The shared bar learned the fold, a home's own tools on its rail, and their choices in its pill, and no longer shows the browser's blue flash on a tap; the extension took it as 1.3.2 (nothing changes there).

## 0.2.1 - 2026-10-19 - The extension's tools

- **Arrow (A), line (L), rectangle (R), ellipse (O)** on the rail, in the pen colors and S / M / L, drawn like the extension's (Shift: 45 degree steps, squares, circles).
- **Text (T):** click and type, Enter for a new line, Escape or Ctrl/Cmd+Enter to finish. F switches the font: Atkinson Hyperlegible (the default) or Comfortaa, both built into the app from the extension's own files (SIL Open Font License). A pen color, size or font picked while typing restyles the words.
- **Sticky notes:** J drops one in the middle, or pick the tool and click where it goes; it grows to fit its words. The Inspector sets new notes' paper, and a picked note's paper (four colors, or any).
- **One model for everything:** shapes, text and notes pick, move, resize and turn like strokes. One line or arrow gets a handle on each end. Double-click or Enter types in a text or note again. The Inspector shows only what fits what is picked: color, paper, line width, font, letter size, Type in it.
- **Keyboard:** with the board focused, Enter puts a new shape, text or note in the middle, picked.
- **Stay in this tool** (on, the extension's way); off, each new thing is picked and Select comes back.
- **Eraser:** shapes and text go whole; sticky notes stay (they have Delete).

## 0.2.0 - 2026-10-19 - Pick it up, move it, rub it out

- **Select (V):** click picks, Shift+click adds or takes away, dragging on an empty spot draws a selection box (anything it touches; Alt for only what is wholly inside), Ctrl/Cmd+A picks everything on the page, and Ctrl/Cmd+click picks without leaving a pen.
- **Move, resize and turn** with the frame's handles (the suite's finger-sized ones on a touch screen): Shift on a corner keeps the shape, Shift while turning steps by 15 degrees. A stroke made bigger gets thicker with it. A perfectly straight line shows only its two end handles.
- **Touch:** tap picks, drag moves, press and hold an empty spot for a selection box; dragging from an empty spot slides the page.
- **Keyboard:** arrow keys nudge (Shift: 10 points; quick nudges join into one undo step), Delete or Backspace removes, Tab and Shift+Tab step through the page's marks in reading order, and Escape steps back one thing at a time (a stroke being drawn, a move under way, what is picked, then the Select tool).
- **Inspector** for what is picked: color, line width, and X, Y, width, height and turn by number (inches or millimeters, "Keep the shape" on by default). The Inspector button gets a dot when something is picked but the Inspector is hidden.
- **Eraser (E):** whole strokes, or part of a stroke (press E again, or pick it in the Inspector), which cuts a stroke where it rubs. Small, Medium and Large size it; each sweep is one undo step.
- The shared bar gained the eraser's sizes and lets each home word a tool's tip; the extension took it as 1.3.1.

## 0.1.1 - 2026-10-19 - One bar with the extension

- **The annotation bar is shared with the WHTBRDR Chrome extension** (1.3.0): the same tools, colors, sizes, names, icons and keys, from one master in `_edtr-suite/whtbrdr-bar.js` and `.css`, copied into both by `_edtr-suite/paste_whtbrdr_bar.py`. The rail and the pill at the top of the board are built from it.
- **Keys:** 1-5 pick a pen and 6-9 a highlighter, whatever tool is in use; [ and ] change the size; P and H still pick the tool.
- **Sizes:** Small, Medium and Large for every tool (in the pill), as in the extension. The Inspector can still set an exact size for the pen or the highlighter.
- **Colors:** the extension's five pens; yellow, green, pink and now blue highlighters. Colors changed in 0.1.0 start over on these.
- **Highlights:** see-through instead of blended on a dark page color, so they don't vanish; one being drawn no longer looks darker where it crosses another.
- **Fixed:** a Shift straight line could jump back at the end.
- **The SUITE block** is now the master copy, with WHTBRDR in it (still `listed: false`).

## 0.1.0 - 2026-10-19 - The shell and one page

The first version (milestone 1 of the spec), built in a chat: the suite shell, pens and highlighters with stylus pressure and palm rejection, page sizes, zoom and slide, undo for everything, the help panel, dark mode and the phone layout.
