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

#HUE 색 평면 분할
src_hsv =cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
H_plane, S_plane, V_plane = cv2.split(src_hsv)

#b_plane = src[:, :, 0]
#g_plane = src[:, :, 1]
#r_plane = src[:, :, 2]


# HUE display
cv2.imshow('src', src)
cv2.imshow('H_plane', H_plane) # 색 종류
cv2.imshow('S_plane', S_plane) # 선명도
cv2.imshow('V_plane', V_plane)  # 밝기

cv2.waitKey()

cv2.destroyAllWindows()