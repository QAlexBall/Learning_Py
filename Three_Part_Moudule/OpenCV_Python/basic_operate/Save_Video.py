# 保存视频
import cv2
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('H:/Video/output.avi', fourcc, 20.0, (640, 480))
while(cap.isOpened()):
	# 第一个参数ret的值为True或False，代表有没有读到图片
	# 第二个参数是frame，是当前截取一帧的图片。
	ret, frame = cap.read()
	if ret == True:
		frame = cv2.flip(frame, 0)

		# Write the flipped frame
		out.write(frame)

		cv2.imshow('frame', frame)
		if cv2.waitKey(1) == ord('q'):
			break
	else:
		 break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()