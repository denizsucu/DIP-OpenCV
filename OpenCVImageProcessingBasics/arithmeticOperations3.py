import cv2 as cv
import numpy as np

img1 = cv.imread("images/image.jpg")
img2 = cv.imread("images/img1.png")

row, col, channel = img2.shape
roi = img1[0:row, 0:col]    # region of img2

img2Gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)    # convert gray
cv.imshow("Gray Image", img2Gray)

ret, mask = cv.threshold(img2Gray, 200, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)     # invert to mask

cv.imshow("Mask", mask)
cv.imshow("Mask's Invert", mask_inv)

img1_bg = cv.bitwise_and(roi, roi, mask=mask)   # we gave the img1's bg to img2's mask
cv.imshow("img1 Background", img1_bg)

img2_fg = cv.bitwise_and(img2, img2, mask=mask_inv)
cv.imshow("img2 Foreground", img2_fg)

finalImage = cv.add(img1_bg, img2_fg)   # Finally we add img2 fg and img1 bg
img1[0:row, 0:col] = finalImage
cv.imshow("Final Image", img1)

cv.waitKey(0)
cv.destroyAllWindows()
