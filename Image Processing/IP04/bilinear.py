import cv2
import numpy as np


def my_bilinear(src, scale):
    (h, w) = src.shape
    h_dst = int(h * scale + 0.5)
    w_dst = int(w * scale + 0.5)

    dst = np.zeros((h_dst, w_dst), np.int8)

    # bilinear interpolation 적용
    for row in range(h_dst):
        for col in range(w_dst):
            s_r = int(row/scale)
            s_c = int(col/scale)
            dh = row / scale - s_r
            dw = col / scale - s_c
            if s_r + 1 < h and s_c + 1 < w:
                dst[row, col] = ((1 - dh) * (1 - dw) * src[s_r, s_c]) + ((1 - dh) * dw * src[s_r, s_c + 1]) \
                                + (dh * dw * src[s_r + 1, s_c + 1]) + (dh * (1 - dw) * src[s_r + 1, s_c])
            else:
                dst[row, col] = src[s_r, s_c]
    return dst


if __name__ == '__main__':
    src = cv2.imread('./Lena.png', cv2.IMREAD_GRAYSCALE)

    scale = 1/2
    #이미지 크기 1/2배로 변경
    my_dst_mini = my_bilinear(src, scale)
    my_dst_mini = my_dst_mini.astype(np.uint8)

    #이미지 크기 2배로 변경(Lena.png 이미지의 shape는 (512, 512))
    my_dst = my_bilinear(my_dst_mini, 1/scale)
    my_dst = my_dst.astype(np.uint8)

    cv2.imshow('original', src)
    cv2.imshow('my bilinear mini', my_dst_mini)
    cv2.imshow('my bilinear', my_dst)

    cv2.waitKey()
    cv2.destroyAllWindows()


