#!/usr/bin/env python3
"""
build-offline.py — turn the CDN version of PDFEDTR into a single,
fully self-contained file that runs with no network connection at all.

It makes exactly three substitutions in the source HTML:

  1. The two CDN <script src> tags  -> the library source, inlined.
  2. The Google Fonts <link>        -> @font-face rules with base64 woff2.
  3. The pdf.js workerSrc CDN URL   -> a Blob URL built from inlined source.

The icon block in index.html (built by build-icons.py) rides along untouched:
its icons are data: URIs. Its manifest link points at manifest.webmanifest,
which a file opened from disk simply ignores.

Everything else in the file is left byte-for-byte alone, so the two
versions never drift apart in behaviour.
"""

import base64
import pathlib
import re
import sys

HERE = pathlib.Path('/home/claude')
VENDOR = HERE / 'vendor' / 'node_modules'

SRC = HERE / 'index.html'
OUT = HERE / 'pdf-offline.html'


def read_text(p):
    return pathlib.Path(p).read_text(encoding='utf-8')


def b64_file(p):
    return base64.b64encode(pathlib.Path(p).read_bytes()).decode('ascii')


def main():
    html = read_text(SRC)

    # ── Load the vendored libraries (from npm, so versions are pinned) ──
    pdfjs = read_text(VENDOR / 'pdfjs-dist/build/pdf.min.js')
    pdfjs_worker = read_text(VENDOR / 'pdfjs-dist/build/pdf.worker.min.js')
    pdflib = read_text(VENDOR / 'pdf-lib/dist/pdf-lib.min.js')

    # Safety check: a literal "</script" anywhere in the source would close
    # the tag early and corrupt the page. Verified absent, but assert it so a
    # future library bump can't silently break the build.
    for name, body in (('pdf.js', pdfjs), ('pdf.worker', pdfjs_worker), ('pdf-lib', pdflib)):
        if '</script' in body.lower():
            sys.exit(f'ERROR: {name} contains a literal </script — cannot inline as-is.')

    # ── 1 & 3. Replace the two CDN script tags ──
    # The worker goes into a script tag with a non-JavaScript `type`, which
    # tells the browser to parse it as inert data rather than run it. The app
    # then reads its text back out and wraps it in a Blob URL, which is what
    # pdf.js actually wants for workerSrc.
    script_block = (
        '  <!--\n'
        '    OFFLINE BUILD — pdf.js and pdf-lib are inlined below rather than\n'
        '    loaded from a CDN, so this file works with no network at all.\n'
        '    Versions are pinned: pdf.js 3.11.174, pdf-lib 1.17.1 (both from npm).\n'
        '  -->\n'
        '  <script>\n' + pdfjs + '\n  </script>\n'
        '  <script>\n' + pdflib + '\n  </script>\n'
        '  <!-- pdf.js worker source, held as inert text (type is not JavaScript,\n'
        '       so the browser will not execute it here). main.js turns this into\n'
        '       a Blob URL and hands that to pdf.js as its worker. -->\n'
        '  <script id="pdfjs-worker-src" type="text/plain">\n' + pdfjs_worker + '\n  </script>\n'
    )

    old_scripts = re.compile(
        r'  <!--\n    PDF\.js.*?'
        r'<script src="https://cdn\.jsdelivr\.net/npm/pdf-lib@1\.17\.1/dist/pdf-lib\.min\.js"></script>\n',
        re.DOTALL,
    )
    html, n = old_scripts.subn(lambda m: script_block, html)
    assert n == 1, f'expected 1 CDN script block, replaced {n}'

    # ── 2. Replace the Google Fonts stylesheet with inlined faces ──
    faces = [
        ('IBM Plex Sans', 300, 'ibm-plex-sans/files/ibm-plex-sans-latin-300-normal.woff2'),
        ('IBM Plex Sans', 400, 'ibm-plex-sans/files/ibm-plex-sans-latin-400-normal.woff2'),
        ('IBM Plex Sans', 500, 'ibm-plex-sans/files/ibm-plex-sans-latin-500-normal.woff2'),
        ('IBM Plex Sans', 600, 'ibm-plex-sans/files/ibm-plex-sans-latin-600-normal.woff2'),
        ('IBM Plex Mono', 400, 'ibm-plex-mono/files/ibm-plex-mono-latin-400-normal.woff2'),
        ('IBM Plex Mono', 600, 'ibm-plex-mono/files/ibm-plex-mono-latin-600-normal.woff2'),
    ]
    css_parts = [
        '  <!--\n'
        '    OFFLINE BUILD — IBM Plex is embedded below as base64 woff2 instead of\n'
        '    being fetched from Google Fonts. Latin subset only, and only the\n'
        '    weights this UI actually uses, to keep the file from bloating.\n'
        '  -->\n'
        '  <style>\n'
    ]
    for family, weight, rel in faces:
        data = b64_file(VENDOR / '@fontsource' / rel)
        css_parts.append(
            f'    @font-face {{\n'
            f'      font-family: "{family}";\n'
            f'      font-style: normal;\n'
            f'      font-weight: {weight};\n'
            f'      font-display: swap;\n'
            f'      src: url(data:font/woff2;base64,{data}) format("woff2");\n'
            f'    }}\n'
        )
    css_parts.append('  </style>\n')
    font_css = ''.join(css_parts)

    old_font_link = re.compile(
        r'  <link href="https://fonts\.googleapis\.com/css2\?[^"]*" rel="stylesheet" />\n'
    )
    html, n = old_font_link.subn(lambda m: font_css, html)
    assert n == 1, f'expected 1 Google Fonts link, replaced {n}'

    # ── 3 (cont). Point pdf.js at a Blob URL built from the inlined worker ──
    old_worker = (
        "/* ── Configure PDF.js worker ── */\n"
        "pdfjsLib.GlobalWorkerOptions.workerSrc =\n"
        "  'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';"
    )
    new_worker = """/* ── Configure PDF.js worker (offline build) ──
   pdf.js runs its heavy parsing on a Web Worker, and it needs a URL to load
   that worker from — normally a CDN address. With no network that's not an
   option, so instead the worker's entire source is sitting inert in a
   <script type="text/plain"> tag at the top of this file. Reading that text
   back out and wrapping it in a Blob gives us a real, local URL
   (blob:...) that behaves exactly like a hosted .js file would.        */
pdfjsLib.GlobalWorkerOptions.workerSrc = URL.createObjectURL(
  new Blob(
    [document.getElementById('pdfjs-worker-src').textContent],
    { type: 'text/javascript' }
  )
);"""
    assert old_worker in html, 'workerSrc block not found'
    html = html.replace(old_worker, new_worker, 1)

    # ── 4. Icons / manifest: nothing to do ──
    # The icon block in index.html is made of data: URIs (see build-icons.py),
    # so it needs no rewriting here - it is carried through verbatim and works
    # offline as-is. (Its manifest link is ignored off a disk.) Sanity-check that it
    # is actually present, so a future edit to index.html cannot quietly ship
    # an offline build with no icon.
    assert 'APP-ICON-BLOCK-START' in html, 'icon/manifest block missing from index.html'
    assert 'rel="manifest"' in html, 'manifest link missing from index.html'

    pathlib.Path(OUT).write_text(html, encoding='utf-8')
    size = pathlib.Path(OUT).stat().st_size
    print(f'Wrote {OUT} — {size:,} bytes ({size/1024/1024:.2f} MB)')


if __name__ == '__main__':
    main()
