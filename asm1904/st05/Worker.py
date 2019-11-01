class Worker():
	Worker_behaviour = None
	IO_behaviour = None

	def __init__(self, Name = '', Surname = '', Position = ''):
		self.Name = Name
		self.Surname = Surname
		self.Position = Position

	def SetBehaviour(self, Worker_behaviour, IO_behaviour):
		self.Worker_behaviour = Worker_behaviour
		self.IO_behaviour = IO_behaviour

	def execute(self):
    	self.human_behaviour.execute(self.Surname)


    def read():
    	self.IO_behaviour = read(self)

    def write():
    	self.IO_behaviour = write(self)
    	
class WorkerBehaviour():
	def execute(self, Name):
		raise NotImplementedError()

class SellerBehaviour(WorkerBehaviour):
	def execute(self, Name):
		print (Name + 'Seller')

class ManagerBehaviout(WorkerBehaviour):
	def execute(self, Name):
		print(Name + 'Manager')

class CleanerBehaviour(WorkerBehaviour):
	def execute(self, Name):
		print(Name + 'Cleaner')
	
class IOBehaviourr():
    def read(self, Worker):
        raise NotImplementedError()

    def write(self, Worker):
        raise NotImplementedError()

class IO_Console(IOBehaviour):
    def read(self, Worker):
        human.Name = input("Name: ")
        human.Surname = input("Surname: ")
        human.Position = input("Position: ")

    def write(self, Worker):
        print(human.Name, human.Surname, human.Position)

class Seller(Worker):
	behaviour = SellerBehaviour()
	IOBehaviour = IO_Console()

class Manager(Worker):
	 behaviour = WorkerBehaviour()
	 IOBehaviour = IO_Console()

class Cleaner(Worker):
	behaviour = CleanerBehaviour()
	IOBehaviour = IO_Console()
