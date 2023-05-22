# -*- coding: UTF-8 -*-
import cv2
import matplotlib.pyplot as plt


def img_show():
    img1 = cv2.imread("src.bmp")
    title = "src"
    plt.subplot(1, 3, 1)
    plt.imshow(img1)
    plt.title(title, fontsize=8)
    plt.xticks([])
    plt.yticks([])
    img2 = cv2.imread("res.bmp")
    title = "res"
    plt.subplot(1, 3, 2)
    plt.imshow(img2)
    plt.title(title, fontsize=8)
    plt.xticks([])
    plt.yticks([])
    img3 = cv2.imread("res_encrypt.bmp")
    title = "res_encrypt"
    plt.subplot(1, 3, 3)
    plt.imshow(img3)
    plt.title(title, fontsize=8)
    plt.xticks([])
    plt.yticks([])
    plt.show()
