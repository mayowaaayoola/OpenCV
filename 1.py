import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\padra\Desktop\MyMCIImage.png")

if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply the Canny edge detector
    edges = cv2.Canny(gray, 125, 175)

    # Create a color mask
    colored_edges = np.zeros_like(img)
    colored_edges[edges != 0] = [0, 255, 0]  # Green color for edges

    # Combine original image with the colored edges
    combined = cv2.addWeighted(img, 0.8, colored_edges, 1, 0)

    # Display the result
    cv2.imshow("Colorized Canny Edges", combined)

    # Save the processed image to a file
    save_success = cv2.imwrite(r"C:\Users\padra\Desktop\Colorized_Edges.png", combined)

    if save_success:
        print("Image saved successfully.")
    else:
        print("Failed to save image.")

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
