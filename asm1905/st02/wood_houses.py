from .houses import house

class wood_house(house):

	def input_info(self):
		self.wood_type = input("Please, input type of your wood: ")

	def output_info(self):
		print("Type of house = _wood house_")
		print("type of wood: ", self.wood_type)

	def edit_info(self):
		new_wood_type = input("What type of wood do you want to change? : ")
		self.wood_type = new_wood_type if new_wood_type else self.wood_type

	def special(self):
		season = int(input('0 - summer, 1 - autumn/spring, 2 - winter: '))
		self.price_coeff = 2-season/2
		print("Price coefficient: ", self.price_coeff)
