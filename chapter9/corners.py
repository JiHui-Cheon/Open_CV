import sys
import numpy as np
import cv2


src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)
# src = cv2.imread('sea.png', cv2.IMREAD_GRAYSCALE)
# src = cv2.imread('flag.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

tm = cv2.TickMeter()

# GFTT
tm.start()

corners = cv2.goodFeaturesToTrack(src, 400, 0.01, 10)

src2 = src.copy()
corners2 = cv2.goodFeaturesToTrack(src2, 400, 0.01, 50) # 코너점 사이의 최소거리를 늘려보기

tm.stop()
print('GFTT: {}ms.'.format(tm.getTimeMilli()))

dst1 = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
dst3 = cv2.cvtColor(src2, cv2.COLOR_GRAY2BGR)

if corners is not None:
    for i in range(corners.shape[0]):
        pt = (int(corners[i, 0, 0]), int(corners[i, 0, 1])) # 원의 중심 좌표
        cv2.circle(dst1, pt, 5, (0, 0, 255), 2)

# print(corners.shape) -> (400, 1, 2)

if corners2 is not None:
    for i in range(corners2.shape[0]):
        pt = (int(corners2[i, 0, 0]), int(corners2[i, 0, 1]))
        cv2.circle(dst3, pt, 5, (0, 0, 255), 2)


# FAST
tm.reset()
tm.start()

fast = cv2.FastFeatureDetector_create(60)
keypoints = fast.detect(src)

tm.stop()
print('FAST: {}ms.'.format(tm.getTimeMilli()))

dst2 = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)


for kp in keypoints:
    pt = (int(kp.pt[0]), int(kp.pt[1]))
    cv2.circle(dst2, pt, 5, (0, 0, 255), 2)

cv2.imshow('src', src)
cv2.imshow('gftf', dst1)
cv2.imshow('fast', dst2)
cv2.imshow('gftf<', dst3)
cv2.waitKey()

cv2.destroyAllWindows()
