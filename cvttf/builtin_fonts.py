import cvttf_NotoSansCJK_Black
import cvttf_NotoSansCJK_Bold
import cvttf_NotoSansCJK_DemiLight
import cvttf_NotoSansCJK_Light
import cvttf_NotoSansCJK_Medium
import cvttf_NotoSansCJK_Regular
import cvttf_NotoSansCJK_Thin

import os
from .font_class import FontFamily, Font, FontSet
_CVTTF_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


path_black = cvttf_NotoSansCJK_Black.get_TTF_path()
path_bold = cvttf_NotoSansCJK_Bold.get_TTF_path()
path_demilight = cvttf_NotoSansCJK_DemiLight.get_TTF_path()
path_light = cvttf_NotoSansCJK_Light.get_TTF_path()
path_medium = cvttf_NotoSansCJK_Medium.get_TTF_path()
path_thin = cvttf_NotoSansCJK_Thin.get_TTF_path()
path_regular = cvttf_NotoSansCJK_Regular.get_TTF_path()

# built-in font families
FONT_NOTO_SANS = Font(path_regular)


def load_noto_sans_fonts():
    fontsets = []
    for prefix in [f.split('-')[0] for f in os.listdir(_CVTTF_ROOT_PATH+'/fonts/NotoSans/others')]:
        prefix_path = _CVTTF_ROOT_PATH+'/fonts/NotoSans/others/'+prefix

        if os.path.isfile(prefix_path+'-Regular.ttf'):
            fontset_components = {2: prefix_path+'-Regular.ttf'}
            for width, suffix in zip([1, 3, 4], ['-Light.ttf', '-Bold.ttf', '-Black.ttf']):
                if os.path.isfile(prefix_path+suffix):
                    fontset_components[width] = prefix_path+suffix
            fontsets.append(FontSet(fontset_components))
    return fontsets

# for fs in load_noto_sans_fonts(): print(fs)