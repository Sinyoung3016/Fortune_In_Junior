import numpy as np
import cv2
import time


def Quantization_Luminance():
    luminance = np.array(
        [[16, 11, 10, 16, 24, 40, 51, 61],
         [12, 12, 14, 19, 26, 58, 60, 55],
         [14, 13, 16, 24, 40, 57, 69, 56],
         [14, 17, 22, 29, 51, 87, 80, 62],
         [18, 22, 37, 56, 68, 109, 103, 77],
         [24, 35, 55, 64, 81, 104, 113, 92],
         [49, 64, 78, 87, 103, 121, 120, 101],
         [72, 92, 95, 98, 112, 100, 103, 99]])
    return luminance


def C(w, n=8):
    if w == 0:
        return (1 / n) ** 0.5
    else:
        return (2 / n) ** 0.5


def C_I(p, n=8):
    dst = np.zeros((n,n))
    for h in range(n):
        for w in range(n):
            if p[h, w] == 0:
                dst[h, w] = (1 / n) ** 0.5
            else:
                dst[h, w] = (2 / n) ** 0.5

    return dst


def DCT(block, n=8):
    ######################################
    # TODO                               #
    # DCT 완성                            #
    ######################################
    dst = np.zeros(block.shape)
    y, x = dst.shape
    v, u = np.mgrid[0:y, 0:x]

    for y_ in range(y):
        for x_ in range(x):
            p_x = (np.pi * (2 * u + 1) * x_) / (n * 2)
            p_y = (np.pi * (2 * v + 1) * y_) / (n * 2)
            p_F = np.cos(p_x) * np.cos(p_y)
            dst[y_, x_] = C(y_) * C(x_) * np.sum(p_F * block[v, u])
    return np.round(dst)


def DCT_inv(block, n=8):
    ###################################################
    # TODO                                            #
    # DCT_inv 완성                                     #
    # DCT_inv 는 DCT와 다름.                            #
    ###################################################
    dst = np.zeros(block.shape)
    y, x = dst.shape
    v, u = np.mgrid[0:y, 0:x]

    for y_ in range(y):
        for x_ in range(x):
            p_x = (np.pi * (2 * x_ + 1) * u) / (n * 2)
            p_y = (np.pi * (2 * y_ + 1) * v) / (n * 2)
            p_F = np.cos(p_x) * np.cos(p_y)
            dst[y_, x_] = np.sum(C_I(v) * C_I(u) * block[v, u] * p_F)

    return np.round(dst)


def img2block(src, n=8):
    ######################################
    # TODO                               #
    # img2block 완성                      #
    # img를 block으로 변환하기              #
    ######################################
    (h, w) = src.shape
    h = (h + (h % n) if h % n != 0 else h)
    w = (w + (w % n) if w % n != 0 else w)
    b_h = h // n
    b_w = w // n
    dst = np.zeros((h, w), dtype=np.uint8)
    dst[:h, :w] = src

    blocks = list()
    for h_ in range(b_h):
        for w_ in range(b_w):
            blocks.append(dst[n * h_:n * (h_ + 1), n * w_:n * (w_ + 1)])

    return np.array(blocks)


def block2img(blocks, src_shape, n=8):
    ###################################################
    # TODO                                            #
    # block2img 완성                                   #
    # 복구한 block들을 image로 만들기                     #
    ###################################################
    (h, w) = src_shape
    h = (h + (h % n) if h % n != 0 else h)
    w = (w + (w % n) if w % n != 0 else w)
    b_h = h // n
    b_w = w // n
    dst = np.zeros(src_shape, dtype=np.uint8)

    for h_ in range(b_h):
        for w_ in range(b_w):
            block = blocks[h_ * b_h + w_]
            dst[n * h_:n * (h_ + 1), n * w_:n * (w_ + 1)] = block
    return dst[:src_shape[0], :src_shape[1]]


