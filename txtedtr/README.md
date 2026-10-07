# TXTEDTR

A small text editor that is one HTML file. No build step, no npm, no CDN. Open
`index.html` in a browser and it runs.

Version history lives in [CHANGELOG.md](CHANGELOG.md).

## Running it

**As a web page.** Double-click `index.html`, or serve the folder with any
static server (`python3 -m http.server 8000`) and visit it. Chrome and Edge are
the best hosts, because they support the File System Access API - that is what
lets Save write back over the file you opened instead of dropping a new copy in
Downloads. Firefox and Safari fall back to a file picker for Open and a
download for Save.

## Installing it as an app

Served over HTTPS, TXTEDTR can be installed into the dock or Start menu, where
it opens in its own window with no address bar. `manifest.webmanifest` is what
makes that possible.

**What you need in the folder:**

```
index.html
manifest.webmanifest
sw.js
icon-192.png              192x192, artwork fills the square
icon-512.png              512x512, artwork fills the square
icon-maskable-512.png     512x512, artwork inside the middle 80%
```

The maskable one is a separate file because Android and some desktop themes
crop icons to a circle or a rounded square. Keeping the artwork inside the
middle 80% means nothing important gets sliced off. If you would rather not
make a third icon, delete that entry from the manifest - the other two are
enough.

**To install:** open the page in Chrome or Edge, then use the browser menu -
"Install page as app" in Chrome, "Apps" then "Install this site as an app" in
Edge. You only do this once per machine.

**Double-clicking files.** The manifest's `file_handlers` registers TXTEDTR for
the extensions it knows how to highlight, so once it is installed you can set
it as the opener for a `.java`, `.php` or `.md` file and it will launch straight
into it. The first time, the browser asks you to confirm.

After adding a file type to `file_handlers`, an installed copy only learns about
it when Chrome refreshes its copy of the manifest, which happens on a launch
after the manifest has changed on the server - sometimes a day later. If the new
type still does not appear under Finder's Open With, uninstall the app from
Chrome (`chrome://apps`, right-click, Remove) and install it again. `launch_handler` is set to
`focus-existing`, so a second file joins the sidebar of the window you already
have open rather than starting a new one. Chromium desktop only; everywhere
else this is quietly ignored.

**HTTPS is not optional here.** Installability needs a secure context, and so
does the File System Access API - on plain HTTP you would also lose Save
writing back to the file you opened, and drop to downloading a copy instead.

**Working offline.** `sw.js` is a service worker, and it is the only reason an
installed TXTEDTR can open with no network. Installing a PWA gives it a window,
an icon and file associations, but the browser still fetches `index.html` from
your server on every launch until a service worker says otherwise.

It uses two strategies on purpose. The document is fetched **network first**,
falling back to the cache only when the network is unreachable - so online you
always get exactly what you last uploaded, and offline you get the last copy
that reached that machine. The icons and manifest are **cache first**, because
they change roughly never. This matters: the usual cache-first-everything
service worker will cheerfully serve last week's `index.html` after you upload
a new one, and that is the classic afternoon lost to "why is my change not
showing up".

The document fetch also passes `cache: "no-store"`. Without it the browser's own
HTTP cache can answer without ever asking your server, which quietly defeats the
whole point - this was measured, not assumed.

**The one habit it asks of you:** bump `APP_VERSION` in `index.html` when you
deploy. That single number is the version in the About tab *and* the service
worker's cache name, so raising it makes the browser fetch a new worker, build a
fresh cache, and delete every old one on activate. Forgetting it is not fatal -
network-first means an online launch still gets your new file - but the stale
cache lingers until you do.

## Features

- Syntax highlighting for HTML, CSS, JavaScript, Java, JSON, Python, Markdown,
  SQL, shell, XML and YAML. The language is guessed from the file extension and
  can be overridden from the status bar.
- Light and dark themes, following the operating system on first run.
- A split view: two panes side by side, each with its own file, scroll, caret
  and gutter, and a draggable divider between them. Ctrl+\\ or the button in
  the top bar. A file lives in **one pane at a time** - opening it on the other
  side swaps the two panes rather than showing two views of one document, which
  would mean keeping two copies of the text in step.
- A live preview pane. Ctrl+Shift+V or the eye in the top bar splits the view
  and turns the right side into a preview of whatever the left side is editing.
  It does not own a file of its own, so the one-file-per-pane rule still holds -
  and it cannot be given one: opening a file or clicking a sidebar row while
  previewing always loads into the editor pane, and the keyboard can never land
  in a preview. While a preview is up **both** panes carry a header - SOURCE on
  the side you are typing in, PREVIEW on the side showing the result, each
  naming its file - so the two sides can never silently disagree about what is
  on screen, and both bodies start at the same height.
