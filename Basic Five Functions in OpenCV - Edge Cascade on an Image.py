
# import cv2 as cv2
# import numpy as np

# # img = cv2.imread(r"C:\Users\padra\Desktop\Python\OpenCV\volume_100_slice_70_jpg.rf.107f05d1e8d46e2122959586bdabbe9a.jpg")

# # applyCanny = cv2.Canny(img, 120, 180)

# # cv2.imshow("Canny Edges", applyCanny)

# img = cv2.imread(r"C:\Users\padra\Desktop\GCcYL1Za0AAUHb2.jpeg")

# applyCanny2 = cv2.Canny(img, 1250, 175)

# cv2.imshow = ("2nd Canny Edges", applyCanny2) - Point of Error

# cv2.waitKey(0)
# cv2.destroyAllWindows

import cv2 as cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\padra\Desktop\GCcYL1Za0AAUHb2.jpeg")

# Apply the Canny edge detector
applyCanny2 = cv2.Canny(img, 125, 175)

# Display the result
cv2.imshow("2nd Canny Edges", applyCanny2)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()


