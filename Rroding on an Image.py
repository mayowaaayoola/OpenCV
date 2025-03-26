
# import cv2 as cv2
# import numpy as np

# img = cv2.imread(r"C:\Users\padra\Desktop\Polycarp to Marcion.png")

# if img is None:
#     print("Image Not Loaded!")
# else:
#     applyCanny = cv2.Canny(img, 120, 180)
#     applyDilate = cv2.dilate(applyCanny, (4,4), iterations = 3)
#     applyErode = cv2.erode(applyDilate, (5,5), iterations = 2)

# cv2.imshow("Eroding an Image", applyErode)

# saveImage = cv2.imwrite(r"C:\Users\padra\Desktop\ErodedImagePolycarp.png", applyErode)

# if saveImage:
#     print("Your Image has been saved")
# else:
#     print("Your image was not saved")

# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np

# Load the image
img = cv2.imread(r"C:\Users\padra\Desktop\Polycarp to Marcion.png")

# Check if the image is read correctly
if img is None:
    print("Image Not Loaded!")
else:
    # Apply Canny edge detection
    applyCanny = cv2.Canny(img, 120, 180)

    # Apply dilation to the edges
    kernel_dilate = np.ones((4, 4), np.uint8)  # Kernel for dilation
    applyDilate = cv2.dilate(applyCanny, kernel_dilate, iterations=3)

    # Apply erosion to the dilated edges
    kernel_erode = np.ones((5, 5), np.uint8)  # Kernel for erosion
    applyErode = cv2.erode(applyDilate, kernel_erode, iterations=2)

    # Display the eroded image
    cv2.imshow("Eroding an Image", applyErode)

    # Save the processed image
    saveImage = cv2.imwrite(r"C:\Users\padra\Desktop\ErodedImagePolycarp.png", applyErode)

    if saveImage:
        print("Your Image has been saved")
    else:
        print("Your image was not saved")

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()  # Add parentheses to actually call the function

