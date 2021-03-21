# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 20:23:56 2021
@author: Lenovo
"""

import cv2
from sys import exit

# Kameradan görüntü alma

cam = cv2.VideoCapture(0) #hangi kamera olduğunu parametre vererek söylüyoruz

print(cam.get(3))
print(cam.get(4))

cam.set(3, 320) # kameranın boyutlarını böyle değiştirebiliyoruz
cam.set(4, 240)

print(cam.get(3))
print(cam.get(4))

if not cam.isOpened():
    print("Kamera tanınmadı.")
    exit()

# ret kameradan görüntü okunup okunmadığını veriyor
# frame resmin çerçevesini veriyor

while True:
    ret , frame = cam.read()
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # görüntü siyah beyaz oldu
    
    if not ret:
        print("Kameradan görüntü gelmiyor.")
        break
    
    cv2.imshow("kamera", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Görüntü sonlandırıldı!")
        break
    
cam.release()
cv2.destroyAllWindows()


# # Video Okuma - Hazır Video üzerinde işlem yapmak istersek 

cam1 = cv2.VideoCapture("sample.mp4")

while cam.isOpened(): # kamera açık mı kontrol ediyor üsttekine gerek kalmadı
    ret, frame = cam1.read()
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if not ret:
        print("Kameradan görüntü okunamıyor")
        break
    
    cv2.imshow("görüntü", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Video sonlandırıldı!")
        break

# Video Çekme İşlemi

cam2 = cv2.VideoCapture(0)

fourrc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter("videogray.avi", fourrc, 30.0, (640, 480)) # bu isimde video oluşacak

while cam2.isOpened():
    
    ret, frame = cam2.read()
    
    if not ret:
        print("Kameradan görüntü alınamadı")
        break
    
    out.write(frame)
    
    cv2.imshow("kamera", frame)
    
    if cv2.waitKey(1) == ord("q"):
        print("Videodan ayrıldınız")
        break
    
cam2.release()
out.release()
cv2.destroyAllWindows()
    
    










