class Human():
    display = None
    behaviour = None
    
    def __init__(self):
        self.firstname = ' '
        self.lastname = ' '
        self.age = ' '
        self.number_stud = ' '
        
    def action(self):
        self.behaviour.action(self)
    
    def read(self):
        self.display.read(self)
        
    def write(self):
        self.display.write(self)
        
     
class BehaviourStudent():
    def action(self, human):
        print('Меня зовут ' + human.firstname + ' ' + human.lastname + ', я студент.')

class BehaviourStarosta():
    def action(self, human):
        print('Я староста этой группы, мне ' + human.age + '.')
        
class BehaviourProforg():
    def action(self, human):
        print('Мой номер студенческого - ' + human.number_stud + '. В этой группе я профорг.')

class ConsoleWork():
    def read(self, human):
        print()
        print ("Заполните анкету ученика")
        human.firstname = input("Введите имя: ")
        human.lastname = input("Введите фамилию: ")
        human.age = input("Введите возраст: ")
        human.number_stud = input("Введите номер студенческого: ")
        
    def write(self, human):
        print(human.firstname + " " + human.lastname + ", возраст: " + human.age + ", номер студенческого: " + human.number_stud)
        
                
class Student(Human):
    display = ConsoleWork()
    behaviour = BehaviourStudent()

    
class Starosta(Human):
    display = ConsoleWork()
    behaviour = BehaviourStarosta()


class Proforg(Human):
    display = ConsoleWork()
    behaviour = BehaviourProforg()  