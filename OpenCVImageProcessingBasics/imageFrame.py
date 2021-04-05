import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

blue = [255, 0, 0]

img = cv.imread("python.png")

replicate = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REFLECT101)
wrap = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=blue)

# To Show Single
cv.imshow("Original", img)
cv.imshow("Replicate", replicate)   # extra border => (aaaaaa|abcdefgh|hhhhhhh)
cv.imshow("Reflect", reflect)   # it reflects image like mirror for only border => (fedcba|abcdefgh|hgfedcb)
cv.imshow("Reflect101", reflect101)     # almost similar with reflect => (gfedcb|abcdefgh|gfedcba)
cv.imshow("Wrap", wrap)     # like side by side (cdefgh|abcdefgh|abcdefg)
cv.imshow("Constant", constant)     # frame is a constant color => (iiiiii|abcdefgh|iiiiiii)

# To Show One Place
plt.subplot(231), plt.imshow(img, 'gray'), plt.title("Original")
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title("Replicate")
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title("Reflect")
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title("Reflect101")
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title("Wrap")
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title("Constant")

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
