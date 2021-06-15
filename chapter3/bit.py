import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


src1 = cv2.imread('lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('square.bmp', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.bitwise_and(src1, src2, dst = None, mask = None)
# dst2 = cv2.bitwise_or(src1, src2, dst = None, mask = None)

plt.subplot(231), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('src1')
# plt.subplot(231), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('src2')
plt.show()