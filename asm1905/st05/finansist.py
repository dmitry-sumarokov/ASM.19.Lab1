from .person import Person
from .fbehavior import F_behavior

class Finansist(Person):

    def __init__(self):
        super().__init__()
        self.account = input('Введите сумму на счете: ')

    def edit(self):
        F_behavior.edit(self)

    def print(self):
        F_behavior.print(self)

    

    
