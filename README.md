# HUST_CSE_LAB_LSB
LSB method hide information
华中科技大学网络空间安全学院网安实践2 LSB隐写

使用说明:
1. 需要安装pillow,numpy,matplotlib,opencv,即pip3 install pillow numpy matplotlib
2. 在windows下,pip3 install opencv-python;在linux下,pip3 install python3-opencv
3. 在程序目录下打开终端,输入python3 main.py,或者直接在ide中运行main.py
4. 用来隐藏的图片请放在程序目录下,命名为src.bmp,如果没有,目录下已经自带一张4k分辨率的bmp图像
5. 准备隐藏的语句请放入flag.txt中,注意,只支持英文、数字和下划线
6. 能隐藏的语句长度和bmp图像大小有关,图像太小可能会丢失信息
7. 加密密钥请在main.py中更改key的值
8. 解密lsb隐写的图片时,需要指定准备解密的字符串长度,请在main.py中更改length的值
9. length过长时,解密出的字符串末尾会出现无效信息
10. length过短时,解密出的字符串会丢失部分信息
