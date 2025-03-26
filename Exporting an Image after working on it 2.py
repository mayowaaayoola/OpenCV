import cv2 as cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\padra\Desktop\GCcYL1Za0AAUHb2.jpeg")

# Check if the image is read correctly
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Apply the Canny edge detector
    applyCanny2 = cv2.Canny(img, 125, 175)

    # Display the result (this may not work in all environments)
    cv2.imshow("2nd Canny Edges", applyCanny2)

    # Save the processed image to a file
    save_success = cv2.imwrite(r"C:\Users\padra\Desktop\Processed_Image.jpg", applyCanny2)

    if save_success:
        print("Image saved successfully.")
    else:
        print("Failed to save image.")

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
