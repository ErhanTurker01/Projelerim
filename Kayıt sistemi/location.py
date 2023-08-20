import cv2
import numpy as np

def locate(x,y,size):
    if x > size[0]/2:
        if y > size[1]/2:
            return('Güney Doğu')
        else:
            return('Kuzey Doğu')
    else:
        if y > size[1]/2:
            return('Güney Batı')
        else:
            return('Kuzey Batı')

def location(name):
    image = cv2.imread(name,cv2.IMREAD_GRAYSCALE)
    size = image.shape
    image = cv2.dilate(image,np.ones((5,5)),iterations=5)
    edge = cv2.Canny(image, 0,255)
    contours,_ = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = cv2.boundingRect(contours[0])
    return locate(x,y,size)
