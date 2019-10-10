class Human():
    human_behaviour = None
    IO_behaviour = None
    
    def __init__(self, Fname =' ', Sname = ' ', Email = ' '):
        self.Fname = Fname
        self.Sname = Sname
        self.Email = Email
        
    def SetBehaviour(self, human_behaviour, IO_behaviour):
        self.human_behaviour = human_behaviour
        self.IO_behaviour = IO_behaviour 
        
    def execute(self):
        self.human_behaviour.execute(self.Sname)
    
    def read(self):
        self.IO_behaviour.read(self)
        
    def write(self):
        self.IO_behaviour.write(self)
                
class EngineerBehaviour():
    def execute(self, Sname):
        print('Position of '+ Sname + ': Engineer')

class SpecialistBehaviour():
    def execute(self, Sname):
        print('Position of '+ Sname + ': Specialist')
        
class DepartmentBehaviour():
    def execute(self, Sname):
        print('Position of '+ Sname + ': Department head')
        
class IOConsole():
    def read(self, human):
        human.Fname = input("First name: ")
        human.Sname = input("Second name: ")
        human.Email = input("Email: ")
        
    def write(self, human):
        print(human.Fname, human.Sname, human.Email)
        
class Engineer(Human):
    human_behaviour = EngineerBehaviour()
    IO_behaviour= IOConsole()
    
class Specialist(Human):
    human_behaviour = SpecialistBehaviour()
    IO_behaviour= IOConsole()

class Department(Human):
    human_behaviour = DepartmentBehaviour()  
    IO_behaviour = IOConsole()