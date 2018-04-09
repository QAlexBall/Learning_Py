# 使用OpenCV绘制不同几何图形
# cv2.line(), cv2.circle(), cv2.rectangel(), cv2.ellipse(), cv2.putText()
# img: 图像
# color: 形状的颜色
# thickness: 线条的粗细
# linetype: 线条的类型, 8连接(默认), 抗锯齿等.


import numpy as np
import cv2
'''
img = np.zeros((512, 512, 3), np.uint8) # Create a black image
cv2.line(img, (0, 0), (400, 512), (255, 0, 0), 5) # Draw a diagonal blue line with thickness of 5 px
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3) # Draw a rectangle
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, (255, 255, 0), -1) # Draw a ellipse

cv2.imshow('image', img)
cv2.waitKey(0)
'''
# pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# pts = pts.reshape((-1, 1, 2))
# cv2.imshow('image', pts)
# cv2.waitKey(0)

# 在图片上添加文字
path = 'H:/Image/1.jpg'
img = cv2.imread(path)
print(img.shape[0] / 3, img.shape[1] / 3)
img = cv2.resize(img, (640, 360), interpolation=cv2.INTER_CUBIC)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 300), font, 0.8, (255, 255, 255), 2)
winname = 'example'
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)

