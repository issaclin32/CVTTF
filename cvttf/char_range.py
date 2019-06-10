# "fontTools" package is only used for checking the supported char range of TTF/OTF fonts

import os
from fontTools.ttLib import TTFont
from typing import Union, Iterable, Set


def find_supported_range(font_path: [str]) -> Set[str]:
    if not os.path.isfile(font_path):
        raise FileNotFoundError(f'font path: {font_path} does not exist.')
    ranges = set()
    with TTFont(font_path, 0, ignoreDecompileErrors=True) as ttf:
        for x in ttf['cmap'].tables:
            for key, code in x.cmap.items():
                ranges.add(chr(int(key)))
    return ranges