- A collapsible sidebar listing every open file, each with a mark showing its
  type, and an L or R showing which pane it is in when the view is split. On the right, a saved file shows a close cross and an unsaved one shows
  a dot - pointing at the row swaps the dot back to the cross, so closing is
  always one click away.
  It always starts collapsed as a narrow rail; Ctrl+B or the rail button opens
  it. That state is deliberately not remembered, so opening it once does not
  leave it open forever.
- A settings modal behind the cog: font size, tab size, where the file pickers
  start, indentation display, auto-close brackets, word wrap, line numbers.
- **Files start in** picks the folder Open and Save As begin in - Desktop by
  default, or Documents, Downloads, or wherever you last saved. The first three
  are passed as `startIn` and apply every time; "where I last saved" instead
  gives the picker an `id`, which is how you ask the browser to remember. The
  two are mutually exclusive: a directory remembered for an id wins over
  `startIn`, so setting both would quietly disable the one you chose.
- Visible indentation, off by default. **Dots** puts a dot in every leading
  space column - the feature other editors call "render whitespace" or "show
  invisibles". **Indent guides** draws a hairline at each indent level instead,
  its spacing following the Tab size setting. Whichever you pick is
  remembered. Both paint a CSS background
  behind the real characters rather than replacing them, so nothing can drift
  out of alignment with the text box above.
- Auto-close brackets, on by default: `(`, `[`, `{` and quotes come in pairs,
  typing the closing character steps over the one already there, Backspace
  between an empty pair removes both, typing an opener with text selected wraps
  the selection, and Enter inside a fresh pair opens the block out. Quotes are
  left alone straight after a word, so `don't` stays `don't`.
- A help panel with the shortcut list and an About tab, from the `?` in the top
  bar or F1.
- Line numbers in a gutter that stays aligned even when a long line wraps
  across several rows.
- Zoom in, out and reset. Zoom and the font size setting are one value, so
  changing either one moves the other.
- Tab size of 2, 4 or 8. It sets how wide a real tab character renders and how
  many spaces the Tab key inserts.
- Find and replace, with match case, whole word and regular expressions. Every
  hit is highlighted at once and the current one is picked out; Enter and
  Shift+Enter walk through them, wrapping at the ends. Replace one or replace
  all, with `$1` backreferences when the regex option is on. Replace all is a
  single edit, so one Ctrl+Z undoes the whole thing.
- Rename a file by clicking its name in the status bar, double-clicking it in
  the sidebar, or pressing F2. The extension drives the language, so renaming
  `notes.txt` to `notes.py` re-colors it. What happens underneath depends on
  where the file lives: a file with nothing on disk yet is simply relabelled; a
  file opened from disk is renamed **on disk** where the browser supports
  `FileSystemHandle.move`; and where it does not, TXTEDTR says so and offers to
  rename the tab while cutting it loose from the original file, so the next Save
  asks where to put it. What it will never do is show one name while writing to
  another.
- Closing every file leaves you with no file. The pane says so and offers the
  two ways out. See **When nothing is open** below.
- Zooming from the status bar as well as the keyboard: a minus and a plus
  either side of the percentage, and a slider if you click the percentage
  itself. All three drive the same list of sizes the Font size setting offers,
  so nothing can invent a size the rest of the app does not know about.
- Beautifying, from Shift+Alt+F or the wand in the top right. Real formatting
  for JSON, CSS, HTML, XML, JavaScript and Java; a whitespace tidy for Python,
  YAML, SQL, Shell and Markdown; greyed out for plain text. One Ctrl+Z undoes
  the whole thing, and a pass that would change more than whitespace is
  abandoned rather than applied. See **Beautifying** below.
- Printing, from Ctrl+P or "Print file" in the sidebar. **Which file** follows
  the same rule as Save - the focused pane's - but only while that is
  unambiguous. With two panes holding two files, or an editor beside a Markdown
  preview, it asks rather than guessing; the focused file is listed first. An
  HTML preview is not offered as a choice, so that case prints the source
  without asking: rendering the user's own markup into the print document would
  undo the sandbox the preview deliberately puts around it.
- Open, Save and Save As, plus drag and drop a file onto the window.
- Ctrl+/ toggles comments over whole lines, using each language's own syntax:
  `//` for JavaScript and Java, `#` for Python, YAML and shell, `--` for
  SQL, and the paired form for CSS, HTML, XML and Markdown, which have no line
  comment. If every non-blank line in the selection is already commented it
  uncomments, otherwise it comments the lot. Markers go in at the shallowest
  indentation in the block so the shape of the code survives. Plain text has no
  comment syntax, so the shortcut does nothing there rather than inventing one.
  Neither does JSON: a parser rejects comments, so commenting a config file
  would be a quiet way to break it.
