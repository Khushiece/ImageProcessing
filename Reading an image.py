#how to read an image:
import cv2
import numpy as np
img=cv2.imread("C:\\Users\\khush\\Desktop\\khushicode\\course 1\\Image Processing\\Image(Open CV).png")
print(type(img))#This code show that it is type of nd array.
print(img.shape)#code to find out the resolution of image.
cv2.imshow("Window",img)#To print the image in window name as window.
cv2.waitKey(0)#yhe image ko window pr rokhne k kiye.
