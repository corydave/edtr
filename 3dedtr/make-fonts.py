"""
make-fonts.py - turn the eight bundled typefaces into three.js "typeface"
JSON files (engine/fonts/*.json), which 3DEDTR's Text shape reads.

Run it again only to change the fonts or the characters they hold:
    pip install fonttools skia-pathops
    python3 make-fonts.py <folder with the .woff files>

The fonts (all SIL Open Font License 1.1, no Reserved Font Names, so a
converted copy may be shared - see engine/LICENSES.txt):
    Inter Bold        (sans)   from @fontsource/inter       5.3.0
    Noto Serif Bold   (serif)  from @fontsource/noto-serif  5.3.0
    Zilla Slab Bold   (slab)   from @fontsource/zilla-slab  5.3.0
    Atkinson Hyperlegible Next Bold (legible)  from @fontsource/atkinson-hyperlegible-next     5.3.0
    Nunito ExtraBold                (rounded)  from @fontsource/nunito                         5.3.0
    Anton                           (display)  from @fontsource/anton                          5.3.0
    Pacifico                        (script)   from @fontsource/pacifico                       5.3.0
    Big Shoulders Stencil Display   (stencil)  from @fontsource/big-shoulders-stencil-display  5.3.0
      (ExtraBold: the stencil's bridges are thickest, so cut-out letters hold together)
Put all the .woff files listed in FONTS below in one folder.
Each comes as two files, "latin" and "latin-ext"; both are read, so the
result covers English plus accented letters (é, ñ, ü, ł, ő, ș ...). A few
fonts lack some rarer letters (it prints which); the app borrows those from
Inter, so they never show as "?".

What happens to each letter:
 1. Its outline is read from the font (accents built from parts are joined).
 2. Overlapping outlines are merged into one (skia-pathops), so the
    extruded letter is one clean solid with no parts inside each other.
 3. The outline is written as three.js expects: "m x y" move, "l x y"
    line, "q x y cx cy" curve (end point first, then the control point).
"""
import json, os, sys
from fontTools.ttLib import TTFont
from fontTools.ttLib.removeOverlaps import removeOverlaps
from fontTools.pens.basePen import BasePen

# Basic Latin, Latin-1 Supplement and Latin Extended-A, plus curly quotes,
# dashes, the ellipsis, the bullet, the euro and the trade mark sign.
CHARS = [c for c in range(0x20, 0x7F)] + [c for c in range(0xA0, 0x180)] + \
        [0x2013, 0x2014, 0x2018, 0x2019, 0x201C, 0x201D, 0x2022, 0x2026, 0x20AC, 0x2122]

FONTS = [  # (output name, family shown in the app, the two files)
    ('sans', 'Inter', ['inter-latin-700-normal.woff', 'inter-latin-ext-700-normal.woff']),
    ('serif', 'Noto Serif', ['noto-serif-latin-700-normal.woff', 'noto-serif-latin-ext-700-normal.woff']),
    ('slab', 'Zilla Slab', ['zilla-slab-latin-700-normal.woff', 'zilla-slab-latin-ext-700-normal.woff']),
    ('legible', 'Atkinson Hyperlegible Next', ['atkinson-hyperlegible-next-latin-700-normal.woff', 'atkinson-hyperlegible-next-latin-ext-700-normal.woff']),
    ('rounded', 'Nunito', ['nunito-latin-800-normal.woff', 'nunito-latin-ext-800-normal.woff']),
    ('display', 'Anton', ['anton-latin-400-normal.woff', 'anton-latin-ext-400-normal.woff']),
    ('script', 'Pacifico', ['pacifico-latin-400-normal.woff', 'pacifico-latin-ext-400-normal.woff']),
    ('stencil', 'Big Shoulders Stencil Display', ['big-shoulders-stencil-display-latin-800-normal.woff', 'big-shoulders-stencil-display-latin-ext-800-normal.woff']),
]
# Only some of them (python3 make-fonts.py <folder> script stencil): the others are left as they are.
ONLY = sys.argv[2:]

class TypefacePen(BasePen):
    """Collects one letter's outline as three.js path commands."""
    def __init__(self, glyphSet):
        super().__init__(glyphSet)
        self.out = []
    def n(self, v):
        return str(round(v))                     # whole font units are plenty (1000 or 2048 per letter height)
    def _moveTo(self, p):
        self.out += ['m', self.n(p[0]), self.n(p[1])]
    def _lineTo(self, p):
        self.out += ['l', self.n(p[0]), self.n(p[1])]
    def _qCurveToOne(self, c, p):
        self.out += ['q', self.n(p[0]), self.n(p[1]), self.n(c[0]), self.n(c[1])]
    def _curveToOne(self, c1, c2, p):
        self.out += ['b', self.n(p[0]), self.n(p[1]), self.n(c1[0]), self.n(c1[1]), self.n(c2[0]), self.n(c2[1])]
    def _closePath(self):
        pass                                     # three.js closes each outline by itself

def convert(src, name, family, files):
    glyphs, meta = {}, None
    for f in files:
        font = TTFont(os.path.join(src, f))
        removeOverlaps(font)                     # one clean outline per letter
        cmap = font.getBestCmap()
        gs = font.getGlyphSet()
        hmtx = font['hmtx']
        if meta is None:
            head, hhea, post = font['head'], font['hhea'], font['post']
            meta = dict(resolution=head.unitsPerEm, ascender=hhea.ascent, descender=hhea.descent,
                        underlinePosition=post.underlinePosition, underlineThickness=post.underlineThickness,
                        boundingBox=dict(xMin=head.xMin, yMin=head.yMin, xMax=head.xMax, yMax=head.yMax))
        for code in CHARS:
            ch = chr(code)
            if ch in glyphs or code not in cmap:
                continue
            gname = cmap[code]
            pen = TypefacePen(gs)
            gs[gname].draw(pen)
            glyphs[ch] = {'ha': hmtx[gname][0], 'o': ' '.join(pen.out)}
    data = dict(glyphs=glyphs, familyName=family, cssFontWeight='bold', cssFontStyle='normal',
                original_font_information=dict(license='SIL Open Font License 1.1', family=family), **meta)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'engine', 'fonts', name + '.json')
    with open(out, 'w') as fh:
        json.dump(data, fh, separators=(',', ':'), ensure_ascii=False)
    missing = [chr(c) for c in CHARS if chr(c) not in glyphs]
    print(name, family, len(glyphs), 'letters,', os.path.getsize(out) // 1024, 'KB', ('missing: ' + ''.join(missing)) if missing else '')

if __name__ == '__main__':
    src = sys.argv[1] if len(sys.argv) > 1 else '.'
    for name, family, files in FONTS:
        if not ONLY or name in ONLY:
            convert(src, name, family, files)
