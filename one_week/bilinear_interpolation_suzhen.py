import numpy as np
import cv2

'''
bilinear interpolation
'''


def bilinear_interpolation_mine(img, out_dim):
    s_h, s_w, s_c = img.shape
    d_h, d_w = out_dim[1], out_dim[0]
    d_img = np.zeros((d_h, d_w, 3), dtype=np.uint8)
    if s_h == d_h and s_w == d_w:
        return img.copy()
    else:
        print("image loaded")
    sca_x = float(s_w) / d_w
    print("sca_x", sca_x)
    sca_y = float(s_h) / d_h
    print("sca_y", sca_y)
    for i in range(s_c):
        for d_y in range(d_h):
            for d_x in range(d_w):
                s_x = (d_x + 0.5) * sca_x - 0.5
                s_y = (d_y + 0.5) * sca_y - 0.5

                s_x0 = int(np.floor(s_x))
                s_x1 = min(s_x0 + 1, s_w - 1)
                s_y0 = int(np.floor(s_y))
                s_y1 = min(s_y0 + 1, s_h - 1)

                s_xx = (s_x1 - s_x) * img[s_y0, s_x0, i] + (s_x - s_x0) * img[s_y0, s_x1, i]
                s_yy = (s_x1 - s_x) * img[s_y1, s_x0, i] + (s_x - s_x0) * img[s_y1, s_x1, i]
                d_img[d_y, d_x, i] = int((s_y1 - s_y) * s_xx + (s_y - s_y0) * s_yy)
    return d_img


if __name__ == '__main__':
    img = cv2.imread('lenna.png')
    cv2.imshow('src', img)
    cv2.waitKey(1)
    dst = bilinear_interpolation_mine(img, (700, 700))
    cv2.imshow('bilinear interp', dst)
    cv2.waitKey()
