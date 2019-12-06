import pickle

from .Creative import Artist
from .Creative import Writer
from .Creative import Poet

class association:
    def __init__(self):
        self.association=[]

    def insertArtist(self):
    	newArtist = Artist()
    	newArtist.read()
    	self.association.append(newArtist)
    	print(' Добавить Художника')

    def insertWriter(self):
    	newWriter = Writer()
    	newWriter.read()
    	self.association.append(newWriter)
    	print('Добавить Писателя')

    def insertPoet(self):
    	newPoet = Poet()
    	newPoet.read()
    	self.association.append(newPoet)
    	print('Добавить Поэта')

    def execute(self):
        self.show()
        print('Input №: ')
        i=int(input())
        print('Задача поставлена')
        self.association[i-1].execute()

    def show(self):
        for (i,association) in enumerate (self.association):
            print(i+1)
            association.write()

    def edit(self):
        self.show()
        print('Input №: ')
        i=int(input())
        self.association[i-1].read()
        print('Добавление выполнено успешно')


    def delete(self):
        self.show()
        print('Input №: ')
        i=int(input())
        self.association.pop(i-1)
        print('Удалено')

    def writefile(self):
        f=open('asm1904/st09/info.dat','wb')
        pickle.dump(self.association,f)
        print('Информация записана в файл')

    def readfile(self):
        f=open('asm1904/st09/info.dat','rb')
        self.association = pickle.load(f)
        print('Информация прочитана')

    def clean(self):
        self.association.clear()
        print('Очищено')
