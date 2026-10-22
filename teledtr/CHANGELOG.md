# TELEDTR Changelog

Newest first. The short form of each entry also lives in the `CHANGELOG` table inside `index.html` (shown in the app's Help > Changelog tab). Add new releases to both.

## 0.3.1 - 2026-10-22 - Two new apps in the family

- TELEDTR and WHTBRDR are now listed in every app's splash screen and Help > More apps, and the splash row marks the app you are in with "You are here".
- The shared SUITE block was pasted in again from `_edtr-suite`: TELEDTR and WHTBRDR in `SUITE_APPS` (TELEDTR with `ink`, the drawing colour for a light tile), their icons in `SUITE_MARKS`, and a 6 + 6 splash grid (4 + 4 + 4 on a phone).

## 0.3.0 - 2026-10-21 - The family's editor layout, and a sections timeline

Dave's layout idea, tried first as a clickable prototype (side-by-side screenshots at desktop, tablet and phone sizes), then built.

- **Tool rail on the left** (SUITE-STANDARD section 1: 56 px, one 40 px button each): **New section** (makes the cursor's line a `#` heading), **Cue mark** (its menu now opens beside the rail, as DSKEDTR's Shapes flyout does), **Speaker**, then **Bold** and **Italic** (moved from the top bar; Lucide-style icons now). On a phone the rail lies along the bottom, and the cue menu opens above it.
- **The sections timeline** replaces the section list: under the script, one block per section, as wide as its time (a minimum for the title, plus a share of the rest by time), so the long sections stand out. "Whole script 0:48" sits at the end. The block the cursor is in is highlighted, with a bar along its foot for how far into the section the cursor is, and the strip scrolls to keep it in sight.
  - Click a block to go to its heading. Drag a block to move the section (a mouse anywhere on it; a finger by the dotted grip on its left edge, so a finger elsewhere still scrolls the strip). A drag starts after 6 px, so a click is still a click; a line shows where it will land.
  - Keys: one block is in the Tab order; Left / Right / Home / End move between blocks, Alt+Left / Alt+Right move the section, Enter goes to it, the Menu key or Shift+F10 open its menu.
  - The menu: Go to, Select its text, Move earlier, Move later, Move to the start, Move to the end.
  - The blocks are kept while you type inside a section (only resized), and rebuilt when a heading changes, so a long script stays quick. Each block looks up its section when used, so it never goes to an old position.
- **The Insert bar above the script is gone**, so the script gets its height back; the section list's width goes to the script too.
- **Phones:** the status line gives way to the timeline, which already shows the total time.
- Help (Getting started, shortcuts), the Features tour's timing slide (now drawn as the timeline) and the splash picture follow the new layout.

## 0.2.0 - 2026-10-21 - Lined up with the family, and a Script check

An alignment pass against the rest of the suite (IMGEDTR, DSKEDTR, 3DEDTR, ANIMEDTR), plus the additions Dave picked.

**Fixed**

- **The Inspector in the prompter scrolls.** It used to sit inside the text's area, so the wheel and swipes over it moved the script instead. It now sits beside the text (its own grid cell, `overscroll-behavior: contain`), and the wheel scrolls the settings.
- A full stop right after bold or italic (`**Security**.`) showed with a space before it, and was counted as a word. It now sits against the word and is not counted (the sample is 106 words, not 107).
- Headings in the editor were drawn bold in the backdrop while the text box on top was not, so the cursor sat slightly off the letters on a heading line. They now look bold through a hairline shadow that does not change the letter widths.
- An "on" switch in the prompter's dark Inspector looked almost the same as "off". On is sunflower there too.
- Opening another script no longer starts the prompter where the last one stopped.
- Going to a section from the rail lands on its heading even when lines wrap (it is measured now, not counted).
- A right-click in the prompter no longer starts or pauses the text.

**The Inspector, like the family's**

- Sections that fold (DSKEDTR's style): **Pace, Text, Colors, Reading line, Mirror, Timers, Speakers**. They start closed and remember being opened (in this browser, separately for the editor and the prompter); each closed heading shows its value ("145 a minute", "64 px"). Alt+Page Down / Alt+Page Up jump between headings; on a heading, Up / Down / Home / End move between them.
- The prompter's Inspector has the same seven sections, so everything can be changed without leaving the prompter.
- Two tabs, as in ANIMEDTR and DSKEDTR: **Inspector** and **Script check**.
- **Reset to the defaults** at the foot of the Inspector.

**New**

- **Script check:** sentences longer than 30 words, cue marks with a typo (`[PASUE]`, `[SLDIE 2]`; they would show as a note and not act), bold or italic left open, a cue missing its `]`, doubled words ("the the"), pauses over 60 seconds, no sections in a long script, and sections more than twice the typical length. Select an item to select it in the script; typos, stray markers and doubled words have a **Fix** button (one Undo step). The count shows on the tab.
- **Find and replace** (Ctrl+F, or the magnifier in the top bar): every match marked in the script, the current one darker and outlined; Enter / Shift+Enter for next and previous; Match case; Replace and Replace all (one Undo step each). Escape closes it and leaves the match selected.
- **Drag a section by its grip** to move it, with a line showing where it will land. Alt+Up / Alt+Down move the focused section too.
- **Menus** on right-click, long-press, the Menu key or Shift+F10: on a section (go to, select its text, move up, down, to the top or bottom) and in the prompter (start, back to the start, paragraphs, bigger and smaller text, mirror, dimming, Inspector, full screen, back to editing).
- **The prompter:** the lines already read are dimmed; the section you are in ("Threats (2 of 4)") and a progress bar sit above the timers; the screen is kept awake while it is open (Screen Wake Lock, on a web address).
- **Prompter keys:** + and - change the text size, F switches full screen (and leaving it with F keeps the prompter open; Escape still goes back to editing), and B or . (a clicker's "blank screen" button) start and pause.
- **Easier reading** (spec section 9): a Letter spacing slider, a **Black on cream** tinted background, and **Move a page at a time** (the text stays still while you read down the screen, then turns).
- **Your settings are remembered** (`teledtr.settings` in this browser), so a new script, a pasted one or a text file starts with your text size, pace, colors and mirror. A .teledtr file still brings its own.
- **Forgiving pauses:** `[PAUSE 3]`, `[PAUSE 3 sec]` and `[PAUSE 3 seconds]` all work like `[PAUSE 3s]`.

**Matching the family**

- The splash has its picture (a 1120 x 630 WebP drawn from the app: the editor with the prompter on a tablet, made by `render_hero.py` in the build folder) and its version line.
- Drop a .teledtr, .txt or .md file anywhere to open it; no splash when a file arrives. An installed TELEDTR is listed as an app that opens .teledtr files (`file_handlers` in the manifest, read through `launchQueue`).
- The phone and tablet sheet first opens at a third of the screen and remembers its height as a share of the screen (`sheet`), per the family standard.
- The logo button's name follows the family ("TELEDTR and its family of apps").
- American spelling throughout ("Colors").
- The Features tour's fifth slide is now the Script check; the prompter slide shows the dimmed lines and the progress bar.

## 0.1.0 - 2026-10-20 - First build (milestone 1)

Milestone 1 of `TELEDTR-SPEC.md` (project doc, sections 1-5, 8, 8b, 9, 11 and 12).

- **Script editor**: write in plain text. Headings (`# Title`) make sections, a rail lists them with their timing, and each section can be moved up or down. `**bold**` and `*italic*` mark words to stress.
- **Cue marks** in square brackets, painted in the editor and never read aloud: `[PAUSE]`, `[PAUSE 3s]`, `[SLIDE 2]`, `[CLICK]`, `[SMILE]`, `[NOTE: ...]`, `[LOOK UP]`. A cue menu inserts them, and a speaker button inserts a `NAME:` line.
- **Timing**: the word count gives the estimated time at the chosen pace. Each `[PAUSE 3s]` adds its seconds; an untimed `[PAUSE]` adds 1.5 seconds.
- **Full-screen prompter**: text size, line spacing, side margins, colours (white on black, black on white, yellow on black), font, reading line, mirror left to right and flip upside down (for a prompter glass), a three-second countdown, and four timers (elapsed, estimate, remaining, and an optional target with "behind" or "ahead").
- **Keys and clicker**: Space starts and pauses; Up and Down change the pace, or move one line when paused; Left and Right move a paragraph; Home goes to the start; Escape goes back to editing, where the cursor is left at the word reached.
- **Save and open**: `.teledtr` files (the script plus its settings), opened again exactly as saved. Plain text (`.txt`) and Markdown (`.md`) files can also be opened. `.docx`, `.srt` and `.vtt` are refused for now (later milestones).
- **Paste** with formatting cleaned up: headings become `#`, bold and italic become `**` and `*`.
- **Family standards**: the shared SUITE block (splash, Help, crash backups, install), copied in unchanged; works offline; nothing is uploaded and no sign-in is needed.
- **Not yet in this build**: voice-follow, rehearsal mode, PDF and text export, and the SuitePrompter link (milestone 2 and later).
