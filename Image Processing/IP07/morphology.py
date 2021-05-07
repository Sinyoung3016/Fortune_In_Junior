import cv2
import numpy as np


def dilation(B, S):
    b_h, b_w = B.shape
    s_h, s_w = S.shape
    s_h //= 2
    s_w //= 2
    dst = np.zeros((b_h, b_w))

    for row in range(b_h):
        for col in range(b_w):
            if B[row, col] == 1:
                drs = row - s_h
                dre = row + s_h
                dcs = col - s_w
                dce = col + s_w
                if -1 < drs and dre < b_h and -1 < dcs and dce < b_w:
                    dst[drs:dre+1, dcs:dce+1] = S

    return dst


def erosion(B, S):
    b_h, b_w = B.shape
    s_h, s_w = S.shape
    s_h //= 2
    s_w //= 2
    dst = np.zeros((b_h, b_w))

    for row in range(b_h):
        for col in range(b_w):
            if B[row, col] == 1:
                drs = row - s_h
                dre = row + s_h
                dcs = col - s_w
                dce = col + s_w
                if -1 < drs and dre < b_h and -1 < dcs and dce < b_w:
                    if np.array_equal(B[drs:dre + 1, dcs:dce + 1], S):
                        dst[row, col] = 1

    return dst


def opening(B, S):
    return dilation(erosion(B, S), S)


def closing(B, S):
    return erosion(dilation(B, S), S)


if __name__ == '__main__':
    B = np.array(
        [[0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 1, 1, 1, 0],
         [0, 0, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]])

    S = np.array(
        [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]])

    cv2.imwrite('morphology_B.png', (B * 255).astype(np.uint8))

    img_dilation = dilation(B, S)
    img_dilation = (img_dilation * 255).astype(np.uint8)
    print(img_dilation)
    cv2.imwrite('morphology_dilation.png', img_dilation)

    img_erosion = erosion(B, S)
    img_erosion = (img_erosion * 255).astype(np.uint8)
    print(img_erosion)
    cv2.imwrite('morphology_erosion.png', img_erosion)

    img_opening = opening(B, S)
    img_opening = (img_opening * 255).astype(np.uint8)
    print(img_opening)
    cv2.imwrite('morphology_opening.png', img_opening)

    img_closing = closing(B, S)
    img_closing = (img_closing * 255).astype(np.uint8)
    print(img_closing)
    cv2.imwrite('morphology_closing.png', img_closing)
