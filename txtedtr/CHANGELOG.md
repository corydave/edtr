# TXTEDTR changelog

A single-file HTML text editor, no dependencies and no build step.

The version lives in one place - `APP_VERSION` in `index.html`. Bumping it and
uploading is the whole deploy: the service worker builds its cache name from
that string, so a new version rotates the cache and users get the new build the
next time they open the app.

The same history, condensed to one line per change, is in the app itself under
Help (F1) -> Changelog. That copy is a `CHANGELOG` table in `index.html`, so
adding a release means editing both.

A note on accuracy: entries from **1.3** onward are exact. Earlier ones are
reconstructed from the build history, and the work before 1.1 shipped with no
version number at all, so it is grouped rather than split into releases it
never had.

---

## 1.23

**Changed** - zoom for a projector.

- **The top of the zoom range went from 286% to 514%.** `ZOOM_STEPS` gains 48, 56, 64 and 72px on top of the old ceiling of 40px. Everything that draws the control - the minus/plus buttons, the percentage readout, the slider's `max`, the Font size dropdown and the clamp in `setZoomIndex()` - is derived from `ZOOM_STEPS.length`, so adding sizes to the end of the array is the whole change. Saved settings keep working too: the stored value is an index, and appending never shifts the indexes that already exist.
- The small end is untouched, and 14px is still 100%.

## 1.22

**Changed** - made for fingers.

- The shared SUITE block was pasted in again (new: the touch standard, `SUITE_TOUCH` and `suiteNumberPop()`).

## 1.21

**Changed** - the source, front and center.

- **The top bar is the family's standard 52px tall**, and Inspector headings and labels match IMGEDTR's (headings 12px bold capitals with .08em spacing, labels 13px).
- **About starts with a "View the source on GitHub" button** (github.com/corydave/edtr), with a line on why: free and open source (MIT license), runs in your browser, keeps your files on your device, needs no sign-in, works offline.
- The shared SUITE block was pasted in again from `_edtr-suite` (new: `suiteSourceBox()`, drawn by `renderSuiteCredits()`).

## 1.20

**Changed** - links to edtrapps.com and GitHub.

