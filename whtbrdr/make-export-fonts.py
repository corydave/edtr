#!/usr/bin/env python3
"""Put TrueType copies of WHTBRDR's two fonts into index-online.html, for PDF export.

Run it from this folder whenever the fonts inside index-online.html change
(they are the @font-face rules near the top of its <style>):

    python3 make-export-fonts.py
    python3 build-offline.py

Why: the page shows its words in two fonts, Atkinson Hyperlegible and
Comfortaa, kept inside the page as WOFF2 (a squeezed font file that browsers
read). A PDF needs the plain TrueType kind instead: pdf-lib, which writes
WHTBRDR's PDFs, can't put a WOFF2 font into a PDF (the letters come out
invisible). So this script unpacks each WOFF2 into TrueType, once, and keeps
it in the page as base64 text inside an inert
<script type="application/octet-stream"> (a type browsers never run), between
the EXPORT-FONTS-START and EXPORT-FONTS-END markers. Section 8n of the page
reads them when it writes a PDF.

Both fonts are under the SIL Open Font License 1.1, which allows this (the
same fonts, in another file format).

Needs Python 3 with fontTools and brotli:  pip install fonttools brotli
"""

import base64
import io
import pathlib
import re
import sys

from fontTools.ttLib import TTFont

HERE = pathlib.Path(__file__).resolve().parent
PAGE = HERE / 'index-online.html'
FONTS = [('atkinson', 'WHTBRDR Atkinson'), ('comfortaa', 'WHTBRDR Comfortaa')]
START, END = '<!-- EXPORT-FONTS-START', '<!-- EXPORT-FONTS-END -->'


def main():
    html = PAGE.read_text(encoding='utf-8')
    blocks = []
    for font_id, family in FONTS:
        m = re.search(r'font-family: "' + re.escape(family) + r'";[^}]*?url\(data:font/woff2;base64,([A-Za-z0-9+/=]+)\)', html, re.S)
        if not m:
            sys.exit('make-export-fonts.py: no WOFF2 found for ' + family)
        font = TTFont(io.BytesIO(base64.b64decode(m.group(1))))
        font.flavor = None                       # WOFF2 -> plain TrueType
        out = io.BytesIO()
        font.save(out)
        text = base64.b64encode(out.getvalue()).decode('ascii')
        lines = '\n'.join(text[i:i + 120] for i in range(0, len(text), 120))
        blocks.append('<script type="application/octet-stream" id="font-ttf-%s">\n%s\n</script>' % (font_id, lines))
        print('  %-10s %6d bytes of TrueType' % (font_id, len(out.getvalue())))
    block = (START + ': made by make-export-fonts.py from the WOFF2 fonts above, for PDF export\n'
             '     (section 8n). Browsers never run this type of script. Do not edit by hand. -->\n'
             + '\n'.join(blocks) + '\n' + END)
    if START in html:
        a = html.index(START)
        b = html.index(END, a) + len(END)
        html = html[:a] + block + html[b:]
    else:
        if html.count('</body>') != 1:
            sys.exit('make-export-fonts.py: expected one </body>')
        html = html.replace('</body>', block + '\n</body>')
    PAGE.write_text(html, encoding='utf-8')
    print('wrote the fonts into index-online.html (now run build-offline.py)')


if __name__ == '__main__':
    main()