- Tab and Shift+Tab indent and outdent whole blocks, Enter keeps indentation,
  and Ctrl+Z still works because edits go through the browser's own undo stack.

## Keyboard shortcuts

Press `F1` in the app, click the `?` in the top bar, or open Settings and click
Keyboard shortcuts, for this list. `Ctrl` is `Cmd` on a Mac.

Every shortcut has a switch beside it in that panel and every one starts on.
Turn off any that collide with your system - `Alt + 1 ... 9` is how ChromeOS
opens apps from the shelf, for instance - and the choice is remembered. "Turn
them all back on" at the bottom of the list undoes the lot.

The switches live in a `SHORTCUTS` table in the source, which is the single
source for the rows in the panel, the switches, and the guard the key handler
checks before acting - so a shortcut cannot end up listed but unswitchable, or
switched off but still firing. Only the disabled ones are stored, which means a
shortcut added later starts on for people who already have saved settings.

| Keys | Action |
| --- | --- |
| Ctrl + N / O / S | New / Open / Save |
| Ctrl + Shift + S | Save As |
| Ctrl + W | Close file |
| Shift + Alt + F | Beautify the current file |
| Ctrl + W | Close the current file - or the window, once no file is left |
| Ctrl + Plus / Minus | Zoom in / out (or the buttons in the status bar) |
| Ctrl + P | Print |
| F2 | Rename the current file |
| Alt + Down / Up | Next / previous file |
| Alt + 1 ... 9 | Jump to file |
| Ctrl + Tab | Next file |
| Ctrl + PgDn / PgUp | Next / previous file |
| Ctrl + F | Find |
| Ctrl + H | Find and replace |
| Ctrl + B | Show or hide the file sidebar |
| Ctrl + \\ | Split the view / unsplit |
| Ctrl + Shift + V | Preview HTML or Markdown |
| Ctrl + Comma | Settings |
| Ctrl + Plus / Minus / 0 | Zoom in / out / reset |
| Ctrl + scroll wheel | Zoom |
| Alt + Z | Toggle word wrap |
| Alt + L | Toggle line numbers |
| Tab / Shift + Tab | Indent / outdent |
| Ctrl + / | Toggle comment |
| F1 | Keyboard shortcuts and About |

One caveat while it runs as a web page: browsers keep `Ctrl + Tab` and
`Ctrl + PgUp` / `Ctrl + PgDn` for their own tabs, so those never reach the
editor there. `Alt + Up` / `Alt + Down` and `Alt + 1 ... 9` always work. Under
Electron there is no browser to intercept them and all of them work.

## How it works

### Panes

A pane is one complete editor: a gutter, the colored layer, and the text box
over it. There is one normally and two when the view is split, and they are
built in JS rather than written into the markup because the second comes and
goes.

The hinge the whole split rests on is that `el.gutter`, `el.wrap`,
`el.highlight` and `el.input` are **getters onto the focused pane**. Nearly
every function here - indent, comment, find, autoclose, rename, save - means
"the editor the user is typing in", so all of them kept working untouched when
the split arrived and simply follow the keyboard. Only the handful that must
address one particular pane - rendering, the gutter, scroll syncing - take one
as an argument.

Three layers stacked on top of each other:

```
+--------------------------------------------------+
| gutter |  <pre id="highlight">  colored text      |   painted, not editable
| 1 2 3  |  <textarea id="input"> invisible text    |   real typing happens here
+--------------------------------------------------+
```

The textarea sits on top with `color: transparent`, so you see its caret and
its selection but not its text. The `<pre>` underneath holds the same
characters wrapped in colored spans. Identical font, size, line height, padding
and wrapping rules on both layers is what keeps them aligned, so any change to
one has to be made to the other. The gutter holds one box per logical line, and
when word wrap is on each box is resized to match the height of the line it
labels.

The code is organised into eleven commented sections; the header comment in
`index.html` lists them.

## Saving settings

Settings live in one localStorage key, written whole by `saveSettings` every
time any of them changes.

`start()` puts them back by calling the ordinary setters, and each of those
saves as it goes. That is right once the app is running and wrong during
startup: a setter called early writes a state that is only half restored.

That is how the per-shortcut switches were being lost. `setStartIn` saved
while `state.shortcutsOff` was still its empty default, because the real value
was not read back in until the line after - so storage got `{}` written over
the good value. The switch survived one restart, from the copy already in
memory, and was gone by the next. Nothing else was affected, because every
other setting is written again by a later setter in the chain.

`restoringSettings` fixes it by suppressing writes for the length of the
restore and doing one save at the end, which makes the order stop mattering -
for that setting and for any added later.

## Risky characters

Text arriving by copy and paste - from a web page, a PDF, a chat window, a
Word document - carries characters that look like source and are not. A curly
quote will not close a Python string. A no-break space is not a space. A
zero-width joiner is not anything at all, and you cannot see it to delete it.

