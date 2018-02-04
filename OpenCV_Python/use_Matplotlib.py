import numpy as np 
import cv2
from matplotlib import pyplot as plt 

# import shutil
# shutil.copyfile('H:/Image/2.jpg', 'Image/image.jpg')

img = cv2.imread('Image/image.jpg', cv2.IMREAD_COLOR)
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
# plt.show()

b, g, r = cv2.split(img)
img2 = cv2.merge([r, g, b])
plt.subplot(121);plt.imshow(img) # expects true color
plt.subplot(122);plt.imshow(img2) # expects distorted color
plt.show()

cv2.imshow('bgr image', img)
cv2.imshow('rgb image', img2)
if cv2.waitKey(0) == ord('q'):
	cv2.destroyWindow('image')