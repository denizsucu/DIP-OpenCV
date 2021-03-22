
# Trackbar'lar ile renk ayarlama

import cv2 as cv
import numpy as np

def nothing(x):
    pass

img = np.zeros((512, 512, 3), np.uint8)

cv.namedWindow("resim")

cv.createTrackbar("R", "resim", 0, 255, nothing)
cv.createTrackbar("G", "resim", 0, 255, nothing)
cv.createTrackbar("B", "resim", 0, 255, nothing)

cv.createTrackbar("ON/OFF", "resim", 0, 1, nothing)

while(1):
    cv.imshow("resim", img)
    
    if cv.waitKey(1) & 0xFF == 27:
        break
    
    r = cv.getTrackbarPos("R", "resim")
    g = cv.getTrackbarPos("G", "resim")
    b = cv.getTrackbarPos("B", "resim")
    
    switch = cv.getTrackbarPos("ON/OFF", "resim")
    
    if switch:
        img[:] = [b, g, r]
    else:
        img[:] = 0
    
cv.destroyAllWindows()