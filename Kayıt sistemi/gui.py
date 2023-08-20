from window import *
from functions import reciveInfo
from functions import registerNewUser
from location import location
from shape_locations import shapeLocations
from shapes import shapes
from PIL import ImageTk,Image


loggedUser = ''
x,y=0,100
screen = window(800,600,'#fff59e')

invalidPass = widget(wType='label',text='Invalid pass!',fg='red',bg='#fee59e',x=325+x,y=270+y,w=100,h=20)
invalidID = widget(wType='label',text='Invalid ID!',fg='red',bg='#fee59e',x=325+x,y=270+y,w=100,h=20)
invalidNameOrPass = widget(wType='label',text='Invalid name or password!',fg='red',bg='#fee59e',x=285+x,y=270+y,w=180,h=20)
newID = widget(wType='label',text='Your ID is: ',fg='red',bg='#fee59e',x=285+x,y=270+y,w=180,h=20)
def changePage(n):
    invalidPass.hide()
    invalidID.hide()
    invalidNameOrPass.hide()
    newID.hide()
    screen.changePage(n)
    infoWidget.hide()
    passEntryReg.widget.delete(0,tk.END)
    nameEntryReg.widget.delete(0,tk.END)
    passEntry.widget.delete(0,tk.END)
    idEntry.widget.delete(0,tk.END)
def log():
    global loggedUser
    invalidPass.widget.place_forget()
    loggedUser = reciveInfo(passEntry.widget.get(),idEntry.widget.get())
    if loggedUser == 0:
        invalidPass.show()
    elif loggedUser == 1:
        invalidID.show()
    else:
        screen.addWidgetToPage(2,widget(wType='label',text='Welcome ' + loggedUser.capitalize() + '! Please choose a operation and provide file name.',w=1000,h=20,bg='#fff59e',fg='#555500',x=-100,y=50))
        changePage(2)
def reg():
    global newID
    regID = registerNewUser(passEntryReg.widget.get(),nameEntryReg.widget.get())
    if regID == 0:
        newID.hide()
        invalidNameOrPass.show()
    else:
        newID = widget(wType='label',text='Your ID is: '+regID,fg='red',bg='#fee59e',x=285+x,y=270+y,w=180,h=20)
        newID.show()
        invalidNameOrPass.hide()
        passEntryReg.widget.delete(0,tk.END)
        nameEntryReg.widget.delete(0,tk.END)

screen.addPage()
screen.addWidgetToPage(0,widget(wType='label',text='',w=156+6+23,x=282+x,y=147+y+5,h=26,bg='#000000'))
screen.addWidgetToPage(0,widget(wType='label',text='Welcome to login page!',w=155+24,x=285+x,y=150+y+5,h=20,bg='#fee59e',fg='#555500'))

idEntry = widget(wType='entry',bg='#fee59e',w=156,h=20,x=322+x,y=185+y,fg='#555500')
screen.addWidgetToPage(0,idEntry)
screen.addWidgetToPage(0,widget(wType='label',text='',w=50,x=270+x,y=185+y,h=21,bg='#000000'))
screen.addWidgetToPage(0,widget(wType='label',text='ID',w=44,h=15,x=273+x,y=187.5+y,fg='#555500',bg='#fee59e'))

passEntry = widget(wType='entry',bg='#fee59e',w=156,h=20,x=322+x,y=185+26+y,fg='#555500')
screen.addWidgetToPage(0,passEntry)
screen.addWidgetToPage(0,widget(wType='label',text='',w=50,x=270+x,y=185+26+y,h=21,bg='#000000'))
screen.addWidgetToPage(0,widget(wType='label',text='Pass',w=44,h=15,x=273+x,y=187.5+y+26,fg='#555500',bg='#fee59e'))


screen.addWidgetToPage(0,widget(wType='button',text='Register',w=90,h=29,x=280+x+3,y=187.5+50+y,fg='#555500',bg='#fee59e',command=lambda: changePage(1)))
screen.addWidgetToPage(0,widget(wType='button',text='Login',w=90,h=29,x=280+95+x+3,y=187.5+50+y,fg='#555500',bg='#fee59e',command=lambda: log()))

#######

