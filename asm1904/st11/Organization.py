import pickle 
from .Person import *
from .Director import *

class Organization:
    def __init__(self):
        self.organization=[]
        
    def addPerson(self):
        person=Person()
        person.write()
        self.organization.append(person)

    def addDirector(self):
        person=Director()
        person.write()
        self.organization.append(person)
		
    def updatePerson(self):
        if len(self.organization)==0:
            print("Список пуст!")
            return
        n=int(input("Введите id сотрудника: "))
        if n<=len(self.organization)-1 and 0<=n:
            print("Успешный ввод!")
            self.organization[n].write()
            print("Изменения успешно сохранены!\n")
        else:
            print("Введено некорректное значение!\n")
			
    def deletePerson(self):
        if len(self.organization)==0:
            print("Список персонала пуст!\n")
            return
        n=int(input("Введите id сотрудника: "))
        if n<=len(self.organization)-1 and 0<=n:
            print("Успешный ввод!")
            self.organization.pop(n)
            print("Удаление сотрудника выполнено!\n") 
        else:
            print ("Введено некорректное значение!\n")
        
    def showList(self):
        if len(self.organization)==0:
            print("Список персонала пуст!")
        else:
            i = 0
            print("Список:")
            for x in self.organization:
                print(i,x)
                i+=1
            
    def clearList(self):
        self.organization.clear()
        print("\nСписок персонала успешно очищен!\n")

    def writeToFile(self):
        pickle.dump(self.organization, open('st11/data/storage.dat', 'wb'))
        print("\nЗапись в файл успешно выполнена!\n")

    def readFromFile(self):
        self.organization=pickle.load(open('st11/data/storage.dat', 'rb'))
        print("\nЧтение из файла успешно выполнено!\n")
