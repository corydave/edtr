#!/usr/bin/env python3
"""Make index.html (the offline edition) from index-online.html (the source).

Run it from this folder after every change to index-online.html:

    python3 build-offline.py

The two editions are the suite's way (PDFEDTR does the same):

  index-online.html  the SOURCE. Edit this one. The first time a PDF is
                     opened, it fetches pdf.js from jsDelivr, pinned to one
                     version, and the browser checks each file against its
                     SRI fingerprint (sha384) before using it.
  index.html         MADE by this script. The same page with pdf.js packed
                     inside, so it works with no internet at all. It is the
                     edition the site serves. Never edit it by hand: the
                     next build overwrites it.

What the script does, step by step:
  1. Reads the pdf.js files' names and fingerprints from index-online.html
     (the PDFJS_FILES block), so the fingerprints live in one place only.
  2. Checks that each file in vendor/ matches its fingerprint exactly. If
     one doesn't (a different version, a damaged download), it stops and
     writes nothing.
  3. Squeezes each file with gzip and writes it as base64 text inside a
     <script type="application/octet-stream"> - a type browsers never run.
     The page unpacks it (DecompressionStream) and checks the fingerprint
     again before it uses it.
  4. Switches the edition line to 'offline', and takes jsDelivr out of the
     Content-Security-Policy's connect-src, so this edition can't reach any
     other server even if it wanted to.

To move to a newer pdf.js: put the new pdf.min.mjs and pdf.worker.min.mjs
(from the pdfjs-dist package, its legacy/build folder) in vendor/, put
their version, addresses and fingerprints in index-online.html's
PDFJS_FILES block, and run this script. A fingerprint for a file:

    openssl dgst -sha384 -binary vendor/pdf.min.mjs | openssl base64 -A

(write "sha384-" in front of what it prints). Needs only Python 3.
"""

import base64
import gzip
import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / 'index-online.html'
TARGET = HERE / 'index.html'
VENDOR = HERE / 'vendor'


def fail(words):
    """Stop, say why, and write nothing."""
    print('build-offline.py: ' + words, file=sys.stderr)
    sys.exit(1)


def replace_once(text, old, new, what):
    """Replace `old` with `new`, insisting it appears exactly once (so a change to the page can't slip past)."""
    count = text.count(old)
    if count != 1:
        fail('expected to find %s once in index-online.html, found it %d times' % (what, count))
    return text.replace(old, new)


def main():
    html = SOURCE.read_text(encoding='utf-8')

    # 1. The library block: its files and fingerprints.
    block = re.search(r'/\* PDFJS-LIBRARY-START.*?PDFJS-LIBRARY-END \*/', html, re.S)
    if not block:
        fail('the PDFJS-LIBRARY block is missing from index-online.html')
    files = re.findall(r"(\w+):\s*\{\s*name:\s*'([^']+)',\s*sri:\s*'(sha384-[A-Za-z0-9+/=]+)'", block.group(0))
    if sorted(k for k, _, _ in files) != ['lib', 'worker']:
        fail('the PDFJS_FILES block should list exactly "lib" and "worker"')

    # 2 and 3. Check each vendor file, then pack it.
    packed = []
    for key, name, sri in files:
        path = VENDOR / name
        if not path.is_file():
            fail('vendor/%s is missing' % name)
        data = path.read_bytes()
        got = 'sha384-' + base64.b64encode(hashlib.sha384(data).digest()).decode('ascii')
        if got != sri:
            fail('vendor/%s does not match its fingerprint.\n  expected %s\n  found    %s' % (name, sri, got))
        # mtime=0: the same input always gives the same output (no date inside the gzip).
        squeezed = gzip.compress(data, compresslevel=9, mtime=0)
        text = base64.b64encode(squeezed).decode('ascii')
        # Lines of 120 characters, so the file stays friendly to editors and diffs.
        lines = '\n'.join(text[i:i + 120] for i in range(0, len(text), 120))
        packed.append('<script type="application/octet-stream" id="pdfjs-data-%s">\n%s\n</script>' % (key, lines))
        print('  %-20s %8d bytes -> %8d packed (fingerprint checked)' % (name, len(data), len(text)))

    # 4. The edition line, and the CSP.
    out = replace_once(html, "const PDFJS_EDITION = 'online';", "const PDFJS_EDITION = 'offline';", 'the edition line')
    out = replace_once(out, "connect-src 'self' https://cdn.jsdelivr.net;", "connect-src 'self';", "the CSP's connect-src")
    if 'cdn.jsdelivr.net;' in out.split('</head>')[0]:
        fail('jsDelivr is still in the CSP')

    # A note at the very top, so nobody edits the wrong file.
    out = replace_once(out, '<!DOCTYPE html>\n',
                       '<!DOCTYPE html>\n<!-- MADE BY build-offline.py FROM index-online.html: edit that file, then run\n'
                       '     "python3 build-offline.py". Changes made here are lost at the next build. -->\n',
                       'the doctype line')
    # pdf.js, packed, just before </body> (the page reads it only when the first PDF is opened).
    note = ('<!-- pdf.js %s (Mozilla, Apache License 2.0: vendor/pdfjs-LICENSE.txt), packed by build-offline.py:\n'
            '     gzip, then base64. Browsers never run this type of script; the page unpacks it and checks\n'
            '     its fingerprint before using it (section 8l). -->\n') % re.search(r"PDFJS_VERSION = '([^']+)'", html).group(1)
    out = replace_once(out, '</body>', note + '\n'.join(packed) + '\n</body>', 'the </body> tag')

    TARGET.write_text(out, encoding='utf-8')
    print('wrote index.html: %d bytes (index-online.html is %d)' % (len(out.encode('utf-8')), len(html.encode('utf-8'))))


if __name__ == '__main__':
    main()
