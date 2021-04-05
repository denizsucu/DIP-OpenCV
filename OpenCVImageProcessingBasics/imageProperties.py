import cv2 as cv
import numpy as np

img = cv.imread('image.jpg')    # reads image

print(img.item(100, 100, 1))   # shows a point and print bgr pixels => 0-blue, 1-green, 2-red
img.itemset((100, 100, 1), 255)   # it changes the pixel's color

print(img.shape)   # shows img's height, width values, 3 parameter => colourful, 2 parameters => white-black

# To reach pixels numbers we use "size"
print("Colorful: " + str(img.size))     # colorful image size = gray*3

img = cv.imread('image.jpg', 0)     # reads image gray
print("Gray: " + str(img.size))     # gray image size

print(img.dtype)   # Data type

part = img[250:400, 600:800]    # first part of height and second part width
cv.imshow("part", part)     # it provides cutting a part of image
img[250:400, 400:600] = part    # it provides to show that part of img another location at image

img[:, :, 0] = 0    # resets all blue components 0=>blue, 1=> green, 2=>red
img[:, :, 0] = 255  # it makes full blue

cv.imshow("Image", img)     # shows image


cv.waitKey(0)
cv.destroyAllWindows()
