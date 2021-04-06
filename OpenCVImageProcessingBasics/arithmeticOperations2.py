import cv2 as cv
import numpy as np

img1 = cv.imread("images/img1.png")
img2 = cv.imread("images/img2.png")

total = cv.addWeighted(img1, 0.4, img2, 0.6, 0)     # total of two images with weighted

cv.imshow("Toplam", total)

cv.waitKey(0)
cv.destroyAllWindows()
