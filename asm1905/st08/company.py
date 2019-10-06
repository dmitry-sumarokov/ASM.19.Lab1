import pickle
import os
from employer import employer
from manager import manager
from Context import Context


class Company:
    def __init__(self):
        self._menu_list = [
                        ["Добавить работника", employer],
                        ["Добавить менеджера", manager],
                    ]
        self._employers = []

    def menu(self):
         for i, item in enumerate(self._menu_list):
             print("{0:2}. {1}".format(i, item[0]))
         return int(input())

    def input_employer(self):
        context = Context(self._menu_list[self.menu()][1]())
        context.context_input()
        self._employers.append(context)

    def edit_employer(self):
        self._employers[int(input('Введите № работника: '))].context_edit()

    def print_company(self):
        for i,w in enumerate(self._employers):
            w.context_print(i)

    def delete_employer(self):
        self._employers.pop(int(input('Введите № работника: ')))
        print('+')

    def clear_employersList(self):
        self._employers.clear()
        print('+')

    def save(self):
        with open(os.path.join(os.path.abspath(__name__).replace('.st08.group', '/st08'), 'company.p'), 'wb') as f:
            pickle.dump(self._employers, f)
        print('+')

    def load(self):
        with open(os.path.join(os.path.abspath(__name__).replace('.st08.group', '/st08'), 'company.p'), 'rb') as f:
            self._employers = pickle.load(f)
        print('+')

    def special(self):
        self._employers[int(input('Введите № работника: '))].context_special()
