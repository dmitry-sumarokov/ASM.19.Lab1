import pickle
import os

from .director import Director
from .finansist import Finansist
from .designer import Designer
from .person import Person

class Company:

    def __init__(self):
        self.menu = [
            ['Добавить директора', Director],
            ['Добавить финансиста', Finansist],
            ['Добавить дизайнера', Designer]
        ]
        self.staff = []

    def add_staff(self):
        print()
        for i, item in enumerate(self.menu):
            print(f'{i} - {item[0]}')
        print()
        num = int(input())
        self.staff.append(self.menu[num][1]())

    def edit_staff(self):
        self.staff[int(input('Введите номер сотрудника: '))].edit()
        print('--------------------')
        print('Изменения сохранены')

    def delete_staff(self):
        self.staff.pop(int(input('Введите номер сотрудника: ')))

    def delete_all(self):
        self.staff.clear()

    def show_staff(self):
        for i, staff in enumerate(self.staff):
            print(staff.__class__.__name__+' [id: '+str(i)+']')
            staff.print()

    def save_staff(self):
        f = open(r'data.txt', 'wb')
        pickle.dump(self.staff, f)
        f.close()
        print('Список сохранен')

    def load_staff(self):
        f = open(r'data.txt', 'rb')
        self.staff = pickle.load(f)
        print('Список загружен')
