import cv2
import numpy as np

src = cv2.imread('capture.png')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

cv2.imshow('original', src)
cv2.imshow('gray', gray)
cv2.imshow('rgb', rgb)

print('[BGR] {0}' .format(src[0,0]))
print('[GRAY] {0}' .format(gray[0,0]))
print('[RGB] {0}' .format(rgb[0,0]))

cv2.waitKey()
cv2.destroyAllWindows()