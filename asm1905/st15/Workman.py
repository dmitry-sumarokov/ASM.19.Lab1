class Workman():
	Workman_behaviour = None
	IO_behaviour = None

	def __init__(self, Name =' ', Surname = ' ', Function = ' '):
		self.Name = Name
		self.Surname = Surname
		self.Function = Function

	def SetBehaviour(self, Workman_behaviour, IO_behaviour):
		self.Workman_behaviour = Workman_behaviour
		self.IO_behaviour = IO_behaviour 

	def execute(self):
		self.Workman_behaviour.execute(self.Surname)

	def read(self):
		self.IO_behaviour.read(self)

	def write(self):
		self.IO_behaviour.write(self)

class MechanicBehaviour():
	def execute(self, Surname):
		print('Position of '+ Surname + ': Mechanic')

class MainEngineerBehaviour():
	def execute(self, Surname):
		print('Position of '+ Sname + ': MainEnginerr')

class SecurityBehaviour():
	def execute(self, Surname):
		print('Position of '+ Sname + ': Security ')

class IOConsole():
	def read(self, Workman):
		Workman.Name = input("First name: ")
		Workman.Surname = input("Second name: ")
		Workman.Function = input("Function: ")

	def write(self, Workman):
		print(Workman.Name, Workman.Surname, Workman.Function)

class Mechanic(Workman):
	Workman_behaviour = MechanicBehaviour()
	IO_behaviour= IOConsole()

class MainEnginerr(Workman):
	Workman_behaviour = MainEngineerBehaviour()
	IO_behaviour= IOConsole()

class Security(Workman):
	Workman_behaviour = SecurityBehaviour()  
	IO_behaviour = IOConsole() 