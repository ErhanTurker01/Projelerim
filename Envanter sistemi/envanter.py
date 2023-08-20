class item:
    def __init__(self,code,name,nums):
        self.code = code
        self.name = name
        self.num = nums

    def addItem(self,num):
        self.num += num

    def removeItem(self,num):
        if self.num - num >= 0:
            self.num -= num
        else:
            print("There is not enough {} in inventory!".format(self.name))

    def showInfo(self,where):
        print("Name:{}\nCode:{}\nNumber of {} in {}:{}".format(self.name,self.code,self.name,where,self.num))

class student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.items = []

    def addItem(self,Item,num):
        num = int(num)
        if num <= 0:
            print("Please enter positive intiger!")
            return Item
        if Item.num < num:
            print("There is not enough {} in inventory!".format(Item.name))
            return Item

        contains = False
        index = 0
        for i in range(len(self.items)):
            if  self.items[i].code == Item.code:
                contains = True
                index = i
                break

        if contains:
            self.items[index].num += num
        else:
            self.items.append(item(Item.code,Item.name,num))
        return item(Item.code,Item.name,Item.num-num)
    
    def returnItem(self,Item,num):
        num = int(num)
        if num <= 0:
            print("Please enter positive intiger!")
            return Item
        contains = False
        index = 0
        for i in range(len(self.items)):
            if  self.items[i].code == Item.code:
                contains = True
                index = i
                break

        if not contains or (len(self.items) and self.items[index].num < num):
            print("{} does not have enough {}!".format(self.name,Item.name))
            return Item
        
        self.items[index].num -= num
        if self.items[index].num != 0:
            return item(Item.code,Item.name,Item.num+num)
        self.items.pop(index)
    
    def showInfo(self):
        print("Name:{}\nID:{}\nItems:\n".format(self.name,self.id))
        for Item in self.items:
            Item.showInfo(self.name)



#normalde text dosyaları oluşturup bilgileri kaybetmemek gerekirdi
students = []
items = []

poll = 0
while poll != 9:
    poll = input("\n1)Register new student\n2)Register new item\n3)Get item from inventory\n4)Return item\n5)Show inventory\n6)Show student infos\n7)Add item to inventory\n8)Remove item from inventory\n9)Exit\n")
    poll = int(poll)    

    if poll == 1:
        sName = input("Enter students name:")
        sId = int(input("Enter {}'s ID:".format(sName)))
        students.append(student(sName,sId))

    if poll == 2:
        iName = input("Enter item's name:")
        iCode = int(input("Enter {}'s code:".format(iName)))
        iNum = int(input("Enter how many {} in inventory:".format(iName)))
        items.append(item(iCode,iName,iNum))

    if (poll == 3 or poll == 4) and len(students)>0 and len(items)>0:
        sId = int(input("Enter student ID:"))
        for Student in students:
            if Student.id == sId:
                iCode = int(input("Enter item's code:"))
                for i,Item in enumerate(items):
                    if Item.code == iCode:
                        if poll == 3:
                            num = int(input("Enter how many {} to take:".format(Item.name)))
                            items[i] = Student.addItem(Item,num)
                            break
                        if poll == 4 :
                            num = int(input("Enter how many {} to return:".format(Item.name)))
                            items[i] = Student.returnItem(Item,num)
                            break
                else:
                    print("Invalid code!")
                break
        else:
            print("Invalid ID!")

    if poll == 5:
        for Item in items:
            Item.showInfo("inventory")
    if poll == 6:
        for Student in students:
            Student.showInfo()
    if poll == 7 or poll == 8:
        iCode = int(input("Enter item's code:"))
        for i,Item in enumerate(items):
            if Item.code == iCode:
                if poll == 7:
                    num = int(input("Enter how many to add:"))
                    items[i].addItem(num)
                    break
                else:
                    num = int(input("Enter how many to remove:"))
                    items[i].removeItem(num)
                    break
        else:
            print("Invalid code!")
