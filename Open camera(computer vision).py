import cv2

# Try different camera indices
vs =cv2.VideoCapture(0)


if not vs.isOpened():
    print("Error: Couldn't open the camera.")
else:
    while True:
        ret, img = vs.read()

        # Check if the frame is empty
        if not ret or img is None:
            print("Error: Couldn't read frame from the camera.")
            break

        cv2.imshow('img', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vs.release()
    cv2.destroyAllWindows()



 

