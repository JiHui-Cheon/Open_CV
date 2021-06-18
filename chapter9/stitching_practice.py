import sys
import numpy as np
import cv2


img_names = ['mountain1.png', 'mountain2.png']

imgs = []
for name in img_names:
    img = cv2.imread(name)

    if img is None:
        print('Image load failed!')
        sys.exit()

    imgs.append(img)

stitcher = cv2.Stitcher_create()
status, dst = stitcher.stitch(imgs)

if status != cv2.Stitcher_OK:
    print('Stitch failed!')
    sys.exit()

cv2.imwrite('output.jpg', dst)

cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
