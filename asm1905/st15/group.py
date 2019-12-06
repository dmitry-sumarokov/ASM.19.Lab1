import pickle

from .Workman import Mechanic
from .Workman import MainEngineer
from .Workman import Security

class group:
    def __init__(self):
        self.group=[]

    def insertMechanic(self):
    	newMechanic = Mechanic()
    	newMechanic.read()
    	self.group.append(newMechanic)
    	print(' Добавить Механика')
    	
    def insertMainEngineer(self):
    	newMainEngineer = MainEngineer()
    	newMainEngineer.read()
    	self.group.append(newMainEngineer)
    	print('Добавить главного инженера')

    def insertSecurity(self):
    	newSecurity = Security()
    	newSecurity.read()
    	self.group.append(newSecurity)
    	print('Добавить Охранника')

    def execute(self):
        self.show()
        print('Input №: ')
        i=int(input())
        print('Задача поставлена')
        self.group[i-1].execute()

    def show(self):
        for (i,group) in enumerate (self.group):
            print(i+1)
            group.write()

    def edit(self):
        self.show()
        print('Input №: ')
        i=int(input())
        self.group[i-1].read()
        print('Добавление выполнено успешно')


    def delete(self):
        self.show()
        print('Input №: ')
        i=int(input())
        self.group.pop(i-1)
        print('Удалено')

    def writefile(self):
        f=open('asm1905/st15/info.dat','wb')
        pickle.dump(self.group,f)
        print('Информация записана в файл')

    def readfile(self):
        f=open('asm1905/st15/info.dat','rb')
        self.group = pickle.load(f)
        print('Информация прочитана')

    def clean(self):
        self.group.clear()
        print('Очищено')

    	
