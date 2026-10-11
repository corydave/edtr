#!/usr/bin/env python3
"""
build-offline.py - make index.html, the ONE-FILE edition of PDFEDTR.

    python3 build-offline.py

Run it from anywhere; it always works in its own folder. It needs only
Python 3 - nothing to install.

The two editions (the same arrangement as VCTREDTR):

  index-online.html  THE SOURCE. Edit this one. It loads its two PDF
                     libraries from jsDelivr, each pinned to one version
                     and locked with an "integrity" fingerprint.
  index.html         MADE BY THIS SCRIPT. Never edit it by hand - the next
                     build replaces it. It is the file pdfedtr.app serves,
                     and the same file works from a USB stick or a
                     double-click on a computer that has never been online.

What the script does, step by step:
  1. Reads index-online.html.
  2. Swaps the two jsDelivr <script> tags for the library code itself,
     taken from vendor/. Before it does, it checks each file's fingerprint
     (SHA-384) against the one in index-online.html, so both editions run
     byte-for-byte the same library code. A file that does not match stops
     the build with a message saying where to get the right one.
  3. Puts the pdf.js "worker" (the part that reads PDFs in the background)
     inside the page as inert text, and points pdf.js at a blob: address
     made from that text, so no download is needed.
  4. Tightens the security rules (Content-Security-Policy): this edition
     loads nothing from any other address, so jsDelivr is taken out.
  5. Writes index.html beside it.

Updating a library later: put the new file in vendor/, change the version
and fingerprint in index-online.html's <script> tag (and the worker
address), then run this script.
"""
import base64
import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent   # this script's own folder
SRC = HERE / 'index-online.html'                 # the source (edit this)
OUT = HERE / 'index.html'                        # the one-file edition (made here)
VENDOR = HERE / 'vendor'                         # the exact library files


def fail(msg):
    """Stop the build with a plain message (and a non-zero exit code)."""
    print('build-offline.py: ' + msg, file=sys.stderr)
    sys.exit(1)


def sri(data):
    """The browser's "integrity" fingerprint of some bytes: sha384-<base64>."""
    return 'sha384-' + base64.b64encode(hashlib.sha384(data).digest()).decode()


def inline_js(code):
    """Library code, ready to sit between <script> and </script>."""
    text = code.decode('utf-8')
    # Leave out the "source map" pointer: there is no map file beside the page.
    text = re.sub(r'//# sourceMappingURL=\S+\s*$', '', text)
    # A literal "</script" inside the code would end the <script> element early.
    if '</script' in text.lower():
        text = re.sub(r'</(script)', r'<\\/\1', text, flags=re.I)
    return text


def take_library(page, url_pattern, vendor_name, nice_name):
    """Find the <script src=...> tag for one library, check the vendor copy's
    fingerprint against the tag's, and return (page with the code inlined, code)."""
    tag = re.search(r'<script src="(' + url_pattern + r')"\s+integrity="(sha384-[^"]+)"[^>]*></script>', page)
    if not tag:
        fail('could not find the ' + nice_name + ' <script> tag in index-online.html')
    path = VENDOR / vendor_name
    if not path.exists():
        fail('vendor/' + vendor_name + ' is missing. Download it from ' + tag.group(1))
    data = path.read_bytes()
    if sri(data) != tag.group(2):
        fail('vendor/' + vendor_name + ' is not the file index-online.html expects. '
             'Download that exact file from ' + tag.group(1))
    block = ('<!-- ' + nice_name + ', built in by build-offline.py (from vendor/' + vendor_name + ') -->\n'
             '  <script>\n' + inline_js(data) + '\n  </script>')
    return page[:tag.start()] + block + page[tag.end():]


if not SRC.exists():
    fail('index-online.html is missing. It is the source this script builds index.html from.')
page = SRC.read_text(encoding='utf-8')

# ---- 2. The two libraries: swap each jsDelivr tag for the code itself ----
page = take_library(page, r'https://cdn\.jsdelivr\.net/npm/pdfjs-dist@[\d.]+/build/pdf\.min\.js',
                    'pdf.min.js', 'PDF.js')
page = take_library(page, r'https://cdn\.jsdelivr\.net/npm/pdf-lib@[\d.]+/dist/pdf-lib\.min\.js',
                    'pdf-lib.min.js', 'pdf-lib')

# ---- 3. The pdf.js worker: inert text in the page, then a blob: address ----
worker = (VENDOR / 'pdf.worker.min.js')
if not worker.exists():
    fail('vendor/pdf.worker.min.js is missing (from the same pdfjs-dist version as pdf.min.js).')
worker_code = inline_js(worker.read_bytes())
# A <script> whose type is not JavaScript is never run: the browser just keeps its text.
worker_tag = ('\n  <!-- The pdf.js worker\'s code, kept as inert text (its type is not\n'
              '       JavaScript, so the browser does not run it here). The app turns it\n'
              '       into a blob: address and hands that to pdf.js. -->\n'
              '  <script id="pdfjs-worker-src" type="text/plain">\n' + worker_code + '\n  </script>\n')
page, n = re.subn(r'(</head>)', lambda m: worker_tag + m.group(1), page, count=1)
if n != 1:
    fail('could not find </head> in index-online.html')

old_worker = re.search(r"pdfjsLib\.GlobalWorkerOptions\.workerSrc =\s*'https://cdn\.jsdelivr\.net/npm/pdfjs-dist@[\d.]+/build/pdf\.worker\.min\.js';", page)
if not old_worker:
    fail('could not find the pdf.js workerSrc line in index-online.html')
new_worker = ("// One-file edition: the worker's code is inside this page (see\n"
              "// #pdfjs-worker-src near the top). Wrapping that text in a Blob gives a real,\n"
              "// local address (blob:...) that works exactly like a hosted .js file.\n"
              "pdfjsLib.GlobalWorkerOptions.workerSrc = URL.createObjectURL(\n"
              "  new Blob([document.getElementById('pdfjs-worker-src').textContent], { type: 'text/javascript' })\n"
              ");")
page = page[:old_worker.start()] + new_worker + page[old_worker.end():]

# ---- 4. Security rules: nothing loads from jsDelivr in this edition ----
csp = re.search(r'<meta http-equiv="Content-Security-Policy" content="([^"]+)"', page)
if not csp:
    fail('could not find the Content-Security-Policy in index-online.html')
tight = csp.group(1).replace(' https://cdn.jsdelivr.net', '')
page = page[:csp.start(1)] + tight + page[csp.end(1):]
if 'jsdelivr' in tight:
    fail('the security rules still mention jsDelivr after tightening')

# Sanity checks, so a future edit cannot quietly ship a broken one-file edition.
if 'cdn.jsdelivr.net/npm/' in re.sub(r'<script id="pdfjs-worker-src".*?</script>', '', page, flags=re.S):
    fail('a jsDelivr address is still left in the page')
if 'APP-ICON-BLOCK-START' not in page:
    fail('the icon block (from build-icons.py) is missing from index-online.html')

OUT.write_text(page, encoding='utf-8')
size = OUT.stat().st_size
print('Wrote ' + OUT.name + ' - {:,} bytes ({:.2f} MB)'.format(size, size / 1024 / 1024))
