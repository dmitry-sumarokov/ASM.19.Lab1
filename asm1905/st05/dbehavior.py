from .behavior import Behavior

class D_behavior():

    def __init__(self):
        pass

    def edit(self):
        Behavior.edit(self)
        new_clients = input('Введите новое кол-во клиентов: ')
        self.clients = int(new_clients) if new_clients else self.clients

    def print(self):
        Behavior.print(self)
        print(f'Кол-во клиентов: {self.clients}\n')
        
        