screen.addPage()
screen.addWidgetToPage(1,widget(wType='label',text='',w=156+6+23,x=282+x,y=147+y+5,h=26,bg='#000000'))
screen.addWidgetToPage(1,widget(wType='label',text='Welcome to register page!',w=155+24,x=285+x,y=150+y+5,h=20,bg='#fee59e',fg='#555500'))

nameEntryReg = widget(wType='entry',bg='#fee59e',w=156,h=20,x=322+x,y=185+y,fg='#555500')
screen.addWidgetToPage(1,nameEntryReg)
screen.addWidgetToPage(1,widget(wType='label',text='',w=50,x=270+x,y=185+y,h=21,bg='#000000'))
screen.addWidgetToPage(1,widget(wType='label',text='Name',w=44,h=15,x=273+x,y=187.5+y,fg='#555500',bg='#fee59e'))

passEntryReg = widget(wType='entry',bg='#fee59e',w=156,h=20,x=322+x,y=185+26+y,fg='#555500')
screen.addWidgetToPage(1,passEntryReg)
screen.addWidgetToPage(1,widget(wType='label',text='',w=50,x=270+x,y=185+26+y,h=21,bg='#000000'))
screen.addWidgetToPage(1,widget(wType='label',text='Pass',w=44,h=15,x=273+x,y=187.5+y+26,fg='#555500',bg='#fee59e'))

    

screen.addWidgetToPage(1,widget(wType='button',text='Back',w=90,h=29,x=280+x+3,y=187.5+50+y,fg='#555500',bg='#fee59e',command=lambda: changePage(0)))
screen.addWidgetToPage(1,widget(wType='button',text='Register',w=90,h=29,x=280+95+x+3,y=187.5+50+y,fg='#555500',bg='#fee59e',command=lambda: reg()))

#####

screen.addPage()
offSet = 100
screen.addWidgetToPage(2,widget(wType='label',text='',w=176,x=247+offSet,y=97,h=30,bg='#000000'))
screen.addWidgetToPage(2,widget(wType='label',text='Find location of object',w=170,x=250+offSet,y=100,h=24,fg='#555500',bg='#fee59e'))

screen.addWidgetToPage(2,widget(wType='label',text='',w=176,x=247+offSet,y=137,h=30,bg='#000000'))
screen.addWidgetToPage(2,widget(wType='label',text='Find location of shapes',w=170,x=250+offSet,y=140,h=24,fg='#555500',bg='#fee59e'))

screen.addWidgetToPage(2,widget(wType='label',text='',w=176,x=247+offSet,y=177,h=30,bg='#000000'))
screen.addWidgetToPage(2,widget(wType='label',text='Find shapes of objects',w=170,x=250+offSet,y=180,h=24,fg='#555500',bg='#fee59e'))

fileEntry = widget(wType='entry',w=170,x=70+offSet,y=137,h=30,fg='#555500',bg='#fee59e')
screen.addWidgetToPage(2,fileEntry)

infoWidget = widget(wType='label',text='',w=170,x=250+offSet,y=380,h=24,fg='#555500',bg='#fee59e')
screen.addWidgetToPage(2,infoWidget)
def showLoc():
    global infoWidget
    infoWidget.hide()
    infoWidget = widget(wType='label',text=location(fileEntry.widget.get()),w=170,x=250+offSet,y=380,h=24,fg='#555500',bg='#fee59e')
    infoWidget.show()

def showLocShape():
    global infoWidget
    infoWidget.hide()
    infoWidget = widget(wType='label',text=shapeLocations(fileEntry.widget.get()),w=450,x=100+offSet,y=250,h=270,fg='#555500',bg='#fee59e')
    infoWidget.show()

def showShape():
    global infoWidget
    shapes(fileEntry.widget.get())
    infoWidget.hide()
    infoWidget = widget(wType='label',text='Image is saved',w=170,x=250+offSet,y=380,h=24,fg='#555500',bg='#fee59e')
    infoWidget.show()
    
screen.addWidgetToPage(2,widget(wType='button',text='Enter',w=80,x=430+offSet,y=97,h=30,fg='#555500',bg='#000000',command=showLoc))
screen.addWidgetToPage(2,widget(wType='button',text='Enter',w=80,x=430+offSet,y=137,h=30,fg='#555500',bg='#000000',command=showLocShape))
screen.addWidgetToPage(2,widget(wType='button',text='Enter',w=80,x=430+offSet,y=177,h=30,fg='#555500',bg='#000000',command=showShape))

