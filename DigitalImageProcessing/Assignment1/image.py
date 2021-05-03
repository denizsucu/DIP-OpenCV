import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def flipImage(img, flipType):
    (h, w) = img.shape
    img2 = np.zeros([h, w], np.uint8)
    if flipType == "vertical":
        for i in range(h):
            img2[i, :] = img[h - i - 1, :]
    elif flipType == "horizontal":
        for i in range(w):
            img2[:, i] = img[:, w - i - 1]
    else:
        print("Wrong Flip Type!")
    return img2


def generateHistogram(gray_img):
    (h, w) = gray_img.shape
    hist = [0]*256

    for i in range(gray_img.shape[0]):
        for j in range(gray_img.shape[1]):
            hist[gray_img[i, j]] += 1
    return hist


def cumulativeDistFreq(c):
    cumDistFreq = [0] * len(c)
    cumDistFreq[0] = c[0]

    for i in range(1, len(c)):
        cumDistFreq[i] = cumDistFreq[i - 1] + c[i]

    for x in cumDistFreq:
        cumDistFreq = x * 255 / cumDistFreq[-1]

    return cumDistFreq


def equalizeHistogram(gray_img):
    frq = cumulativeDistFreq(generateHistogram(gray_img))
    equalizedImage = np.interp(gray_img, range(0, 256), frq)
    return equalizedImage


def main():
    originalImage = cv.imread("image.jpg")
    grayImage = cv.cvtColor(originalImage, cv.COLOR_BGR2GRAY)
    # print(grayImage.shape)    # it gives the shape of image
    flpImg1 = flipImage(grayImage, "horizontal")
    flpImg2 = flipImage(grayImage, "vertical")
    cv.imshow("gray", grayImage)
    cv.imshow("Flip Image", flpImg1)
    cv.imwrite("flip-h.png", flpImg1)
    cv.imwrite("flip-v.png", flpImg2)
    plt.plot(generateHistogram(grayImage))
    plt.show()
    equalizedImage = equalizeHistogram(grayImage)
    cv.imwrite("eq.png", equalizedImage)
    # cv.imshow("Equalize Histogram", equalizedImage)
    # plt.plot(generateHistogram(equalizedImage))
    # plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
