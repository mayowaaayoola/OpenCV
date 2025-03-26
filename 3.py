import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\padra\Desktop\MyMCIImage.png")

# Check if the image is read correctly
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Sobel edge detection
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)  # Sobel X
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)  # Sobel Y
    sobel_combined = cv2.sqrt(sobelx**2 + sobely**2)

    # Convert to uint8 type for display
    sobel_combined = cv2.convertScaleAbs(sobel_combined)

    # Display the result
    cv2.imshow("Sobel Edge Detection", sobel_combined)

    # Save the processed image to a file
    save_success = cv2.imwrite(r"C:\Users\padra\Desktop\Sobel_Edges.png", sobel_combined)

    if save_success:
        print("Image saved successfully.")
    else:
        print("Failed to save image.")

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
