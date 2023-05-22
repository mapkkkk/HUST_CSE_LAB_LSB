# -*- coding: UTF-8 -*-
from PIL import Image


def plus(str):
    return str.zfill(8)


def get_key(strr):
    tmp = strr
    f = open(tmp, "rb")
    s = f.read()
    str = ""
    for i in range(len(s)):
        str = str + plus(bin(s[i]).replace('0b', ''))
    f.closed
    return str


def mod(x, y):
    return x % y


def func(str1, str2, str3):
    im = Image.open(str1)
    width = im.size[0]
    height = im.size[1]
    count = 0
    key = get_key(str2)
    keylen = len(key)
    for h in range(0, height):
        for w in range(0, width):
            pixel = im.getpixel((w, h))
            a = pixel[0]  # R
            b = pixel[1]  # G
            c = pixel[2]  # B
            if count == keylen:
                break
            a = a - mod(a, 2) + int(key[count])
            count += 1
            if count == keylen:
                im.putpixel((w, h), (a, b, c))
                break
            b = b - mod(b, 2) + int(key[count])
            count += 1
            if count == keylen:
                im.putpixel((w, h), (a, b, c))
                break
            c = c - mod(c, 2) + int(key[count])
            count += 1
            if count == keylen:
                im.putpixel((w, h), (a, b, c))
                break
            if count % 3 == 0:
                im.putpixel((w, h), (a, b, c))
    im.save(str3)


def lsb_en(old, new, enc):
    # raw,output,flag
    func(old, enc, new)
