#휘도

import cv2
import numpy as np

src = cv2.imread('capture.png')
(h, w, c) = src.shape
yuv = cv2.cvtColor(src, cv2.COLOR_BGR2YUV)
my_y = np.zeros((h,w))
my_y = (src[:,:,0] * 0.114) + (src[:,:,1] * 0.587) + (src[:,:,2] * 0.299)
my_y = (my_y + 0.5).astype(np.uint8)

cv2.imshow('original', src)
cv2.imshow('cvtColor', yuv[:,:,0])
cv2.imshow('my_y', my_y)

print(yuv[0:5, 0:5, 0])
print(yuv[0:5, 0:5])

cv2.waitKey()
cv2.destroyAllWindows()