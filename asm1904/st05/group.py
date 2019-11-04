import pickle

from .Worker import Seller
from .Worker import Manager
from .Worker import Cleaner

class group:
    def __init__(self):
        self.group=[]

    def insertSeller(self):
    	newSeller = Seller()
    	newSeller.read()
    	self.group.append(newSeller)
    	print('Add new Seller')
    	
    def insertManager(self):
    	newManager = Manager()
    	newManager.read()
    	self.group.append(newManager)
    	print('Add new Manager')

    def insertCleaner(self):
    	newCleaner = Cleaner()
    	newCleaner.read()
    	self.group.append(newCleaner)
    	print('Add new Cleaner')

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
        f=open('asm1904/st05/info.dat','wb')
        pickle.dump(self.group,f)
        print('Information written to file')

    def readfile(self):
        f=open('asm1904/st05/info.dat','rb')
        self.group = pickle.load(f)
        print('Information read from file')

    def clean(self):
        self.group.clear()
        print('Clean completed')

    	
