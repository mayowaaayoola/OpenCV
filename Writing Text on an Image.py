import cv2 as cv2
import numpy as np

img = cv2.imread(r"C:\Users\padra\Desktop\DUWoGzye_400x400.jpg")

cv2.putText(img, "Writing text on an image", (20, 30), cv2.FONT_HERSHEY_TRIPLEX, 1.2, (255, 0, 200), 4)

cv2.imshow("Text on Image", img)

cv2.waitKey(0)

