# import cv2 as cv2
# import numpy as np

# # Load the image
# img4line = cv2.imread("C:\\Users\\padra\\Desktop\\Polycarp to Marcion.png")

# # Draw a line on the image
# cv2.line(img4line, (200, 300), (300, 400), (215, 215, 255), thickness=3)

# # Display the image with the line
# cv2.imshow('Line on Image', img4line)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2 as cv2
import numpy as np

# Load the image
img4line = cv2.imread("C:\\Users\\padra\\Desktop\\Polycarp to Marcion.png")

# Get the dimensions of the image
height, width, _ = img4line.shape

# Draw a horizontal line to split the image
cv2.line(img4line, (0, height // 2), (width, height // 2), (215, 215, 255), thickness=3)

# Draw a vertical line to split the image
cv2.line(img4line, (width // 2, 0), (width // 2, height), (215, 215, 255), thickness=3)

# Display the image with the lines
cv2.imshow('Lines on Image', img4line)

cv2.waitKey(0)
cv2.destroyAllWindows()

