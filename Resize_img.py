import cv2
import numpy as np
img=cv2.imread("C:\\Users\\khush\\Desktop\\khushicode\course 1\\Image Processing\\Image(Open CV).png")
#img_resize=cv2.resize(img,(256,256))
#Agar humko size pata na ho to tb...half size krne k code:
img_resize=cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))

cv2.imshow("Window",img_resize)

cv2.waitKey(0)