#!/usr/bin/env python3
"""
Build index.html, the ONE-FILE edition: the whole app in a single file,
with the drawing engine, the letter-outline reader and every font inside.
It is the main edition: vctredtr.app serves it, and the same file works
with no internet at all - from a USB stick, an email attachment, or a
double-click on a computer that has never been online.

    python3 build-offline.py

Edit index-online.html (the source), then run this from this folder to
make index.html. Never edit index.html by hand: the next build replaces
it. It needs only Python 3, nothing to install.

What it does:
  1. Reads index-online.html, the online edition (it loads its two
     libraries from jsDelivr and its fonts from fonts/). Never edited here.
  2. Puts the two libraries INSIDE the page instead: Paper.js (the drawing
     engine) and opentype.js (reads letter outlines for "Turn into
     shapes"). The copies are in vendor/, and the script first checks their
     fingerprints (SHA-384) against the ones in index-online.html, so both
     editions run byte-for-byte the same library code.
  3. Puts every font from fonts/ inside the page too (as base64 text), in
     VCTR_EMBEDDED.fonts, which the app looks for before using fonts/.
  4. Tightens the rule book (Content-Security-Policy): this edition loads
     nothing from any other address, so jsDelivr is taken out.
  5. Swaps the tab icon for one inside the page. The install manifest and
     the other icon links stay: on the website they make the app
     installable; opened from a file, the browser simply skips them.

The result is about 2 MB. On the website it installs and checks for
updates like the online edition. Opened from a file it shows a small "o"
beside the version number and has no updates to fetch: to update it, run
this script again or copy the new index.html.
"""
import base64
import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / 'index-online.html'   # the online edition: the source
OUT = HERE / 'index.html'          # the one-file edition this script makes


def fail(msg):
    print('build-offline.py: ' + msg, file=sys.stderr)
    sys.exit(1)


def sri(data):
    """The browser's "integrity" fingerprint of some bytes: sha384-<base64>."""
    return 'sha384-' + base64.b64encode(hashlib.sha384(data).digest()).decode()


def inline_js(code):
    """Library code ready to sit inside <script>...</script>."""
    text = code.decode('utf-8')
    # Leave out the "source map" pointer: there is no map file beside the page.
    text = re.sub(r'//# sourceMappingURL=\S+\s*$', '', text)
    # "</script" inside the code would end the <script> element early.
    if '</script' in text.lower():
        text = re.sub(r'</(script)', r'<\\/\1', text, flags=re.I)
    return text


if not SRC.exists():
    fail('index-online.html is missing. It is the source this script builds index.html from.')
page = SRC.read_text(encoding='utf-8')

# ---- 1. Paper.js: swap the jsDelivr <script> tag for the code itself ----
paper_tag = re.search(r'<script src="https://cdn\.jsdelivr\.net/npm/paper@([\d.]+)/dist/paper-core\.min\.js"\s+'
                      r'integrity="(sha384-[^"]+)"[^>]*></script>', page)
if not paper_tag:
    fail('could not find the Paper.js <script> tag in index-online.html')
paper = (HERE / 'vendor' / 'paper-core.min.js').read_bytes()
if sri(paper) != paper_tag.group(2):
    fail('vendor/paper-core.min.js is not the Paper.js ' + paper_tag.group(1) + ' that index-online.html expects. '
         'Download that exact file from https://cdn.jsdelivr.net/npm/paper@' + paper_tag.group(1) + '/dist/paper-core.min.js')

# ---- 2. opentype.js: the page loads it itself when needed; here it goes in up front ----
ot_url = re.search(r"const OPENTYPE_URL = '(https://cdn\.jsdelivr\.net/npm/opentype\.js@([\d.]+)/[^']+)'", page)
ot_sri = re.search(r"const OPENTYPE_SRI = '(sha384-[^']+)'", page)
if not ot_url or not ot_sri:
    fail('could not find OPENTYPE_URL / OPENTYPE_SRI in index-online.html')
