import os
from typing import List, Dict, Union, Optional
from .char_range import find_supported_range

import PIL.ImageFont

"""
example for complex fonts:
Noto_Sans = Font({
    'CJK': {
        'black': 'NotoSansCJKtc-Black.otf',
        }
    'Hindu':{
        ...
    }
})
"""

class FontSet:
    """
    A set of font files with different font weight(width)
    example:
    noto = FontSet({
        1: (path of NotoSansCJK_Thin.otf)
        1.5: (path of NotoSansCJK_Light.otf)
        2: (path of NotoSansCJK_Regular.otf)
        ...
    })
    """
    def __init__(self, font_paths: Dict[Union[int, float], str]):
        # check if TTF/OTF file exist
        for font_width, path in font_paths.items():
            if not os.path.isfile(path):
                raise FileNotFoundError(f'TTF file: {path} does not exist.')
            if type(font_width) not in [int, float] or font_width <= 0:
                raise ValueError('font width should be larger than 0.0, datatype: int or float')
        self.font_paths = font_paths


# use only 3 sizes for TTF: 12pt, 32pt, 96pt
# resizing image to draw fonts sizes between them
class FontFamily:
    def __init__(self, TTF_path: Union[str, List[FontSet]], size: int = 32):
        self._supported_range = {}
        if type(TTF_path) is str:
            if not os.path.isfile(TTF_path):
                raise FileNotFoundError(f'TTF file: {TTF_path} does not exist.')
            self._font = PIL.ImageFont.truetype(TTF_path, size)
        elif type(TTF_path) is list and type(TTF_path[0]) is FontSet:  # "isinstance" cannot be used in generic types
            for index_fontset, fontset in enumerate(TTF_path):
                supported_range = find_supported_range(list(fontset.font_paths.values())[0])  # if both "regular" and "bold" are provided, check "regular" only
                print(supported_range)
                self._supported_range.update( zip(supported_range, [index_fontset]*len(supported_range)) )
        else:
            raise TypeError('TTF path can only be "str" or "List[FontSet]"')
        return


class Font:
    def __init__(self, TTF_path: Union[str, List[FontSet]], size: int = 32):
        if type(TTF_path) is str:
            if not os.path.isfile(TTF_path):
                raise FileNotFoundError(f'TTF file: {TTF_path} does not exist.')
            self._font = PIL.ImageFont.truetype(TTF_path, size)
        elif type(TTF_path) == List[FontSet]:
            pass
        else:
            raise TypeError('TTF path can only be "str" or "List[FontSet]"')
        return


    @property
    def font(self) -> PIL.ImageFont.FreeTypeFont:
        return self._font