# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:55:47 2019

@author: alena
"""

import pickle
        
class Man():
    
    man_behaviour = None
    file_behaviour = None
    
    def __init__(self, name =' ', surname=' ', year = ' ', email = ' ', category = ' '):
        self.name = name
        self.surname = surname
        self.year = year
        self.category = category
        
    def SetBehaviour(self, man_behaviour, file_behaviour):
        self.man_behaviour = man_behaviour
        self.file_behaviour = file_behaviour 
        
    def special(self):
        self.man_behaviour.special(self)
    
    def read(self):
        self.file_behaviour.read(self)
        
    def write(self):
        self.file_behaviour.write(self)
        
class AnalystBehaviour():
    def special(self, man):
        print('Analyst: ', man.name, man.surname, man.year, man.category)

class DeveloperBehaviour():
    def special(self, man):
        print('Developer: ', man.name, man.surname, man.year, man.category)
        
class TesterBehaviour():
    def special(self, man):
        print(' Tester: ', man.name, man.surname, man.year, man.category)
                 
class fileConsole():
    def read(self, man):
        man.name = input("name: ")
        man.surname = input("surname: ")
        man.year = input("year: ")
        man.category = input("category: ")
        
    def write(self, man):
        print(man.name, man.surname, man.year, man.category)
        
class Analyst(Man):
    man_behaviour = AnalystBehaviour()
    file_behaviour= fileConsole()
    
class Developer(Man):
    man_behaviour = DeveloperBehaviour()
    file_behaviour= fileConsole()

class Tester(Man):
    man_behaviour = TesterBehaviour()  
    file_behaviour = fileConsole()

class team:
    def __init__(self):
        self.team=[]

    def insertAnalyst(self):
        newAnalyst = Analyst()
        newAnalyst.read()
        self.team.append(newAnalyst)

    def insertDeveloper(self):
        newDeveloper = Developer()
        newDeveloper.read()
        self.team.append(newDeveloper)
        
    def insertTester(self):
        newTester = Tester()
        newTester.read()
        self.team.append(newTester)
                
    def show(self):
        if not self.team:
            print('No team')
        else:
            for (i,team) in enumerate (self.team):
                print(i+1)
                team.write()

    def clean(self):
        self.team.clear()

    def edit(self):
        self.show()
        print('Input # ')
        i=int(input())
        self.team[i-1].read()
            
    def delete(self):
        self.show()
        print('Input # ')
        i=int(input())
        self.team.pop(i-1)

    def writefile(self):
        f=open('asm1905/st11/team.dat','wb')
        pickle.dump(self.team,f)
        
    def readfile(self):
        f=open('asm1905/st11/team.dat','rb')
        self.team = pickle.load(f)

    def special(self):
        self.show()
        print('Input # ')
        i=int(input())
        self.team[i-1].special()