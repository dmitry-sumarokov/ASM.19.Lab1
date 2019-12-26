from .employee import BaseEmployee


class Context:

    def __init__(self, employee: BaseEmployee):
        self.employee = employee

    def do_magic_logic(self):
        print(self.employee.do_magic())

    def do_add_employee(self):
        self.employee.first_name = input('Введите имя: ')
        self.employee.gender = input('Введите пол: ')
        self.employee.age = int(input('Введите возраст: '))
        self.employee.do_init()

    def do_print(self,number):
        print(f'________________{number}_________________')
        print(f'Имя: {self.employee.first_name}')
        print(f'Пол: {self.employee.gender}')
        print(f'Возраст: {self.employee.age}')
        self.employee.do_print()

    def do_edit(self):
        print('Если не хотите вносить изменения, оставьте поля пустыми')
        new_first_name = input('Введите имя: ')
        self.employee.first_name = new_first_name if new_first_name else self.employee.first_name
        new_gender = input('Введите пол: ')
        self.employee.gender = new_gender if new_gender else self.employee.gender
        new_age = input('Введите возраст: ')
        self.employee.age = int(new_age) if new_age else self.employee.age
        self.employee.do_edit()