TXTEDTR marks them and offers to clean them. It never changes them behind your
back: the marker appears, the status bar counts them, and clicking that count
does the replacing and says what it changed. One Ctrl+Z puts it all back.

### Two tiers, because the same character can be right or wrong

| Tier | What | Where it is flagged |
|---|---|---|
| always | No-break and other look-alike spaces; zero-width space, non-joiner, joiner, word joiner, soft hyphen, stray BOM; line and paragraph separators; **bidirectional controls** | Every file, Markdown and plain text included |
| code | Curly quotes, primes, en and em dashes, minus sign, ellipsis, full-width forms, the Greek question mark | Only in JavaScript, Java, Python, JSON, CSS, SQL, Shell and YAML |

Markdown, plain text, HTML and XML are prose as often as not, so they get the
"always" tier only - a `.md` file is entitled to its curly quotes.

The bidi controls are the one entry that is an attack rather than an
annoyance. They reorder how source *displays* without changing what runs, so a
reviewer can read one program while the compiler reads another. They are
flagged everywhere, prose included.

Homoglyphs - a Cyrillic `а` among Latin letters - are deliberately **not**
flagged. There is no safe mechanical fix, and a file with Russian in it would
light up with false positives. Flagging them usefully needs to know they sit
inside an otherwise-ASCII identifier, which is more than this pass attempts.

### Two things that turned out not to need code

Both were on the original worry list and neither survived checking:

- **Line endings.** A `<textarea>` normalises CRLF and CR to LF on the way in,
  so mixed endings cannot exist inside the editor.
- **A BOM at the start of a file.** `Blob.text()` strips it during UTF-8
  decode. A BOM in the *middle* of a file does survive, and that one is
  flagged.

### Why it is not part of the beautifier

Every reindenting pass proves it moved whitespace only, by stripping `\s+`
from the text before and after and requiring the two to match. In JavaScript
`\s` covers a no-break space and a BOM, so swapping those for a plain space
would pass - but it does **not** cover zero-width characters, bidi controls,
curly quotes or dashes, so cleaning those would be refused as "changed more
than whitespace". Correctly: this is a different promise, so it gets its own
operation and its own report.

### The sub-pixel cost, measured

Wrapping a character in a span to mark it costs about 0.011px, whatever CSS is
attached - a bare span with no styling measures the same, because the browser
rounds each inline run's advance width independently. No `text-rendering` mode
avoids it; `geometricPrecision`, `optimizeLegibility` and `font-kerning: none`
all measure identically.

This is not new and not specific to the markers: the syntax highlighter has
always done it, at roughly 0.0156px per token span, or 0.078px on an ordinary
five-token line. A line with a handful of risky characters drifts about as
much as being highlighted at all. Two hundred on one line would reach 2px, but
a line like that has bigger problems.

Marker styling is therefore limited to `background` and `outline`, which paint
without occupying space. Padding, borders, font weight or letter-spacing would
pull the layers apart properly rather than by a fraction.

The scan is cached against the text it ran on, because `updateStatus` fires on
every keyup and most keystrokes do not change the document; and it is skipped
entirely above `MAX_HIGHLIGHT_BYTES`, the same threshold that turns off
highlighting.

## Beautifying

Shift+Alt+F, or the wand in the top right. What it does depends on the
language, because "beautify" means three quite different things and pretending
otherwise is how a formatter eats somebody's file.

| Tier | Languages | What happens |
|---|---|---|
| Rebuild | JSON | Parsed into data and written back out. Exact, because the parser is the authority on what the file meant. |
| Reindent | CSS, HTML, XML, JavaScript, Java | Whitespace moves and nothing else. No rewrapping, no normalised spacing inside a line, no opinion about where your braces go. |
| Tidy | Python, YAML, SQL, Shell, Markdown | Trailing whitespace, stray indent tabs, a missing final newline. |
| Nothing | Plain text | The button greys out. |

Python and YAML get the tidy tier rather than a reindent because indentation
IS the syntax there - reindenting them would not be tidying, it would be
rewriting the program. Markdown gets less again: two trailing spaces is a
deliberate line break, so the one thing tidy normally does is the one thing it
must not do there.

### The promises it makes

**One undo.** The whole reformat is applied by selecting the document and
typing over it via `execCommand`, so it lands as a single entry in the
browser's own undo stack. One Ctrl+Z puts the file back. Assigning to
`textarea.value` would be simpler and would throw the undo history away, which
is the wrong trade for a button whose first job is to be safe to press.

