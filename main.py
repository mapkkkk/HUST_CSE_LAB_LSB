# -*- coding: UTF-8 -*-
import task as ta
key = "Hust_cse_lsb_hidden_FIag_X0r_passwd"  # encrypt passwd
with open("flag.txt", "r", encoding='utf-8') as f:
    flag = f.read()
length = len(flag)  # decrypt str length,default is len(flag),but can be number,e.g:32,64,etc

ta.ui()
ta.lsb_encode()
ta.lsb_decode(length)
ta.lsb_xor_encode(key)
ta.lsb_xor_decode(key, length)
ta.show()
