# WHTBRDR - changelog

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
