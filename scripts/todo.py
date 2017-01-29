#!/usr/bin/env python3

import os
import glob
import sys
from PIL import Image, ImageChops

blanks = {
    'sprite': Image.open('blanks/sprite.png'),
    'back_sprite': Image.open('blanks/back_sprite.png'),
    'icon': Image.open('blanks/icon.png'),
}

def glob_open(globstr, directory='data'):
    for filename in glob.glob(os.path.join(directory, globstr)):
        yield os.path.basename(os.path.dirname(filename)), Image.open(filename)

def image_subsprites(image, slices, dimensions):
    result = {}
    slice_w, slice_h = dimensions
    w, h = image.size

    for top_left, name in slices.items():
        x1, y1 = top_left
        x2, y2 = (x1 + slice_w, y1 + slice_h)

        if x1 < w and y1 < h:
            subimage = image.transform(dimensions, Image.EXTENT, (x1, y1, x2, y2), Image.NEAREST)
            result[name] = subimage

    return result


def image_equal(a, b):
    return ImageChops.difference(a, b).getbbox() is None


missing = {}
def add_missing(name, category):
    if name not in missing:
        missing[name] = []

    missing[name].append(category)


for name, sprite in glob_open('*/sprite.png'):
    slices = {
        (0, 0): 'front',
        (64, 0): 'front-shiny',
        (128, 0): 'back',
        (192, 0): 'back-shiny',
        (0, 64): 'front-female',
        (128, 64): 'back-female',
    }

    subsprites = image_subsprites(sprite, slices, (64, 64))

    for subsprite_name, subsprite in subsprites.items():
        blank = blanks['back_sprite'] if 'back' in subsprite_name else blanks['sprite']
        if image_equal(subsprite, blank):
            add_missing(name, subsprite_name)

for name, icon in glob_open('*/icon.png'):
    slices = {
        (0, 0): 'icon-1',
        (0, 32): 'icon-2',
    }

    subsprites = image_subsprites(icon, slices, (32, 32))

    for subsprite_name, subsprite in subsprites.items():
        if image_equal(subsprite, blanks['icon']):
            add_missing(name, subsprite_name)

nice_names = {
    'front': 'Front Sprite',
    'front-shiny': 'Front Sprite (Shiny)',
    'back': 'Back Sprite',
    'back-shiny': 'Back Sprite (Shiny)',
    'front-female': 'Front Sprite (Female)',
    'back-female': 'Back Sprite (Female)',
    'icon-1': 'Icon (First Frame)',
    'icon-2': 'Icon (Second Frame)',
}

with open('TODO.md', 'w') as output:
    print('# Missing Sprites', file=output)
    for id, missing_sprites in missing.items():
        missing_values = ', '.join(nice_names[category] for category in missing_sprites)

        print('- `{}`: {}'.format(id, missing_values), file=output)
