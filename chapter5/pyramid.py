import sys
import numpy as np
import cv2


src = cv2.imread('cat.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()


rc = (250, 120, 200, 200)  # rectangle tuple

# 원본 영상에 그리기
cpy = src.copy()
cv2.rectangle(cpy, rc, (0, 0, 255), 2) # (이미지, 좌표, color(B,G,R), 선 두께)
cv2.imshow('src', cpy)
cv2.waitKey()

# 피라미드 영상에 그리기
for i in range(1, 4):
    src = cv2.pyrDown(src)
    cpy = src.copy()
    cv2.rectangle(cpy, rc, (0, 0, 255), 2, shift = i) # shift = 좌표값의 축소비율
    cv2.imshow('src', cpy)
    cv2.waitKey()
    cv2.destroyWindow('src')

cv2.destroyAllWindows()
