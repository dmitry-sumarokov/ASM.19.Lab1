import os
import pickle

from .context import Context
from .employee import Chief, Engeneer, Specialist, ChiefSpecialist

MENU = [
    ('Начальник', Chief),
    ('Инженер', Engeneer),
    ('Специалист', Specialist),
    ('Главного специалист', ChiefSpecialist)
]


class Group:

    def __init__(self):
        self.employee_list = []

    def add_employee(self):
        for i, (name, _) in enumerate(MENU):
            print(f'{i}: {name}')
        choice = int(input())

        context = Context(MENU[choice][1]())
        context.do_add_employee()
        self.employee_list.append(context)

    def edit_employee(self):
        emp_idx = int(input('Введите номер сотрудника: '))
        self.employee_list[emp_idx].do_edit()

    def remove_employee(self):
        emp_idx = int(input('Введите номер сотрудника: '))
        self.employee_list.pop(emp_idx)

    def print_group(self):
        for i, obj in enumerate(self.employee_list):
            obj.do_print(i)

    def clear_group(self):
        self.employee_list.clear()

    def save_to_file(self):
        filepath = os.path.join(os.path.abspath(__name__).replace('.st09.group', '/st09'), 'save.pkl')
        with open(filepath, 'wb') as f:
            pickle.dump(self.employee_list, f)

    def load_from_file(self):
        filepath = os.path.join(os.path.abspath(__name__).replace('.st09.group', '/st09'), 'save.pkl')
        with open(filepath, 'rb') as f:
            self.employee_list = pickle.load(f)

    def do_magic(self):
        emp_idx = int(input('Введите номер сотрудника: '))
        self.employee_list[emp_idx].do_magic_logic()
