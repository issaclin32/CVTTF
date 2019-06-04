import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'\\..')
import numpy as np
import cv2
import cvttf

im = cv2.imread('.\\koala.jpg')
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
test_text = """English: koala / Chinese: 無尾熊 / Japanese: コアラ 
/ Vietnamese: gấu túi / Hindu: कोआला/ Thai: โคอาลา / Russian: коа́ла / Hebrew: קוֹאָלָה‎ / """
cvttf.putText(im, '', (10, 10), None, 0.7)

cv2.imshow('', im)
cv2.waitKey(0)