# 学习使用OpenCV处理鼠标事件
# cv2.setMouseCallback()
# 创建一个简单程序, 在图片双击的位置绘制一个圆圈

import cv2
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

import numpy as np
# mouse callback function

'''
def draw_circle(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img, (x, y), 100, (255, 0, 0), -1)

# 创建图像与窗口并将窗口与回调函数绑定
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
	cv2.imshow('image', img)
	quit = cv2.waitKey(0)
	if quit == ord('q'):
		break
cv2.destroyAllWindows()

'''

drawing = False # 当鼠标按下时变为True
mode = True # 如果mode为true绘制矩阵, 按'm'变成绘制曲线
ix, iy = -1, -1

# 创建回调函数
def draw_circle(event, x, y, flags, param):
	global ix, iy, drawing, mode
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y
	elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
		if drawing == True:
			if mode == True:
				cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
			else:
				cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
	elif event == cv2.EVENT_LBUTTONUP:
		drawing == False
		
# 创建图像与窗口并将窗口与回调函数绑定
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
	cv2.imshow('image', img)
	quit = cv2.waitKey(0)
	if quit == ord('q'):
		break
cv2.destroyAllWindows()