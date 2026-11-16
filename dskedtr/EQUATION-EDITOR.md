# The equation editor (from DSKEDTR 0.47.0)

A guide to the equation component in DSKEDTR, written so it can be lifted
into another project. It covers what the component does, how it is built,
the pieces you need to copy, the hooks the host app must provide, and the
traps found while building it.

The working code is in `dskedtr/index-online.html`:

- the dialog's HTML follows the comment `EQUATIONS (0.47.0)` (around line 2283);
- the JavaScript module follows the block comment `EQUATIONS (0.47.0)` (around line 18288, ending just before `function wireTemplates`);
- the CSS follows the comment `/* Equations (0.47.0)` (next to the `.changelog` rules).

---

## 1. What it does

- One dialog, three ways to write the same thing (a LaTeX string):
  - **Build it**: MathLive's visual editor. Type as on a calculator (`/` makes a fraction, `^` a power), or use its keyboard of symbols, which opens by itself on touch screens.
  - **Type LaTeX**: a textarea, plus buttons that insert the usual pieces at the cursor.
  - **Chemistry**: mhchem syntax (`2H2 + O2 -> 2H2O`), stored as `\ce{...}`, with buttons and examples.
- The preview updates as you type, and mistakes are described in plain words ("Not right yet: Missing close brace"). The Add button stays disabled until the equation is valid.
- Alt text is written automatically from the equation, can be edited, and can be reset to the automatic words.
- The result is drawn as **vector outlines**, not as live maths. After it is made, nothing needs MathJax or MathLive to show, print, export or save it.

---

## 2. The big decision: MathJax draws, MathLive edits

| Job | Library | Why |
|---|---|---|
| Turn LaTeX into shapes | **MathJax 3.2.2**, `es5/tex-svg-full.js` (Apache 2.0) | It writes pure SVG paths. KaTeX writes HTML and CSS fonts, which can't become part of an SVG drawing or a PDF. MathJax reads the same LaTeX, and it includes mhchem. |
| Visual editing | **MathLive 0.111.1**, `mathlive.min.js` (MIT) | A good `<math-field>` element with an on-screen keyboard. It uses the KaTeX fonts (20 `.woff2` files). |
| Alt text for maths | MathLive's `convertLatexToSpeakableText` | It works well once tidied (see section 7). |
| Alt text for chemistry | Our own `chemSpeech` | MathLive returns an empty string for `\ce`. |
| MathML for HTML export | `MathJax.tex2mml` | It is rebuilt through a whitelist (see section 8). |

MathLive has **no `\ce` support**, so chemistry can't be built visually. That is why chemistry has its own tab.

If the other project only needs to *display* maths in HTML (no PDF, no canvas), KaTeX alone is lighter. Everything below assumes you want shapes.

---

## 3. Files to bring

```
vendor/tex-svg-full.js        MathJax 3.2.2 (2.3 MB)
vendor/mathlive.min.js        MathLive 0.111.1 (0.8 MB)
vendor/mathlive-fonts/        KaTeX_*.woff2, 20 files (300 KB)
vendor/LICENSES.txt           MathJax (Apache 2.0), MathLive and KaTeX fonts (MIT)
```

The CDN addresses and their fingerprints. The fingerprints were computed from the npm packages, which jsDelivr serves unchanged:

```js
const MATH_LIBS = {
  mathjax: {
    id: 'libMathJax',
    url: 'https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg-full.js',
    sri: 'sha384-4kE/rQ11E8xT9QgrCBTyvenkuPfQo8rXYQvJZuMgxyPOoUfpatjQPlgdv6V5yhUK'
  },
  mathlive: {
    id: 'libMathLive',
    url: 'https://cdn.jsdelivr.net/npm/mathlive@0.111.1/mathlive.min.js',
    sri: 'sha384-fnT74hn6eDg87dvsrlWHThK0ymBGqcjBpUEH0G2PGfpjT1Np0HMWfmheS3xKuzoX'
  }
};
```

---

## 4. Loading: only when the editor opens

Neither library loads at start-up. `loadMathLibs()` runs the first time the dialog opens, and it returns the same promise every time after that.

- **Online edition:** a `<script src integrity crossorigin="anonymous">` from jsDelivr. The browser refuses a file whose fingerprint doesn't match.
- **One-file (offline) edition:** both libraries sit in the page as **text**:
  ```html
  <script type="text/plain" id="libMathJax">...</script>
  <script type="text/plain" id="libMathLive">...</script>
  ```
  The browser does not run `type="text/plain"` blocks, so start-up stays fast. To run one, `addMathLib()` creates a new `<script>`, sets its `textContent` to the block's text, and appends it to the page. The CSP needs `'unsafe-inline'` in `script-src` for this. No `blob:` or `eval` is needed.
