#creating self drawn image.
import cv2
import numpy as np
#Reading of image.....
img=np.zeros((512,512,3))#Providing shapes to my image.....
#draw the rectangele:
cv2.rectangle(img,pt1=(5,5),pt2=(510,510),color=(255,0,0),thickness=3)
#agar thickness -1 diye to rectangle andar se fil completely filled.
#draw circle()
cv2.circle(img,center=(250,250),radius=200,color=(0,0,255),thickness=5)
#create font or text.
cv2.putText(img,org=(50,250),color=(0,255,255),thickness=2,text="HELLO!",lineType=cv2.LINE_AA,fontFace=cv2.FONT_ITALIC,fontScale=4)
cv2.imshow("Window",img)
cv2.waitKey(0)