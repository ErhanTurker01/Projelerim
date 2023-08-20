import turtle
#ekran
sc=turtle.Screen()
sc.bgcolor("black")
sc.title("Pong")
sc.setup(width=800,height=600)
sc.tracer(0)

#oyuncular
oyuncu_1 =turtle.Turtle()
oyuncu_1.speed(0)
oyuncu_1.shape("square")
oyuncu_1.color("white")
oyuncu_1.shapesize(stretch_wid=5,stretch_len=1)
oyuncu_1.penup()
oyuncu_1.goto(-350,0)

oyuncu_2 =turtle.Turtle()
oyuncu_2.speed(0)
oyuncu_2.shape("square")
oyuncu_2.color("white")
oyuncu_2.shapesize(stretch_wid=5,stretch_len=1)
oyuncu_2.penup()
oyuncu_2.goto(350,0)

#top
top=turtle.Turtle()
top.speed(0)
top.shape("square")
top.color("white")
top.penup()
top_x=2
top_y=2

#score
score1=0
score2=0
score =turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.goto(-10,250)
score.hideturtle()
score.write("0          0", align="center", font=("Courier", 24, "normal"))

def oyuncu_1_up():
    y=oyuncu_1.ycor()
    y+=20
    oyuncu_1.sety(y)

def oyuncu_1_down():
    y=oyuncu_1.ycor()
    y-=20
    oyuncu_1.sety(y)

def oyuncu_2_up():
    y=oyuncu_2.ycor()
    y+=20
    oyuncu_2.sety(y)

def oyuncu_2_down():
    y=oyuncu_2.ycor()
    y-=20
    oyuncu_2.sety(y)

def topharaket():
    y=top.ycor()
    top.sety(y+top_y)
    x=top.xcor()
    top.setx(x+top_x)

sc.listen()
sc.onkeypress(oyuncu_1_up,"w")
sc.onkeypress(oyuncu_1_down,"s")
sc.onkeypress(oyuncu_2_up,"o")
sc.onkeypress(oyuncu_2_down,"l")

while True:
    sc.update()
    topharaket()
    if oyuncu_1.ycor()>250:
        oyuncu_1.sety(250)
    if oyuncu_1.ycor()<-250:
        oyuncu_1.sety(-250)
    if oyuncu_2.ycor()>250:
        oyuncu_2.sety(250)
    if oyuncu_2.ycor()<-250:
        oyuncu_2.sety(-250)
    #üst ve alt
    if top.ycor()>290:
        top_y *=-1
        top.sety(290)
    if top.ycor()<-280:
        top_y *=-1
        top.sety(-280)
    #sağ ve sol
    if top.xcor()>370:
        top_x *=-1
        top.goto(0,0)
        score1+=1
        score.clear()
        score.write("{}          {}".format(score1,score2), align="center", font=("Courier", 24, "normal"))
        top_x=-2
    
    if top.xcor()<-370:
        top_x *=-1
        top.goto(0,0)
        score2+=1
        score.clear()
        score.write("{}          {}".format(score1,score2), align="center", font=("Courier", 24, "normal"))
        top_x=2
    
    #oyuncu ve top
    if top.xcor()>330 and top.xcor()<350 and top.ycor()<oyuncu_2.ycor()+50 and top.ycor()>oyuncu_2.ycor()-50 and top_x>0:
        top_x *=-1.1
    if top.xcor()<-330 and top.xcor()>-350 and top.ycor()<oyuncu_1.ycor()+50 and top.ycor()>oyuncu_1.ycor()-50 and top_x<0:
        top_x *=-1.1