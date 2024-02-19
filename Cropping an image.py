import cv2
import numpy as np
img=cv2.imread("C:\\Users\\khush\\Desktop\\khushicode\\course 1\\Image Processing\\Image(Open CV).png")
img_crop=img[100:400,100:500]
cv2.putText(img_crop, "cropped_Image", (10, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255,0), 2)
cv2.imshow("window",img_crop)
cv2.waitKey(0)

