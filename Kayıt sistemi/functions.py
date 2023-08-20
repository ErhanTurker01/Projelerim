import random as rn
def reciveInfo(password,id):
    try:
        userFile = open(id+'.txt','r')
        info = userFile.readlines()
        if(info[0] == password+'\n'):
            return info[1]
        else:
            return 0
    except:
        return 1


def registerNewUser(password,name):
    if password == '' or name == '':
        return 0
    else:
        idFile = open('ids.txt','r')
        lastId = int(idFile.readlines()[0])

        idFile.close()
        idFile = open('ids.txt','w')
        randnum = rn.randint(1,15)
        idFile.write(str(lastId+randnum)+'\n')
        newUserFile = open(str(lastId+randnum) + '.txt','w')
        newUserFile.write(password + '\n' + name)
        idFile.close()
        newUserFile.close()
        return str(lastId+randnum)
