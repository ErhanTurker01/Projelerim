#Megaya ardunio IDE de bulunan pyfirmata dosyasını yüklüyoruz

import pyfirmata
import pygame
import time
board = pyfirmata.ArduinoMega('/dev/cu.HC-05')
pin3=board.get_pin('d:3:o')
pin4=board.get_pin('d:4:o')
pin5=board.get_pin('d:5:o')
pin6=board.get_pin('d:6:o')

pin9=board.get_pin('p:9:p')
pin10=board.get_pin('p:10:p')
pin12=board.get_pin('d:12:o')
pin31=board.get_pin('d:31:o')


#bir sebepten ötürü pin.wirte(değişken) yaptığım zaman araba 20-30 duraksıyor bende böyle saçma bir çzöğm buldum
def gazla(pin,va):
    va=round(va,2)
    if (va<0.005):
        pin.write(0)
    elif (va<0.015):
        pin.write(0.01)
    elif (va<0.025):
        pin.write(0.02)
    elif (va<0.035):
        pin.write(0.03)
    elif (va<0.045):
        pin.write(0.04)
    elif (va<0.055):
        pin.write(0.05)
    elif (va<0.065):
        pin.write(0.06)
    elif (va<0.075):
        pin.write(0.07)
    elif (va<0.085):
        pin.write(0.08)
    elif (va<0.095):
        pin.write(0.09)
    elif (va<0.105):
        pin.write(0.1)
    elif (va<0.115):
        pin.write(0.11)
    elif (va<0.125):
        pin.write(0.12)
    elif (va<0.135):
        pin.write(0.13)
    elif (va<0.145):
        pin.write(0.14)
    elif (va<0.155):
        pin.write(0.15)
    elif (va<0.165):
        pin.write(0.16)
    elif (va<0.175):
        pin.write(0.17)
    elif (va<0.185):
        pin.write(0.18)
    elif (va<0.195):
        pin.write(0.19)
    elif (va<0.205):
        pin.write(0.2)
    elif (va<0.215):
        pin.write(0.21)
    elif (va<0.225):
        pin.write(0.22)
    elif (va<0.235):
        pin.write(0.23)
    elif (va<0.245):
        pin.write(0.24)
    elif (va<0.255):
        pin.write(0.25)
    elif (va<0.265):
        pin.write(0.26)
    elif (va<0.275):
        pin.write(0.27)
    elif (va<0.285):
        pin.write(0.28)
    elif (va<0.295):
        pin.write(0.29)
    elif (va<0.305):
        pin.write(0.3)
    elif (va<0.315):
        pin.write(0.31)
    elif (va<0.325):
        pin.write(0.32)
    elif (va<0.335):
        pin.write(0.33)
    elif (va<0.345):
        pin.write(0.34)
    elif (va<0.355):
        pin.write(0.35)
    elif (va<0.365):
        pin.write(0.36)
    elif (va<0.375):
        pin.write(0.37)
    elif (va<0.385):
        pin.write(0.38)
    elif (va<0.395):
        pin.write(0.39)
    elif (va<0.405):
        pin.write(0.4)
    elif (va<0.415):
        pin.write(0.41)
    elif (va<0.425):
        pin.write(0.42)
    elif (va<0.435):
        pin.write(0.43)
    elif (va<0.445):
        pin.write(0.44)
    elif (va<0.455):
        pin.write(0.45)
    elif (va<0.465):
        pin.write(0.46)
    elif (va<0.475):
        pin.write(0.47)
    elif (va<0.485):
        pin.write(0.48)
    elif (va<0.495):
        pin.write(0.49)
    elif (va<0.505):
        pin.write(0.5)
    elif (va<0.515):
        pin.write(0.51)
    elif (va<0.525):
        pin.write(0.52)
    elif (va<0.535):
        pin.write(0.53)
    elif (va<0.545):
        pin.write(0.54)
    elif (va<0.555):
        pin.write(0.55)
    elif (va<0.565):
        pin.write(0.56)
    elif (va<0.575):
        pin.write(0.57)
    elif (va<0.585):
        pin.write(0.58)
    elif (va<0.595):
        pin.write(0.59)
    elif (va<0.605):
        pin.write(0.6)
    elif (va<0.615):
        pin.write(0.61)
    elif (va<0.625):
        pin.write(0.62)
    elif (va<0.635):
        pin.write(0.63)
    elif (va<0.645):
        pin.write(0.64)
    elif (va<0.655):
        pin.write(0.65)
    elif (va<0.665):
        pin.write(0.66)
    elif (va<0.675):
        pin.write(0.67)
    elif (va<0.685):
        pin.write(0.68)
    elif (va<0.695):
        pin.write(0.69)
    elif (va<0.705):
        pin.write(0.7)
    elif (va<0.715):
        pin.write(0.71)
    elif (va<0.725):
        pin.write(0.72)
    elif (va<0.735):
        pin.write(0.73)
    elif (va<0.745):
        pin.write(0.74)
    elif (va<0.755):
        pin.write(0.75)
    elif (va<0.765):
        pin.write(0.76)
    elif (va<0.775):
        pin.write(0.77)
    elif (va<0.785):
        pin.write(0.78)
    elif (va<0.795):
        pin.write(0.79)
    elif (va<0.805):
        pin.write(0.8)
    elif (va<0.815):
        pin.write(0.81)
    elif (va<0.825):
        pin.write(0.82)
    elif (va<0.835):
        pin.write(0.83)
    elif (va<0.845):
        pin.write(0.84)
    elif (va<0.855):
        pin.write(0.85)
    elif (va<0.865):
        pin.write(0.86)
    elif (va<0.875):
        pin.write(0.87)
    elif (va<0.885):
        pin.write(0.88)
    elif (va<0.895):
        pin.write(0.89)
    elif (va<0.905):
        pin.write(0.9)
    elif (va<0.915):
        pin.write(0.91)
    elif (va<0.925):
        pin.write(0.92)
    elif (va<0.935):
        pin.write(0.93)
    elif (va<0.945):
        pin.write(0.94)
    elif (va<0.955):
        pin.write(0.95)
    elif (va<0.965):
        pin.write(0.96)
    elif (va<0.975):
        pin.write(0.97)
    elif (va<0.985):
        pin.write(0.98)
    elif (va<0.995):
        pin.write(0.99)
    elif (va<1.005):
        pin.write(1)

