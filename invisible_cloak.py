import cv2
import numpy as np

cap = cv2.VideoCapture(0)
background = cv2.imread('C:/Users/User/Desktop/Projects/frame.jpg')

while cap.isOpened():

    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower_red = np.array([0,100,100])
        upper_red = np.array([10,255,255])

        mask = cv2.inRange(hsv,lower_red,upper_red)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3),np.uint8))

        part_1 = cv2.bitwise_and(background,background,mask=mask) #Converting all the red pixels to the background

        mask = cv2.bitwise_not(mask) #ignoring all red pixels 

        part_2 = cv2.bitwise_and(frame,frame,mask=mask)

        cv2.imshow("cloak",part_1+part_2)

        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()