opentype = (HERE / 'vendor' / 'opentype.min.js').read_bytes()
if sri(opentype) != ot_sri.group(1):
    fail('vendor/opentype.min.js is not the opentype.js ' + ot_url.group(2) + ' that index-online.html expects. '
         'Download that exact file from ' + ot_url.group(1))

# ---- 3. The fonts, as base64 text: "anton-400" -> "d09GRgABAAAA..." ----
fonts = {}
for f in sorted((HERE / 'fonts').glob('*.woff')):
    fonts[f.stem] = base64.b64encode(f.read_bytes()).decode()
if not fonts:
    fail('no fonts found in fonts/')
# Every font the app lists must be here, or text in it would silently fall back.
wanted = set()
for file, weights in re.findall(r"incl\('[^']+', '\w+', '[^']+', '([a-z0-9-]+)'(?:, \[([0-9, ]+)\])?", page):
    for w in (weights.split(',') if weights else ['400', '700']):
        wanted.add(file + '-' + w.strip())
missing = sorted(wanted - set(fonts))
if missing:
    fail('these fonts are missing from fonts/: ' + ', '.join(missing))

embedded = ('<script>\n/* OFFLINE EDITION: every font the app offers, inside the page (made by\n'
            '   build-offline.py from the fonts/ folder; licences in fonts/LICENSES.txt).\n'
            '   The app reads this before looking for a fonts/ folder. */\n'
            'var VCTR_EMBEDDED = { edition: "offline", fonts: {\n' +
            ',\n'.join('"%s": "%s"' % (k, v) for k, v in fonts.items()) +
            '\n} };\n</script>\n')
libs = ('<!-- OFFLINE EDITION: the drawing engine, Paper.js ' + paper_tag.group(1) + ' (MIT licence, by Juerg Lehni and\n'
        '     Jonathan Puckey), inside the page. Same file as the online edition loads; fingerprint\n'
        '     ' + paper_tag.group(2) + ' -->\n'
        '<script>\n' + inline_js(paper) + '\n</script>\n'
        '<!-- OFFLINE EDITION: opentype.js ' + ot_url.group(2) + ' (MIT licence, by Frederik De Bleser), which reads\n'
        '     letter outlines for "Turn into shapes". Fingerprint ' + ot_sri.group(1) + ' -->\n'
        '<script>\n' + inline_js(opentype) + '\n</script>\n' + embedded)
page = page[:paper_tag.start()] + libs + page[paper_tag.end():]

# ---- 4. The rule book: nothing may load from jsDelivr (or anywhere else) now ----
csp_old = "script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net;"
if csp_old not in page:
    fail('the Content-Security-Policy in index-online.html is not the one this script expects')
page = page.replace(csp_old, "script-src 'self' 'unsafe-inline';", 1)

# ---- 5. The tab icon, inside the page (the other icon links and the
#         manifest stay, for installing from the website) ----
favicon = HERE / 'favicon-32.png'
if favicon.exists():
    page = page.replace('<link rel="icon" href="favicon-32.png" sizes="32x32">',
                        '<link rel="icon" href="data:image/png;base64,' + base64.b64encode(favicon.read_bytes()).decode() + '" sizes="32x32">')
# (img-src already allows data: images, so the tab icon above is allowed.)

# ---- 6. Safety check: the website copy must stay installable ----
# (An early version of this script took the manifest out. Never again: the
# build stops if anything the browser needs for installing is missing.)
for needed in ('<link rel="manifest" href="manifest.webmanifest">', '<link rel="apple-touch-icon"', 'icon-192.png'):
    if needed not in page:
        fail('the page would lose ' + needed + ' - it is needed to install the app from the website')
if "navigator.serviceWorker" not in page:
    fail('the page would lose its service worker registration - it is needed to install the app')

OUT.write_text(page, encoding='utf-8')
print('Wrote %s: %.1f MB, with Paper.js %s, opentype.js %s and %d font files inside.'
      % (OUT.name, OUT.stat().st_size / 1e6, paper_tag.group(1), ot_url.group(2), len(fonts)))
