import cv2 as cv
import numpy as np

img = cv.imread("images/saat.jpg")

print(img[80, 80])  # prints that position's pixel value "bgr"
img[80, 80] = [255, 255, 255]  # it changes this point to white

part = img[30:120, 100:200]  # a part of image
# img[30:120, 100:200] = [(0, 200, 200)]  # fully colorful in rectangle
img[0:90, 0:100] = part     # it copies this part to given location

cv.rectangle(img, (100, 30), (200, 120), (0, 200, 200), 2)  # it shapes that part

cv.imshow("saat", img)
cv.imshow("saat2", part)

cv.waitKey(0)
cv.destroyAllWindows()
