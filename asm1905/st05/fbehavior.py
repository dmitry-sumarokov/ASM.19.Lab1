from .behavior import Behavior

class F_behavior():

    def __init__(self):
        pass

    def edit(self):
        Behavior.edit(self)
        new_account = input('Введите новую сумму на счете: ')
        self.account = int(new_account) if new_account else self.account

    def print(self):
        Behavior.print(self)
        print(f'Сумма на счете: {self.account}\n')
        
        
