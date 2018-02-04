import numpy as np
import cv2

path = 'H:/Image/1.jpg'
# cv2.imread第一个参数是给函数提供完整路径, 第二个参数说明如何读取这幅图片
# cv2.IMREAD_COLOR: 读入一幅彩色图像. 图像的透明度会被忽略
# cv2.IMREAD_GRAYSCALE: 以灰度模式读入图像
# cv2.IMREAD_UNCHANGED: 读入一幅图像, 并包括图像的alpha通道
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
'''
print(img)
cv2.imshow('image', img)
return_keyvalue = cv2.waitKey(10000) # 返回按下那个键的ASCII码, 如果没有按下, 返回-1
print(return_keyvalue)
cv2.destroyWindow('image') # 删除特定的窗口
'''

# 先创建要给窗口, 之后再加载图像.
# 可以决定窗口是否可以调大小, 使用cv2.namedWindow()
# 标签是cv2.WINDOW_NORMAL.
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyWindow('image')

# save image
# cv2.imwrite()用来保存一个图像, 首先需要一个文件名, 之后是想要保存的图像
# cv2.imwrite('Image/imwrite.jpg', img)

# 如果是64位系统, k = cv2.waitKey(0)需要改成 k = cv2.waitKey(0)&0xFF. 
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:
	cv2.destroyWindow('image')
elif k == ord('s'):
	cv2.imwrite('Image/write_test.png', img)
	cv2.destroyWindow('image')