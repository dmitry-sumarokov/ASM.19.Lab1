from abc import ABC, abstractmethod

class house():
	def __init__(self, S=0, weight=0, height=0, number=1):
		self.S=S
		self.weight=weight
		self.height=height
		self.number=number

	@abstractmethod
	def input_info(self):
		pass

	@abstractmethod
	def output_info(self):
		print("Material type: ", self.material_type, " square: ", self.S, " \nweight: ", self.weight, " height: ", self.height, " number of house: ", self.number)
		pass

	@abstractmethod
	def edit_info(self):
		pass

	@abstractmethod
	def special(self):
		pass
