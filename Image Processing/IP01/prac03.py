import numpy as np
import cv2

src = np.zeros((300,300,3), dtype=np.uint8)

src[100:200, :100] = [255,0,0]
src[100:200, 100:200] = [0, 255, 0]
src[100:200, 200:] = [0, 0, 255]

src[:100, :100] = [255,0,255]
src[:100, 100:200] = [255, 255, 0]
src[:100, 200:] = [0, 255, 255]

src[200:, :100] = [255,255,255]
src[200:, 100:200] = [128, 128, 128]
src[200:, 200:] = [0,0,0]

print(src.shape)
print(src[0,0,0], src[0,0,1], src[0,0,2])
print(src[0,0])
#print(src[0])

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()