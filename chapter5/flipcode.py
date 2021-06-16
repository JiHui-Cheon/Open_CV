import cv2
import sys

src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.flip(src, 1)
dst2 = cv2.flip(src, 0)
dst3 = cv2.flip(src, -1)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)

cv2.waitKey()

cv2.destroyAllWindows()

# for f in(-1,0,1):
#     dst = cv2.flip(src, f , dst=None)
#     cv2.imshow('dst',dst)
#     cv2.moveWindow('dst', 30, 300)
#     cv2.waitKey()
# cv2.waitKey()
# cv2.destroyAllWindows()


