from .behavior import Behavior

class Des_behavior():

    def __init__(self):
        pass

    def edit(self):
        Behavior.edit(self)
        new_orders = input('Введите новое кол-во заказов: ')
        self.orders = int(new_orders) if new_orders else self.orders

    def print(self):
        Behavior.print(self)
        print(f'Кол-во заказов: {self.orders}\n')
