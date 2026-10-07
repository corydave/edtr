#!/usr/bin/env python3
"""Draw the 3DEDTR app icons.

Run it from this folder whenever the mark changes:

    python3 make-icons.py

It redraws every PNG the manifest and index.html refer to. The shapes here
are the same numbers as icon.svg and as the inline mark in index.html's top
bar (and SUITE_MARKS in the shared block), so if you edit one, edit them all.

The mark, in a 32 x 32 grid:
  - a bronze rounded plate (3DEDTR's family colour, #7a4100)
  - a cube seen from above and to one side, as three four-sided faces:
      top    (16,5.5) (26,11) (16,16.5) (6,11)        white
      left   (6,11) (16,16.5) (16,27.5) (6,22)         white at 82% (a shade)
      right  (26,11) (16,16.5) (16,27.5) (26,22)       orange (#f45922)
"""

from PIL import Image, ImageDraw

PLATE = (122, 65, 0, 255)       # #7a4100
WHITE = (255, 255, 255, 255)
ORANGE = (244, 89, 34, 255)     # #f45922, the same accent the other apps use


def mix(a, b, amount):
    """Blend colour a towards colour b by `amount` (0..1)."""
    return tuple(round(a[i] + (b[i] - a[i]) * amount) for i in range(3)) + (255,)


# White at 82% opacity on the bronze plate is this solid colour.
SHADE = mix(PLATE, WHITE, 0.82)

TOP = [(16, 5.5), (26, 11), (16, 16.5), (6, 11)]
LEFT = [(6, 11), (16, 16.5), (16, 27.5), (6, 22)]
RIGHT = [(26, 11), (16, 16.5), (16, 27.5), (26, 22)]


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
    point = lambda p: (offset + p[0] * scale, offset + p[1] * scale)   # 32-grid -> pixels

    draw.polygon([point(p) for p in TOP], fill=WHITE)
    draw.polygon([point(p) for p in LEFT], fill=SHADE)
    draw.polygon([point(p) for p in RIGHT], fill=ORANGE)

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
