import turtle
import time
import random
import numpy
#array
col=20
row=20
arr = [[0 for i in range(col)] for j in range(row)]

#ekran
w=col*20
h=row*20
sc =turtle.Screen()
sc.bgcolor("black")
sc.setup(width=w,height=h+40)
sc.tracer(0)
sc.title("Snake Game")

#score
max=0
score =turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.goto(0,-h/2-30)
score.hideturtle()
score.write("point:0 max:0", align="center", font=("Courier", 24, "normal"))

#meyve
meyve = turtle.Turtle()
meyve.speed(0)
meyve.shape("square")
meyve.color("red")
meyve.shapesize(stretch_len=16/20,stretch_wid=16/20)
meyve.penup()
x = random.randrange(1,int(w)/20+1)*20-w/2-10
y = random.randrange(1,int(h)/20+1)*20-h/2-10
meyve.goto(x,y)
point=0

#snake head
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.shapesize(stretch_len=16/20,stretch_wid=16/20)
snake.penup()
if w/20%2==0:
    snake.setx(10)
if h/20%2==0:
    snake.sety(10)
if snake.xcor()==meyve.xcor() and snake.ycor()==meyve.ycor():
    snake.sety(snake.ycor()+20)
    snake.setx(snake.xcor()+20)
dx=0
dy=0

#snake eyes
eye1=turtle.Turtle()
eye1.speed(0)
eye1.shape("circle")
eye1.color("green")
eye1.penup()
eye1.shapesize(stretch_len=4/20,stretch_wid=4/20)

eye2=turtle.Turtle()
eye2.speed(0)
eye2.shape("circle")
eye2.color("green")
eye2.penup()
eye2.shapesize(stretch_len=4/20,stretch_wid=4/20)

eye1.goto(snake.xcor()+5,snake.ycor()+5)
eye2.goto(snake.xcor()-5,snake.ycor()+5)


#ekran çizgileri
pen =turtle.Turtle()
pen.color("gray")
pen.penup()
pen.goto(-300,300)
pen.hideturtle()

for i in range(0,int(w/20)+1):
    pen.penup()
    pen.goto(i*20-w/2,-h/2)
    pen.pendown()
    pen.goto(i*20-w/2,h/2)
pen.penup()
pen.goto(-w/2,h/2)
for i in range(0,int(h/20)+1):
    pen.penup()
    pen.goto(-w/2,i*20-h/2)
    pen.pendown()
    pen.goto(w/2,i*20-h/2)

#haraket
def up():
    global dy,dx,body
    if point==0 or body[1].ycor()-20!=snake.ycor():
        dy=20
        dx=0
def down():
    global dy,dx,body
    if point==0 or body[1].ycor()+20!=snake.ycor():
        dy=-20
        dx=0
def right():
    global dy,dx,body
    if point==0 or body[1].xcor()-20!=snake.xcor():
        dy=0
        dx=20
def left():
    global dy,dx,body
    if point==0 or body[1].xcor()+20!=snake.xcor():
        dy=0
        dx=-20


sc.listen()
sc.onkeypress(up,"w")
sc.onkeypress(down,"s")
sc.onkeypress(right,"d")
sc.onkeypress(left,"a")

t=time.time()

def reset():
    global point,dx,dy,body
    
    for i in range(1,point+1):
        body[i].hideturtle()
    body.clear()
    body=[0]
    dx=0
    dy=0
    point=0
    score.clear()
    score.write("point:{} max:{}".format(point,max), align="center", font=("Courier", 24, "normal"))
    snake.goto(0,0)
    if w/20%2==0:
        snake.setx(10)
    if h/20%2==0:
        snake.sety(10)
    while snake.xcor()==meyve.xcor() and snake.ycor()==meyve.ycor():
                x = random.randrange(1,int(w)/20+1)*20-w/2-10
                y = random.randrange(1,int(h)/20+1)*20-h/2-10
                meyve.goto(x,y)
    eye1.goto(snake.xcor()+5,snake.ycor()+5)
    eye2.goto(snake.xcor()-5,snake.ycor()+5)
    x = random.randrange(1,int(w)/20+1)*20-w/2-10
    y = random.randrange(1,int(h)/20+1)*20-h/2-10
    meyve.goto(x,y)

body =[0]


def addbody():
    body.append(point)
    body[point] = turtle.Turtle()
    body[point].speed(0)
    body[point].shape("square")
    body[point].color("white")
    body[point].shapesize(stretch_len=16/20,stretch_wid=16/20)
    body[point].penup()
    body[point].goto(snake.xcor(),snake.ycor())

def movebody():
    for i in reversed(range(2,point+1)):
        body[i].goto(body[i-1].xcor(),body[i-1].ycor())
    body[1].goto(snake.xcor(),snake.ycor())
    


def meyveyer():
    global point
    for i in range(1,point+1):
        if body[i].xcor()==meyve.xcor() and body[i].ycor()==meyve.ycor():
            return 0
    if snake.xcor()==meyve.xcor() and snake.ycor()==meyve.ycor():
            return 0
    return 1
t=time.time()
while True:
    sc.update()
    if True:
        if time.time()-t>0.1:
            t=time.time()
            if point >0:
                movebody()
            snake.goto(snake.xcor()+dx,snake.ycor()+dy)
            if dy:
                eye1.goto(snake.xcor()+(dx+dy)/4,snake.ycor()+(dx+dy)/4)
                eye2.goto(snake.xcor()-(dx+dy)/4,snake.ycor()+(dx+dy)/4)
            elif dx:
                eye1.goto(snake.xcor()+(dx+dy)/4,snake.ycor()+(dx+dy)/4)
                eye2.goto(snake.xcor()+(dx+dy)/4,snake.ycor()-(dx+dy)/4)
                            


            #duvar çarpışma
            if snake.xcor()>int(w/2)-10 or snake.xcor()<10-w/2 or snake.ycor()>int(h/2)-10 or snake.ycor()<10-h/2:
                reset()

            #kendi ile çarpışma
            if point>0:
                for i in range(1,point+1):
                    if snake.xcor()==body[i].xcor() and snake.ycor()==body[i].ycor():
                        reset()
                        break

            #point
            if snake.xcor()==meyve.xcor() and snake.ycor()==meyve.ycor():
                point+=1
                addbody()
                if point>max:
                    max=point
                score.clear()
                score.write("point:{} max:{}".format(point,max), align="center", font=("Courier", 24, "normal"))
                while meyveyer()==0:
                    x = random.randrange(1,int(w)/20+1)*20-w/2-10
                    y = random.randrange(1,int(h)/20+1)*20-h/2-10
                    meyve.goto(x,y)