#image filtering : sharpen

import cv2
import numpy as np


def my_sharpening_filter_3x3(src):
    mask = np.array([[-1/9,-1/9,-1/9],[-1/9,17/9,-1/9],[-1/9,-1/9,-1/9]])
    dst = cv2.filter2D(src, -1, mask)
    return dst


if __name__ == '__main__':
    src = cv2.imread('Lena.png', cv2.IMREAD_GRAYSCALE)
    dst = my_sharpening_filter_3x3(src)

    cv2.imshow('original', src)
    cv2.imshow('sharpening filter', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()