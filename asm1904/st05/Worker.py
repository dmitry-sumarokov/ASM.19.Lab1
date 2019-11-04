class Worker():
	Worker_behaviour = None
	IO_behaviour = None

	def __init__(self, Fname =' ', Sname = ' ', Position = ' '):
		self.Fname = Fname
		self.Sname = Sname
		self.Position = Position

	def SetBehaviour(self, human_behaviour, IO_behaviour):
		self.human_behaviour = Worker_behaviour
		self.IO_behaviour = IO_behaviour 

	def execute(self):
		self.Worker_behaviour.execute(self.Sname)

	def read(self):
		self.IO_behaviour.read(self)

	def write(self):
		self.IO_behaviour.write(self)

class SellerrBehaviour():
	def execute(self, Sname):
		print('Position of '+ Sname + ': Seller')

class ManagerBehaviour():
	def execute(self, Sname):
		print('Position of '+ Sname + ': Manager')

class CleanerBehaviour():
	def execute(self, Sname):
		print('Position of '+ Sname + ': Cleaner')

class IOConsole():
	def read(self, Worker):
		Worker.Fname = input("First name: ")
		Worker.Sname = input("Second name: ")
		Worker.Position = input("Position: ")

	def write(self, Worker):
		print(Worker.Fname, Worker.Sname, Worker.Position)

class Seller(Worker):
	human_behaviour = SellerrBehaviour()
	IO_behaviour= IOConsole()

class Manager(Worker):
	human_behaviour = ManagerBehaviour()
	IO_behaviour= IOConsole()

class Cleaner(Worker):
	human_behaviour = CleanerBehaviour()  
	IO_behaviour = IOConsole() 