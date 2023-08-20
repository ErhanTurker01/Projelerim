import tkinter as tk
class window:
    def __init__(self,w,h,bg):
        self.win = tk.Tk()
        self.pages = []
        self.win.minsize(width=w,height=h)
        self.win.configure(bg=bg)
    def addPage(self):
        self.pages.append(page())
        self.pages[len(self.pages)-1].showWidgets()
        self.pages[len(self.pages)-1].hideWidgets()
    def changePage(self,pNum):
        for p in self.pages:
            p.hideWidgets()
        self.pages[pNum].showWidgets()
    def addWidgetToPage(self,pNum,Widget):
        self.pages[pNum].addWidget(Widget)
    
class page:
    def __init__(self):
        self.widgets = []
    def addWidget(self,widget):
        self.widgets.append(widget)
    def hideWidgets(self):
        for widget in self.widgets:
            widget.hide()
    def showWidgets(self):
        for widget in self.widgets:
            widget.show()
    
class widget:
    def __init__(self,win=None,w=10,h=10,wType='label',x=0,y=0,text='tk',bg='black',fg='white',command=None):
        self.wType = wType
        self.win = win
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.text = text
        self.fg = fg
        self.bg = bg
        self.command = command
        self.widget = None
        if self.wType == 'label':
            self.widget = tk.Label(master=self.win,text=self.text,width=self.w,height=self.h,fg=self.fg,bg=self.bg)
        elif self.wType == 'button':
            self.widget = tk.Button(master=self.win,text=self.text,width=self.w,height=self.h,fg=self.fg,bg=self.bg,command=self.command)
        elif self.wType == 'entry':
            self.widget = tk.Entry(master=self.win,width=self.w,fg=self.fg,bg=self.bg)
    def show(self):
        self.widget.place(x=self.x,y=self.y,width=self.w,height=self.h)

    def hide(self):
        self.widget.place_forget()
