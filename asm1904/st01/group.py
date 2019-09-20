# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:24:00 2019

@author: us211
"""
import pickle
        
class Human():
    human_behaviour = None
    IO_behaviour = None
    
    def __init__(self, name =' ', age = ' ', email = ' '):
        self.name = name
        self.age = age
        self.email = email
        
    def SetBehaviour(self, human_behaviour, IO_behaviour):
        self.human_behaviour = human_behaviour
        self.IO_behaviour = IO_behaviour 
        
    def execute(self):
        self.human_behaviour.execute(self.name)
    
    def read(self):
        self.IO_behaviour.read(self)
        
    def write(self):
        self.IO_behaviour.write(self)
        
class HumanBehaviour():
    def execute(self, name):
         raise NotImplementedError()
        
class StudentBehaviour(HumanBehaviour):
    def execute(self, name):
        print('Я студент '+ name)

class StarostaBehaviour(HumanBehaviour):
    def execute(self, name):
        print('Я староста '+ name)
        
class ProforgBehaviour(HumanBehaviour):
    def execute(self, name):
        print('Я профорг '+ name)
        
class IOBehavoior():
    def read(self, human):
         raise NotImplementedError()
    def write(self, human):
         raise NotImplementedError()
         
class IOConsole(IOBehavoior):
    def read(self, human):
        human.name = input("name: ")
        human.age = input("age: ")
        human.email = input("email: ")
        
    def write(self, human):
        print(human.name, human.age, human.email)
        
class Student(Human):
    #SetBehaviour(StudentBehaviour(), IOConsole())
    human_behaviour = StudentBehaviour()
    IO_behaviour= IOConsole()
    
class Starosta(Human):
    human_behaviour = StarostaBehaviour()
    IO_behaviour= IOConsole()

class Proforg(Human):
    human_behaviour = ProforgBehaviour()  
    IO_behaviour = IOConsole()


        
class group:
    def __init__(self):
        self.group=[]

    def insertStudent(self):
        newStudent = Student()
        newStudent.read()
        self.group.append(newStudent)
        print('Добавлен студент')
        
    def insertStarosta(self):
        newStarosta = Starosta()
        newStarosta.read()
        self.group.append(newStarosta)
        print('Добавлен староста')
        
    def insertProforg(self):
        newProforg = Proforg()
        newProforg.read()
        self.group.append(newProforg)
        print('Добавлен профорг')
        
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
        f=open('asm1904/st01/group.dat','wb')
        pickle.dump(self.group,f)
        print('Записано в файл')
        
    def readfile(self):
        f=open('asm1904/st01/group.dat','rb')
        self.group = pickle.load(f)
        print('Считано из файла')

    def clean(self):
        self.group.clear()
        print('Очищено')
