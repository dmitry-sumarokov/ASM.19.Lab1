import pickle
import os
from .Context import Context
from .Chief import Chief
from .Engeneer import Engeneer
from .Specialist import Specialist
from .ChiefSpecialist import ChiefSpecialist


class Group:
    def __init__(self):
        self._menu_list = [
                        ["Добавить начальника", Chief],
                        ["Добавить инженера", Engeneer],
                        ["Добавить специалиста", Specialist],
                        ["Добавить главного специалиста", ChiefSpecialist]

            
                    ]
        self._workers = []
        
    def menu(self):
        print("------------------------------")
        for i, item in enumerate(self._menu_list):
            print("{0:2}. {1}".format(i, item[0]))
        print("------------------------------")
        return int(input())
    def do_magic(self):
        self._workers[int(input('Введите номер сотрудника: '))].do_magic_logic()

    def add_worker(self):
            context = Context(self._menu_list[self.menu()][1]())
            context.do_add_worker()
            self._workers.append(context)
    def change_worker(self):
            self._workers[int(input('Введите номер сотрудника: '))].do_edit()
    def print_group(self):
            for i,w in enumerate(self._workers):
                w.do_print(i)
    def remove_worker(self):
        self._workers.pop(int(input('Введите номер сотрудника: ')))
        print('Успешно')
    def clear_worker(self):
        self._workers.clear()
        print('Успешно')
    def save_to_file(self):
        with open(os.path.join(os.path.abspath(__name__).replace('.st19.group', '/st19'), 'group.p'), 'wb') as f:
            pickle.dump(self._workers, f)
        print('Успешно')
    def load_from_file(self):
        with open(os.path.join(os.path.abspath(__name__).replace('.st19.group', '/st19'), 'group.p'), 'rb') as f:
            self._workers = pickle.load(f)
        print('Успешно')
    


        