**Whitespace only, and it is checked.** Every reindenting pass is verified
before the edit is allowed to land: strip all whitespace from the text going
in and the text coming out, and the two must be identical. If they are not,
the edit is abandoned and the status bar says so. That one line catches the
entire class of bug where a formatter drops or duplicates a chunk of a file.
JSON is exempt because it legitimately normalises `1.0` to `1`; it is validated
by the parse instead, and invalid JSON is reported with the position rather
than half-formatted.

**Nothing happens on failure.** A refusal leaves the file untouched and
explains itself in the status bar - no modal, no partial edit.

### Where the reindenter is deliberately conservative

Indentation is taken from the **column of the line that opened the bracket**,
not from a count of open brackets. This matters more than it sounds. `foo(() =>
{` opens three brackets but is one decision by the author, and its body belongs
one step in from that line; counting brackets gives it three levels and makes
the pass useless on any modern JavaScript.

Lines that **continue** a statement keep the indentation they came with, moved
by however far their statement's first line moved. A column of leading `+`
under a long string, an argument list aligned under its opening bracket, the
body of a multi-line comment - all of it stays as written. Only lines that
begin a statement have their indentation decided here.

The test for this is the app's own source: running the reindenter over
`index.html`'s 3200 lines of JavaScript changes **nothing**. A formatter that
disagrees with well-formatted code is a formatter you cannot press.

Known limits, all of which cost a badly indented line and never broken code:
a regular expression is told apart from division by what precedes it, which is
a heuristic; `${...}` inside a template literal is treated as opaque; and a
braceless `if` whose condition wraps across lines does not get the one-line
body indent.

## Ctrl+W when there is nothing left

Ctrl+W (Cmd+W) closes the current file. Press it with no file open and it
closes the window instead, which is what the keystroke means everywhere else.

It gets there two different ways, because the same keystroke belongs to
different owners depending on where the app is running:

**In a browser tab**, Ctrl+W is the *browser's* shortcut for closing a tab.
The app normally intercepts it to close a file; with no file to close it stops
intercepting, and the browser does what the user already expects. No
`window.close()` is involved, and none would work - a page may not close a tab
it did not open.

**In an installed window** there is no tab, so `window.close()` is called,
which is permitted for an installed app. The keystroke is also left
unprevented, so if the platform has its own binding for it that fires too.
Either path closes the window; neither depends on the other.

No confirmation, because nothing being open is precisely the state where there
is nothing to lose - `beforeunload` has no unsaved file to warn about.

**Ctrl+Shift+W is untouched.** It closes the window whatever is open, on
Windows and ChromeOS, and that is a different promise worth keeping. Cmd+Q on
a Mac is the operating system's and was never the app's to intercept.

Because this is the one shortcut that ends the session, it has its own switch
in Settings, separate from Close file - so Ctrl+W can keep closing files
without ever quitting. The empty pane names the shortcut under its buttons,
and stops naming it when the switch is off.

## When nothing is open

The app opens with one file ready to type in, which is worth keeping - but it
used to guarantee that state forever. Every path that could leave a pane
without a file conjured a fresh `Untitled` instead: close your last file and a
new blank one appeared in its place, so "close everything" was not a thing you
could actually do.

A pane may now hold no file. `paneTab(p)` returns null, the textarea is
disabled, and the pane shows a message with a button for each way out - a new
file, or the Open dialog. Both target the pane they belong to, so in a split
view the file lands on the side you clicked.

Three call sites used to reach for `newUntitled` and no longer do: `closeTab`
when nothing is left to show a pane, `setSplit` when the new side has no spare
file to give it, and `setPreview(false)` when the pane coming back from
preview has nowhere to go.

`updatePaneMode` is the one place that decides which of the three things a
pane shows - the editor, a preview, or the no-file message. Having three
visibility flags set from three different functions is how you end up with a
pane showing two of them at once.

### What else had to stop lying

`updateStatus` used to `return` early with no file, which left the previous
file's name, caret position and line count sitting in the status bar
describing something that was no longer on screen. It now blanks those and
reads "No file open", and the filename stops advertising itself as clickable
because there is nothing to rename.

Save, Save As and Print grey out, the language dropdown disables, the find bar
declines to open, and the sidebar list says "No files open" rather than
appearing broken.

`Untitled` numbering restarts from 1 when the last file closes: after clearing
the desk you expect `Untitled-1`, not `Untitled-7`.

Every function that reads `activeTab()` already guarded for a missing tab, so
the change was mostly a matter of stopping the app from preventing the state
rather than teaching it to survive one. A test pokes seventeen of them with
nothing open to keep it that way.

## What the Save dialog suggests

The name field of the Save dialog is a suggestion, and `suggestedName` decides
it from what TXTEDTR actually knows:

| The file | Suggested name |
|---|---|
| Already on disk | Its own name, unchanged |
| Never saved, no language picked | `Untitled-1` - bare, no extension |
| Never saved, language picked | `Untitled-1.py` |

