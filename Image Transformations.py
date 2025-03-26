
import cv2 as cv2
import numpy as np

img = cv2.imread(r"C:\Users\padra\Desktop\Polycarp to Marcion.png")

if img is None:
    print("Error: Image is not loaded")
else:
    translatedImg = translate(img, 80, 120)
    cv2.imshow("Translated Image", translatedImg)
    
    
def translate(img, x, y):
        transMat = np.float32([[1, 0, x], [0, 1, y]])
        dimensions = (img.shape[1], img.shape[0])
        return cv2.warpAffine(img, dimensions, transMat)
    
saveTranslated = cv2.imwrite(r"C:\Users\padra\Desktop\TranslatedPolycarpToMarcion.png")

if saveTranslated:
    print("Translated Image has been saved")
else:
    print("Translated Image has not yet been saved")

cv2.waitKey(0)
cv2.destroyAllWindows()