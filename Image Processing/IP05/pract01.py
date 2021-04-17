import numpy as np
import cv2

from IP05.my_filtering import my_filtering


def get_sobel():
    derivative = np.array([[-1, 0 ,1]])
    blur = np.array([[1],[2],[1]])

    x = np.dot(blur, derivative)
    y = np.dot(derivative.T, blur.T)

    return x, y


if __name__ == '__main__':
    sobel_x, sobel_y = get_sobel()

    src = cv2.imread('./edge_detection_img.png', cv2.IMREAD_GRAYSCALE)
    dst_x = my_filtering(src, sobel_x, 'zero')
    dst_y = my_filtering(src, sobel_y, 'zero')

    dst_x = np.clip(dst_x, 0, 255).astype(np.uint8)
    dst_y = np.clip(dst_y, 0, 255).astype(np.uint8)
    dst = dst_y + dst_x

    cv2.imshow('dst_x', dst_x)
    cv2.imshow('dst_y', dst_y)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()