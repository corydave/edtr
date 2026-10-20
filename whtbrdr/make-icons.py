#!/usr/bin/env python3
"""Draw the WHTBRDR app icons.

Run it from this folder whenever the mark changes:

    python3 make-icons.py

It redraws every PNG the manifest and index.html refer to. The shapes here
are the same numbers as icon.svg, the inline mark in index.html's top bar,
the favicon and SUITE_MARKS in the shared block, so if you edit one, edit
them all. (Same idea as DSKEDTR's make-icons.py.) Needs Python 3 with Pillow.

The mark, in a 32 x 32 grid:
  - a deep rose rounded plate (#9f1239, WHTBRDR's family color)
  - a whiteboard on a stand: two white legs, and a white board
    x 4.5..27.5, y 6.5..22.5
  - a rose marker stroke across the board (a smooth S-shaped curve)
  - an orange step badge (#f45922, the family accent) with a white "1"
"""

from PIL import Image, ImageDraw

PLATE = (159, 18, 57, 255)      # #9f1239, WHTBRDR's rose
WHITE = (255, 255, 255, 255)
ORANGE = (244, 89, 34, 255)     # #f45922, the family's accent


def bezier(p0, p1, p2, p3, steps=40):
    """Points along a cubic Bezier curve (the same curve as the SVG's "c"),
    so Pillow, which only draws straight lines, can draw it as many short ones."""
    points = []
    for i in range(steps + 1):
        t = i / steps
        a, b, c, d = (1 - t) ** 3, 3 * (1 - t) ** 2 * t, 3 * (1 - t) * t ** 2, t ** 3
        points.append((a * p0[0] + b * p1[0] + c * p2[0] + d * p3[0],
                       a * p0[1] + b * p1[1] + c * p2[1] + d * p3[1]))
    return points


# The marker stroke, from icon.svg's path "M8.5 17.5c2-4.2 3.8-4.2 5.3-1.6s3.6 2.4 5.6-2.6",
# written out as two curves with every point in the 32 grid. (The "s" curve's first
# control point is the mirror image of the previous curve's last one.)
STROKE = bezier((8.5, 17.5), (10.5, 13.3), (12.3, 13.3), (13.8, 15.9)) \
    + bezier((13.8, 15.9), (15.3, 18.5), (17.4, 18.3), (19.4, 13.3))[1:]


def thick_line(draw, points, width, color):
    """A line through the points, `width` wide, with round ends and joins.

    Drawn as a row of overlapping dots, close together along the way (like a
    round marker dragged along it): Pillow's own thick lines leave small gaps
    where short pieces meet at an angle."""
    r = width / 2
    step = max(r / 4, 0.5)                   # a dot every quarter of a radius
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        length = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        n = max(1, int(length / step))
        for i in range(n + 1):
            x, y = x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * i / n
            draw.ellipse([x - r, y - r, x + r, y + r], fill=color)


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
        scale = px / 32 * 0.7
    else:
        draw.rounded_rectangle([0, 0, px - 1, px - 1], radius=7 / 32 * px, fill=PLATE)
        scale = px / 32
    offset = (px - 32 * scale) / 2
    at = lambda x, y: (offset + x * scale, offset + y * scale)    # 32-grid point -> pixels

    # The stand's two legs (drawn first: the board covers their tops).
    thick_line(draw, [at(11, 22.5), at(9, 27)], 2 * scale, WHITE)
    thick_line(draw, [at(21, 22.5), at(23, 27)], 2 * scale, WHITE)
    # The board.
    draw.rounded_rectangle([*at(4.5, 6.5), *at(27.5, 22.5)], radius=1.6 * scale, fill=WHITE)
    # The marker stroke.
    thick_line(draw, [at(x, y) for x, y in STROKE], 2 * scale, PLATE)
    # The step badge, and its "1".
    cx, cy = at(23.5, 10)
    r = 3.6 * scale
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=ORANGE)
    thick_line(draw, [at(23.6, 8.4), at(23.6, 11.7)], 1.4 * scale, WHITE)
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
