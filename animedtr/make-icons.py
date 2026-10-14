#!/usr/bin/env python3
"""Draw the ANIMEDTR app icons.

Run it from this folder whenever the mark changes:

    python3 make-icons.py

It redraws every PNG the manifest and index.html refer to. The shapes here
are the same numbers as icon.svg, the inline mark in index.html's top bar
and SUITE_MARKS in the shared block, so if you edit one, edit them all.
(Same idea as DSKEDTR's make-icons.py.) Needs Python 3 with Pillow.

The mark, in a 32 x 32 grid:
  - a gold rounded plate (ANIMEDTR's family colour, #655800)
  - a bouncing ball at the top of its arc (white, r 4.6 at 19.5, 9.5)
  - two fading copies behind it, the onion skin (r 3.6 at 12, 14 and r 3 at 7.5, 21)
  - a keyframe diamond under it in the family orange (#f45922)
"""

from PIL import Image, ImageDraw

PLATE = (101, 88, 0, 255)       # #655800
ORANGE = (244, 89, 34, 255)     # #f45922, the family's accent

# (centre x, centre y, radius, opacity) in the 32 grid - as in icon.svg.
BALLS = [(7.5, 21, 3, 0.35), (12, 14, 3.6, 0.6), (19.5, 9.5, 4.6, 1.0)]
DIAMOND = [(19.5, 22), (22.7, 25.2), (19.5, 28.4), (16.3, 25.2)]


def draw_icon(size, maskable=False):
    """Return the mark drawn at `size` pixels square.

    A maskable icon may be cropped to a circle by the operating system, so in
    that mode the plate fills the whole square and the artwork is drawn smaller,
    inside the safe zone, where no crop can reach it.
    """
    supersample = 4                      # draw big, then shrink: cheap smooth edges
    px = size * supersample
    image = Image.new('RGBA', (px, px), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    if maskable:
        draw.rectangle([0, 0, px, px], fill=PLATE)
        scale = px / 32 * 0.62
    else:
        draw.rounded_rectangle([0, 0, px - 1, px - 1], radius=7 / 32 * px, fill=PLATE)
        scale = px / 32
    offset = (px - 32 * scale) / 2
    unit = lambda value: offset + value * scale      # 32-grid units -> pixels
    for cx, cy, r, opacity in BALLS:
        # White at this opacity over the plate, mixed by hand (so it stays one flat colour).
        colour = tuple(round(255 * opacity + c * (1 - opacity)) for c in PLATE[:3]) + (255,)
        draw.ellipse([unit(cx - r), unit(cy - r), unit(cx + r), unit(cy + r)], fill=colour)
    draw.polygon([(unit(x), unit(y)) for x, y in DIAMOND], fill=ORANGE)
    return image.resize((size, size), Image.LANCZOS)


if __name__ == '__main__':
    for name, size, maskable in [('icon-192.png', 192, False), ('icon-512.png', 512, False),
                                 ('icon-maskable-512.png', 512, True), ('apple-touch-icon.png', 180, True),
                                 ('favicon-32.png', 32, False)]:
        draw_icon(size, maskable).save(name, optimize=True)
        print('wrote', name)
