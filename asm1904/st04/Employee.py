class Employee:
	Employee_behaviour = None
	IO_behaviour = None

	def __init__(self, Name =' ', Surname = ' ', Position = ' '):
		self.Name = Name
		self.Surname = Surname
		self.Position = Position

	def SetBehaviour(self, Employee_behaviour, IO_behaviour):
		self.Employee_behaviour = Employee_behaviour
		self.IO_behaviour = IO_behaviour

	def execute(self):
		self.Employee_behaviour.execute(self.Surname)

	def read(self):
		self.IO_behaviour.read(self)

	def write(self):
		self.IO_behaviour.write(self)

class LeaderBehaviour():
	def execute(self, Surname):
		print('Position of '+ Surname + ': Leader')

class ManagerBehaviour():
	def execute(self, Surname):
		print('Position of '+ Surname + ': Manager')

class AssistantBehaviour():
	def execute(self, Surname):
		print('Position of '+ Surname + ': Assistant')

class IOConsole():
	def read(self, Employee):
		Employee.Name = input("First name: ")
		Employee.Surname = input("Second name: ")
		Employee.Position = input("Position: ")

	def write(self, Employee):
		print(Employee.Name, Employee.Surname, Employee.Position)

class Leader(Employee):
	Employee_behaviour = LeaderBehaviour()
	IO_behaviour= IOConsole()

class Manager(Employee):
	Employee_behaviour = ManagerBehaviour()
	IO_behaviour= IOConsole()

class Assistant(Employee):
	Employee_behaviour = AssistantBehaviour()
	IO_behaviour = IOConsole()
