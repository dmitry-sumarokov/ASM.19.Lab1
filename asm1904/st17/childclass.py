from .parentclass import Animal


class CatBehavior():
	def different(self, name):
		print ('Я кот. Мяу')
		
class DogBehavior():
	def different(self, name):
		print ('Я пес. Гав')
		
class Display():

    def put(self, name):
        print('Кличка:')
        self.name=input()
        print('Возраст:')
        self.age=input()
        print('Пол:')
        self.gender=input()

    def output(self, name):
        print(self.name)
        print(self.age)
        print(self.gender)

"""class Outinscreen(OutBehavior):
	def read(self, animal):
		animal.name = input("Имя:")
		animal.age = input("Возраст:")
		animal.gender = input("Пол:")
	def write(self,animal): 
		print (animal.name, animal.age, animal.gender)"""

class Cat(Animal):
	animal_behavior = CatBehavior()
	display = Display()

class Dog(Animal):
	animal_behavior = DogBehavior()
	display = Display()
    

