class Creative():
	Creative_behaviour = None
	IO_behaviour = None

	def __init__(self, Name =' ', Surname = ' ', Function = ' '):
		self.Name = Name
		self.Surname = Surname
		self.Function = Function

	def SetBehaviour(self, Creative_behaviour, IO_behaviour):
		self.Creative_behaviour = Creative_behaviour
		self.IO_behaviour = IO_behaviour

	def execute(self):
		self.Creative_behaviour.execute(self.Surname)

	def read(self):
		self.IO_behaviour.read(self)

	def write(self):
		self.IO_behaviour.write(self)

class ArtistBehaviour():
	def execute(self, Surname):
		print('Position of '+ Surname + ': Artist')

class WriterBehaviour():
	def execute(self, Surname):
		print('Position of '+ Sname + ': Writer')

class PoetBehaviour():
	def execute(self, Surname):
		print('Position of '+ Sname + ': Poet')

class IOConsole():
	def read(self, Creative):
		Creative.Name = input("First name: ")
		Creative.Surname = input("Second name: ")
		Creative.Function = input("Function: ")

	def write(self, Creative):
		print(Creative.Name, Creative.Surname, Creative.Function)

class Artist(Creative):
	Creative_behaviour = ArtistBehaviour()
	IO_behaviour= IOConsole()

class Writer(Creative):
	Creative_behaviour = WriterBehaviour()
	IO_behaviour= IOConsole()

class Poet(Creative):
	Creative_behaviour = PoetBehaviour()
	IO_behaviour = IOConsole()
