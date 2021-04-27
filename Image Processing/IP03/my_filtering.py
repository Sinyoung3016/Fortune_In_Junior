import cv2
import numpy as np


def my_filtering(src, ftype, fsize, pad_type='zero'):
    mask = my_mask(ftype, fsize)
    src = my_filter(src, mask)

    m_h, m_w = mask.shape
    dst = my_padding(src, (m_h//2, m_w//2), pad_type)
    return dst


def my_mask(ftype, fsize):
    (f_h, f_w) = fsize
    size = f_w * f_h

    mask = np.full((f_h, f_w), 1 / size)
    if ftype == 'sharpen':
        print("sharpen filtering")
        cover = np.zeros((f_h, f_w))
        cover[f_h // 2][f_w // 2] = 2
        mask = cover - mask
    if ftype == 'average':
        print("average filtering")
    return mask


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


def main():
    src = cv2.imread('Lena.png', cv2.IMREAD_GRAYSCALE)
    # Average filter zero padding
    dst1 = my_filtering(src, 'average', (3, 3), 'zero')
    dst2 = my_filtering(src, 'average', (5, 5), 'zero')
    dst3 = my_filtering(src, 'average', (11, 13), 'zero')
    # Sharpening filter zero padding
    dst4 = my_filtering(src, 'sharpen', (3, 3), 'zero')
    dst5 = my_filtering(src, 'sharpen', (5, 5), 'zero')
    dst6 = my_filtering(src, 'sharpen', (11, 13), 'zero')
    # Sharpening filter repetition padding
    dst7 = my_filtering(src, 'sharpen', (11, 13), 'repetition')

    dst1 = dst1.astype(np.uint8)
    dst2 = dst2.astype(np.uint8)
    dst3 = dst3.astype(np.uint8)
    dst4 = dst4.astype(np.uint8)
    dst5 = dst5.astype(np.uint8)
    dst6 = dst6.astype(np.uint8)
    dst7 = dst7.astype(np.uint8)

    cv2.imshow('origin', src)
    cv2.imshow('Average33', dst1)
    cv2.imshow('Average55', dst2)
    cv2.imshow('Average1113', dst3)
    cv2.imshow('Sharpening33', dst4)
    cv2.imshow('Sharpening55', dst5)
    cv2.imshow('Sharpening1113', dst6)
    cv2.imshow('repetition', dst7)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()