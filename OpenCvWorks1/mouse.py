# Mouse Hareketleri İle İşlemler

import cv2 as cv
import numpy as np

isDrawing = False
mod = False
xi,yi, = -1, -1

#◘ Events
def draw(event, x, y, flags, param):
    
    global isDrawing
    global xi, yi
    
    if event == cv.EVENT_LBUTTONDOWN:
        xi, yi = x, y
        isDrawing = True
        
    elif event == cv.EVENT_MOUSEMOVE:
        if isDrawing == True:
            if mod: 
                cv.circle(img, (x,y),10, (100, 50, 0),-1)
            else:
                cv.rectangle(img,(xi,yi),(x,y),(0, 100, 100), -1)

        else:
            pass            
    elif event == cv.EVENT_LBUTTONUP:
        isDrawing = False
        if mod: 
            cv.circle(img, (x,y),10, (100, 50, 0),-1)
        else:
            cv.rectangle(img,(xi,yi),(x,y),(0, 100, 100), -1)
    
    # # çift click olduğunda bir çember çizer
    # if event == cv.EVENT_LBUTTONDBLCLK:
    #     cv.circle(img,(x,y), 50, (155, 150, 80), 3)

    
img = np.ones((512,512, 3), np.uint8)

cv.namedWindow("paint")

cv.setMouseCallback("paint", draw)

while(1):
    cv.imshow("paint", img)
    
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    if cv.waitKey(1) & 0xFF == ord("m"):
        mod = not mod
    

cv.destroyAllWindows()