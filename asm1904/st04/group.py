import pickle

from .Employee import Leader
from .Employee import Manager
from .Employee import Assistant

class group:
    def __init__(self):
        self.group=[]

    def insertLeader(self):
    	newLeader = Leader()
    	newLeader.read()
    	self.group.append(newLeader)
    	print('Add new Leader')

    def insertManager(self):
    	newManager = Manager()
    	newManager.read()
    	self.group.append(newManager)
    	print('Add new Manager')

    def insertAssistant(self):
    	newAssistant = Assistant()
    	newAssistant.read()
    	self.group.append(newAssistant)
    	print('Add new Assistant')

    def execute(self):
        self.show()
        print('Input №: ')
        i=int(input())
        print('Task set')
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
        print('Edited')


    def delete(self):
        self.show()
        print('Input №: ')
        i=int(input())
        self.group.pop(i-1)
        print('Deleted')

    def writefile(self):
        f=open('asm1904/st04/info.dat','wb')
        pickle.dump(self.group,f)
        print('Written to file')

    def readfile(self):
        f=open('asm1904/st04/info.dat','rb')
        self.group = pickle.load(f)
        print('Read from file')

    def clean(self):
        self.group.clear()
        print('Cleaned')
