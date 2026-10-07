#!/usr/bin/env python3
"""
Build index.html, the ONE-FILE edition of DSKEDTR: the whole app in a
single file, with its four libraries and the font inside. It works with no
internet at all - from a USB stick, an email attachment, or a double-click.

    python3 build-offline.py

Edit index-online.html (the source), then run this from this folder to
make index.html. Never edit index.html by hand: the next build replaces it.
It needs only Python 3, nothing to install. (Same idea as VCTREDTR's
build-offline.py, cut down to what DSKEDTR uses so far.)

What it does:
  1. Reads index-online.html (it loads opentype.js from jsDelivr and its
     font from fonts/).
  2. Puts the libraries INSIDE the page: opentype.js (reads the font),
     Paper.js (the geometry behind Merge Shapes), pdf-lib (writes PDFs) and
     fontkit (lets pdf-lib put the font in a PDF). Each copy in vendor/
     must have the same fingerprint (SHA-384) that index-online.html asks
     for, so both editions run byte-for-byte the same library code.
  3. Puts the font files from fonts/ inside the page as base64 text, in
     DSK_EMBEDDED.fonts, which the app reads before trying fonts/.
  4. Tightens the rule book (Content-Security-Policy): this edition loads
     nothing from any other address, so jsDelivr is taken out.
  5. Puts the tab icon inside the page too. The install manifest and the
     other icon links stay: on the website they make the app installable.
  6. Refuses to finish if anything installing needs has gone missing.
"""
import base64
import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / 'index-online.html'
OUT = HERE / 'index.html'


def fail(msg):
    print('build-offline.py: ' + msg, file=sys.stderr)
    sys.exit(1)


def sri(data):
    """The browser's "integrity" fingerprint of some bytes: sha384-<base64>."""
    return 'sha384-' + base64.b64encode(hashlib.sha384(data).digest()).decode()


def inline_js(code):
    """Library code ready to sit inside <script>...</script>."""
    text = code.decode('utf-8')
    text = re.sub(r'//# sourceMappingURL=\S+\s*$', '', text)   # no map file beside the page
    if '</script' in text.lower():                              # would end the <script> early
        text = re.sub(r'</(script)', r'<\\/\1', text, flags=re.I)
    return text


if not SRC.exists():
    fail('index-online.html is missing. It is the source this script builds index.html from.')
page = SRC.read_text(encoding='utf-8')

# ---- 1 and 2. The libraries: swap each jsDelivr <script> tag for the code itself ----
def library(package, filename, licence):
    """Find a library's <script> tag, check vendor/'s copy, and return (tag match, inline script)."""
    tag = re.search(r'<script src="https://cdn\.jsdelivr\.net/npm/' + re.escape(package) + r'@([\d.]+)/dist/' + re.escape(filename) +
                    r'"\s+integrity="(sha384-[^"]+)"[^>]*></script>', page)
    if not tag:
        fail('could not find the ' + package + ' <script> tag in index-online.html')
    code = (HERE / 'vendor' / filename).read_bytes()
    if sri(code) != tag.group(2):
        fail('vendor/' + filename + ' is not the ' + package + ' ' + tag.group(1) + ' that index-online.html expects. '
             'Download that exact file from https://cdn.jsdelivr.net/npm/' + package + '@' + tag.group(1) + '/dist/' + filename)
    block = ('<!-- OFFLINE EDITION: ' + package + ' ' + tag.group(1) + ' (' + licence + '), inside the page.\n'
             '     Same file the online edition loads; fingerprint ' + tag.group(2) + ' -->\n'
             '<script>\n' + inline_js(code) + '\n</script>\n')
    return tag, block

tag, opentype_block = library('opentype.js', 'opentype.min.js', 'MIT licence, by Frederik De Bleser')
paper_tag, paper_block = library('paper', 'paper-core.min.js', 'MIT licence, by Juerg Lehni and Jonathan Puckey')
pdflib_tag, pdflib_block = library('pdf-lib', 'pdf-lib.min.js', 'MIT licence, by Andrew Dillon')
fontkit_tag, fontkit_block = library('@pdf-lib/fontkit', 'fontkit.umd.min.js', 'MIT licence, by Devon Govett and Andrew Dillon')

# ---- 3. The fonts, as base64 text ----
wanted = re.findall(r"'(atkinson-hyperlegible-\d+)'", page)
fonts = {}
for name in sorted(set(wanted)):
    f = HERE / 'fonts' / (name + '.woff')
    if not f.exists():
        fail('fonts/' + f.name + ' is missing')
    fonts[name] = base64.b64encode(f.read_bytes()).decode()
if not fonts:
    fail('found no font names in index-online.html')

embedded = ('<script>\n/* OFFLINE EDITION: the fonts, inside the page (made by build-offline.py\n'
            '   from the fonts/ folder; licence in fonts/LICENSES.txt). */\n'
            'var DSK_EMBEDDED = { edition: "offline", fonts: {\n' +
            ',\n'.join('"%s": "%s"' % (k, v) for k, v in fonts.items()) +
            '\n} };\n</script>\n')
# Swap the tags from the LAST in the page to the first, so the positions of
# the earlier tags stay the same while the later ones change.
swaps = [(tag, opentype_block + embedded), (paper_tag, paper_block), (pdflib_tag, pdflib_block), (fontkit_tag, fontkit_block)]
for m, block in sorted(swaps, key=lambda s: s[0].start(), reverse=True):
    page = page[:m.start()] + block + page[m.end():]

# ---- 4. The rule book: nothing may load from jsDelivr now ----
csp_old = "script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net;"
if csp_old not in page:
    fail('the Content-Security-Policy in index-online.html is not the one this script expects')
page = page.replace(csp_old, "script-src 'self' 'unsafe-inline';", 1)

# ---- 5. The tab icon, inside the page ----
icon = HERE / 'icon.svg'
if icon.exists():
    page = page.replace('<link rel="icon" href="icon.svg" type="image/svg+xml">',
                        '<link rel="icon" href="data:image/svg+xml;base64,' + base64.b64encode(icon.read_bytes()).decode() + '" type="image/svg+xml">')

# ---- 6. Safety check: the website copy must stay installable ----
for needed in ('<link rel="manifest" href="manifest.webmanifest">', '<link rel="apple-touch-icon"', 'icon-192.png'):
    if needed not in page:
        fail('the page would lose ' + needed + ' - it is needed to install the app from the website')
if 'navigator.serviceWorker' not in page:
    fail('the page would lose its service worker registration - it is needed to install the app')
for f in ('manifest.webmanifest', 'sw.js', 'icon-192.png', 'icon-512.png', 'icon-maskable-512.png', 'apple-touch-icon.png'):
    if not (HERE / f).exists():
        fail(f + ' is missing - run make-icons.py for the icons; the manifest and sw.js sit beside index.html')

OUT.write_text(page, encoding='utf-8')
print('Wrote %s: %.2f MB, with opentype.js %s, Paper.js %s, pdf-lib %s, fontkit %s and %d font files inside.'
      % (OUT.name, OUT.stat().st_size / 1e6, tag.group(1), paper_tag.group(1), pdflib_tag.group(1), fontkit_tag.group(1), len(fonts)))
