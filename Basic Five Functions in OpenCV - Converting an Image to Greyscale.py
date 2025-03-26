import cv2 as cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

img = cv2.imread(r"C:\Users\padra\Desktop\Python\OpenCV\volume_100_slice_70_jpg.rf.107f05d1e8d46e2122959586bdabbe9a.jpg")

grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Img", grayimg)

cv2.waitKey(0)
cv2.destroyAllWindows()







