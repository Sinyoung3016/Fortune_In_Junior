import cv2
import numpy as np


def my_filtering(src, mask, pad_type='zero'):
    src = my_filter(src, mask)

    m_h, m_w = mask.shape
    dst = my_padding(src, (m_h//2, m_w//2), pad_type)
    return dst


def my_filter(src, mask):
    m_h, m_w = mask.shape
    s_h, s_w = src.shape

    d_h = s_h - m_h + 1
    d_w = s_w - m_w + 1
    dst = np.zeros((d_h, d_w))

    for i in range(d_h):
        for j in range(d_w):
            fil_img = src[i:i + m_h, j:j + m_w]
            dst[i, j] = np.sum(mask * fil_img)

    dst = np.where(dst > 255, 255, dst)
    dst = np.where(dst < 0, 0, dst)

    return dst


def my_padding(src, pad_shape, pad_type='zero'):
    (h, w) = src.shape
    (p_h, p_w) = pad_shape
    pad_img = np.zeros((h+2*p_h, w+2*p_w))
    pad_img[p_h:p_h+h, p_w: p_w+w] = src

    if pad_type == 'repetition':
        print("repetition padding")
        # up
        pad_img[:p_h, p_w:p_w+w] = src[0]
        # down
        pad_img[h+p_h:2*h+p_h, p_w:p_w+w] = src[h-1]
        # left & right
        for i in range(p_w):
            pad_img[:, i] = pad_img[:, p_w]
            pad_img[:, w + p_w + i] = pad_img[:, w + p_w - 1]
    else:
        print("zero padding")

    return pad_img