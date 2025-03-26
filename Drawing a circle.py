import cv2 as cv2
import numpy as np

img4circle = cv2.imread("C:\\Users\\padra\\Desktop\\GLw9lIsXwAE7cah.jpeg")
cv2.imshow('CircleOnImage', img4circle)

#cv2.circle(img4circle, (250,250), 50, (215,0,255), thickness=4)
#cv2.imshow('Circle', img4circle)

# cv2.circle(img4circle, (img4circle.shape[1]//2, img4circle.shape[0]//3), 70, (105,90,255), thickness=8)
# cv2.imshow('Circle2', img4circle)

# cv2.circle(img4circle, (img4circle.shape[1]//8, img4circle.shape[0]//7), 70, (105,190,255), thickness=8)
# cv2.imshow('Circle3', img4circle)

cv2.circle(img4circle, (img4circle.shape[1]//8, img4circle.shape[0]//7), 70, (105,190,255), thickness=-2)
cv2.imshow('Circle3', img4circle)

cv2.waitKey(0)
cv2.destroyAllWindows()

