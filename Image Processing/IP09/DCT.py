import cv2
import numpy as np


#jpeg는 보통 block size = 8
def C(w, n = 8):
    if w == 0:
        return (1/n)**0.5
    else:
        return (2/n)**0.5


def Spatial2Frequency_mask(block, n = 8):
    dst = np.zeros(block.shape)
    v, u = dst.shape

    y, x = np.mgrid[0:u, 0:v]
    mask = np.zeros((n*n, n*n))

    ##########################################################################
    # ToDo                                                                   #
    # mask 만들기                                                             #
    # mask.shape = (16x16)                                                   #
    # DCT에서 사용된 mask는 (4x4) mask가 16개 있음 (u, v) 별로 1개씩 있음 u=4, v=4  #
    # 4중 for문으로 구현 시 감점 예정                                             #
    ##########################################################################

    for v_ in range(v):
        for u_ in range(u):
            p_x = (np.pi * (2 * x + 1) * u_) / (n * 2)
            p_y = (np.pi * (2 * y + 1) * v_) / (n * 2)
            p_F = np.cos(p_x) * np.cos(p_y)
            mask[v_ * n:(v_+1) * n, u_ * n : (u_+1) * n] = my_normalize(p_F)

    return mask


def my_normalize(src):
    dst = src.copy()
    if src.min() != 1:
        src = src - src.min()
        dst = src / src.max()
    return dst * 255


if __name__ == '__main__':
    block_size = 4
    src = np.ones((block_size, block_size))

    mask = Spatial2Frequency_mask(src, n=block_size)
    mask = mask.astype(np.uint8)
    print(mask)

    #크기가 너무 작으니 크기 키우기 (16x16) -> (320x320)
    mask = cv2.resize(mask, (320, 320), interpolation=cv2.INTER_NEAREST)

    cv2.imshow('mask_201902699', mask)
    cv2.waitKey()
    cv2.destroyAllWindows()
