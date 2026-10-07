# PDFEDTR changelog

Newest first. The short form of each entry also lives in the `CHANGELOG`
table inside `index.html` (shown in Help > Changelog), so the tab still works
offline and opened straight off a disk. A new release goes in both.

The version lives in one place - `APP_VERSION` in `index.html` - which fills in
the badge beside the wordmark and the help panel. After editing `index.html`,
run `build-offline.py` to regenerate `pdf-offline.html`; never hand-edit the
offline file.

Releases before 1.4 went out without notes. Rather than guess at them, this
file starts at 1.4.

## 1.4 - 2026-09-25 - Family alignment

- **Help panel** (new): the ? button beside the theme toggle, or press `?` or
  `F1`. Four tabs - Keyboard shortcuts, About, Changelog, More apps - the same
  four, in the same order, as every app in the family. App shortcuts stand
  down while it is open, so arrows move between tabs instead of nudging the
  selection or changing page behind it.
- **More apps** lists the rest of the family (TXTEDTR, PDFEDTR, IMGEDTR,
  SNDEDTR, VIDEDTR, SCRNCSTR) with this app marked "You are here". It is the
  shared SUITE block, pasted identically into every app, so it needs no
  network. Clicking the logo opens it directly.
- **Theme button** uses the family's sun and moon icons, and its name now says
  where it will take you ("Switch to dark mode"). It also sets `data-theme` on
  `<html>` alongside the existing `dark` class, which is what the shared More
  apps styles read.
- **Tooltips** use hyphens instead of em dashes ("Select - Esc", "Undo -
  Ctrl+Z" and four more), and so do three screen-reader labels.
- **Version** comes from a single `APP_VERSION` constant.
- **Renamed** `pdf.html` to `index.html`, matching the other apps, so the
  server serves it at the folder's address. `build-offline.py` and
  `build-icons.py` now read `index.html`. The offline build is still
  `pdf-offline.html`.
- **`icon.svg`** had picked up an 8 KB content-credentials (C2PA) metadata
  block again on the way down from a chat; stripped back to the clean 648-byte
  file. The HTML embeds its own icons, so the app was never affected.