- `build-offline.py` puts the blocks in at the marker comment `<!--MATH-LIBRARIES ...-->`. It first checks each vendor file against the SRI in `MATH_LIBS`, and it escapes `</script` as the other inlined libraries do. A lone `<!--` is harmless: MathJax has one, in a regular expression. It only becomes dangerous if `<script` also appears, so the build refuses that combination.

**MathJax settings** have to be set on `window.MathJax` *before* the script runs:

```js
window.MathJax = {
  loader:  { load: [] },              // never fetch extra components
  startup: { typeset: false },        // don't touch the page
  options: { enableMenu: false, enableAssistiveMml: false, enableExplorer: false, enableEnrichment: false },
  tex:     { packages: MATH_PACKAGES, maxBuffer: 20 * 1024, maxMacros: 2000 },
  svg:     { fontCache: 'none' }      // every glyph inline, no <use> references
};
```

Then wait for `MathJax.startup.promise` before calling anything.

**MathLive settings**, applied right after it loads:

```js
MathLive.MathfieldElement.fontsDirectory = null;   // we supply the fonts ourselves
MathLive.MathfieldElement.soundsDirectory = null;  // no clicks or beeps fetched
// then one FontFace per KaTeX font: a data: URI in the offline edition
// (DSK_EMBEDDED.mathFonts), vendor/mathlive-fonts/*.woff2 online
```

The family, style and weight for each font file are listed in `MATH_FONTS` in the module.

---

## 5. LaTeX to outlines

`texToArt(latex)` returns either `{ contours, w, h }` or `{ error }`.

