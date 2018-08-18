# 用摄像头捕获视频
# 先创建一个VideoCapture对象. 它的参数可以实设备的索引号
# 或是一个视频文件. 
# Cap.isOpen检查是否初始化成功
# cap.get(propId)可以获取是平的一些参数信息, propId从0~18代表视频的一个属性
# cap.set(propId, value)可以修改视频属性
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
# 利用cv2.VideoWriter_fourcc(*’XVID’)定义视频格式，然后创建视频写入对象。
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('/path/to/output.avi', fourcc, 20, (640, 480))
while(True):
	# Capture frame-by-frame
	ret, frame = cap.read() # cap.read()返回True/False
	print(cap.get(3), cap.get(4))
	out.write(frame)

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#Display the resulting frame
	cv2.imshow('frame', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()