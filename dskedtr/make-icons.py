#!/usr/bin/env python3
"""Draw the DSKEDTR app icons.

Run it from this folder whenever the mark changes:

    python3 make-icons.py

It redraws every PNG the manifest and index.html refer to. The shapes here
are the same numbers as icon.svg, the inline mark in index.html's top bar
and SUITE_MARKS in the shared block, so if you edit one, edit them all.
(Same idea as VCTREDTR's make-icons.py.) Needs Python 3 with Pillow.

The mark, in a 32 x 32 grid:
  - an emerald rounded plate (DSKEDTR's family colour, #065f46)
  - an open two-page spread: two white pages, x 5..15.5 and 16.5..27, y 7..25
  - left page: an orange picture block (#f45922) and two text lines
  - right page: a headline bar and three text lines, in the plate colour
"""

from PIL import Image, ImageDraw

PLATE = (6, 95, 70, 255)        # #065f46
WHITE = (255, 255, 255, 255)
ORANGE = (244, 89, 34, 255)     # #f45922, the family's accent

# (x, y, width, height, corner radius, colour) in the 32 grid - as in icon.svg.
SHAPES = [
    (5, 7, 10.5, 18, 1.2, WHITE),
    (16.5, 7, 10.5, 18, 1.2, WHITE),
    (7, 9, 6.5, 6, 0.8, ORANGE),
    (7, 17.2, 6.5, 1.6, 0.8, PLATE),
    (7, 20.4, 4.5, 1.6, 0.8, PLATE),
    (18.5, 9, 6.5, 2.6, 0.8, PLATE),
    (18.5, 14, 6.5, 1.6, 0.8, PLATE),
    (18.5, 17.2, 6.5, 1.6, 0.8, PLATE),
    (18.5, 20.4, 4.5, 1.6, 0.8, PLATE),
]


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
    for x, y, w, h, r, colour in SHAPES:
        draw.rounded_rectangle([unit(x), unit(y), unit(x + w), unit(y + h)], radius=r * scale, fill=colour)
    return image.resize((size, size), Image.LANCZOS)


ICONS = [
    ('icon-192.png', 192, False),
    ('icon-512.png', 512, False),
    ('icon-maskable-512.png', 512, True),
    ('apple-touch-icon.png', 180, False),
    ('favicon-32.png', 32, False),
]

if __name__ == '__main__':
    for name, size, maskable in ICONS:
        draw_icon(size, maskable).save(name, optimize=True)
        print('wrote', name)
