#cv2 function

import cv2
import numpy as np

src = cv2.imread('capture.png', cv2.IMREAD_GRAYSCALE)
add_src = cv2.add(src, 128)
sub_src= cv2.subtract(src, 128)

cv2.imshow('src', src)
cv2.imshow('add_src', add_src)
cv2.imshow('sub_ src', sub_src)

cv2.waitKey()
cv2.destroyAllWindows()