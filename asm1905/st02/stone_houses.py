from .houses import house

class stone_house(house):

	def input_info(self):
		self.stone_strong = input("Please, input level of stone strong: ")

	def output_info(self):
		print("Type of house = _stone house_")
		print("level of stone strong: ", self.stone_strong)

	def edit_info(self):
		new_stone_strong = input("What type of stone strong do you want to change? : ")
		self.stone_strong = new_stone_strong if new_stone_strong else self.stone_strong

	def special(self):
		season = int(input('0 - summer, 1 - autumn/spring, 2 - winter: '))
		self.stone_live = (2-season/2)*100
		print("Stone live: ", self.stone_live)
