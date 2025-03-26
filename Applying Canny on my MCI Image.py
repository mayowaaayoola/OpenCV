
import cv2 as cv2
import numpy as np

img = cv2.imread(r"C:\Users\padra\Desktop\MyMCIImage.png")

if img is None:
    print("Error: Image is not found")
else:
    applyCanny = cv2.Canny(img, 100, 150)

cv2.imshow("My MCI Image Canny", applyCanny)

save_myCanny = cv2.imwrite(r"C:\Users\padra\Desktop\MyMCIImageCanny.png", applyCanny)

if save_myCanny:
    print("Image has been saved successfully")
else:
    print("Check your work again")

cv2.waitKey(0)
cv2.destroyAllWindows