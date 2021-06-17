import sys
import numpy as np
import cv2


# 영상 불러오기
src1 = cv2.imread('graf1.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('graf3.png', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

# 특징점 알고리즘 객체 생성 (KAZE, AKAZE, ORB 등)
feature = cv2.KAZE_create()
feature2 = cv2.AKAZE_create()
feature3 = cv2.ORB_create() #default 5000 개

# 특징점 검출 및 기술자 계산
kp1 = feature.detect(src1)
_, desc1 = feature.compute(src1, kp1)

kp2, desc2 = feature.detectAndCompute(src2, None)

kp3 = feature2.detect(src1)
_, desc3 = feature2.compute(src1, kp3)
kp4, desc4 = feature2.detectAndCompute(src2, None)

kp5 = feature3.detect(src1)
_, desc5 = feature3.compute(src1, kp5)
kp6, desc6 = feature3.detectAndCompute(src2, None)

print('desc1.shape:', desc1.shape)
print('desc1.dtype:', desc1.dtype)
print('desc2.shape:', desc2.shape)
print('desc2.dtype:', desc2.dtype)

# 검출된 특징점 출력 영상 생성
dst1 = cv2.drawKeypoints(src1, kp1, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
dst2 = cv2.drawKeypoints(src2, kp2, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
dst3 = cv2.drawKeypoints(src1, kp3, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
dst4 = cv2.drawKeypoints(src2, kp4, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
dst5 = cv2.drawKeypoints(src1, kp5, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
dst6 = cv2.drawKeypoints(src2, kp6, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('kaze1', dst1)
cv2.imshow('kaze2', dst2)
cv2.imshow('akaze1', dst3)
cv2.imshow('akaze2', dst4)
cv2.imshow('orb1', dst5)
cv2.imshow('orb2', dst6)

cv2.waitKey()
cv2.destroyAllWindows()
