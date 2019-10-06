from simple import simple

class Context:
    def __init__(self, simple: simple):
        self._simple = simple

    def context_input(self):
        self._simple._id = input('Введите id: ')
        self._simple._fullname = input('Введите ФИО: ')
        self._simple._pay = int(input('Введите ЗП: '))
        self._simple._age = int(input('Введите возраст: '))
        self._simple._email = input('email: ')
        self._simple.input_inf()

    def context_print(self,number):
        self._simple.print_inf()
        print(f'\n№: {number}',
              f'id/паспорт: {self._simple._id}',
              f'ФИО: {self._simple._fullname}',
              f'Зарплата: {self._simple._pay}',
              f'Возраст: {self._simple._age}',
              f'email: {self._simple._email}', sep='\n')

    def context_special(self):
        self._simple.special()
        #print(f'special: {self._simple._special}')

    def context_edit(self):
        new_id = input('Ред. id: ')
        self._simple._id = new_id if new_id else self._simple._id
        new_fullname = input('Ред. ФИО: ')
        self._simple._fullname = new_fullname if new_fullname else self._simple._fullname
        new_pay = input('Ред. ЗП: ')
        self._simple._pay = int(new_pay) if new_pay else self._simple._pay
        new_age = input('Ред. возраст: ')
        self._simple._age = int(new_age) if new_age else self._simple._age
        new_email = input('Ред. email: ')
        self._simple._email = new_email if new_email else self._simple._email
