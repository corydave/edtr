#!/usr/bin/env python3
"""Draw the VCTREDTR app icons.

Run it from this folder whenever the mark changes:

    python3 make-icons.py

It redraws every PNG the manifest and index.html refer to. The shapes here
are the same numbers as icon.svg and as the inline mark in index.html's top
bar (and SUITE_MARKS in the shared block), so if you edit one, edit them all.

The mark, in a 32 x 32 grid:
  - a violet rounded plate (VCTREDTR's family colour, #5b21b6)
  - a white rounded square     x 5..19,  y 12..26, corner radius 2.5
  - a white circle             centre (19.5, 12.5), radius 7.5
  - their overlap in orange (#f45922): the Merge Shapes idea
"""

from PIL import Image, ImageChops, ImageDraw

PLATE = (91, 33, 182, 255)      # #5b21b6
WHITE = (255, 255, 255, 255)
ORANGE = (244, 89, 34, 255)     # #f45922, the same accent IMGEDTR and SCRNCSTR use


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

    square = [unit(5), unit(12), unit(19), unit(26)]
    circle = [unit(12), unit(5), unit(27), unit(20)]
    draw.rounded_rectangle(square, radius=2.5 * scale, fill=WHITE)
    draw.ellipse(circle, fill=WHITE)

    # The overlap: the circle, but only inside the square (left of x=19, below y=12).
    overlap = Image.new('L', (px, px), 0)
    ImageDraw.Draw(overlap).ellipse(circle, fill=255)
    box = Image.new('L', (px, px), 0)
    ImageDraw.Draw(box).rectangle([unit(5), unit(12), unit(19), unit(26)], fill=255)
    mask = ImageChops.darker(overlap, box)            # keeps only where BOTH are painted
    image.paste(Image.new('RGBA', (px, px), ORANGE), (0, 0), mask)

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