The reasoning behind the middle row: with the language dropdown still on Plain
Text, TXTEDTR does not know what the file is, so it does not pretend to. You
type the extension. Once you have picked a language you have said what the
file is, and the dialog should not make you say it again.

A file that came from disk keeps its own name because you already chose it,
and second-guessing that is how you end up with `report.txt.md`.

Switching language before the first save replaces a stale extension rather
than stacking another one on - but only when the existing extension is one
TXTEDTR recognises, so a name like `data.v2` keeps its suffix instead of
losing it to a bad guess.

## The zoom control

Three ways into one value, `state.zoomIndex`, which is an index into
`ZOOM_STEPS` rather than a font size. 100% is whatever the default step is, so
the percentage is a ratio against the size the editor opens at. The steps run
9px to 40px, which reads as roughly 64% to 286%.

Everything routes through `setZoomIndex`, which clamps. Putting the clamp
there rather than in each caller is why the buttons, the slider, Ctrl+plus and
Ctrl+scroll cannot disagree about where the ends of the range are, and why the
minus and plus can simply grey out when there is nowhere further to go.

`updateZoomControl` is the other half: it pushes `state.zoomIndex` back out to
all four visible pieces - the two steps, the readout, the slider - so
whichever one you touched, the rest catch up.

The slider's track and thumb are drawn in CSS rather than left to the browser.
A native range takes its unfilled track colour from `color-scheme`, not from
our variables, which put a bright white bar across the dark popover; setting
`color-scheme` on the input does not fix it in Chromium, and setting it on
`:root` would restyle every select and scrollbar in the app.

## Printing

A `<textarea>` does not paginate, so printing one loses everything past the
first page with no sign that it happened. The file is rebuilt instead as
ordinary elements inside `#print-doc`, and an `@media print` block hides the
whole interface and shows only that.

Two things are deliberately not inherited from the screen. Printing **always
wraps**, whatever the word wrap setting says, because paper has no sideways
scroll and an unwrapped long line would fall off the edge and be lost silently.
And source prints **black on white** rather than in syntax colors, since colored
code on a black-and-white printer turns to grey mush - change `#print-body` in
the print block if you would rather have colored handouts.

Line numbers follow the line-numbers setting, and the gutter widens to fit the
largest number so nothing clips past a thousand lines.

The print block also has to undo the app's own screen layout. On screen `html,
body` are pinned to the window with `height: 100%` and `overflow: hidden` so
the editor scrolls rather than the page, and `body` is a flex column. All three
are wrong on paper: together they crop the document at one page height and
throw the rest away silently, which is exactly the failure the rebuild was
meant to avoid. `@media print` therefore resets height, overflow and display
before anything else - if printing ever goes back to producing a single page,
that reset is the first thing to check.

## The preview belongs to the file

Each tab carries a `preview` flag. Turning the preview on sets it for the file
in front of you; everything else follows from that one fact:

- Close a file and its preview goes with it. Whatever surfaces in its place
  decides for itself - a file that wants no preview gets the full width.
- Come back to a file that had one and it comes back with it.
- Rename a file out of Markdown, or switch its language to something with
  nothing to render, and the preview closes rather than sitting there
  explaining why it is empty.

`syncPreview` is the single reconciler. It asks what the current file wants,
compares that with what is on screen, and opens or closes the preview to
match. Every path that can change the answer ends there: switching file,
closing one, renaming, changing the language, splitting, pressing the button.
It carries a reentrancy guard, because opening a preview calls `setSplit`,
which focuses a pane, and anything in that chain calling back in would
recurse.

The preview mirrors the FIRST editor pane, which is the pane it sits beside.
In a two-file split that means the left one - the same file the Preview button
has always acted on.

**Where the stale preview came from.** `activateTab` re-rendered the preview
when you switched files; `closeTab` never did. So closing a previewed file
handed the surviving pane a new one and left the preview rendering a file that
no longer existed. `syncPreview` repaints even when the layout does not
change, which is that case exactly.

**The split conflict.** A preview needs the right-hand pane. If you are
already looking at two files and you switch the left one to a file whose
preview is on, the preview takes that pane and the file that was there steps
aside - still open in the sidebar, just not displayed - and `previewRestore`
puts it back when you switch away. This is what the Preview button has always
done during a two-file split; now it happens on file switches too.

Unsplitting by hand while a preview is up clears the flag, so it does not
spring back the next time anything reconciles.

## Turning the preview off

Closing the preview puts the view back the way it was, which depends on how it
got there:

| When the preview opened | When it closes |
|---|---|
| From one pane - the preview split the view itself | Back to one full-width pane |
| From a split you already had | The split stays, and the pane gets back the file the preview displaced |

`previewRestore` is the note that makes this possible: turning the preview on
records whether the view was already split and which file the pane it took
over was holding.

The split is the part that matters. When the preview has to split the view to
make room for itself, that second pane exists for one reason, and leaving it
behind means closing the preview drops you into a split you never asked for
with nothing on the other side. Closing the preview means "let me get on with
the file".

Two related cases fall out of the same rule. Closing your last file while
previewing closes the preview too, since a preview with nothing to mirror is a
preview of nothing - so you land on one empty pane rather than an empty editor
beside an empty preview. And unsplitting by hand while previewing discards the
note, because the pane it referred to is gone.

## The preview pane

HTML and Markdown are handled by deliberately different machinery.

**HTML** goes into an `<iframe sandbox="allow-scripts">`. Note what is *not*
there: `allow-same-origin`. The previewed page can run its own JavaScript but
sits in an opaque origin, so it cannot reach TXTEDTR's storage, DOM or file
handles. Granting both flags together is the classic mistake - it undoes the
sandbox completely. The cost of the sandbox is that relative paths do not
resolve, so `<img src="logo.png">` and sibling stylesheets come up empty;
self-contained pages preview perfectly.

**Markdown** is rendered by `renderMarkdown` into an ordinary div, not a frame.
That is safe because every byte of that HTML is generated here from escaped
input, and it means the preview keeps its scroll position while you type, where
an iframe reloads and jumps to the top.

The renderer is a deliberate subset, not CommonMark. It covers ATX headings,
fenced code, blockquotes, nested lists, GFM tables, rules, paragraphs, and the
usual inline run - code spans, bold, italic, strikethrough, links, images and
bare URLs. It does **not** cover reference-style links, setext headings,
indented code blocks, or raw HTML. Raw HTML is escaped and shown as text, which
is the safe direction to be wrong in. URLs with a `javascript:`, `data:` or
`vbscript:` scheme are rewritten to `#`.

