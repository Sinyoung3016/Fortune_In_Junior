#image filtering : sharpen

import cv2
import numpy as np


def my_padding(src, pad_shape, pad_type='zero'):
    (h, w) = src.shape # 512
    (p_h, p_w) = pad_shape
    pad_img = np.zeros((h+2*p_h, w+2*p_w))
    pad_img[p_h:p_h+h, p_w: p_w+w] = src

    if pad_type == 'repetition':
        print("repetition padding")
        # up
        pad_img[:p_h, p_w:p_w+w] = src[0]
        # down
        pad_img[h+p_h:2*h+p_h, p_w:p_w+w] = src[h-1]
        # left
        for i in range(p_w):
            pad_img[:, i] = pad_img[:, p_w]
        # right
        for i in range(p_w):
            pad_img[:, w+p_w+i] = pad_img[:, w+p_w-1]
    else:
        print("zero padding")
    return pad_img


def main():
    src = cv2.imread('Lena.png', cv2.IMREAD_GRAYSCALE)

    # zero padding
    dst1 = my_padding(src, (30,50))
    dst1 = dst1.astype(np.uint8)

    # repetition padding
    dst2 = my_padding(src, (30, 50), 'repetition')
    dst2 = dst2.astype(np.uint8)

    cv2.imshow('zero padding', dst1)
    cv2.imshow('repetition padding', dst2)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()