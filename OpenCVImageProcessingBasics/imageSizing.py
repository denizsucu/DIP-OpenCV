import cv2 as cv


def main():
    img = cv.imread("images/image.jpg")
    screen_resolution = 680, 420

    scale_width = screen_resolution[0] / img.shape[1]
    scale_height = screen_resolution[1] / img.shape[0]
    scale = min(scale_width, scale_height)

    window_width = int(img.shape[1] * scale)
    window_height = int(img.shape[0] * scale)

    cv.namedWindow("Resizeable Window", cv.WINDOW_NORMAL)     # it provides us resizeable window
    cv.resizeWindow("Resizeable Window", window_width, window_height)

    cv.imshow("Resizeable Window", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
