#parent class

import pickle
        
class Person ():
    person_position = None
    IO_position = None
    
    def __init__(self, name =' ', age = ' ', stazh = ' '):
        self.name = name
        self.age = age
        self.stazh = stazh
        
    def SetPosition(self, person_position, IO_position):
        self.person_position = person_position
        self.IO_position = IO_position 
        
    def execute(self):
        self.person_position.execute(self.name)
    
    def read(self):
        self.IO_position.read(self)
        
    def write(self):
        self.IO_position.write(self)
        
class PersonPosition():
    def execute(self, name):
         raise NotImplementedError()
        
class DancerPosition(PersonPosition):
    def execute(self, name):
        print('Я танцор '+ name)

class SoloistPosition(PersonPosition):
    def execute(self, name):
        print('Я солист '+ name)
        
class ChoreographerPosition(PersonPosition):
    def execute(self, name):
        print('Я хореограф '+ name)
        
class IOPosition():
    def read(self, person):
         raise NotImplementedError()
    def write(self, person):
         raise NotImplementedError()
         
class IOConsole(IOPosition):
    def read(self, person):
        person.name = input("name: ")
        person.age = input("age: ")
        person.stazh = input("stazh: ")
        
    def write(self, person):
        print(person.name, person.age, person.stazh)
        
class Dancer(Person):
    #SetPosition(DancerPosition(), IOConsole())
    person_position = DancerPosition()
    IO_position= IOConsole()
    
class Soloist(Person):
    person_position = SoloistPosition()
    IO_position= IOConsole()

class Choreographer(Person):
    person_position = ChoreographerPosition()  
    IO_position = IOConsole()


        
class group:
    def __init__(self):
        self.group=[]

    def insertDancer(self):
        newDancer = Dancer()
        newDancer.read()
        self.group.append(newDancer)
        print('Добавлен Танцор')
        
    def insertSoloist(self):
        newSoloist = Soloist()
        newSoloist.read()
        self.group.append(newSoloist)
        print('Добавлен Солист')
        
    def insertChoreographer(self):
        newChoreographer = Choreographer()
        newChoreographer.read()
        self.group.append(newChoreographer)
        print('Добавлен Хореограф')
        
    def execute(self):
        self.show()
        print('Введите номер: ')
        i=int(input())
        self.group[i-1].execute()
        print('Особое действие выполнено')
        
    def show(self):
        for (i,group) in enumerate (self.group):
            print(i+1)
            group.write()

    def edit(self):
        self.show()
        print('Введите номер: ')
        i=int(input())
        self.group[i-1].read()
        print('Отредактирован')
            

    def delete(self):
        self.show()
        print('Введите номер: ')
        i=int(input())
        self.group.pop(i-1)
        print('Удален')

    def writefile(self):
        f=open('asm1904/st02/group.dat','wb')
        pickle.dump(self.group,f)
        print('Записано в файл')
        
    def readfile(self):
        f=open('asm1904/st02/group.dat','rb')
        self.group = pickle.load(f)
        print('Считано из файла')

    def clean(self):
        self.group.clear()
        print('Очищено')
