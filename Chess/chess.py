import turtle
import os
from pygame import mixer
turtle.colormode(255)
pixel=70
w=8*pixel
h=8*pixel
pl=["pawn","rook","knight","bishop","queen","king"]
fullscreen=False
showlastmove=False

########################################Algoritma########################################

def center(initialx,initialy):
    for xc in range(0,8):
        for yc in range(0,8):
            if (initialx>=-w/2+xc*pixel and initialx<=-w/2+xc*pixel+pixel) and (initialy>=-h/2+yc*pixel and initialy<=-h/2+yc*pixel+pixel):
                return (-w/2+xc*pixel+pixel/2,-h/2+yc*pixel+pixel/2)

def select(x,y):
    for piece in piecelist:
        for selected in piece:
            if selected.xcor()==x and selected.ycor()==y:
                return selected

def typeofpiece(piece):
    global pl
    c=-1
    for type in piecelist:
        c+=1
        if piece in type:
            return pl[c]

def moves(piece):
    if not isincheck(colorofpiece(piece)):
        temp=0
        if typeofpiece(piece)=="rook":
            for i in range(0,8):
                for j in range(0,8):
                    if rookmove2(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                        if difcolor(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                            move[temp].color(255,100,100)
                        move[temp].goto(w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2)
                        move[temp].showturtle()
                        temp+=1
        if typeofpiece(piece)=="bishop":
            for i in range(0,8):
                for j in range(0,8):
                    if bishopmove2(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                        if difcolor(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                            move[temp].color(255,100,100)
                        move[temp].goto(w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2)
                        move[temp].showturtle()
                        temp+=1
        if typeofpiece(piece)=="queen":
            for i in range(0,8):
                for j in range(0,8):
                    if queenmove2(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                            if difcolor(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                                move[temp].color(255,100,100)
                            move[temp].goto(w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2)
                            move[temp].showturtle()
                            temp+=1
        if typeofpiece(piece)=="king":
            for i in range(0,8):
                for j in range(0,8):
                    if kingmove(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                        if difcolor(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                            move[temp].color(255,100,100)
                        move[temp].goto(w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2)
                        move[temp].showturtle()
                        temp+=1
        if typeofpiece(piece)=="knight":
            for i in range(0,8):
                for j in range(0,8):
                    if knightmove2(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                        if difcolor(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                            move[temp].color(255,100,100)
                        move[temp].goto(w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2)
                        move[temp].showturtle()
                        temp+=1
        if typeofpiece(piece)=="pawn":
            for i in range(0,8):
                for j in range(0,8):
                    if pawnmove2(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                        if difcolor(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                            move[temp].color(255,100,100)
                        move[temp].goto(w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2)
                        move[temp].showturtle()
                        temp+=1
    else:
        temp=0
        if typeofpiece(piece)=="rook":
            for i in range(0,8):
                for j in range(0,8):
                    if rookmove2(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2) or canprotect(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                        if difcolor(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                            move[temp].color(255,100,100)
                        move[temp].goto(w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2)
                        move[temp].showturtle()
                        temp+=1
        if typeofpiece(piece)=="bishop":
            for i in range(0,8):
                for j in range(0,8):
                    if bishopmove2(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2) or canprotect(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                        if difcolor(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                            move[temp].color(255,100,100)
                        move[temp].goto(w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2)
                        move[temp].showturtle()
                        temp+=1
        if typeofpiece(piece)=="queen":
            for i in range(0,8):
                for j in range(0,8):
                    if queenmove2(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2) or canprotect(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                            if difcolor(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                                move[temp].color(255,100,100)
                            move[temp].goto(w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2)
                            move[temp].showturtle()
                            temp+=1
        if typeofpiece(piece)=="king":
            for i in range(0,8):
                for j in range(0,8):
                    if kingmove(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                        if difcolor(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                            move[temp].color(255,100,100)
                        move[temp].goto(w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2)
                        move[temp].showturtle()
                        temp+=1
        if typeofpiece(piece)=="knight":
            for i in range(0,8):
                for j in range(0,8):
                    if knightmove2(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2) or canprotect(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                        if difcolor(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                            move[temp].color(255,100,100)
                        move[temp].goto(w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2)
                        move[temp].showturtle()
                        temp+=1
        if typeofpiece(piece)=="pawn":
            for i in range(0,8):
                for j in range(0,8):
                    if pawnmove2(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2) or canprotect(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                        if difcolor(piece,w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2):
                            move[temp].color(255,100,100)
                        move[temp].goto(w/2-pixel*i-pixel/2,h/2-pixel*j-pixel/2)
                        move[temp].showturtle()
                        temp+=1

def hidemoves():
    for i in move:
        i.hideturtle()
        i.color(150,150,255)

def lastmove(px,py,x,y):
    if showlastmove:
        new.showturtle()
        last.showturtle()
        new.goto(x,y)
        last.goto(px,py)
        
def piecexist(x,y):
    for piece in piecelist:
        for check in piece:
            if check.xcor()==x and check.ycor()==y:
                return True
    return False

def colorofpiece(piece):
    if piece.shape()=="wp.gif" or piece.shape()=="wr.gif" or piece.shape()=="wb.gif" or piece.shape()=="wa.gif" or piece.shape()=="wq.gif" or piece.shape()=="wk.gif":
        return "white"
    else:
        return "black"
def opcolorofpiece(piece):
    if piece.shape()=="wp.gif" or piece.shape()=="wr.gif" or piece.shape()=="wb.gif" or piece.shape()=="wa.gif" or piece.shape()=="wq.gif" or piece.shape()=="wk.gif":
        return "black"
    else:
        return "white"

def samecolor(piece,x,y):
    selected=select(x,y)
    if selected is None:
        return False
    if colorofpiece(selected)==colorofpiece(piece):
        return True
    else:
        return False

def difcolor(piece,x,y):
    selected=select(x,y)
    if selected is None:
        return False
    if colorofpiece(selected)!=colorofpiece(piece):
        return True
    return False

def deletepiece(x,y):
    piece=select(x,y)
    piece.goto(3899,3899)
    piece.hideturtle
    del piece

def attack(piece,x,y):
    b=1
    if colorofpiece(piece)=="black":
        b=-1
    if typeofpiece(piece)=="bishop" and bishopmovec(piece,x,y):
        return True
    if typeofpiece(piece)=="rook" and rookmovec(piece,x,y):
        return True
    if typeofpiece(piece)=="queen" and queenmovec(piece,x,y):
        return True
    if typeofpiece(piece)=="knight" and knightmovec(piece,x,y):
        return True
    if typeofpiece(piece)=="king" and kingmove(piece,x,y):
        return True
    if typeofpiece(piece)=="pawn" and (x==piece.xcor()+pixel or x==piece.xcor()-pixel) and y==piece.ycor()+pixel*b:
        return True
    
    return False
def attackingquares(color):
    squares=[]
    if color=="black":
        for piece in blackpieces:
            for i in range(0,8):
                for j in range(0,8):
                    if attack(piece,w/2-pixel/2-pixel*i,h/2-pixel/2-pixel*j):
                        squares.append((w/2-pixel/2-pixel*i,h/2-pixel/2-pixel*j))
    elif color =="white":
        for piece in whitepieces:
            for i in range(0,8):
                for j in range(0,8):
                    if attack(piece,w/2-pixel/2-pixel*i,h/2-pixel/2-pixel*j):
                        squares.append((w/2-pixel/2-pixel*i,h/2-pixel/2-pixel*j))
    return set(squares)
def isattackedby(color,x,y):
    squares=attackingquares(color)
    for i in squares:
        if x==i[0] and y==i[1]:
            del squares
            return True
    del squares
    return False
def iskingattackedby(color,x,y):
    if colorofpiece(king[0])==color:
        sking=king[0]
    else:
        sking=king[1]
    if attack(select(x,y),sking.xcor(),sking.ycor()):
        return True
    return False

def isincheck(color):
    if colorofpiece(king[0])==color:
        selected=king[0]
    else:
        selected=king[1]
    if isattackedby(opcolorofpiece(selected),selected.xcor(),selected.ycor()):
        return True
    return False
def checknextmove(piece,x,y):
    a,b=piece.xcor(),piece.ycor()
    con=False
    if piecexist(x,y):
        con=True
        selected=select(x,y)
        selected.goto(999,999)
    piece.goto(x,y)
    if isincheck(colorofpiece(piece)):
        piece.goto(a,b)
        if con:
            selected.goto(x,y)
        return False
    if con:
        selected.goto(x,y)
    piece.goto(a,b)
    return True
def canprotect(piece,x,y):
    def canprotectcon():
        selected=select(x,y)
        selected.goto(999,999)
        a,b=piece.xcor(),piece.ycor()
        piece.goto(x,y)
        if isincheck(colorofpiece(piece)):
            piece.goto(a,b)
            selected.goto(x,y)
            return False
        piece.goto(a,b)
        selected.goto(x,y)
        return True
    if typeofpiece(piece)=="queen" and queenmove2(piece,x,y):
        a,b=piece.xcor(),piece.ycor()
        piece.goto(x,y)
        if isincheck(colorofpiece(piece)):
            piece.goto(a,b)
            return False
        piece.goto(a,b)
        return True
    elif typeofpiece(piece)=="queen" and queenmovec(piece,x,y) and piecexist(x,y) and colorofpiece(select(x,y))==opcolorofpiece(piece) and iskingattackedby(colorofpiece(piece),x,y):
        return canprotectcon()

    if typeofpiece(piece)=="knight" and knightmove2(piece,x,y):
        a,b=piece.xcor(),piece.ycor()
        piece.goto(x,y)
        if isincheck(colorofpiece(piece)):
            piece.goto(a,b)
            return False
        piece.goto(a,b)
        return True
    elif typeofpiece(piece)=="knight" and knightmovec(piece,x,y) and piecexist(x,y) and colorofpiece(select(x,y))==opcolorofpiece(piece) and iskingattackedby(colorofpiece(piece),x,y):
        return canprotectcon()

    if typeofpiece(piece)=="rook" and rookmove2(piece,x,y):
        a,b=piece.xcor(),piece.ycor()
        piece.goto(x,y)
        if isincheck(colorofpiece(piece)):
            piece.goto(a,b)
            return False
        piece.goto(a,b)
        return True
    elif typeofpiece(piece)=="rook" and rookmovec(piece,x,y) and piecexist(x,y) and colorofpiece(select(x,y))==opcolorofpiece(piece) and iskingattackedby(colorofpiece(piece),x,y):
        return canprotectcon()

    if typeofpiece(piece)=="pawn" and pawnmove2(piece,x,y):
        a,b=piece.xcor(),piece.ycor()
        piece.goto(x,y)
        if isincheck(colorofpiece(piece)):
            piece.goto(a,b)
            return False
        piece.goto(a,b)
        return True
    elif typeofpiece(piece)=="pawn" and pawnmovec(piece,x,y) and piecexist(x,y) and colorofpiece(select(x,y))==opcolorofpiece(piece) and iskingattackedby(colorofpiece(piece),x,y):
        return canprotectcon()

    if typeofpiece(piece)=="bishop" and bishopmove2(piece,x,y):
        a,b=piece.xcor(),piece.ycor()
        piece.goto(x,y)
        if isincheck(colorofpiece(piece)):
            piece.goto(a,b)
            return False
        piece.goto(a,b)
        return True
    elif typeofpiece(piece)=="bishop" and bishopmovec(piece,x,y) and piecexist(x,y) and colorofpiece(select(x,y))==opcolorofpiece(piece) and iskingattackedby(colorofpiece(piece),x,y):
        return canprotectcon()

def rookmove(piece,x,y):
    if isincheck(colorofpiece(piece)):
        if canprotect(piece,x,y):
            return True
        return False
    if (piece.xcor()!=x and piece.ycor()!=y) or (piece.xcor()==x and piece.ycor()==y):
        return False
    if (piecexist(x,y)) and colorofpiece(select(x,y))==colorofpiece(piece):
        return False
    if x==piece.xcor() and piece.ycor()<y:
        for i in range(int(piece.ycor()+pixel),int(y),pixel):
            if piecexist(x,i):
                return False
    if x==piece.xcor() and piece.ycor()>y:
        for i in range(int(piece.ycor()-pixel),int(y),-pixel):
            if piecexist(x,i):
                return False
    if y==piece.ycor() and piece.xcor()<x:
        for i in range(int(piece.xcor()+pixel),int(x),pixel):
            if piecexist(i,y):
                return False
    
    if y==piece.ycor() and piece.xcor()>x:
        for i in range(int(piece.xcor()-pixel),int(x),-pixel):
            if piecexist(i,y):
                return False
    return checknextmove(piece,x,y)
def rookmove2(piece,x,y):
    if (piece.xcor()!=x and piece.ycor()!=y) or (piece.xcor()==x and piece.ycor()==y):
        return False
    if (piecexist(x,y)) and colorofpiece(select(x,y))==colorofpiece(piece):
        return False
    if x==piece.xcor() and piece.ycor()<y:
        for i in range(int(piece.ycor()+pixel),int(y),pixel):
            if piecexist(x,i):
                return False
    if x==piece.xcor() and piece.ycor()>y:
        for i in range(int(piece.ycor()-pixel),int(y),-pixel):
            if piecexist(x,i):
                return False
    if y==piece.ycor() and piece.xcor()<x:
        for i in range(int(piece.xcor()+pixel),int(x),pixel):
            if piecexist(i,y):
                return False
    
    if y==piece.ycor() and piece.xcor()>x:
        for i in range(int(piece.xcor()-pixel),int(x),-pixel):
            if piecexist(i,y):
                return False
    return checknextmove(piece,x,y)
def rookmovec(piece,x,y):
    if (piece.xcor()!=x and piece.ycor()!=y) or (piece.xcor()==x and piece.ycor()==y):
        return False
    if x==piece.xcor() and piece.ycor()<y:
        for i in range(int(piece.ycor()+pixel),int(y),pixel):
            if piecexist(x,i):
                return False
    if x==piece.xcor() and piece.ycor()>y:
        for i in range(int(piece.ycor()-pixel),int(y),-pixel):
            if piecexist(x,i):
                return False
    if y==piece.ycor() and piece.xcor()<x:
        for i in range(int(piece.xcor()+pixel),int(x),pixel):
            if piecexist(i,y):
                return False
    
    if y==piece.ycor() and piece.xcor()>x:
        for i in range(int(piece.xcor()-pixel),int(x),-pixel):
            if piecexist(i,y):
                return False
    return True

def bishopmove(piece,x,y):
    if isincheck(colorofpiece(piece)):
        if canprotect(piece,x,y):
            return True
        return False
    if x==piece.xcor() and y==piece.ycor():
        return False
    if piecexist(x,y) and colorofpiece(select(x,y))==colorofpiece(piece):
        return False
    if x-piece.xcor()!=y-piece.ycor() and x-piece.xcor()!=-y+piece.ycor():
        return False
    if x>piece.xcor() and y>piece.ycor():
        for i,j in set(zip(range(int(piece.xcor())+pixel,int(x),pixel),range(int(piece.ycor())+pixel,int(y),pixel))):
            if piecexist(i,j):
                return False
        return checknextmove(piece,x,y)
    if x<piece.xcor() and y<piece.ycor():
        for i,j in set(zip(range(int(piece.xcor())-pixel,int(x),-pixel),range(int(piece.ycor())-pixel,int(y),-pixel))):
            if piecexist(i,j):
                return False
        return checknextmove(piece,x,y)
    if x<piece.xcor() and y>piece.ycor():
        for i,j in set(zip(range(int(piece.xcor())-pixel,int(x),-pixel),range(int(piece.ycor())+pixel,int(y),pixel))):
            if piecexist(i,j):
                return False
        return checknextmove(piece,x,y)
    if x>piece.xcor() and y<piece.ycor():
        for i,j in set(zip(range(int(piece.xcor())+pixel,int(x),pixel),range(int(piece.ycor())-pixel,int(y),-pixel))):
            if piecexist(i,j):
                return False
        return checknextmove(piece,x,y)
    return False
def bishopmove2(piece,x,y):
    if x==piece.xcor() and y==piece.ycor():
        return False
    if piecexist(x,y) and colorofpiece(select(x,y))==colorofpiece(piece):
        return False
    if x-piece.xcor()!=y-piece.ycor() and x-piece.xcor()!=-y+piece.ycor():
        return False
    if x>piece.xcor() and y>piece.ycor():
        for i,j in set(zip(range(int(piece.xcor())+pixel,int(x),pixel),range(int(piece.ycor())+pixel,int(y),pixel))):
            if piecexist(i,j):
                return False
        return checknextmove(piece,x,y)
    if x<piece.xcor() and y<piece.ycor():
        for i,j in set(zip(range(int(piece.xcor())-pixel,int(x),-pixel),range(int(piece.ycor())-pixel,int(y),-pixel))):
            if piecexist(i,j):
                return False
        return checknextmove(piece,x,y)
    if x<piece.xcor() and y>piece.ycor():
        for i,j in set(zip(range(int(piece.xcor())-pixel,int(x),-pixel),range(int(piece.ycor())+pixel,int(y),pixel))):
            if piecexist(i,j):
                return False
        return checknextmove(piece,x,y)
    if x>piece.xcor() and y<piece.ycor():
        for i,j in set(zip(range(int(piece.xcor())+pixel,int(x),pixel),range(int(piece.ycor())-pixel,int(y),-pixel))):
            if piecexist(i,j):
                return False
        return checknextmove(piece,x,y)
    return False
def bishopmovec(piece,x,y):
    if x==piece.xcor() and y==piece.ycor():
        return False
    if x-piece.xcor()!=y-piece.ycor() and x-piece.xcor()!=-y+piece.ycor():
        return False
    if x>piece.xcor() and y>piece.ycor():
        for i,j in set(zip(range(int(piece.xcor())+pixel,int(x),pixel),range(int(piece.ycor())+pixel,int(y),pixel))):
            if piecexist(i,j):
                return False
        return True
    if x<piece.xcor() and y<piece.ycor():
        for i,j in set(zip(range(int(piece.xcor())-pixel,int(x),-pixel),range(int(piece.ycor())-pixel,int(y),-pixel))):
            if piecexist(i,j):
                return False
        return True
    if x<piece.xcor() and y>piece.ycor():
        for i,j in set(zip(range(int(piece.xcor())-pixel,int(x),-pixel),range(int(piece.ycor())+pixel,int(y),pixel))):
            if piecexist(i,j):
                return False
        return True
    if x>piece.xcor() and y<piece.ycor():
        for i,j in set(zip(range(int(piece.xcor())+pixel,int(x),pixel),range(int(piece.ycor())-pixel,int(y),-pixel))):
            if piecexist(i,j):
                return False
        return True
    return False

def queenmove(piece,x,y):
    if isincheck(colorofpiece(piece)):
        if canprotect(piece,x,y):
            return True
    if bishopmove(piece,x,y) or rookmove(piece,x,y):
        return True
    return False
def queenmove2(piece,x,y):
    if bishopmove2(piece,x,y) or rookmove2(piece,x,y):
        return True
    return False
def queenmovec(piece,x,y):
    if bishopmovec(piece,x,y) or rookmovec(piece,x,y):
        return True
    return False

def kingmove(piece,x,y):
    a,b=piece.xcor(),piece.ycor()
    piece.goto(-999,-999)
    for i in range(-1,2):
        for j in range(-1,2):
            if i==0 and j==0:
                continue
            if a+i*pixel==x and b+j*pixel==y and not piecexist(x,y) and not isattackedby(opcolorofpiece(piece),x,y):
                piece.goto(a,b)
                return True
            elif piecexist(x,y) and difcolor(piece,x,y) and a+i*pixel==x and b+j*pixel==y and not isattackedby(opcolorofpiece(piece),x,y):
                piece.goto(a,b)
                return True
    piece.goto(a,b)
    return False

def knightmove(piece,x,y):
    if isincheck(colorofpiece(piece)):
        if canprotect(piece,x,y):
            return True
        return False
    for i in range(-1,2):
        for j in range(-1,2):
            if j==0 or i==0:
                continue
            if piece.xcor()+pixel*i*2==x and piece.ycor()+pixel*j==y and not piecexist(x,y):
                return checknextmove(piece,x,y)
            elif piecexist(x,y) and difcolor(piece,x,y) and piece.xcor()+pixel*i*2==x and piece.ycor()+pixel*j==y:
                return checknextmove(piece,x,y)
            if piece.xcor()+pixel*i==x and piece.ycor()+pixel*j*2==y and not piecexist(x,y):
                return checknextmove(piece,x,y)
            elif piecexist(x,y) and difcolor(piece,x,y) and piece.xcor()+pixel*i==x and piece.ycor()+pixel*j*2==y:
                return checknextmove(piece,x,y)
def knightmove2(piece,x,y):
    for i in range(-1,2):
        for j in range(-1,2):
            if j==0 or i==0:
                continue
            if piece.xcor()+pixel*i*2==x and piece.ycor()+pixel*j==y and not piecexist(x,y):
                return checknextmove(piece,x,y)
            elif piecexist(x,y) and difcolor(piece,x,y) and piece.xcor()+pixel*i*2==x and piece.ycor()+pixel*j==y:
                return checknextmove(piece,x,y)
            if piece.xcor()+pixel*i==x and piece.ycor()+pixel*j*2==y and not piecexist(x,y):
                return checknextmove(piece,x,y)
            elif piecexist(x,y) and difcolor(piece,x,y) and piece.xcor()+pixel*i==x and piece.ycor()+pixel*j*2==y:
                return checknextmove(piece,x,y)
def knightmovec(piece,x,y):
    for i in range(-1,2):
        for j in range(-1,2):
            if j==0 or i==0:
                continue
            if piece.xcor()+pixel*i*2==x and piece.ycor()+pixel*j==y:
                return True
            if piece.xcor()+pixel*i==x and piece.ycor()+pixel*j*2==y:
                return True

def pawnmove(piece,x,y):
    if isincheck(colorofpiece(piece)):
        if canprotect(piece,x,y):
            return True
        return False
    b=1
    if colorofpiece(piece)=="black":
        b=-1
    if piece.xcor()==x and piece.ycor()+pixel*b==y and not piecexist(x,y):
        return checknextmove(piece,x,y)
    if piece.xcor()+pixel==x and piece.ycor()+pixel*b==y and piecexist(x,y) and difcolor(piece,x,y):
        return checknextmove(piece,x,y)
    if piece.xcor()-pixel==x and piece.ycor()+pixel*b==y and piecexist(x,y) and difcolor(piece,x,y):
        return checknextmove(piece,x,y)
    if piece.xcor()==x and piece.ycor()+2*pixel*b==y and not piecexist(x,y) and not piecexist(x,y-pixel*b) and piece.ycor()==-175*b:
        return checknextmove(piece,x,y)
def pawnmove2(piece,x,y):
    b=1
    if colorofpiece(piece)=="black":
        b=-1
    if piece.xcor()==x and piece.ycor()+pixel*b==y and not piecexist(x,y):
        return checknextmove(piece,x,y)
    if piece.xcor()+pixel==x and piece.ycor()+pixel*b==y and piecexist(x,y) and difcolor(piece,x,y):
        return checknextmove(piece,x,y)
    if piece.xcor()-pixel==x and piece.ycor()+pixel*b==y and piecexist(x,y) and difcolor(piece,x,y):
        return checknextmove(piece,x,y)
    if piece.xcor()==x and piece.ycor()+2*pixel*b==y and not piecexist(x,y) and not piecexist(x,y-pixel*b) and piece.ycor()==-175*b:
        return checknextmove(piece,x,y)
    return False
def pawnmovec(piece,x,y):
    b=1
    if colorofpiece(piece)=="black":
        b=-1
    if piece.xcor()==x and piece.ycor()+pixel*b==y and not piecexist(x,y):
        return True
    if piece.xcor()+pixel==x and piece.ycor()+pixel*b==y and piecexist(x,y) and difcolor(piece,x,y):
        return True
    if piece.xcor()-pixel==x and piece.ycor()+pixel*b==y and piecexist(x,y) and difcolor(piece,x,y):
        return True
    if piece.xcor()==x and piece.ycor()+2*pixel*b==y and not piecexist(x,y) and not piecexist(x,y-pixel*b) and piece.ycor()==-175*b:
        return True
    return False

def follow(piece):
    if fullscreen:
        piece.goto(cursorx-645,-cursory+400)
    else:
        piece.goto(cursorx-645,-cursory+430)


selectedx=0
selectedy=0
didselect=0
turn=1
follower=[]
def click(x,y):
    global didselect,selectedx,selectedy,turn,follower
    x,y=center(x,y)
    if didselect==False:
        x,y=center(x,y)
        selected=select(x,y)
        if selected is None:
            selectedy,selectedx=0,0
            exit()
        selectedx,selectedy=x,y
        if turn==1 and colorofpiece(selected)=="white":
            didselect=True
            moves(selected)
            follower.clear()
            follower.append(selected)
        if turn==-1 and colorofpiece(selected)=="black":
            didselect=True
            moves(selected)
            follower.clear()
            follower.append(selected)
        exit()

        
    elif didselect==True:
        con,con2=False,False
        hidemoves()
        follower[0].goto(selectedx,selectedy)
        selected=select(selectedx,selectedy)
        if selected is None:
            didselect=False
            exit()
        x,y=center(x,y)
        selected_type=typeofpiece(selected)
        if selected_type=="rook" and rookmove(selected,x,y):
            if(piecexist(x,y)):
                con=True
                deletepiece(x,y)
            turn*=-1
            selected.goto(x,y)
            con2=True
        if selected_type=="pawn" and pawnmove(selected,x,y):
            if(piecexist(x,y)):
                con=True
                deletepiece(x,y)
            turn*=-1
            selected.goto(x,y)
            con2=True
        if selected_type=="bishop" and bishopmove(selected,x,y):
            if(piecexist(x,y)):
                con=True
                deletepiece(x,y)
            turn*=-1
            selected.goto(x,y)
            con2=True
        if selected_type=="king" and kingmove(selected,x,y):
            if(piecexist(x,y)):
                con=True
                deletepiece(x,y)
            turn*=-1
            selected.goto(x,y)
            con2=True
        if selected_type=="queen" and queenmove(selected,x,y):
            if(piecexist(x,y)):
                con=True
                deletepiece(x,y)
            turn*=-1
            selected.goto(x,y)
            con2=True
        if selected_type=="knight" and knightmove(selected,x,y):
            if(piecexist(x,y)):
                con=True
                deletepiece(x,y)
            turn*=-1
            selected.goto(x,y)
            con2=True
        if con and con2:
            mixer.music.load('capture.mp3')
            mixer.music.play()
            lastmove(selectedx,selectedy,x,y)
        elif con2:
            mixer.music.load('move.mp3')
            mixer.music.play()
            lastmove(selectedx,selectedy,x,y)
        didselect=False
        
#########################################################################################





########################################ekran########################################
sc =turtle.Screen()
sc.bgcolor("bisque")
sc.setup(width=w,height=h)
sc.tracer(0)
sc.title("Chess")
sc.onclick(click)

mixer.init()
sc.register_shape("wp.gif")
sc.register_shape("bp.gif")
sc.register_shape("br.gif")
sc.register_shape("wr.gif")
sc.register_shape("bb.gif")
sc.register_shape("wb.gif")
sc.register_shape("ba.gif")
sc.register_shape("wa.gif")
sc.register_shape("bq.gif")
sc.register_shape("wq.gif")
sc.register_shape("bk.gif")
sc.register_shape("wk.gif")
sc.register_shape("green.gif")
sc.register_shape("blue.gif")
sc.register_shape("red.gif")
canvas = turtle.getcanvas()
cursorx, cursory = canvas.winfo_pointerxy()
################################################################################

########################################Kareler########################################
def square(x,y,xyer):
    p =turtle.Turtle()
    p.hideturtle()
    p.penup()
    p.goto(x,y)
    p.pendown()
    p.fillcolor(xyer)
    p.begin_fill()
    p.setx(p.xcor()+pixel)
    p.sety(p.ycor()-pixel)
    p.setx(p.xcor()-pixel)
    p.sety(p.ycor()+pixel)
    p.end_fill()
    del p

for j in range(0,4):
    for i in range(0,4):
        square(i*pixel*2-h/2+pixel,h/2-j*pixel*2-pixel,"navajo white")
for j in range(0,4):
    for i in range(0,4):
        square(i*pixel*2-h/2,h/2-j*pixel*2,"navajo white")
for j in range(0,4):
    for i in range(0,4):
        square(i*pixel*2-w/2,w/2-j*pixel*2-pixel,"burlywood")
for j in range(0,4):
    for i in range(0,4):
        square(i*pixel*2-h/2+pixel,h/2-j*pixel*2,"burlywood")
################################################################################




########################################Setup########################################
turtle.colormode(255)
str =("/rb/ab/bb/qb/kb/bb/ab/rb/"),("/pb/pb/pb/pb/pb/pb/pb/pb/"),("/ / / / / / / / /"),("/ / / / / / / / /"),("/ / / / / / / / /"),("/ / / / / / / / /"),("/pw/pw/pw/pw/pw/pw/pw/pw/"),("/rw/aw/bw/qw/kw/bw/aw/rw/"),("w")
pawn_num,bishop_num,knight_num,rook_num,king_num,queen_num=0,0,0,0,0,0
pawn_color,pawn_cor,rook_color,rook_cor,knight_cor,knight_color=[],[],[],[],[],[]
bishop_cor,bishop_color,queen_cor,queen_color,king_cor,king_color=[],[],[],[],[],[]
skip=0
for i in range(0,8):
    xyer=0
    for j in range(1,len(str[i])):

        if skip:
            skip-=1
            continue

        if str[i][j]==" ":
            xyer+=1
            skip=1
            continue

        if str[i][j]=="p":
            pawn_color.append(str[i][j+1])
            pawn_num+=1
            pawn_cor.append((-xyer*pixel+w/2-pixel/2,-i*pixel+h/2-pixel/2))
            xyer+=1
            skip=2
            continue

        if str[i][j]=="r":
            rook_color.append(str[i][j+1])
            rook_num+=1
            rook_cor.append((-xyer*pixel+w/2-pixel/2,-i*pixel+h/2-pixel/2))
            xyer+=1
            skip=2
            continue

        if str[i][j]=="a":
            knight_color.append(str[i][j+1])
            knight_num+=1
            knight_cor.append((-xyer*pixel+w/2-pixel/2,-i*pixel+h/2-pixel/2))
            xyer+=1
            skip=2
            continue

        if str[i][j]=="b":
            bishop_color.append(str[i][j+1])
            bishop_num+=1
            bishop_cor.append((-xyer*pixel+w/2-pixel/2,-i*pixel+h/2-pixel/2))
            xyer+=1
            skip=2
            continue

        if str[i][j]=="q":
            queen_color.append(str[i][j+1])
            queen_num+=1
            queen_cor.append((-xyer*pixel+w/2-pixel/2,-i*pixel+h/2-pixel/2))
            xyer+=1
            skip=2
            continue

        if str[i][j]=="k":
            king_color.append(str[i][j+1])
            king_num+=1
            king_cor.append((-xyer*pixel+w/2-pixel/2,-i*pixel+h/2-pixel/2))
            xyer+=1
            skip=2
            continue
################################################################################

######lastmove#######
last=turtle.Turtle()
last.penup()
last.shape("square")
last.shapesize(stretch_wid=3.4,stretch_len=3.4)
last.color(70,150,70)
last.hideturtle()
new=turtle.Turtle()
new.penup()
new.shape("green.gif")
new.hideturtle()
#####################


########################################Haraketler########################################
move=[]
for i in range(0,64):
    move.append(i)
    move[i]=turtle.Turtle()
    move[i].hideturtle()
    move[i].shape("square")
    move[i].penup()
    move[i].color(150,150,255)

################################################################################

##############################Parçalar##########################
blackpieces,whitepieces=[],[]
pawn=[]
for i in range(0,pawn_num):
    pawn.append(i)
    pawn[i] = turtle.Turtle()
    pawn[i].speed(0)
    if pawn_color[i]=="w":
        pawn[i].shape("wp.gif")
        whitepieces.append(pawn[i])
    else :
       pawn[i].shape("bp.gif")
       blackpieces.append(pawn[i])
    pawn[i].penup()
    a,b=pawn_cor[i]
    pawn[i].goto(-a,b)
rook=[]
for i in range(0,rook_num):
    rook.append(i)
    rook[i] = turtle.Turtle()
    rook[i].speed(0)
    if rook_color[i]=="w":
        rook[i].shape("wr.gif")
        whitepieces.append(rook[i])
    else :
        rook[i].shape("br.gif")
        blackpieces.append(rook[i])
    rook[i].penup()
    a,b=rook_cor[i]
    rook[i].goto(-a,b)
bishop=[]
for i in range(0,bishop_num):
    bishop.append(i)
    bishop[i] = turtle.Turtle()
    bishop[i].speed(0)
    if bishop_color[i]=="w":
        bishop[i].shape("wb.gif")
        whitepieces.append(bishop[i])
    else :
        bishop[i].shape("bb.gif")
        blackpieces.append(bishop[i])
    bishop[i].penup()
    a,b=bishop_cor[i]
    bishop[i].goto(-a,b)
knight=[]
for i in range(0,knight_num):
    knight.append(i)
    knight[i] = turtle.Turtle()
    knight[i].speed(0)
    if knight_color[i]=="w":
        knight[i].shape("wa.gif")
        whitepieces.append(knight[i])
    else :
        knight[i].shape("ba.gif")
        blackpieces.append(knight[i])
    knight[i].penup()
    a,b=knight_cor[i]
    knight[i].goto(-a,b)
king=[]
for i in range(0,king_num):
    king.append(i)
    king[i] = turtle.Turtle()
    king[i].speed(0)
    if king_color[i]=="w":
        king[i].shape("wk.gif")
        whitepieces.append(king[i])
    else :
        king[i].shape("bk.gif")
        blackpieces.append(king[i])
    king[i].penup()
    a,b=king_cor[i]
    king[i].goto(-a,b)
queen=[]
for i in range(0,queen_num):
    queen.append(i)
    queen[i] = turtle.Turtle()
    queen[i].speed(0)
    if queen_color[i]=="w":
        queen[i].shape("wq.gif")
        whitepieces.append(queen[i])
    else :
        queen[i].shape("bq.gif")
        blackpieces.append(queen[i])
    queen[i].penup()
    a,b=queen_cor[i]
    queen[i].goto(-a,b)
    piecelist=[pawn,rook,knight,bishop,queen,king]
################################################################

while True:
    cursorx,cursory = canvas.winfo_pointerxy()
    if didselect==True:
        follow(follower[0])
    sc.update()