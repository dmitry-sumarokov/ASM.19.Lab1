class Animals():
    Behaviour = None
    Display = None
    
    def __init__(self):
        self.Name = ''
        self.Klass = ''
        self.Age = ''
        self.MaxAge = ''
        self.Detki = ''

    def SetBehaviour(self, Behaviour, Display):
        self.Behaviour = Behaviour
        self.Display = Display

    def Feature(self):
        self.Behaviour.Feature_animal(self)

    def Read (self):
        self.Display.Read(self)

    def Write (self):
        self.Display.Write(self)
        
class Behaviour_Mammals():
        def Feature_animal(self, Animals):
            print('\n Кормят детей молоком.')
            
class Behaviour_Fish():
        def Feature_animal(self, Animals):
            print('\n Метают икру.')
    
class Behaviour_Bird():
        def Feature_animal(self, Animals):
            print('\n Имеют клюв.')
    
class Behaviour_Reptile():
        def Feature_animal(self, Animals):
            print('\n Хладнокровные, имеют низкую температуру тела.')

class Disp():
    def Read(self, Animals):
        Animals.Name = input("Введите имя животного: \n")
        Animals.Klass = input("Введите класс: \n")
        Animals.Age = input("Введите возраст : \n")
        Animals.MaxAge = input("Введите максимальный возраст: \n")
        Animals.Detki = input("Введите количество деток: \n")
        
    def Write(self, Animals):
        print(Animals.Name, Animals.Klass, Animals.Age, Animals.MaxAge, Animals.Detki)


class Mammals(Animals):
    def __init__(self):
        self.SetBehaviour(Behaviour_Mammals(), Disp())
        
class Fish(Animals):
    def __init__(self):
        self.SetBehaviour(Behaviour_Fish(),Disp())
        
class Bird(Animals):
    def __init__(self):
        self.SetBehaviour(Behaviour_Bird(),Disp())
        
class Reptile(Animals):
    def __init__(self):
        self.SetBehaviour(Behaviour_Reptile(),Disp())
