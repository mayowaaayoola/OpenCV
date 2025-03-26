import cv2 as cv2

capture = cv2.VideoCapture("C:\\Users\\padra\\Desktop\\Python\\OpenCV\\How to install opencv in Python 3.10.mp4")

while True:
    isTrue, frame = capture.read()
    cv2.imshow('Video1', frame)

    if cv2.waitKey(20) & 0XFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()