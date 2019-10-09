from .person import Person
from .desbehavior import Des_behavior

class Designer(Person):

    def __init__(self):
        super().__init__()
        self.orders = input('Введите кол-во заказов: ')

    def edit(self):
        Des_behavior.edit(self)

    def print(self):
        Des_behavior.print(self)
