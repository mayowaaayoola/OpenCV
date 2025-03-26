
# import cv2 as cv2
# import numpy as np

# img = cv2.imread(r"C:\Users\padra\Desktop\MyMCIImage.png")

# if img is None:
#     print("Error: Image is not found")
# else:
#     applyCanny = cv2.Canny(img, 100, 150)
#     applyDilate = cv2.dilate(applyCanny, (8,8), iterations=4)

# cv2.imshow("My Apply Dilate", applyDilate)

# savemyDilate = cv2.imwrite(r"C:\Users\padra\Desktop\applyDilate.png", applyDilate)

# if savemyDilate:
#     print("You are now dilated!")
# else:
#     print("Consult your physician :)")

# cv2.waitKey(0)
# cv2.destroyAllWindows


import cv2
import numpy as np

# Load the image
img = cv2.imread(r"C:\Users\padra\Desktop\MyMCIImage.png")

# Check if the image is read correctly
if img is None:
    print("Error: Image is not found")
else:
    # Apply Canny edge detection
    applyCanny = cv2.Canny(img, 100, 150)

    # Apply dilation to the edges
    kernel = np.ones((8, 8), np.uint8)  # Define a kernel
    applyDilate = cv2.dilate(applyCanny, kernel, iterations=4)

    # Display the result
    cv2.imshow("My Apply Dilate", applyDilate)

    # Save the processed image
    savemyDilate = cv2.imwrite(r"C:\Users\padra\Desktop\Dilated_Image.png", applyDilate)

    if savemyDilate:
        print("You are now dilated!")
    else:
        print("Consult your physician :)")

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