- Under the credits on the "no file open" screen, and in About: "All the apps at edtrapps.com - Free and open source on GitHub (MIT license)". edtrapps.com is the new home of the whole family; the source is github.com/corydave/edtr, now with an MIT license at its root.
- The shared SUITE block was pasted in again from `_edtr-suite` (it also carries the other apps' new splash).

## 1.19

**Added** - a tour of the features.

- **Features, a new first tab in Help** (F1 or the Help button): an animated tour of five of TXTEDTR's favorite features - Live HTML preview, Color-coded code, Smart find and replace, Catches hidden characters and Split view - each with a small looping drawing, a title and a sentence or two. Previous and Next, the dots, or the Left and Right arrow keys move between them; the animation has a pause button, and it starts paused when the device asks for less motion. Keyboard shortcuts is one tab over. (The ? key itself stays a character you type, as before.)
- **The "no file open" screen ends with a "See what TXTEDTR can do" card**, after the row of apps and the credits, which opens the same tour.
- The shared SUITE block was pasted in again from `_edtr-suite` (new: `renderSuiteFeatures`, `suiteFeaturesOpen`, `suiteFeaturesCard` and their styles).

## 1.18

**Fixed** - the installed app opens again after the move to the new host.

After txtedtr.app moved from HostGator to Cloudflare, the installed app (and "Open with TXTEDTR" from the computer) showed "This site can't be reached" (ERR_FAILED) until a hard refresh. Cause: the app started at `./index.html`, Cloudflare answers `/index.html` with a redirect to `/`, and Chrome will not open an app window with a redirected response handed over by a service worker. The other apps start at `./`, so they never hit it.

- `manifest.webmanifest`: `start_url` and the file handler's `action` are now `./`. An explicit `"id": "./index.html"` keeps the app's identity the same, so existing installs update in place rather than becoming a second app.
- `sw.js`: caches `./` instead of `./index.html`, and a new `cleanResponse()` copies any redirected response into a clean one before handing it over, so old shortcuts that still point at `/index.html` open too, online and offline.

## 1.17

**Changed** - DSKEDTR joins the family.

Help -> More apps and the row of apps on the "There is no file open" screen now include DSKEDTR (dskedtr.app), the new desktop publishing app (newsletters, flyers and booklets, with text that flows between boxes), with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js` and `suite-block.css`; with nine apps, the row shows 4 + 4 on a phone.

## 1.16

- Names of the other apps in Help (in the changelog, About and the guides) are now links that open that app. Each link opens in a new tab; this app's own name stays plain. Shared SUITE block: new `suiteLinkApps()` (called from `renderSuiteApps()`, so no app wiring needed).

## 1.15

**Changed** - 3DEDTR joins the family.

Help -> More apps and the row of apps on the "There is no file open" screen now include 3DEDTR (3dedtr.app), the new 3D modeling app with shape merging, with its own icon. The shared SUITE block was pasted in again from `_edtr-suite/suite-block.js` and `suite-block.css`; with eight apps, the row shows 4 + 3 on a phone.

## 1.14

**Changed** - Help -> More apps shows each app's real icon.

TXTEDTR's copy of the shared SUITE block was the first version (v1), which drew a simple line icon on a blue tile for every app. It now has the current block (v4) from `_edtr-suite/suite-block.js` and `suite-block.css`, the same as the other apps, so More apps shows the apps' real icons.

**Added** - the rest of the app family on the "There is no file open" screen.

Under the Create and Open buttons, a row of icons for the other apps (each opens in a new tab), with the credits line underneath - the same row the other apps show on their splash screen. In split view only the left pane shows it, so it never appears twice. TXTEDTR's start-up is unchanged: it still has no splash screen.

## 1.13

**Added** - VCTREDTR in Help -> More apps.

The new vector drawing app (vctredtr.app) joins the list of apps in the family. Only its entry in `SUITE_APPS` was added: TXTEDTR keeps its v1 copy of the shared block, as before.

## 1.12

**Added** - the Save dialog works out the file type from the file's contents
when you have not said what it is.

Until now the suggested extension came from the Language dropdown, which meant
it only worked once you had told it. Type a page of HTML into a new file and
press Save, and the dropdown still said Plain Text - so the suggestion was a
bare name. `sniffExtension` reads the text instead, and suggests `.html`.

It recognises HTML, CSS, JavaScript, JSON, Python, Java, Markdown, SQL, shell,
YAML, XML and **PHP** - the last of these by extension only, since the editor
has no PHP highlighting yet.

**It is a suggestion, never a rule.** The name field is still yours to
overwrite, and three things outrank the sniffer: a file that came from disk
keeps its own name, a language picked from the dropdown wins, and choosing
"Plain Text" by hand is treated as a real answer rather than an absent one
(`tab.langChosen`).

### Deliberately timid

Every rule wants a signal that is hard to produce by accident, and when
nothing is certain it returns nothing at all and you get the bare name you
used to. A wrong suggestion is worse than none - that one is a single Enter
away from a file called `notes.js` that is not JavaScript.

Ordering is mostly about files that are honestly two things at once: PHP is
usually HTML too, so PHP is tested first; XML opens with a tag like HTML, so
XML is first; JSON is valid JavaScript, so JSON is first; and a fenced code
block is tested before the languages it can contain, or a Markdown file
explaining some JavaScript reads as JavaScript. Markdown's own rules come
last, because `# something` is a heading here and a comment in half the
languages above - it wants two signals, which keeps a commented Python file
out of it.

`stripQuotedMarkup` blanks quoted runs containing `<` before the markup rules
look, so a JavaScript file holding `el.innerHTML = '<div><p>hi</p></div>'` is
not offered a `.html` name. Only runs containing `<`, and only within one
line: broader than that it eats ordinary prose between two apostrophes.

**Known limit:** a file that quotes or discusses another language unquoted can
still be misread. The detector's own source and its test corpus both are, which
is how that limit was found. The cost is bounded to a wrong suggestion in a
dialog you can edit.

Tested against 53 synthetic cases including the traps above, and 15 real files.

## 1.11

**Added** - a More apps tab in the help panel, after Keyboard shortcuts, About
and Changelog. It lists every app in the family (TXTEDTR, PDFEDTR, IMGEDTR,
SNDEDTR, VIDEDTR, SCRNCSTR) with this one marked "You are here". The list is
the shared SUITE block, pasted identically into every app, so it works offline
and never asks a server for anything. Clicking the logo opens the tab directly.

**Changed** - the theme button moved in front of the help button. Every app in
the family now ends its top bar the same way: Inspector (where there is one),
Theme, Help, Settings.

## 1.10.1

**Changed** - About and Changelog swapped places in the info panel, so the tab
order runs Keyboard shortcuts, About, Changelog.

`populateChangelog` now warns to the console when no entry matches
`APP_VERSION`. Bumping the version without adding the entry would silently
drop the "you are here" badge and leave the panel implying the newest release
is one behind - invisible to a user, which is exactly why it needs saying
somewhere.

## 1.10

**Added** - a Changelog tab in the info panel, beside Keyboard shortcuts and
About. Newest release first, with the version you are running marked.

Its entries live in a `CHANGELOG` table inside `index.html` rather than being
fetched from this file, because the app is meant to work opened straight off a
disk or launched offline from the service worker cache, with nothing beside
it. The in-app entries are the short form - one scannable line each - and this
file is the long form with the reasoning. **A new release needs adding in both
places.**

## 1.9.1

**Fixed** - settings did not survive a second restart.

`start()` restores settings by calling the ordinary setters, each of which
saves as it goes. That is right once the app is running and wrong during
startup, where a setter writes a state that is only half restored.
`setStartIn` saved while `state.shortcutsOff` was still its empty default, so
storage got `{}` over the good value. The per-shortcut switches survived one
restart from the copy still in memory, then vanished.

Writes are now suppressed for the length of the restore, with one save at the
end, so the order stops mattering. The bug predates 1.9 - it arrived with the
per-shortcut switches.

## 1.9

**Added** - risky character detection.

Characters that look like source and are not get a marker in the editor and a
count in the status bar; clicking the count replaces them and reports what
changed. Never silent, and one Ctrl+Z undoes the lot.

Two tiers. *Always*: look-alike spaces, zero-width characters, soft hyphen,
mid-file BOM, line and paragraph separators, and bidirectional controls - the
"Trojan Source" problem, the one entry that is an attack rather than an
annoyance. *Code only*: curly quotes, primes, dashes, minus sign, ellipsis,
full-width forms, the Greek question mark. Prose languages keep their
typography.

Homoglyphs are deliberately not flagged - no safe mechanical fix, and a file
containing Russian would light up with false positives.

Two items investigated and found to need no code: a `<textarea>` normalises
CRLF and CR to LF on input, so mixed line endings cannot exist; and
`Blob.text()` strips a leading BOM during decode.

## 1.8

**Changed** - the preview now belongs to the file rather than to the layout.

Each tab carries a `preview` flag, and one reconciler makes the view match it.
Close a file and its preview goes with it; whatever surfaces decides for
itself; come back to a file and its preview returns. Renaming or switching a
file out of a previewable type closes the preview rather than leaving it
explaining why it is empty.

**Fixed** - the stale preview. `activateTab` re-rendered the preview on a file
switch; `closeTab` never did, so closing a previewed file left the preview
rendering a file that no longer existed.

Consequence worth knowing: opening a *new* file while previewing closes the
preview, because the new file arrives without one.

## 1.7.1

**Fixed** - the HTML preview snapped to the top on every refresh.

The preview is sandboxed without `allow-same-origin`, so its scroll position
cannot be read or set from outside. A small shim rides along inside the
previewed document instead, reporting position by `postMessage` and restoring
it after the next reload. The position is baked into the shim rather than
requested afterwards, so the scroll happens while the document is still
parsing.

## 1.7

**Added** - Ctrl/Cmd+W closes the window once no file is left.

In a browser tab the app stops intercepting the key and lets the browser close
the tab; in an installed window it calls `window.close()`. Has its own on/off
switch, separate from Close file. Ctrl+Shift+W is untouched.

## 1.6.1

**Fixed** - closing the preview left the view split with an empty pane.

Closing it now restores whatever was there before: one full-width pane if the
preview created the split, or the previous two-file split with its displaced
file put back.

**Changed** - the Language dropdown is sorted alphabetically. Only the
dropdown; the `LANGUAGES` table keeps its own order, because `EXT_TO_LANG` is
built by walking it.

## 1.6

**Changed** - closing every file leaves you with no file.

The app used to conjure a fresh `Untitled` whenever the last one closed, which
made "close everything" impossible. A pane may now hold nothing and says so,
with buttons for New and Open. The status bar, sidebar, Save, Save As and
Print all follow suit rather than describing a file that is not there.

## 1.5

**Added** - the version number beside the wordmark, in small grey italics, fed
from `APP_VERSION`.

**Added** - zoom controls in the status bar: minus and plus either side of the
percentage, and a slider when the percentage itself is clicked.

**Changed** - the Save dialog suggests a smarter name. An unsaved file with no
language picked suggests a bare name; one whose language you set suggests that
extension. A file already on disk keeps its own name.

## 1.4

**Added** - the beautifier, on a wand icon and Shift+Alt+F.

Three tiers. *Rebuild*: JSON, parsed and rewritten. *Reindent*: CSS, HTML,
XML, JavaScript, Java - whitespace moves and nothing else. *Tidy*: Python,
YAML, SQL, Shell, Markdown - trailing whitespace and stray indent tabs only,
because in Python and YAML indentation is the syntax.

Every reindenting pass proves it moved whitespace only before the edit lands;
a failure abandons the edit rather than guessing. The whole reformat is one
undo step.

Indentation derives from the column of the line that opened a bracket, not a
count of open brackets, and continuation lines keep the alignment they came
with. The test is the app's own source: reindenting its 3,200 lines of
JavaScript changes nothing.

## 1.3

**Added** - printing, on Ctrl+P and a sidebar button.

A `<textarea>` does not paginate, so the file is rebuilt as ordinary elements
and an `@media print` block shows only that. When two things could sensibly go
to the printer, it asks which. Printing always wraps, whatever the word wrap
setting says.

**Fixed** (1.3.1) - only the first page printed. The app pins itself to the
window on screen, and height, overflow and display all had to be undone for
paper.

## 1.2.1

**Fixed** - the preview pane could be handed a file, leaving the two panes
disagreeing about what was on screen.

**Fixed** - the PREVIEW header shifted its pane down relative to the source.
Both panes now carry a header.

**Changed** - Save As starts in Desktop rather than Documents.

## 1.2

**Added** - the live preview pane.

HTML and XML render in an iframe sandboxed with `allow-scripts` but
deliberately *without* `allow-same-origin`. Markdown goes through a hand-rolled
renderer into a plain div, which keeps its scroll position where an iframe
would reload.

## 1.1

**Added** - the two-pane split view, with the sidebar kept as the file list.

Panes became an abstraction with `el.gutter`, `el.wrap`, `el.highlight` and
`el.input` as getters onto the focused one, which is what let the split arrive
without rewriting every function that touches the editor.

**Added** - `APP_VERSION`, and with it the deploy ritual.

## Before 1.1

Everything up to here shipped unnumbered.

- The editor core: a transparent `<textarea>` over a syntax-highlighted
  `<pre>`, with a gutter as a third column. Chosen over CodeMirror and Monaco
  to keep the single file and the zero dependencies.
- Syntax highlighting for HTML, CSS, JavaScript, JSON, Python, Markdown, SQL,
  Shell, XML, YAML - and Java.
- Light and dark mode; tabs for multiple open files; zoom shortcuts;
  toggleable line numbers with a narrow gutter; Open, Save and Save As;
  toggleable word wrap.
- A redesign: a collapsible sidebar holding just the open files, a slim top bar
  with the cog and the theme toggle, and settings in a modal. Font size and tab
  size added there.
- A `?` icon opening a tabbed Keyboard shortcuts / About panel, with a
  per-shortcut on/off switch - Alt+1 to 9 opens shelf apps on a Chromebook.
- Installable as a PWA: manifest, icons, file associations, and a service
  worker for offline launching. Network-first for the document with
  `cache: "no-store"`, because the browser's own HTTP cache was defeating it.
- Find and replace with regular expressions.
- Click-to-rename filenames, in the status bar and the sidebar.
- Ctrl+/ comment toggling, per language. JSON is excluded on purpose: parsers
  reject comments, so commenting a config file would be a quiet way to break
  it later.
- Inlined Lucide icons for the interface and Simple Icons logos for the file
  marks, every one checked to clear 3:1 contrast in both themes.
