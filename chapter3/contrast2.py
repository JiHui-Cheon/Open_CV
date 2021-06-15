import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2


src = cv2.imread('Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()


dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)

#made_functions
#gmin= np.min(src)
#gmax= np.max(src)
#dst = ((src - gmin) * 255. / (gmax - gmin)).astype(np.uint8) #numpy사용 동일 결과

hist = cv2.calcHist([src], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([dst], [0], None, [256], [0, 256])

cv2.imshow('src', src)
# cv2.moveWindow('src', 20, 50) 
cv2.imshow('dst', dst)
# cv2.moveWindow('dst', 700, 50)

plt.plot(hist)
plt.plot(hist2)
plt.show()

cv2.waitKey()

# plt.plot(hist)
# plt.show()


cv2.destroyAllWindows()
