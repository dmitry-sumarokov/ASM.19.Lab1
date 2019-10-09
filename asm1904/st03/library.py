# -*- coding: utf-8 -*-

import pickle
        
class Edition():
    edition_behaviour = None
    IO_behaviour = None
    
    def __init__(self, name =' ', author = ' ', year = ' '):
        self.name = name
        self.author = author
        self.year = year
        
    def SetBehaviour(self, edition_behaviour, IO_behaviour):
        self.edition_behaviour = edition_behaviour
        self.IO_behaviour = IO_behaviour 
        
    def execute(self):
        self.edition_behaviour.execute(self.name)
    
    def read(self):
        self.IO_behaviour.read(self)
        
    def write(self):
        self.IO_behaviour.write(self)
        
class EditionBehaviour():
    def execute(self, name):
         raise NotImplementedError()
        
class BookBehaviour(EditionBehaviour):
    def execute(self, name):
        print('Книга ')

class JournalBehaviour(EditionBehaviour):
    def execute(self, name):
        print('Журнал ')
        
class NewspaperBehaviour(EditionBehaviour):
    def execute(self, name):
        print('Газета ')
        
class IOBehavoior():
    def read(self, edition):
         raise NotImplementedError()
    def write(self, edition):
         raise NotImplementedError()
         
class IOConsole(IOBehavoior):
    def read(self, edition):
        edition.name = input("name: ")
        edition.author = input("author: ")
        edition.year = input("year: ")
        
    def write(self, edition):
        print('Название: ' + edition.name,'\nАвтор: ' + edition.author, '\nГод издания: ' + edition.year)
        
class Book(Edition):
    #SetBehaviour(StudentBehaviour(), IOConsole())
    edition_behaviour = BookBehaviour()
    IO_behaviour= IOConsole()
    
class Journal(Edition):
    edition_behaviour = JournalBehaviour()
    IO_behaviour= IOConsole()

class Newspaper(Edition):
    edition_behaviour = NewspaperBehaviour()  
    IO_behaviour = IOConsole()


        
class library:
    def __init__(self):
        self.library=[]

    def insertBook(self):
        newBook = Book()
        newBook.read()
        self.library.append(newBook)
        print('Добавлена книга')
        
    def insertJournal(self):
        newJournal = Journal()
        newJournal.read()
        self.library.append(newJournal)
        print('Добавлен журнал')
        
    def insertNewspaper(self):
        newNewspaper = Newspaper()
        newNewspaper.read()
        self.library.append(newNewspaper)
        print('Добавлена газета')

        
    def show(self):
        for (i,library) in enumerate (self.library):
            print(i+1)
            library.execute()
            library.write()
            
    def edit(self):
        self.show()
        print('Введите номер: ')
        i=int(input())
        self.library[i-1].read()
        print('Отредактировано')
            

    def delete(self):
        self.show()
        print('Введите номер: ')
        i=int(input())
        self.library.pop(i-1)
        print('Удалено')

    def writefile(self):
        f=open('asm1904/st03/library.dat','wb')
        pickle.dump(self.library,f)
        print('Записано в файл')
        
    def readfile(self):
        f=open('asm1904/st03/library.dat','rb')
        self.library = pickle.load(f)
        print('Считано из файла')

    def clean(self):
        self.library.clear()
        print('Очищено')
