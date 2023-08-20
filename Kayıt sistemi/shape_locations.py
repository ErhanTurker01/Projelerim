import cv2 
import numpy as np
from shapes import whichShape
from location import locate

def isClose(x1,x2):
    return 30>abs(x1-x2)

def locationRespectTo(loc1,loc2):
    output = ''
    if not isClose(loc1[1],loc2[1]):
        if loc1[1]>loc2[1]:
            output = 'Kuzey '
        else:
            output = 'Güney '
    if not isClose(loc1[0],loc2[0]):
        if loc1[0]>loc2[0]:
            output += 'Batı'
        else:
            output += 'Doğu'
    return output


    



def shapeLocations(name):
    output = ''
    image = cv2.imread(name,cv2.IMREAD_GRAYSCALE)
    size = image.shape
    image = cv2.dilate(image , np.ones((3,3)),iterations=8)
    edge = cv2.Canny(image, 0,255)
    contours,_ = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    shapes,locs = [],[]
    for cont in contours:
        shapes.append(whichShape(cont))
        x,y,w,h = cv2.boundingRect(cont)
        locs.append((x,y))
    for i in range(4):
        output += 'Şekil: ' + shapes[i] + '\n' + 'Konum: ' + locate(locs[i][0],locs[i][1],size) + '\n' + 'Etrafındaki şekiller: '
        for j in range(4):
            if j == i:
                continue
            output += shapes[j] + '-' + locationRespectTo(locs[i],locs[j]) + ',' 
        output = output[:-1]
        output += '\n\n'
    return output
        
