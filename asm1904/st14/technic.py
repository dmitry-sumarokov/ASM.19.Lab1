#parent class

import pickle

class technic():

    t_behaviour = None
    IObehaviour = None

    def __init__(self, brend = ' ' , color = ' ', year = ' '):
        self.brend = brend
        self.color = color
        self.year = year

                     
    def SetBehaviaur (self, t_behaviour, IObehaviour):
        self.t_behaviour = t_behaviour
        self.IObehaviour = IObehaviour
            
    def spesial(self):
        self.t_behaviour.spesial(self.brend)
            
    def read(self):
        self.IObehaviour.read(self)
            
    def write(self):
        self.IObehaviour.write(self)
            
# chaldclass
        

            
class AMBehaviour():
    def spesial(self, brend):
        print('Это машина! Престегни ремень!')
        
class MOTOBehaviour():
    def spesial(self, brend):
        print('Это мотоцикл! Не забудь шлем!')
        
class ATVBehaviour():
    def spesial(self, brend):
        print('Это квадроцикл! Ездить только по бездорожью!!')
        
        
class IObehaviour():
    def read(self, technic):
         raise NotImplementedError()
    def write(self, technic):
         raise NotImplementedError()
         
class IOConsole(IObehaviour):
    def read(self, technic):
        technic.brend = input("Марка: ")
        technic.color = input("Цвет: ")
        technic.year = input("Год выпуска: ")
        
    def write(self, technic):
        print(technic.brend, technic.color, technic.year)
        
class AM(technic):
    t_behaviour = AMBehaviour()
    IObehaviour= IOConsole()
    
class MOTO(technic):
    t_behaviour = MOTOBehaviour()
    IObehaviour= IOConsole()

class ATV(technic):
    t_behaviour = ATVBehaviour()
    IObehaviour = IOConsole()

# Container
        
class Container():
    def __init__(self):
            self.Container=[]

    def insertAM(self):
        newAM = AM()
        newAM.read()
        self.Container.append(newAM)
        print('Добавлен автомобиль')
        
    def insertMOTO(self):
        newMOTO = MOTO()
        newMOTO.read()
        self.Container.append(newMOTO)
        print('Добавлен мотоцикл')
        
    def insertATV(self):
        newATV = ATV()
        newATV.read()
        self.Container.append(newATV)
        print('Добавлен квадроцикл')
        
    def printlist(self):
        if not self.Container:
            
            print('Не найдено')
            return
        
    def spesial(self):
        self.printlist()
        print('Введите номер: ')
        i=int(input())
        if (i <= len (self.Container)):
            self.Container[i-1].spesial()
        else:
            print('Такого номера не существует!!!')

        
    def show(self):
        for (i,Container) in enumerate (self.Container):
            print(i+1)
            Container.write()

    def edit(self):
        self.show()
        print('Введите номер: ')
        i=int(input())
        if (i <= len (self.Container)):
            self.Container[i-1].read()
            print('Исправленно')
        else:
            print('Такого номера не существует!!!')
            

    def delete(self):
        self.show()
        print('Введите номер: ')
        i=int(input())
        if (i <= len (self.Container)):
            self.Container.pop(i-1)
            print('Удален')
        else:
            print('Такого номера не существует!!!')

    def writefile(self):
        #f=open('desktop/st14/technic.dat','wb')
        #pickle.dump(self.Container,f)
        with open ('technic.dat','wb') as fp:
            pickle.dump(self.Container,fp)
            print('Записано в файл')
        
    def readfile(self):
       # f=open('desktop/st14/technic.dat','rb')
        #self.Container = pickle.load(f)
        with open ('technic.dat','rb') as fp:
            self.Container.extend(pickle.load(fp))
            print('Считано из файла')

    def clean(self):
        self.Container.clear()
        print('Очищено')
        
        
        
        

