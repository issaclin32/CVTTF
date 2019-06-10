import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))+'\\..\\')
import numpy as np
import cv2
import cvttf

def test_1():
    im = cv2.imread('.\\koala.jpg')
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    test_text = """English: koala / Chinese: 無尾熊 / Japanese: コアラ 
    / Vietnamese: gấu túi / Hindu: कोआला/ Thai: โคอาลา / Russian: коа́ла / Hebrew: קוֹאָלָה‎ / """
    cvttf.putText(im, '', (10, 10), None, 0.7)

    cv2.imshow('', im)
    cv2.waitKey(0)
    return

def test_2():
    from cvttf.font_class import FontFamily, FontSet
    from cvttf.builtin_fonts import path_regular

    fs0 = FontSet({2: path_regular})
    fs1 = FontSet('../cvttf/fonts/NotoSansDevanagari-hinted/NotoSansDevanagari-Regular.ttf')
    ff = FontFamily([fs0, fs1])

    for k, v in ff._char_range_combined.items():
        if v == 1:
            print(k, v, end='  ')
    return


if __name__ == '__main__':
    test_2()