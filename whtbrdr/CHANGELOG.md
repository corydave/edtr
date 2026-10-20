# WHTBRDR - changelog

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
