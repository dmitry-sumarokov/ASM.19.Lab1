from abc import ABC, abstractmethod


class StudentAbs(ABC):

    def __init__(self):
        self.age = ''
        self.student_kind = ''
        pass

    @abstractmethod
    def do_input(self):
        self.first_name = input('Введите имя: ')
        self.second_name = input('Введите фамилию: ')
        self.parent_name = input('Введите отчество: ')
        self.age = str(input('Введите возраст: '))
        pass

    @abstractmethod
    def do_print(self):
        print('Имя: ' + self.first_name)
        print('Фамилия :' + self.second_name)
        print('Отчество' + self.parent_name)
        print('Возраст :' + self.age)
        print('Тип: ' + self.student_kind)
        pass

    @abstractmethod
    def do_edit(self):
        self.do_input()
        pass

    @abstractmethod
    def do_magic(self):
        pass
