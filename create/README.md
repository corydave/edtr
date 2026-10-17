# EDTR Studio

Every EDTR app in one window: a rail of app icons down the left, and the
app you pick beside it. Apps keep running while you switch, so nothing
closes behind you. On a phone the rail tucks behind a small **Apps** tab on
the left edge.

- `index.html` - the Studio (one file, with the shared SUITE block inside)
- `sw.js` - keeps a copy of the Studio for offline use (only the Studio's
  own files; each app keeps its own copy, as always)
- `manifest.webmanifest`, `icon*.png`, `icon.svg`, `apple-touch-icon.png` -
  installing it as an app

## How it finds the apps

The Studio sits beside the apps' folders and opens each one at
`../<app>/` (for example `../imgedtr/`). It checks for the app's
`manifest.webmanifest` first:

| What it finds | What it opens | What works |
|---|---|---|
| The folder is on this site | `../imgedtr/` | Everything: Open, Save, offline, install |
| The folder isn't here (404) | `https://imgedtr.app/` | Most things. Chrome blocks the Open/Save *dialogs* inside another site's frame, so Save buttons that use them may fail (downloads still work), and settings and crash backups are kept apart from the app on its own site |
| No answer (offline) | `../imgedtr/` | The app's own offline copy answers |

Opened straight from a disk (`file:`), it uses the folders beside it.

## Putting it live at edtrapps.com/create/

edtrapps.com is the `edtr-main` Worker. Its build (set in Cloudflare under
Workers & Pages > edtr-main > Settings > Build) gathers the site into `dist/`:

- **Root directory:** `/` (the repo root)
- **Build command:**
  ```
  rm -rf dist && mkdir dist && cp -R apps-landing/. dist/ && for d in create txtedtr pdfedtr imgedtr sndedtr videdtr scrncstr vctredtr 3dedtr dskedtr animedtr; do cp -R "$d" dist/; done && rm -f dist/README.md
  ```
- **Deploy command:** `npx wrangler deploy`, which reads `wrangler.jsonc` at the
  repo root and serves `dist/`.

The result is laid out as in the repo: `/` from `apps-landing`, `/create/` from
`create/`, and `/imgedtr/` and the other app folders beside them. The apps' own
sites (imgedtr.app and friends) stay exactly as they are.

## Notes

- Every app's service worker now only clears its **own** old caches (they
  used to clear every cache on the site, which was fine on their own
  domains but would wipe each other's offline copies on one shared site).
- The SUITE block's "EDTR STUDIO" section is what makes an app Studio-aware:
  `suiteInStudio()`, links to sister apps opening in the Studio, Ctrl+Shift+number
  passed up (unless the app uses that key itself), and the splash's "More apps" row and install hint hidden.
- The frames may use: camera, microphone, screen sharing, clipboard, full
  screen, autoplay and keeping the screen awake. Nothing else.
