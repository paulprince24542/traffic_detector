import cv2

cap1 = cv2.VideoCapture(0)  # Camera 1
cap2 = cv2.VideoCapture(1)  # Camera 2

cap1.set(3, 640)
cap1.set(4, 480)


cap2.set(3, 640)
cap2.set(4, 480)

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    cv2.imshow('Camera 1', frame1)
    cv2.imshow('Camera 2', frame2)
    if cv2.waitKey(1) == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()