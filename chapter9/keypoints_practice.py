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
feature3 = cv2.ORB_create()

# 특징점 검출
kp1 = feature.detect(src1)
kp2 = feature.detect(src2)

kp3 = feature2.detect(src1)
kp4 = feature2.detect(src2)

kp5 = feature3.detect(src1)
kp6 = feature3.detect(src2)

print('# of kp1:', len(kp1))
print('# of kp2:', len(kp2))

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

# for i in range(1, 7):
#     dst = cv2.drawKeypoints(src1, kp3, None,
#                          flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


cv2.imshow('kaze1', dst1)
cv2.imshow('kaze2', dst2)
cv2.imshow('akaze1', dst3)
cv2.imshow('akaze2', dst4)
cv2.imshow('orb1', dst5)
cv2.imshow('orb2', dst6)

cv2.waitKey()
cv2.destroyAllWindows()
