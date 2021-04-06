import cv2
from matplotlib import pyplot as plt

resim = cv2.imread("images/image.jpg", 0)  # read image, siyah beyaz olma sebebi 0

cv2.namedWindow("resim", cv2.WINDOW_NORMAL) #boyut değişebilir
cv2.imshow("resim", resim)

cv2.imshow("resim penceresi", resim)

plt.imshow(resim, cmap="gray")
plt.show()

k = cv2.waitKey(0)  # tuşların hexadecimal olarak değeri


if k == 27:
    print("ESC tuşuna basıldı")
elif k == ord("q"):
    print("q tuşuna basıldı, resim kayıt edildi")
    cv2.imwrite("treegray.jpg", resim)

# cv2.destroyWindow("resim penceresi")
cv2.destroyAllWindows()  # herhangi bir yere basınca kapanacak

