# edtrapps.com

The home page for the EDTR apps. Upload everything in this folder to the
root of edtrapps.com:

- `index.html` - the whole page (styles and script inside).
- `shots/` - the screenshots (copied from `apps-landing/shots`; GAMEDTR's left out).
- `icons/` - each app's 192px icon, for the story timeline.
- `fonts/` - Atkinson Hyperlegible and Comfortaa, kept on the site so no outside
  font server sees visitors (see `fonts/LICENSES.txt`).

To add or change an app: edit the `APPS` list in `index.html` (same format as the
daveghidiu.com/edtr hub page), add its screenshots to `shots/` and its icon to
`icons/`.

Worth doing on the server: send the header
`Content-Security-Policy: frame-ancestors 'none'` (it can't go in a meta tag),
and make sure Cloudflare Web Analytics / automatic beacon injection is off for
this domain and the app domains, so the "nothing is tracked" spirit holds.