pygame.init()
def main():
    sc=time.time()
    beyazled=False
    kirimizled=False
    cakar=False
    cakars=time.time()
    cakari=50
    joysticks = {}
    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 
            if event.type == pygame.JOYDEVICEADDED:
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connencted")
            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")
        for joystick in joysticks.values():
            buttons = joystick.get_numbuttons()
            for i in range(buttons):
                button = joystick.get_button(i)
            hats = joystick.get_numhats()
            for i in range(hats):
                hat = joystick.get_hat(i)

            axis0 = joystick.get_axis(0)
            axis1 = -joystick.get_axis(1)
            axis2 = joystick.get_axis(2)
            axis3 = joystick.get_axis(3)

            if(hat[1]):
                cakari+=float(hat[1])/2000
            if cakari<2:
                cakari=2
            if cakari>100:
                cakari=100
            if cakar:
                if time.time()-cakars>float(cakari)/100:
                    beyazled = not beyazled
                    kirimizled = not kirimizled
                    cakars=time.time()

            if time.time()-sc>0.4:
                if joystick.get_button(button+4):
                    beyazled = not beyazled
                    sc=time.time()
                if joystick.get_button(button+5):
                    kirimizled = not kirimizled
                    sc=time.time()
                if joystick.get_button(button+3):
                    cakar = not cakar
                    sc=time.time()
            if joystick.get_button(button):
                pin12.write(not kirimizled)
                pin31.write(not beyazled)
            elif joystick.get_button(button+2):
                pin12.write(kirimizled)
                pin31.write(not beyazled)
            else:
                pin12.write(kirimizled)
                pin31.write(beyazled)
            
            







            sagMotor = abs(axis1)*abs((axis3-1)/2)
            solMotor = abs(axis1)*abs((axis3-1)/2)
            if axis2>=0:
                sagMotor*=(-axis2+1)
            else:
                solMotor*=(axis2+1)
            if joystick.get_button(button+1):
                if axis1<0.1 and axis1>-0.1:
                    sagMotor=abs(axis2)*abs((axis3-1)/2)
                    solMotor=abs(axis2)*abs((axis3-1)/2)
                    if axis2>0:
                        pin3.write(0)
                        pin4.write(1)
                        pin5.write(1)
                        pin6.write(0) 
                    else:
                        pin3.write(1)
                        pin4.write(0)
                        pin5.write(0)
                        pin6.write(1) 
                elif axis1>=0:
                    pin3.write(1)
                    pin4.write(0)
                    pin5.write(1)
                    pin6.write(0)    
                else:
                    pin3.write(0)
                    pin4.write(1)
                    pin5.write(0)
                    pin6.write(1)  
                gazla(pin9,sagMotor)
                gazla(pin10,solMotor)
            else:
                gazla(pin9,0)
                gazla(pin10,0)
            print(sagMotor)
            



if __name__ == "__main__":
    main()
    pygame.quit()
    gazla(pin9,0)
    gazla(pin10,0)
    pin31.write(0)
    pin12.write(0)
    board.exit()