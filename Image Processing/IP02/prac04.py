#histogram stretch

import numpy as np
import cv2
import matplotlib.pyplot as plt

def my_calcHist_gray_mini_img(mini_img):
    h, w = mini_img.shape[:2]
    hist = np.zeros((256,), dtype=np.int)
    for row in range(h):
        for col in range(w):
            intensity = mini_img[row, col]
            hist[intensity] += 1
    return hist

def my_hist_stretch(src, hist):
    (h, w) = src.shape
    dst = np.zeros((h,w), dtype=np.uint8)
    min = 256
    max = -1

    for i in range(len(hist)):
        if hist[i] != 0 and i < min:
            min = i
        if hist[i] != 0 and i > max:
            max = i

    hist_stretch = np.zeros(hist.shape, dtype = np.int)
    for i in range(min, max+1):
        j = int((255-0)/(max-min) * (i-min) + 0)
        hist_stretch[j] = hist[i]

    for row in range(h):
        for col in range(w):
            dst[row, col] = (255-0)/(max-min) * (src[row, col] - min) + 0

    return dst, hist_stretch

if __name__ == '__main__':
    src = cv2.imread('capture.png', cv2.IMREAD_GRAYSCALE)
    hist = my_calcHist_gray_mini_img(src)

    dst, hist_stretch = my_hist_stretch(src, hist)

    binX = np.arange(len(hist_stretch))
    plt.bar(binX, hist, width=0.8, color='g')
    plt.title('image')
    plt.xlabel('pixel intensity')
    plt.ylabel('pixel num')
    plt.show()

    plt.bar(binX, hist_stretch, width=0.8, color='g')
    plt.title('stretch image')
    plt.xlabel('pixel intensity')
    plt.ylabel('pixel num')
    plt.show()

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()