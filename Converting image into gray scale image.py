#how to read an image:
import cv2
import numpy as np

img=cv2.imread("C:\\Users\\khush\\Desktop\\khushicode\\course 1\\Image Processing\\Image(Open CV).png")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.putText(img_gray, "Gray Scale Img", (10, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)
print(type(img))#This code show that it is type of nd array.
print(img_gray.shape)#code to find out the resolution of image.
cv2.imshow("Window",img_gray)#To print the image in window name as window.
cv2.waitKey(0)#yhe image ko window pr rokhne k kiye.
