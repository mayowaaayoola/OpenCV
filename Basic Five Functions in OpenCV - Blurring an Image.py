import cv2 as cv2

# Load the image
img = cv2.imread("C:/Users/padra/Desktop/DUWoGzye_400x400.jpg")

# Apply Gaussian blur to the image
blur = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)

# Display the blurred image
cv2.imshow("Blurred Image", blur)

# Wait for a key press and close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()





