import cv2

# Read the image
img = cv2.imread(r"C:\Users\padra\Desktop\MyMCIImage.png")

# Check if the image is read correctly
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray, 125, 175)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

    # Display the result
    cv2.imshow("Contours", img)

    # Save the processed image to a file
    save_success = cv2.imwrite(r"C:\Users\padra\Desktop\Contours.png", img)

    if save_success:
        print("Image saved successfully.")
    else:
        print("Failed to save image.")

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
