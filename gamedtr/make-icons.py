#!/usr/bin/env python3
"""Draw the GAMEDTR app icons.

Run it from this folder whenever the mark changes:

    python3 make-icons.py

It redraws every PNG the manifest and index.html refer to. The shapes here
are the same numbers as icon.svg and as the inline mark in index.html's top
bar (and SUITE_MARKS in the shared block), so if you edit one, edit them all.

The mark, in a 32 x 32 grid:
  - a crimson rounded plate (GAMEDTR's family colour, #991b1b)
  - a white game controller: a rounded bar (x 3.5, y 9, 25 x 12, corner 6)
    plus two round handles (centres 8.5,20.5 and 23.5,20.5, radius 3.8)
  - a crimson plus-shaped direction pad (two bars crossing at 9.5,15)
  - two orange buttons (centres 21.6,13.6 and 24.4,16.4, radius 1.6)
"""

from PIL import Image, ImageDraw

PLATE = (153, 27, 27, 255)      # #991b1b
WHITE = (255, 255, 255, 255)
ORANGE = (244, 89, 34, 255)     # #f45922, the same accent the other apps use


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
    # Turn a position on the 32-grid into a pixel position.
    p = lambda v: offset + v * scale

    def rect(x, y, w, h, colour, radius=0):
        box = [p(x), p(y), p(x + w), p(y + h)]
        if radius:
            draw.rounded_rectangle(box, radius=radius * scale, fill=colour)
        else:
            draw.rectangle(box, fill=colour)

    def circle(cx, cy, r, colour):
        draw.ellipse([p(cx - r), p(cy - r), p(cx + r), p(cy + r)], fill=colour)

    rect(3.5, 9, 25, 12, WHITE, radius=6)      # the controller's bar
    circle(8.5, 20.5, 3.8, WHITE)              # left handle
    circle(23.5, 20.5, 3.8, WHITE)             # right handle
    rect(8.5, 12, 2, 6, PLATE)                 # direction pad, up-down bar
    rect(6.5, 14, 6, 2, PLATE)                 # direction pad, left-right bar
    circle(21.6, 13.6, 1.6, ORANGE)            # top button
    circle(24.4, 16.4, 1.6, ORANGE)            # lower button

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
