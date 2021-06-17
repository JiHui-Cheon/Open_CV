import sys
import numpy as np
import cv2


# 영상 불러오기
src1 = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('img3.jpg', cv2.IMREAD_GRAYSCALE)


if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

# 특징점 알고리즘 객체 생성 (KAZE, AKAZE, ORB 등)
feature = cv2.KAZE_create()
feature2 = cv2.AKAZE_create() #hamming distance를 사용
feature3 = cv2.ORB_create()

# 특징점 검출 및 기술자 계산
kp1, desc1 = feature.detectAndCompute(src1, None)
kp2, desc2 = feature.detectAndCompute(src2, None)

kp3, desc3 = feature2.detectAndCompute(src1, None)
kp4, desc4 = feature2.detectAndCompute(src2, None)

kp5, desc5 = feature3.detectAndCompute(src1, None)
kp6, desc6 = feature3.detectAndCompute(src2, None)


# 특징점 매칭
matcher = cv2.BFMatcher_create()
matcher2 = cv2.BFMatcher_create(cv2.NORM_HAMMING)

matches = matcher.match(desc1, desc2)
matches2 = matcher2.match(desc3, desc4)
matches3 = matcher2.match(desc5, desc6)

print('# of kp1:', len(kp1))
print('# of kp2:', len(kp2))
print('# of matches:', len(matches))
print()
print('# of kp3', len(kp3))
print('# of kp4', len(kp4))
print('# of matchs:', len(matches2))
print()
print('# of kp5', len(kp5))
print('# of kp6', len(kp6))
print('# of matches:', len(matches3))

# 특징점 매칭 결과 영상 생성
dst = cv2.drawMatches(src1, kp1, src2, kp2, matches, None)
dst2 = cv2.drawMatches(src1, kp3, src2, kp4, matches2, None)
dst3 = cv2.drawMatches(src1, kp5, src2, kp6, matches3, None)

cv2.imshow('kaze', dst)
cv2.imshow('akaze', dst2)
cv2.imshow('orb', dst3)

cv2.waitKey()
cv2.destroyAllWindows()
