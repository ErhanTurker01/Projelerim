from gui import screen
import random as rn

try:
    idFile = open('ids.txt','r')
except:
    idFile = open('ids.txt','a+')
    idFile.write(str(rn.randint(22000,44000))+'\n')
    idFile.close()

screen.changePage(0)
screen.win.mainloop()