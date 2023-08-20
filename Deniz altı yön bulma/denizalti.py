import numpy as np
from itertools import permutations
from itertools import combinations
from time import sleep
################################################################################################################################################
poolMap=np.zeros((20,20),dtype=int)
coordinates=np.zeros((5,2),dtype=int)
################################################################################################################################################


poolMap[5][5]=1 #BASLANGIC
poolMap[12][7]=2 #1.HEDEF
poolMap[8][13]=2 #2.HEDEF
poolMap[10][15]=2 #3.HEDEF
poolMap[15][11]=2 #4.HEDEF


#HAVUZ KONUMLARINNIN KOORDİNAT LISTESI
coordinates[0]=[5,5]#BASLANGIÇ
coordinates[1]=[12,7]#1.HEDEF
coordinates[2]=[8,13]#2.HEDEF
coordinates[3]=[10,15]#3.HEDEF
coordinates[4]=[15,11]#4.HEDEF

point = 15 #her hedefin puanı
score = 0 #başlangıç puanı
time = 0.5 #print aralığı


def distance(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def scoreOfPath(path):
    global coordinates,point
    if len(path) == 0:
        return 0
    initialDistance = distance(coordinates[0],coordinates[path[0]])
    if len(path) == 1:
        return point-initialDistance
    Distance = initialDistance
    for i in range(0,len(path)-1):
        Distance += distance(coordinates[path[i]],coordinates[path[i+1]])
    return point*len(path)-Distance

def allPaths(List):
    l,L= [],[]
    for i in range(len(List)+1):
        l += list(combinations(List,i))
    for i in range(len(l)):
        L += list(permutations(l[i]))
    return L

def bestPathByTrying():
    global coordinates
    paths = allPaths(list(range(1,len(coordinates))))
    max = 0
    bestPath = []
    for path in paths:
        score = scoreOfPath(path)
        if score > max:
            max = score
            bestPath = path
    return bestPath

def makeLine(cor1,cor2):
    global poolMap
    c1,c2 = [0,0],[0,0]
    c1[0],c2[0]=cor1[0],cor2[0]
    c1[1],c2[1]=cor1[1],cor2[1]
    while True:
        if(cor1[0] != cor2[0]):
            cor1[0] -= (cor1[0]-cor2[0])/abs(cor1[0]-cor2[0])
            poolMap[cor1[0]][cor1[1]]=7
            continue
        if(cor1[1] != cor2[1]):
            cor1[1] -= (cor1[1]-cor2[1])/abs(cor1[1]-cor2[1])
            poolMap[cor1[0]][cor1[1]]=7
            continue
        if cor1[0] == cor2[0] and cor1[1] == cor2[1]:
            poolMap[cor1[0]][cor1[1]]=2
            break
    cor1[0],cor2[0]=c1[0],c2[0]
    cor1[1],cor2[1]=c1[1],c2[1]

def move(cor1,cor2):
    global poolMap
    if(cor1[0] != cor2[0]):
        poolMap[cor1[0]][cor1[1]]=0
        cor1[0] -= (cor1[0]-cor2[0])/abs(cor1[0]-cor2[0])
        poolMap[cor1[0]][cor1[1]]=1
    elif(cor1[1] != cor2[1]):
        poolMap[cor1[0]][cor1[1]]=0
        cor1[1] -= (cor1[1]-cor2[1])/abs(cor1[1]-cor2[1])
        poolMap[cor1[0]][cor1[1]]=1

bestPath = bestPathByTrying()
for route in bestPath:
    while distance(coordinates[0],coordinates[route])>0:
        makeLine(coordinates[0],coordinates[route])
        print(poolMap)
        print(score)
        move(coordinates[0],coordinates[route])
        score-=1
        if(coordinates[0][0] == coordinates[route][0] and coordinates[0][1] == coordinates[route][1]):
            score+=point
        sleep(time)
    print(poolMap)
    print(score)