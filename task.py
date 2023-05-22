# -*- coding: UTF-8 -*-
import lsb_en as en
import lsb_de as de
import os
import re
import img


def str_xor(s: str, k: str):
    k = (k * (len(s) // len(k) + 1))[0:len(s)]
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s, k))


def only_en_and_num(src_str):
    tmp = re.sub(u"([^[0-9a-zA-Z_])", "", src_str)
    tmp = str(tmp)
    return tmp


def lsb_encode():
    src = "src.bmp"
    out = "res.bmp"
    flag = "flag.txt"
    en.lsb_en(src, out, flag)
    print("lsb encoding finished,img output path is 'res.bmp'")


def lsb_decode(length):
    src = "res.bmp"
    flag_res = "flag_output.txt"
    de.lsb_de(length, src, flag_res)
    with open("flag.txt", "r", encoding='utf-8') as f:
        flag = f.read()
    os.remove("flag_output.txt")
    flag = str(flag)
    flag = only_en_and_num(flag)
    print("lsb decoding finished,flag is: ", flag)
    return flag


def lsb_xor_encode(key):
    with open("flag.txt", "r", encoding='utf-8') as f:
        flag = f.read()
    flag = str_xor(flag, key)
    xor_res = flag
    with open("tmp.txt", "w") as f2:
        f2.write(flag)
    src = "src.bmp"
    out = "res_encrypt.bmp"
    flag = "tmp.txt"
    en.lsb_en(src, out, flag)
    os.remove("tmp.txt")
    print("lsb encrypt encoding finished,output path is 'res_encrypt.bmp',flag encrypt res is: ", xor_res)


def lsb_xor_decode(key, length):
    src = "res_encrypt.bmp"
    flag_res = "tmp2.txt"
    de.lsb_de(length, src, flag_res)
    with open("tmp2.txt", "r", encoding='utf-8') as f:
        flag = f.read()
    os.remove("tmp2.txt")
    flag = str_xor(flag, key)
    flag = str(flag)
    flag = only_en_and_num(flag)
    print("lsb decrypt decoding finished,flag is: ", flag)
    return flag


def ui():
    print("Please put img into the dir and rename it as 'src.bmp' and write what you want hide in 'flag.txt'")
    print("Attention!Only support English,Number,underline!")
    print("If you get ready,press any key to continue.")
    input()


def show():
    print("imgs from left to right: src,res,res_encrypt")
    img.img_show()
