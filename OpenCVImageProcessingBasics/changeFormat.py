import cv2 as cv
import numpy as np


def submit(path, image, jpg_quality=None, png_compress=None):
    if jpg_quality:
        cv.imwrite(path, image, [int(cv.IMWRITE_JPEG_QUALITY), jpg_quality])

    elif png_compress:
        cv.imwrite(path, image, [int(cv.IMWRITE_PNG_COMPRESSION), png_compress])

    else:
        cv.imwrite(path, image)


def main():
    img_path = 'images/img1.png'
    img = cv.imread(img_path)

    cv.imshow("Image", img)

    final_jpg = "images/img1JPG.jpg"
    submit(final_jpg, img, jpg_quality=85)  # submits the image jpg format

    final_png = "images/img1PNG.png"
    submit(final_png, img, png_compress=4)  # submit the image png compression format

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
