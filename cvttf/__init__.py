import os
from typing import Tuple, Optional, Union, List

import numpy as np
import cv2
import PIL.Image  # dependency to PIL(Pillow) will be removed in future releases
import PIL.ImageFont
import PIL.ImageDraw


from .char_range import find_supported_range as _find_supported_range
from .builtin_fonts import *
from . import builtin_fonts  # built-in font families
from .font_class import Font

from . import font_class
from . import builtin_fonts
from .drawing_functions import putText

_CVTTF_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


# built-in colors
COLOR_RED = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (255, 0, 0)
COLOR_YELLOW = (0, 255, 255)
COLOR_PURPLE = (255, 0, 255)
COLOR_CYAN = (255, 255, 0)



def _determine_font():
    raise NotImplementedError('not implemented yet.')

