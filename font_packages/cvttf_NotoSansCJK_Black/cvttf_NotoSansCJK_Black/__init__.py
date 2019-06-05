from os.path import isfile, abspath, dirname


def get_TTF_path() -> str:
    TTF_path = dirname(abspath(__file__))+'/NotoSansCJKtc-Black.otf'
    if not isfile(TTF_path):
        raise FileNotFoundError(f'file "{TTF_path}" does not exist.')
    return TTF_path