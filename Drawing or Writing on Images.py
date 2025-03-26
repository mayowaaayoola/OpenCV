import cv2 as cv2
import numpy as np

#blankimg = np.zeros((500,500,3), dtype = 'uint8')
#cv2.imshow('Blank Image', blankimg)

#img2 = cv2.imread("C:\\Users\\padra\\Desktop\\Sabinus.jpg")
#cv2.imshow('img2', img2)

#Painting img2 with a colour
#img2[101:218, 336:398] = 0, 205, 0
#cv2.imshow('Coloured', img2)

#Painting part of blankimg with colour
#blankimg[220:293, 317:469] = 215,205,0
#cv2.imshow('PartColoured', blankimg)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Drawing a rectangle

img2 = cv2.imread("C:\\Users\\padra\\Desktop\\Sabinus.jpg")
cv2.imshow('img3', img2)

cv2.rectangle(img2, (10,10), (213,312), (15,205,255), thickness = 4)
cv2.imshow('Drawing a rectangle on a picture', img2)

#Drawing a rectangle to fill an image
img2 = cv2.imread("C:\\Users\\padra\\Desktop\\Sabinus.jpg")
cv2.imshow('img4', img2)

cv2.rectangle(img2, (30,40), (230,325), (105,205,255), thickness = cv2.FILLED)
cv2.imshow('Drawing a rectangle to fill a picture', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

