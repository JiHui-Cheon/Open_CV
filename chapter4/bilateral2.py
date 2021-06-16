import sys
import numpy as np
import cv2
src = cv2.imread('lenna.bmp')
if src is None:
    print('Image load failed!')
    sys.exit()

#스페이스바를 눌러보며 변하는 값을 확인
for d in(10,50,100,200):
    dst = cv2.bilateralFilter(src, -1, d, 5)
    cv2.imshow('dst', dst) 
    cv2.moveWindow('dst', 31, 300)
    cv2.waitKey()
cv2.destroyAllWindows()