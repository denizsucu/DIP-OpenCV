
# Farklı Geometrik Şekillerin Bir Görüntü Üzerine Çizilimi

import cv2 as cv
import numpy as np

img = np.zeros((512,512,3), np.uint8)

# çizgi çizelim
cv.line(img,(0,0), (511, 511), (255,0,0),5) # name, start p., finish p, color, tickness
cv.line(img,(511,0), (0, 511), (255,0,0),5)

# Dikdörtgen Çizelim
cv.rectangle(img,(50,50), (200, 300), (0,255,0),5)
cv.rectangle(img,(250,50), (400, 300), (0,0,250),-1) #içi dolu olacak

# Çember ya da daire çizelim
cv.circle(img, (255,255), 50, (150,150,150), 2) # img, center, radius, color, tickness
cv.circle(img, (350,350), 50, (250,150,100), -1)

#Elips çizelim
cv.ellipse(img, (255,255), (100, 150), 0, 0, 180,(255,100,0), 3 )
cv.ellipse(img, (400,355), (100, 150), 0, 0, 180,(255,100,0), -1 )

# Çokgen çizmek
points = np.array([[20,30],[100,120],[255,255],[10,400]], np.int32)
pointShaped = points.reshape(-1,1,2)

cv.polylines(img,[points],True, (255,255,255), 3)

# Yazı Yazmak
font = cv.FONT_HERSHEY_COMPLEX

cv.putText(img, "OpenCv", (50,250), font, 2, (0,155, 155), 2, cv.LINE_AA)

cv.imshow("resim", img)

cv.waitKey(0)
cv.destroyAllWindows()