## Keeping the preview's place

An HTML preview refreshes by being reloaded - a new `srcdoc` is a new
document, and a new document starts at scroll zero. On a long file that means
every keystroke threw the reader back to the top.

It cannot be fixed from outside the frame. The preview is sandboxed **without**
`allow-same-origin`, so it sits in an opaque origin and the app cannot read
its `scrollY` before the reload or set it afterwards. Adding `allow-same-origin`
would make both possible and dismantle the sandbox in the same stroke - the
previewed page could then reach TXTEDTR's own DOM and storage. A scroll
position is not worth that.

So a small shim rides along inside the previewed document instead
(`previewShim`). It reports where the reader is by `postMessage`, which crosses
that wall without opening it, and restores the position after the next reload.

Two details carry the weight:

**The position is written into the shim, not requested over `postMessage`.**
The parent already knows where the reader was, so it bakes the number into the
script it appends. The scroll therefore happens while the document is still
parsing, rather than after a round trip - the difference between staying put
and visibly jumping to the top and back.

**The reload check compares the TEXT, not `srcdoc`.** `srcdoc` now carries the
shim, and the shim changes every time the reader scrolls; comparing the whole
string would reload the frame on every scroll, which is the original bug only
worse. `p.previewText` holds the last text handed over, and that is what gets
compared.

The shim stops forcing the scroll the moment the reader moves it themselves,
so a late-loading image cannot yank them back. A document that has since got
shorter clamps and stays clamped rather than fighting. Switching to a
different file starts at the top.

Incoming messages are guarded on `e.source` rather than origin - an opaque
origin gives nothing to compare - and the payload is shape-checked, because
anything inside that frame can post to us, including the user's own page.

Two limits worth knowing. An unclosed `<!--` in the previewed HTML swallows
the shim, and that preview goes back to jumping; nothing else breaks. And a
reload still resets what a scroll position cannot cover: form fields typed
into inside the preview, CSS animations, and any state the previewed page's
own scripts were holding. Avoiding that needs no reload at all, which needs
same-origin access, which is the trade refused above.

## Adding a language

The Language dropdown is sorted by label so it can be scanned by letter.
Only the dropdown is sorted: `LANGUAGES` itself keeps its own order, because
`EXT_TO_LANG` is built by walking it and which language wins a shared
extension depends on that order. The sort collates with `sensitivity: "base"`
so case does not decide it - a plain comparison puts JSON above JavaScript,
because "S" sorts before "a".


In section 4, add an entry to `LANGUAGES`:

```js
mylang: {
  label: "My Language",
  ext: ["ml", "mylang"],
  rules: [
    { re: /#.*/y,       cls: "tok-comment" },
    { re: RE_QUOTED,    cls: "tok-string"  },
    identifierRule(words("if else while"), words("print len")),
    { re: RE_NUMBER,    cls: "tok-number"  }
  ]
}
```

