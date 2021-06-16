import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0.5, 0],
                [0, 1, 0]], dtype=np.float32)

h, w = src.shape[:2]
dst = cv2.warpAffine(src, aff, (w + int(h * 0.5), h))
dst2 = cv2.warpAffine(src, aff, (0, 0))
# 창의 크기가 바뀌지 않아서 사진이 짤림.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
