import cv2

# Read the image
img = cv2.imread(r"C:\Users\padra\Desktop\MyMCIImage.png")

# Check if the image is read correctly
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply the Canny edge detector
    edges = cv2.Canny(gray, 125, 175)

    # Create a color mask where edges are white and other regions are black
    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Combine original image with the edge mask
    combined = cv2.addWeighted(img, 0.8, edges_colored, 0.5, 0)

    # Display the result
    cv2.imshow("Edges Overlayed on Original", combined)

    # Save the processed image to a file
    save_success = cv2.imwrite(r"C:\Users\padra\Desktop\Overlayed_Edges.png", combined)

    if save_success:
        print("Image saved successfully.")
    else:
        print("Failed to save image.")

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