1. `MathJax.tex2svg(latex, { display: true })` returns an `mjx-container` with an `<svg>` inside.
2. Mistakes appear as an element `[data-mml-node="merror"]`. Its message is in `data-mjx-error`, or failing that in its `textContent`.
3. The viewBox is in MathJax units: **1000 to the em**. Its x and y are negative (the box starts above the baseline), so the outlines are shifted to put the top-left at 0, 0.
4. `svgToContours(svg)` walks the SVG, combining each element's `transform` into one matrix as it goes:
   - `<path>`: the letters and symbols. Quadratic curves (`Q`, `T`) become the exact cubic curve (control points 2/3 of the way to the quadratic's control point). `S` and `T` reflect the previous control point.
   - `<rect>`: fraction bars and root bars. An outlined rect (from `\boxed`) becomes four thin bars.
   - `<line>` (from `\cancel`): a thin rectangle along the line.
   - Outlined `<ellipse>` or `<circle>` (from `\enclose`): a ring, an outer outline plus a reversed inner one.
   - `<text>`: a character MathJax's fonts don't have (é, 東). It is drawn with the host's own opentype.js font (in DSKEDTR, Atkinson Hyperlegible).
   - Everything else is ignored. **Nothing from MathJax's SVG is ever put on the page as it is**; only the numbers are read out of it.
5. `artAtSize(art, size)` scales the outlines to points for letters `size` pt tall (`k = size / 1000`), rounded to 0.01.

**Contour format** (the same as DSKEDTR's merged shapes):

```js
{ closed: true, pts: [[x, y, inX, inY, outX, outY], ...] }   // handles relative to the point
```

**Fill rule:** use **non-zero** for equations. Glyphs overlap, and even-odd would punch holes where they cross.

---

## 6. The data model

In DSKEDTR an equation is a `type: 'path'` object with an `eq` field:

```js
{
  type: 'path', x, y, w, h, w0, h0, contours, fill, stroke, strokeWidth, alt, decorative: false,
  eq: { latex, mode: 'visual' | 'latex' | 'chem', size /* pt it was made at */, altAuto: true }
}
```

- The outlines are made at `eq.size`. The object can be shown at any size: the letter size shown is `eq.size * w / w0`.
- Editing the equation keeps the object's top-left corner and its current scale.
- `altAuto` stays true until someone types alt text. After that, a change to the equation keeps their words.
- **Loading a file:** keep `eq` only if `latex` is a non-empty string. Pass it through `cleanText(latex, 5000, true)`; line breaks are kept because `%` in LaTeX comments out the rest of its line. Accept `mode` only from the list, clamp `size` to 1-400, and read `altAuto` as a boolean. Check the outline like any shape.
- **No file-version bump is needed:** an older app sees an ordinary shape.

In a project without DSKEDTR's path objects, the simplest equivalent is to store `{ latex, mode, size, altAuto, w0, h0, d }`, where `d` is SVG path data built from the contours, and draw it as a single `<path fill-rule="nonzero">`.

---

## 7. Alt text

`autoAlt(latex)` decides which reader to use: pure `\ce{...}` goes to `chemSpeech`, maths with embedded `\ce{}` gets each piece replaced, and everything else goes to `mathSpeech`.

**`mathSpeech`** cleans up MathLive's output, which is written for a speech engine:

| MathLive writes | We write |
|---|---|
| `'X'` (each single letter, in capitals and quotes) | `x` |
| `'capital E'` | `capital E` |
| `pie` (so π is pronounced right) | `pi` |
| `;` (a pause) | `,` |
| `b squared . End` | `b squared. End` |

So `x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}` becomes "x equals the fraction minus b plus or minus the square root of b squared minus 4 a c. End square root over 2 a. End fraction."

**`chemSpeech`** follows a fixed set of rules:

- `->` becomes "gives"; `<=>` becomes "is in equilibrium with".
- `(aq)`, `(s)`, `(l)` and `(g)` become "aqueous", "solid", "liquid" and "gas".
- `^2+` becomes "charge 2 plus", and so does a bare `OH-` (meaning "charge minus").
- `^` and `v` written as separate words become "gas given off" and "precipitate".
- Counts and elements are spaced apart (`NaOH` becomes "Na O H").
- Brackets are spoken.

For example, `2H2 + O2 -> 2H2O` becomes "2 H 2 plus O 2 gives 2 H 2 O".

---

## 8. Output for screen readers

- **Tagged PDF:** a `Formula` structure element, with the alt text as `/Alt` and a `BBox` attribute, and matching `Formula` marked content in the page's content stream. This is in place of `Figure`, and it is what PDF/UA expects for maths.
- **HTML export:** `mathMLFor()` calls `MathJax.tex2mml(latex)` and parses the result as XML with `DOMParser`. It then **rebuilds the MathML element by element** with `createElementNS`, keeping only a whitelist of MathML elements (`MATHML_TAGS`) and attributes (`MATHML_ATTRS`, values capped at 80 characters). It adds `display="block"`, `alttext`, and the equation's colour and size. If MathJax can't be loaded, the export falls back to the outline SVG with `role="img"` and `aria-label`.

---

## 9. Security, from the start

- LaTeX is untrusted input. It only ever goes to MathJax, and only in the editor and the HTML export.
- **The package list is fixed.** These are used:
  ```js
  const MATH_PACKAGES = ['base','ams','mhchem','boldsymbol','cancel','mathtools','braket','gensymb',
    'upgreek','textmacros','cases','enclose','extpfeil','physics'];
  ```
- **These are left out on purpose:**
  - `html` (`\href`, `\class`, `\style`, `\cssId`);
  - `require` and `autoload` (they load code);
  - `newcommand` (macros);
  - `unicode`, `color`, `bbox`, `action`;
  - `noerrors` and `noundefined`. These would *hide* mistakes: `noundefined` draws unknown commands in red instead of reporting them.
- `\href{javascript:...}`, `\style{...}` and `\require{...}` are all reported as mistakes. That is tested.
- The page only ever gets numbers (outlines), plain text, or whitelisted MathML. Nothing goes through `innerHTML`.
- MathLive fetches nothing: no fonts directory, no sounds.

---

## 10. The dialog

```
#eqDialog
  #eqTabs (role=tablist)   eqTab-visual | eqTab-latex | eqTab-chem
  #eqPane-visual           help text, #eqVisualBox (math-field goes here), #eqVisualNote
  #eqPane-latex            #eqLatexBits (buttons), #eqLatexIn (textarea)
  #eqPane-chem             #eqChemBits, #eqChemIn, #eqChemExamples
  #eqPreviewWrap > svg#eqPreview (aria-hidden; our own drawing of the outlines)
  #eqStatus (role=status)  mistakes and loading messages
  #eqAlt + #eqAltAuto      alt text, and "Use the automatic words"
  #eqSizeRow > #eqSizeIn   letter size (new equations only)
  #eqCancel, #eqGo
```

- The tabs use the suite's `suiteWireTabs`: arrow keys, Home and End. The tab used last is remembered in `localStorage` under `dskedtr-eq-mode`.
- All three tabs are views of one string, `eqLatex`. Moving into Chemistry stashes the maths, and coming back out restores it (`eqStash`), so a quick look at Chemistry doesn't wipe the work.
- The visual editor is read with `field.getValue('latex-expanded')`, not `.value`. That turns MathLive's shorthand (`\differentialD`) into LaTeX that MathJax understands.
- An unfilled MathLive box shows up as `\placeholder{}`, which MathJax doesn't know. That error is shown as "fill in the empty boxes".
- Ctrl or Cmd+Enter adds the equation from anywhere in the dialog. Escape cancels.
- In DSKEDTR, the dialog opens from: the rail button, the E key, a double-click, Enter on a picked equation, the quick pill's button, and the Inspector's "Change the equation...".

---

## 11. Traps (each one cost time)

1. **MathLive's keyboard and modal dialogs.** `showModal()` makes everything outside the dialog inert, and the keyboard normally attaches to `<body>`. Set `mathVirtualKeyboard.container = theDialog`. In a custom container, MathLive gives the keyboard **height 0 and `overflow: hidden`**, so it is invisible. The fix:
   ```css
   #eqDialog .ML__keyboard { position: sticky; bottom: 0; overflow: visible; z-index: 10; }
   ```
   While the keyboard is up, pad the form by its height (listen for its `geometrychange` event) so everything can still be scrolled to.
2. **MathLive's menu** opens outside the dialog. Hide it with `math-field::part(menu-toggle) { display: none; }` and `field.menuItems = []`.
3. **MathLive run from text** can't work out its own address, and it logs "Can't use relative paths..." to the console. That only matters for finding fonts, which we supply ourselves. `addMathLib()` silences just those messages while the script runs.
4. **The MathJax config must exist before the script runs.** Setting it afterwards does nothing.
5. **`fontCache: 'none'`** is required. Otherwise glyphs are `<use>` references to shared definitions, and the outline reader skips `<use>`.
6. **Typing before the libraries have loaded:** `texToArt` returns "empty" (rather than an error) until `MathJax.tex2svg` exists, and the preview runs again once loading finishes.
7. **Picking an equation:** test against its bounding box, not the glyph outline. Thin strokes are nearly impossible to click.
8. **A shape with corner handles only:** any code that expects a top-middle handle (DSKEDTR's rotate-handle line) has to fall back to the midpoint of the top corners.

---

## 12. What a host app must provide

To move the component into another project, these are the things it depends on, with DSKEDTR's names:

| Need | DSKEDTR name | Notes |
|---|---|---|
| `$` (`getElementById`), `setText`, `setField`, `clear`, `svgEl`, `r2` | small helpers | trivial to recreate |
| `cleanText(text, max, keepNewlines)` | input sanitiser | strips control characters |
| `pathData(o)` | contours to SVG `d` | for the preview, and for drawing if you don't have path objects |
| `FONTS['atkinson-hyperlegible-400']` | an opentype.js font | only for `<text>` fallbacks; can be dropped (those characters are then skipped) |
| `suiteWireTabs(tablist, onChange)` | tab keyboard support | from the suite block |
| `recordUndo`, `relayoutAndRender`, `selectObjects`, `announce`, `updateInspector` | app plumbing | replace with the host's own |
| `touchScreen()` | `matchMedia('(pointer: coarse)')` | decides whether the keyboard opens by itself |

Portable as they are: `loadMathLibs`, `addMathLib`, `setUpMathLive`, `matMul`, `parseTransform`, `pathToContours`, `svgToContours`, `texToArt`, `artAtSize`, `mathSpeech`, `chemSpeech`, `chemInside`, `autoAlt` and `mathMLFor`. These have no other app dependencies beyond the helpers above.

---

## 13. Test checklist (what was verified in Playwright for DSKEDTR)

- E opens the dialog on Build it, with focus in the visual editor; typing `x^2`, then →, then `+1/2` produces LaTeX; Ctrl+Enter adds it.
- Undo removes it and redo returns it.
- Chemistry: an example fills in and its alt text is correct; the Build it tab shows the chemistry note.
- Mistakes are reported (a missing brace, `\foo`), `\href`, `\style` and `\require` are refused, and Add stays disabled.
- Maths survives a trip through the Chemistry tab; the quick buttons insert at the cursor; typed alt text is kept, and "automatic" restores the automatic words.
- Double-click and Enter open the dialog for changing; a change keeps the place and the scale.
- The Inspector size and the width field keep the shape; there are corner handles only; dragging a handle keeps the shape.
- Saving and reopening keep all equations; the loader cleans a hostile `eq`, and drops a malformed one so it becomes a plain shape.
- The PDF has `/Formula` elements with `/Alt` and marked content; the PNG renders; the HTML has `<math alttext>` and no scripts or links.
- On a phone: tapping keys on the keyboard of symbols builds `x+1`, the Add button can be scrolled to and works, and the keyboard hides afterwards.
- axe finds no violations on any tab, in light or dark mode.
- The offline edition fetches nothing from the network; the online edition loads both libraries with SRI only when the editor opens.
- No console errors.

---

## 14. Possible next steps

- Equations **inside a line of text** (they would flow with the words). Not built yet.
- A building block of common formulas (quadratic formula, Pythagoras, common reactions).
- An animated feature card for the splash tour.
