import cv2 as cv2

img2 = cv2.imread(r"C:\Users\padra\Desktop\GMGXQTyXgAA0udT.jpeg")

cv2.imshow('4009', img2)

def rescaleFrame(frame, scale = 0.3):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

cv2.waitKey(0)


import cv2 as cv2

capture = cv2.VideoCapture("C:\\Users\\padra\\Desktop\\Python\\OpenCV\\How to install opencv in Python 3.10.mp4")

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)


    cv2.imshow('Video1', frame)
    cv2.imshow('Video1 resized', frame_resized)

    if cv2.waitKey(20) & 0XFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()