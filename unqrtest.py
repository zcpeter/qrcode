# coding = utf-8
import os
import zxing    #导入解析包

zx = zxing.BarCodeReader()      #调用zxing二维码读取包
zxdata = zx.decode('qrcode.jpg')    #图片解码

print(zxdata)    #打印出二维码名字
