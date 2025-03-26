import cv2

# Read the image
img = cv2.imread(r"C:\Users\padra\Desktop\MyMCIImage.png")

# Check if the image is read correctly
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Laplacian edge detection
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)

    # Display the result
    cv2.imshow("Laplacian Edge Detection", laplacian)

    # Save the processed image to a file
    save_success = cv2.imwrite(r"C:\Users\padra\Desktop\Laplacian_Edges.png", laplacian)

    if save_success:
        print("Image saved successfully.")
    else:
        print("Failed to save image.")

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
