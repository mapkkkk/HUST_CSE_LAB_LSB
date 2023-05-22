# -*- coding:UTF-8 -*-
from PIL import Image


def mod(x, y):
    return x % y


def func(le, str1, str2):
    b = ""
    im = Image.open(str1)
    lenth = le * 8
    width = im.size[0]
    height = im.size[1]
    count = 0
    for h in range(0, height):
        for w in range(0, width):
            pixel = im.getpixel((w, h))
            if count % 3 == 0:
                count += 1
                b = b + str((mod(pixel[0], 2)))
                if count == lenth:
                    break
            if count % 3 == 1:
                count += 1
                b = b + str((mod(pixel[1], 2)))
                if count == lenth:
                    break
            if count % 3 == 2:
                count += 1
                b = b + str((mod(pixel[2], 2)))
                if count == lenth:
                    break
        if count == lenth:
            break
    with open(str2, "w", encoding='utf-8') as f:
        for i in range(0, len(b), 8):
            stra = int(b[i:i + 8], 2)
            f.write(chr(stra))
            stra = ""
    f.closed


def lsb_de(le, new, flag_res):
    # len,input,flag_output
    func(le, new, flag_res)
