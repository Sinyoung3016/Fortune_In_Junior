#histogram

import cv2
import numpy as np
import matplotlib.pyplot  as plt

src = cv2.imread('capture.png', cv2.IMREAD_GRAYSCALE)
#src =cv2.add(src, 40)
#src = src + 40

hist = cv2.calcHist([src], [0], None, [256], [0,256])
plt.plot(hist, color='r')
plt.title('histogram plot')
plt.xlabel('pixel intensity')
plt.ylabel('pixel num')
plt.show()

histFlatten = hist.flatten()

binX = np.arange(len(histFlatten))
plt.bar(binX, histFlatten, width=2, color='g')
plt.title('histogram bar')
plt.xlabel('pixel intensity')
plt.ylabel('pixel num')
plt.show()


