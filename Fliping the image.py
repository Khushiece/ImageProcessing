import cv2
import numpy as np

img=cv2.imread("C:\\Users\\khush\\Desktop\\khushicode\\course 1\\Image Processing\\Image(Open CV).png")
img_flip=cv2.flip(img,-1)
cv2.putText(img_flip, "Flipped Image", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)
cv2.imshow("Window",img_flip)
cv2.waitKey(0)