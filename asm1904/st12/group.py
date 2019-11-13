# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:24:00 2019

@author: us211
"""
import pickle
        
from .human import Engineer
from .human import Specialist
from .human import Department

        
class group:
    def __init__(self):
        self.group=[]

    def insertEngineer(self):
        newEngineer = Engineer()
        newEngineer.read()
        self.group.append(newEngineer)
        print('Add Engineer')
        
    def insertSpecialist(self):
        newSpecialist = Specialist()
        newSpecialist.read()
        self.group.append(newSpecialist)
        print('Add Specialist')
        
    def insertDepartment(self):
        newDepartment = Department()
        newDepartment.read()
        self.group.append(newDepartment)
        print('Add Department head')
        
    def execute(self):
        self.show()
        print('Input №: ')
        i=int(input())
        print('Task completed')
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
        print('Edit completed')
            

    def delete(self):
        self.show()
        print('Input №: ')
        i=int(input())
        self.group.pop(i-1)
        print('Delete completed')

    def writefile(self):
        f=open('asm1904/st12/info.dat','wb')
        pickle.dump(self.group,f)
        print('Information written to file')
        
    def readfile(self):
        f=open('asm1904/st12/info.dat','rb')
        self.group = pickle.load(f)
        print('Information read from file')

    def clean(self):
        self.group.clear()
        print('Clean completed')
