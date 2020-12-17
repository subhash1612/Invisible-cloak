import cv2
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if ret: #If the frame is read successfully
        cv2.imshow("frame",frame)
        if cv2.waitKey(5) == ord('q'):
            cv2.imwrite('frame.jpg',frame)
            break


cap.release()
cv2.destroyAllWindows()