import numpy as np
import cv2
import PIL.Image  # dependency to PIL(Pillow) will be removed in future releases
import PIL.ImageFont
import PIL.ImageDraw

from typing import Tuple, Optional, List
from .font_class import Font, FontSet, FontFamily
from .builtin_fonts import FONT_NOTO_SANS

def putText(img: np.ndarray, text: str, org: Tuple[int, int],
            fontFace: Optional[Font] = FONT_NOTO_SANS,
            fontScale = 0.5, color: Tuple[int] = (255, 255, 255),
            thickness = None, lineType = None, bottomLeftOrigin: bool = False,
            multi_line: bool = True, use_fallback_font: bool = True)-> None:
    """
    putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) -> img
    .   @brief Draws a text string.
    .
    .   Renders the specified text string in the image.
    .   To use TTF/OTF font files, check "Cvttf.Font"
    .
    .   @param img Image.
    .   @param text Text string to be drawn.
    .   @param org Bottom-left corner of the text string in the image.
    .   @param fontFace Font type, see cv::HersheyFonts.
    .   @param fontScale Font scale factor that is multiplied by the font-specific base size.
    .   @param color Text color.
    .   @param thickness Thickness of the lines used to draw a text.
    .   @param lineType Line type. See the line for details.
    .   @param bottomLeftOrigin When true, the image data origin is at the bottom-left corner. Otherwise,
    .   it is at the top-left corner.
    .   @param multi_line Draw the text at the next line whenever text exceeds image width.
    .   Also, starts a new line if "\n" appears in the text.
    .   @param use_fallback_font Line type. See the line for details.
    """
    # --- handling potential problems ---
    if len(img.shape) > 4 or len(img.shape) < 2 or img.dtype != np.uint8:
        raise TypeError('argument "img" should be an OpenCV image. (np.array with dtype=uint8)')
    if len(org) != 2:
        raise ValueError('argument "org" should be in the format of (x,y)')
    if len(img.shape) == 2:
        gray = True
        # Clinear = 0.2126 R + 0.7152 G + 0.0722 B
        if len(color) == 3:
            color = (color[2]*0.2126 + color[1]*0.7152 + color[0]*0.0722, )
    else:
        gray = False

    if len(color) != 3:
        if gray and len(color) == 1:
            pass
        else:
            raise ValueError('The length of "color" should be 3(RGB) or 1(grayscale)')



    # TODO: determine which Noto Sans font to be used based on the language of "text"

    img_h, img_w = img.shape[0:2]
    font_img = PIL.Image.new('RGB', (img_w, img_h), color=(0, 0, 0))
    draw = PIL.ImageDraw.Draw(font_img)
    draw.text(org, text, font=fontFace.font, fill=color+(0,))  # fill: BGRA

    font_img = np.array(font_img)
    img[:] = np.where(font_img > 0, font_img, img)

    return None