import cv2
import numpy as np
img = cv2.imread('../Image/image.jpg')
px = img[100, 100]
print(px)
blue = img[100, 100, 0]
print(blue)

img[100, 100] = [255, 255, 255]
print(img[100, 100])
