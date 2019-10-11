from .parentclass import Animal
from .childclass import Dog
from .childclass import Cat
from .childclass import CatBehavior
from .childclass import DogBehavior
from .childclass import Display

import pickle

class Container:
  def __init__(self):
    self.list=[]
  
  def addCat(self):
    newcat = Cat()
    newcat.put()
    self.list.append(Cat())
    print ('Объект записан')

  def addDog(self):
    newdog = Dog()
    newdog.put()
    self.list.append(Dog())
    print ('Объект записан')

  def printlist(self):
    if not self.list:
      print('Нет данных')
      return

    for (i,elem) in enumerate (self.list):
        print('Объект №', i+1)
        #print(i+1)
        elem.output()

  def clearlist(self):
        self.list.clear()

  def remove_elem(self):
    print('Номер элемента?')
    number=int(input())
    if (number <= len(self.list)):
      del self.list[number-1]
      print('Элемент удален успешно')  
    else:
      print('Элемент уже удален или еще не добавлен')
      print('Выберите 4 пункт меню для просмотра')  

  def edit_elem(self):
    print('Номер элемента?')
    number=int(input())
    if (number <= len(self.list)):
        self.list[number-1].put()
    else:
      print('Нет такого элемента:( ')
      print('Выберите 4 пункт меню для просмотра')  
              
  def recording(self):
        with open('outfile.dat','wb') as fp:
            pickle.dump(self.list,fp)
            print('Записано!')

  def read(self):
    with open ('outfile.dat', 'rb') as fp:
            self.list.extend(pickle.load(fp))
            print('Считано!')
  
  def different(self):
    self.printlist()
    print('Номер элемента?')
    number=int(input())
    self.list[number-1].different()
  
    
          

    
