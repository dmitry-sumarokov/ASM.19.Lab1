import pickle
        
class Workers():
    workers_behaviour = None
    IO_behaviour = None
    
    def __init__(self, surname =' ', age = ' ', qualification = ' '):
        self.surname = surname
        self.age = age
        self.qualification = qualification
        
    """def SetBehaviour(self, workers_behaviour, IO_behaviour):
        self.workers_behaviour = workers_behaviour
        self.IO_behaviour = IO_behaviour """
        
    def execute(self):
        self.workers_behaviour.execute(self.surname)
    
    def read(self):
        self.IO_behaviour.read(self)
        
    def write(self):
        self.IO_behaviour.write(self)
        
class WorkersBehaviour():
    def execute(self, surname):
         raise NotImplementedError()
        
class DrillerBehaviour(WorkersBehaviour):
    def execute(self, surname):
        print('Бурильщик '+ surname)

class GeologistBehaviour(WorkersBehaviour):
    def execute(self, surname):
        print('Геолог '+ surname)
        
class DeveloperBehaviour(WorkersBehaviour):
    def execute(self, surname):
        print('Разработчик '+ surname)
        
class IOBehavoior():
    def read(self, workers):
         raise NotImplementedError()
    def write(self, workers):
         raise NotImplementedError()
         
class IOConsole(IOBehavoior):
    def read(self, workers):
        workers.surname = input("surname: ")
        workers.age = input("age: ")
        workers.qualification = input("qualification: ")
        
    def write(self, workers):
        print(workers.surname, workers.age, workers.qualification)
        
class Driller(Workers):
    workers_behaviour = DrillerBehaviour()
    IO_behaviour= IOConsole()
    
class Geologist(Workers):
    workers_behaviour = GeologistBehaviour()
    IO_behaviour= IOConsole()

class Developer(Workers):
    workers_behaviour = DeveloperBehaviour()  
    IO_behaviour = IOConsole()


        
class workers:
    def __init__(self):
        self.staff=[]

    def insertDriller(self):
        newDriller = Driller()
        newDriller.read()
        self.staff.append(newDriller)
                
    def insertGeologist(self):
        newGeologist = Geologist()
        newGeologist.read()
        self.staff.append(newGeologist)
                
    def insertDeveloper(self):
        newDeveloper = Developer()
        newDeveloper.read()
        self.staff.append(newDeveloper)
                
    def execute(self):
        self.show()
        print('Введите номер: ')
        i=int(input())
        self.staff[i-1].execute()
              
    def show(self):
        for (i,staff) in enumerate (self.staff):
            print(i+1)
	    self.staff[i-1].execute()
            staff.write()

    def edit(self):
        self.show()
        print('Введите номер: ')
        i=int(input())
        self.staff[i-1].read()
                    
    def delete(self):
        self.show()
        print('Введите номер: ')
        i=int(input())
        self.staff.pop(i-1)

    def writefile(self):
        f=open('asm1905/st10/staff.dat','wb')
        pickle.dump(self.staff,f)
              
    def readfile(self):
        f=open('asm1905/st10/staff.dat','rb')
        self.staff = pickle.load(f)

    def clean(self):
        self.staff.clear()
