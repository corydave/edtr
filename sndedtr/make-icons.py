#!/usr/bin/env python3
"""Draw the SNDEDTR app icons.

Run it from this folder whenever the mark changes:

    python3 make-icons.py

It redraws every PNG the manifest refers to. The shapes here are the same
numbers as icon.svg and as the inline mark in index.html's top bar, so if you
edit one, edit all three.
"""

from PIL import Image, ImageDraw

PLATE  = (75, 85, 99, 255)      # #4b5563  the gray rounded plate (SNDEDTR's family colour)
ACCENT = (209, 213, 219, 255)   # #d1d5db  border and the short outer bars
LIGHT  = (255, 255, 255, 255)   # #ffffff  the two tall inner bars

# x, y, width, height, colour - in the same 64x64 grid as icon.svg
BARS = [
    (13, 24, 6, 16, ACCENT),
    (45, 25, 6, 14, ACCENT),
    (24, 17, 6, 30, LIGHT),
    (34, 11, 6, 42, LIGHT),
]


def draw_icon(size, maskable=False):
    """Return the mark drawn at `size` pixels square.

    A maskable icon may be cropped to a circle by the operating system, so in
    that mode the plate fills the whole square and the artwork is drawn smaller,
    inside the safe zone, where no crop can reach it.
    """
    supersample = 4                      # draw big, then shrink: cheap antialiasing
    px = size * supersample
    image = Image.new('RGBA', (px, px), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    if maskable:
        draw.rectangle([0, 0, px, px], fill=PLATE)
        scale = px / 64 * 0.62
    else:
        draw.rounded_rectangle([0, 0, px - 1, px - 1], radius=14 / 64 * px, fill=PLATE)
        scale = px / 64

    offset = (px - 64 * scale) / 2
    unit = lambda value: offset + value * scale      # 64-grid units -> pixels

    draw.rounded_rectangle(
        [unit(6), unit(6), unit(58), unit(58)],
        radius=11 * scale, outline=ACCENT, width=max(1, round(3 * scale)),
    )
    for x, y, w, h, colour in BARS:
        draw.rounded_rectangle(
            [unit(x), unit(y), unit(x + w), unit(y + h)],
            radius=3 * scale, fill=colour,
        )

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
