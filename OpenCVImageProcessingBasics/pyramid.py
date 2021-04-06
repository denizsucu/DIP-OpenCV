import cv2 as cv

img = cv.imread("images/image.jpg")

up = cv.pyrUp(img)
down = cv.pyrDown(img)  # like image order size

cv.imshow("Original Image", img)
cv.imshow("Up Image", up)
cv.imshow("Down Image", down)

cv.waitKey(0)
cv.destroyAllWindows()
