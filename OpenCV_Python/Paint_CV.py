# 使用OpenCV绘制不同几何图形
# cv2.line(), cv2.circle(), cv2.rectangel(), cv2.ellipse(), cv2.putText()
# img: 图像
# color: 形状的颜色
# thickness: 线条的粗细
# linetype: 线条的类型, 8连接(默认), 抗锯齿等.

# paint line
import numpy as np
import cv2

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == ord('q'):
	cv2.destroyAllWindows()
	pass