Two rules of thumb: every regex needs the sticky flag `y`, and rules are tried
in order, so comments and strings go first.

Optionally add a line to `LANGUAGE_ICONS` just below to pick the mark it gets in
the sidebar, and one to `COMMENTS` to teach Ctrl+/ how that language writes a
comment. Leaving either out is fine - an unlisted language falls back to the
plain page icon, and one with no comment syntax simply cannot be commented.

## Wrapping it in Electron

The webapp is the whole app. Electron just gives it a window, a real menu bar
and unrestricted disk access.

```
txtedtr/
  index.html      <- this file, unchanged
  main.js
  package.json
```

`package.json`:

```json
{
  "name": "txtedtr",
  "version": "1.0.0",
  "main": "main.js",
  "scripts": { "start": "electron ." },
  "devDependencies": { "electron": "^32.0.0" }
}
```

`main.js`:

```js
const { app, BrowserWindow } = require("electron");
const path = require("path");

function createWindow() {
  const win = new BrowserWindow({
    width: 1100,
    height: 750,
    webPreferences: {
      // Security defaults. The page is plain HTML and JS and needs neither
      // Node nor a shared context, so do not hand it either.
      nodeIntegration: false,
      contextIsolation: true
    }
  });
  win.loadFile(path.join(__dirname, "index.html"));
}

app.whenReady().then(() => {
  createWindow();
  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});
```

Then:

```
npm install
npm start
```

That is the entire port. Electron runs Chromium, so the File System Access API
that Open and Save already use is available and everything keeps working.

When you want a native File menu, or want to open a file by double-clicking it
in Finder or Explorer, that is when you replace the `FileBridge` object in
section 8 with calls over `ipcRenderer` to Node's `fs` in the main process. The
rest of the editor does not touch the disk, which is why that swap is contained
to one object.

To ship an installer, `electron-builder` is the usual next step.

## Known limits

- **No multiple cursors.** This is a property of the architecture, not an
  oversight. The editor is a real `<textarea>`, and a textarea has exactly one
  selection - `selectionStart` and `selectionEnd`, one pair of numbers. There is
  no API for a second caret, and the multi-range Selection API does not apply to
  form fields. Getting multiple cursors means giving up the textarea for a
  `contenteditable` element with an entirely synthetic caret, selection model,
  input pipeline and undo stack - which is what CodeMirror and Monaco are, and
  most of why they are as large as they are. Find and replace with regular
  expressions covers most of what people reach for multiple cursors to do.

- **No "always on top."** A web page cannot raise its own window above other
  applications - there is no API for it, by design, and no manifest field
  either. It is one line in an Electron wrapper
  (`new BrowserWindow({ alwaysOnTop: true })`). The only browser-side
  approximation is the Document Picture-in-Picture API, which does open a
  genuinely always-on-top window, but it is a small floating panel that the
  whole editor would have to be moved into, and the normal app window stays
  open behind it.

- Highlighting is regex based, not a parser. It is accurate on normal code and
  imperfect on unusual code. JavaScript regular-expression literals are not
  highlighted, because telling `/` the divide operator from `/` the start of a
  regex needs real parsing.
- HTML does not highlight the contents of embedded `<script>` and `<style>`.
- Files over 400 KB render as plain text so typing stays responsive.
- Preferences are kept in `localStorage`. If that is unavailable the editor
  still runs, it just starts from defaults each time.

## Icons in the interface

Two sets, both inlined as SVG path data rather than loaded from a package or a
CDN - the same reason nothing else here has a dependency.

**Interface glyphs** are [Lucide](https://lucide.dev), in the `ICONS` table.
They share one frame: 24x24, no fill, a 2px round-capped stroke inheriting the
text color.

**Language marks** in the sidebar are [Simple Icons](https://simpleicons.org),
in the `LOGOS` table. Simple Icons publishes every brand mark as a single SVG
path under CC0, which is what makes them practical here - one line each. They
are filled shapes rather than strokes, so `setIcon` checks which table a name
came from and writes the matching wrapper.

Adding an icon to either set means pasting the innards of its SVG as one more
line in the right table. Languages with no brand mark - plain text, XML, SQL,
JSON, Java - use a Lucide icon instead; Java's cup is a trademark and is not in
Simple Icons, and Lucide's coffee cup reads better at 14px than the OpenJDK
mark would.

The colored marks carry their brand color, defined per theme in `--lang-*`.
Each value is the brand color nudged toward white or black until it clears 3:1
against the sidebar, which is the WCAG bar for a meaningful graphic. JavaScript
moves furthest: `#f7df1e` is effectively invisible on a light chrome.

## Ideas for next

Find and replace, a session that reopens yesterday's tabs, a native Electron
menu bar, per-tab detected indentation, and a minimap if you ever want one.
