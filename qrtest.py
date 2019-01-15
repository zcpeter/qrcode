import qrcode
import os
import sys
import time
 
QRImagePath = os.getcwd() + '/qrcode.png'   #临时存储位置
qr = qrcode.QRCode(    
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)   #设置图片格式
 
data = 'http://weixin.qq.com/r/LS1PV5jEucXGrdw093g-'  #运行时输入数据
qr.add_data(data)
qr.make(fit=True)
 
img = qr.make_image()
img.save('qrcode.png')  #生成图片
 
if sys.platform.find('darwin') >= 0:
    os.system('open %s' % QRImagePath)
   
elif sys.platform.find('linux') >= 0:
    os.system('xdg-open %s' % QRImagePath)
else:
    os.system('call %s' % QRImagePath)
   
#time.sleep(15)   #间隔5个单位
#os.remove(QRImagePath)  #删除图片

