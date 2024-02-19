#how to read an image:
import cv2
import numpy as np

img=cv2.imread("C:\\Users\\khush\\Desktop\\khushicode\\course 1\\Image Processing\\Image(Open CV).png")
#img_crop=img[0:400,0:400])
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(type(img))#This code show that it is type of nd array.
print(img.shape)#code to find out the resolution of image.
imgBlue=img[:,:,0]
imgGreen=img[:,:,1]
imgRed=img[:,:,2]
new_img=np.hstack((imgBlue,imgGreen,imgRed))#jb humko multiple image pr kaam krna ho tb use krte h.
cv2.imshow("Window",new_img)#To print the image in window name as window.
cv2.waitKey(0)#yhe image ko window pr rokhne k kiye.
