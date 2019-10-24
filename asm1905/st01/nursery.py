import pickle
from .cats import Cats, Siamese, British, Lop_eared, Sphinx


class Nursery():
	def __init__(self):
		self._menu_list = [
			["Siamese cat", Siamese],
			["British cat", British],
			["Lop-eared cat", Lop_eared],
			["Sphinx", Sphinx]
			]
		self.cats_list = []
        
	def menu(self):
		print("________________________________")
		for i, item in enumerate(self._menu_list):
			print("{0:2}. {1}".format(i, item[0]))
		return int(input())
	def do_special_meow(self):
		self.cats_list[int(input('Enter number of the cat'))].special_meow()

	def add_cat(self):
		behav = Behaviour(self._menu_list[self.menu()][1]())
		behav.do_add_the_cat()
		self.cats_list.append(behav)

	def change_cat(self):
		for i,w in enumerate(self.cats_list):
			w.do_print(i)
		self.cats_list[int(input('Enter number of the cat: '))].do_edit()

	def print_cats(self):
		for i,w in enumerate(self.cats_list):
			w.do_print(i)


	def remove_the_cat(self):
		self.cats_list.pop(int(input('Enter number of the cat: ')))

	def clear_cats_list(self):
		self.cats_list.clear()
       
	def save_to_file(self):
		with open('cat_list.p', 'wb') as f:
			pickle.dump(self.cats_list, f)

	def load_from_file(self):
		with open('cat_list.p', 'rb') as f:
			self.cats_list = pickle.load(f)


class Behaviour():

    def __init__(self, cat: Cats):
        self._cat = cat

    def special_meow(self):
        print(self._cat.do_meow())



    def do_add_the_cat(self):
        self._name = input('Enter the name: ')
        self._gender = input('Enter the gender: ')
        self._age = int(input('Enter the age: '))
        self._colour = input('Enter the colour: ')

    def do_print(self,number):
        print('________________{0}_________________\nName: {1}\nGender: {2}\nAge: {3}\nColour {4}\n{5}'.format(
                                number, self._name, self._gender, self._age, self._colour, self._cat.do_meow()))


    def do_edit(self):
        new_name = input('Enter the name: ')
        self._name = new_name if new_name else self._name
        new_gender = input('Enter the gender: ')
        self._gender = new_gender if new_gender else self._gender
        new_age = input('Enter the age: ')
        self._age = int(new_age) if new_age else self._age
        new_colour = input('Enter the colour: ')
        self._colour=new_colour if new_colour else self._colour 
      
