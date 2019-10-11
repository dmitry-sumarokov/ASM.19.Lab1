from .person import Person
from .dbehavior import D_behavior

class Director(Person):

    def __init__(self):
        super().__init__()
        self.clients = input('Введите кол-во клиентов: ')

    def edit(self):
        D_behavior.edit(self)

    def print(self):
        D_behavior.print(self)

    

    
