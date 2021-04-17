import numpy as np
import cv2

from IP05.my_filtering import my_filtering

if __name__ == '__main__':

    src = cv2.imread('./threshold_test.png', cv2.IMREAD_GRAYSCALE)
    ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)

    print('ret :', ret)
    cv2.imshow('src', src)
    cv2.imshow('dst', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()