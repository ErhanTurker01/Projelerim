import serial
import turtle
import math
from serial.tools import list_ports

port = serial.Serial('//dev/cu.usbserial-1110',9600)
cizgi=180
sc =turtle.Screen()
sc.bgcolor("black")
sc.setup(width=1000,height=1000)
sc.tracer(0)
sc.title("Sonar")
sonar=[]
for i in range(0,cizgi):
    sonar.append(0)
    sonar[i]=turtle.Turtle()
    sonar[i].color("red")
    sonar[i].penup()
    sonar[i].goto(0,0)
    sonar[i].pendown()
    sonar[i].hideturtle()
sonar.append(0)
sonar[cizgi]=turtle.Turtle()
sonar[cizgi].color("red")
sonar[cizgi].penup()
sonar[cizgi].goto(0,0)
sonar[cizgi].pendown()
sonar[cizgi].hideturtle()
a=turtle.Turtle()
a.color("red")
a.penup()
a.goto(-500,-300)
a.pendown()
a.goto(500,-300)
a.penup()
a.hideturtle()


d=-(math.pi)/cizgi
count=-1
k=1
while True:
    data = port.readline()
    mesafe = data.decode()
    mesafe = mesafe.rstrip()
    x=int(float(mesafe))
    if(x>50):x=50
    if d>math.pi-math.pi/cizgi:
        k=-1
    if d<0+math.pi/cizgi:
        k=1
    d+=k*(math.pi)/cizgi
    count+=k
    print(x)
    sonar[count].clear()
    sonar[count].pendown()
    sonar[count].goto(math.cos(d)*x*5,math.sin(d)*x*5)
    sonar[count].goto(0,0)
    sc.update()
