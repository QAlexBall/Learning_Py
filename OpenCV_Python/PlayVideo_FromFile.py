# 从文件中播放视频
import numpy as np
import cv2

cap = cv2.VideoCapture('H:/Video/output.avi')
#获得码率及尺寸  
fps = cap.get(5)
size = (int(cap.get(3)), int(cap.get(4)))  
'''
if cap.isOpened():
	while True:
		ret, frame = cap.read()
		cv2.imshow('myself', frame)
		k = cv2.waitKey(25)
		if k == ord('q'):
			break;
cv2.destroyWindows('myself')
'''

if cap.isOpened():  
    while True:  
        ret, frame = cap.read()  
        if ret == True:  
            cv2.imshow('video', frame)  
        else:  
            break  
        if cv2.waitKey(20) == ord('q'):  
            break  
cv2.destroyAllWindows()