def my_zigzag_scanning(src, mode='encoding', block_size=8):
    dst = []
    if mode == 'encoding':
        dst.append(src[0, 0])
        for k in range(1, block_size):
            if k % 2 == 1:  # 홀수
                for r in range(k + 1):
                    dst.append(src[r, k - r])
            else:
                for r in range(k + 1):
                    dst.append(src[k - r, r])
        p = 0
        for k in range(block_size-1, 0, -1):
            p += 1
            if k % 2 == 1:  # 홀수
                for r in range(k):
                    dst.append(src[p + r, block_size - 1 - r])
            else:
                for r in range(k):
                    dst.append(src[block_size - 1 - r, p + r])
        idx = 0
        for t in range(len(dst)):
            if dst[t] != 0:
                idx = t

        dst = dst[:idx+1]
        dst.append('EOB')
    elif mode == 'decoding':
        dst = np.zeros((block_size,block_size))
        dst[0, 0] = src[0]
        i = 1
        for k in range(1, block_size):
            if k % 2 == 1:  # 홀수
                for r in range(k + 1):
                    if src[i] == 'EOB':
                        break
                    dst[r, k - r] = src[i]
                    i += 1
            else:
                for r in range(k + 1):
                    if src[i] == 'EOB':
                        break
                    dst[k - r, r] = src[i]
                    i += 1
        p = 0
        for k in range(block_size-1, 0, -1):
            if src[i] == 'EOB':
                break
            p += 1
            if k % 2 == 1:  # 홀수
                for r in range(k):
                    if src[i] == 'EOB':
                        break
                    dst[p + r, block_size - 1 - r] = src[i]
                    i += 1
            else:
                for r in range(k):
                    if src[i] == 'EOB':
                        break
                    dst[block_size - 1 - r, p + r] = src[i]
                    i += 1
    return dst


def Encoding(src, n=8):
    #################################################################################################
    # TODO                                                                                          #
    # Encoding 완성                                                                                  #
    # Encoding 함수를 참고용으로 첨부하긴 했는데 수정해서 사용하실 분은 수정하셔도 전혀 상관 없습니다.              #
    #################################################################################################
    print('<start Encoding>')
    # img -> blocks
    blocks = img2block(src, n=n)

    # subtract 128
    blocks -= 128

    # DCT
    blocks_dct = []
    for block in blocks:
        blocks_dct.append(DCT(block, n=n))
    blocks_dct = np.array(blocks_dct)

    # Quantization + thresholding
    Q = Quantization_Luminance()
    QnT = np.round(blocks_dct / Q)

    # zigzag scanning
    zz = []
    for i in range(len(QnT)):
        zz.append(my_zigzag_scanning(QnT[i]))
    return zz, src.shape


def Decoding(zigzag, src_shape, n=8):
    #################################################################################################
    # TODO                                                                                          #
    # Decoding 완성                                                                                  #
    # Decoding 함수를 참고용으로 첨부하긴 했는데 수정해서 사용하실 분은 수정하셔도 전혀 상관 없습니다.              #
    #################################################################################################
    print('<start Decoding>')

    # zigzag scanning
    blocks = []
    for i in range(len(zigzag)):
        blocks.append(my_zigzag_scanning(zigzag[i], mode='decoding', block_size=n))
    blocks = np.array(blocks)

    # Denormalizing
    Q = Quantization_Luminance()
    blocks = blocks * Q

    # inverse DCT
    blocks_idct = []
    for block in blocks:
        blocks_idct.append(DCT_inv(block, n=n))
    blocks_idct = np.array(blocks_idct)

    # add 128
    blocks_idct += 128

    # block -> img
    dst = block2img(blocks_idct, src_shape=src_shape, n=n)
    return dst


def main():
    start = time.time()
    src = cv2.imread('./Lena.png', cv2.IMREAD_GRAYSCALE)
    comp, src_shape = Encoding(src, n=8)

    # 과제의 comp.npy, src_shape.npy를 복구할 때 아래 코드 사용하기(위의 2줄은 주석처리하고, 아래 2줄은 주석 풀기)
    #comp = np.load('comp.npy', allow_pickle=True)
    #src_shape = np.load('src_shape.npy')

    recover_img = Decoding(comp, src_shape, n=8)
    total_time = time.time() - start

    print('time : ', total_time)
    if total_time > 45:
        print('감점 예정입니다.')
    cv2.imshow('recover img', recover_img)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
