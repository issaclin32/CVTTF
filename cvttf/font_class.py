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
    NotoSansCJK = FontSet({
        1: (path of NotoSansCJK_Thin.otf)
        1.5: (path of NotoSansCJK_Light.otf)
        2: (path of NotoSansCJK_Regular.otf)
        ...
    })
    """
    def __init__(self, font_paths: Union[ str, Dict[Union[int, float], str] ]):
        if type(font_paths) is str:
            font_paths = {1: font_paths}
        # check if TTF/OTF file exist
        for font_width, path in font_paths.items():
            if not os.path.isfile(path):
                raise FileNotFoundError(f'TTF file: {path} does not exist.')
            if type(font_width) not in [int, float] or font_width <= 0:
                raise ValueError('font width should be larger than 0.0, datatype: int or float')
        self.font_paths = font_paths

    def __str__(self):
        return f'FontSet({str(self.font_paths)})'


# use only 3 sizes for TTF: 12pt, 32pt, 96pt
# resizing image to draw fonts sizes between them
class FontFamily:
    def __init__(self, TTF_path: Union[str, List[FontSet]], size: int = 32):
        self._char_range_combined: Dict[str, int] = {}
        self._char_range_for_each_fontset: List[set] = []
        if type(TTF_path) is str:
            if not os.path.isfile(TTF_path):
                raise FileNotFoundError(f'TTF file: {TTF_path} does not exist.')
            self._font = PIL.ImageFont.truetype(TTF_path, size)

        elif type(TTF_path) is list and type(TTF_path[0]) is FontSet:  # "isinstance" cannot be used in generic types
            # precedence: TTF_path[0] > TTF_path[1] > ...
            # key-value pairs from TTF_path[0] will overwrite those from TTF_path[1]
            for index_fontset, fontset in enumerate(reversed(TTF_path)):
                supported_range = find_supported_range(list(fontset.font_paths.values())[0])  # if both "regular" and "bold" are provided, check "regular" only
                self._char_range_combined.update( zip(supported_range, [len(TTF_path)-index_fontset-1]*len(supported_range)) )
                self._char_range_for_each_fontset.append(set(supported_range))
        else:
            raise TypeError('TTF path can only be "str" or "List[FontSet]"')

        return

    def find_fontset(self, text: str, allow_unsupported_fonts: bool = True) -> Union[int, List[int]]:
        """
        return an integer if "text" can be displayed using only one charset (e.g. NotoSans Thai)
        otherwise, return a list of integer which shows what charset should be chosen for each character
        e.g. ETF基金 -> [0,0,0,4,4]
        if there are some characters that are not supported by every FontSet in this FontFamily,
        then, put 0 in corresponding position (if "allow_supported_fonts" is set to True)
        or raise Exception (if "allow_supported_fonts" is set to False)
        """

        # check if "text" can be displayed using only one charset
        st = set(text)
        for i, r in enumerate(self._char_range_for_each_fontset):
            if st in r:
                return i

        # if not, check each character
        ret = []
        for c in text:
            if c in self._char_range_combined:
                ret.append(self._char_range_combined[c])
            else:
                if allow_unsupported_fonts:
                    ret.append(0)
                else:
                    raise ValueError(f'character "{c}" is not supported in this font family.')
        return ret


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