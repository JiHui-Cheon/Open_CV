import sys
import numpy as np
import cv2


src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, -1, 1, 0, delta=128) # grayscale로 보기위해서 delta값을 임의로 128 넣어줌.
dy = cv2.Sobel(src, -1, 0, 1, delta=128)
# dalta값 0 넣으면 검정색으로 보임.

cv2.imshow('src', src)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.waitKey()

cv2.destroyAllWindows()
