import sys
import numpy as np
import cv2


# 컬러 영상 불러오기
src = cv2.imread('candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

# 컬러 영상 속성 확인
print('src.shape:', src.shape)  # src.shape: (480, 640, 3)
print('src.dtype:', src.dtype)  # src.dtype: uint8

#HUE 색 평면 분활
src_YCrCb =cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
Y_plane, Cr_plane, Cb_plane = cv2.split(src_YCrCb)


# HUE display
cv2.imshow('src', src)
cv2.imshow('Y_plane', Y_plane) # 밝기
cv2.imshow('Cr_plane', Cr_plane) # 색차
cv2.imshow('Cb_plane', Cb_plane)  # 색차

cv2.waitKey()

cv2.destroyAllWindows()