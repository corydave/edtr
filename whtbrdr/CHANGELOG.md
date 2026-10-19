# WHTBRDR - changelog

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
