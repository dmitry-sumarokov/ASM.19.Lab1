

class Student():
    Display = None
    IO_behaviour = None

    def __init__(self, name=' ', age=' ', gender=' '):
        self.name = name
        self.age = age
        self.gender = gender

    def SetBehaviour(self,Display, IO_behaviour):
        self.human_behaviour = Display
        self.IO_behaviour = IO_behaviour

    def execute(self):
        self.human_behaviour.execute(self.name)

    def read(self):
        self.IO_behaviour.read(self)

    def write(self):
        self.IO_behaviour.write(self)




class StudentBehaviour():
    def execute(self, name):
        raise NotImplementedError()


class BachelorBehaviour(StudentBehaviour):
    def execute(self, name):
        print(name + 'bachelor')


class MasterBehaviour(StudentBehaviour):
    def execute(self, name):
        print(name + 'master')


class Graduate_studentBehaviour(StudentBehaviour):
    def execute(self, name):
        print(name + 'graduate student')


class IOBehavoior():
    def read(self, student):
        raise NotImplementedError()

    def write(self, student):
        raise NotImplementedError()


class IO_Console(IOBehavoior):
    def read(self, human):
        human.name = input("name: ")
        human.age = input("age: ")
        human.email = input("gender: ")

    def write(self, human):
        print(human.name, human.age, human.gender)


class Bachelor(Student):
    behaviour = BachelorBehaviour()
    IO_behaviour = IO_Console()


class Master(Student):
    behaviour = MasterBehaviour()
    IO_behaviour = IO_Console()


class Graduate_student(Student):
    behaviour = Graduate_studentBehaviour()
    IO_behaviour = IO_Console()