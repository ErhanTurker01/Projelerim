import cv2
import numpy as np

def whichShape(cont):
    poly = len(cv2.approxPolyDP(cont,0.01 * cv2.arcLength(cont, True),True))
    x,y,w,h = cv2.boundingRect(cont)
    if poly == 3:
        return 'Ucgen'
    if poly == 4:
        if w==h:
            return 'Kare'
        else:
            return 'Dikdortgen'
    return 'Daire'

def shapes(name):
    image = cv2.imread(name,cv2.IMREAD_GRAYSCALE)
    edge = cv2.Canny(image, 0,255)
    contours,_ = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cont in contours:
        x,y,w,h = cv2.boundingRect(cont)
        image = cv2.putText(image,whichShape(cont),(x,y+h+30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)
    cv2.imwrite('shapeNames.png',image)
