import pickle

from asm1904.st12.ProforgAction import ProforgAction
from asm1904.st12.StarostaAction import StarostaAction
from asm1904.st12.StudentAction import StudentAction


class Group:
    def __init__(self):
        self.group = []
        self.addMenu = {
            "1": ("Добавить студента", StudentAction()),
            "2": ("Добавить старосту", StarostaAction()),
            "3": ("Добавить профорга", ProforgAction()),
            "4": ("Назад", None)
        }

    def get_action_list(self):
        while True:
            # try:
            #     print(self.group[1].do_input())
            # except ValueError:
            #     print('ok')
            print()
            print('')
            print('Кого добавить:')
            for k in range(1, len(self.addMenu) + 1):
                print(k, " - ", self.addMenu[str(k)][0])
            command_number = input()
            try:
                int(command_number)
            except ValueError:
                print('Нужно ввести число от 1 до ' + str(len(self.addMenu)))
                continue
            if int(command_number) == 4:
                break
            if 1 <= int(command_number) <= len(self.addMenu) + 1:
                # print(self.addMenu[command_number][1]())
                self.group.append(self.addMenu[command_number][1].do_input())
                print('---------------')
                print(self.group)
                break

    def print_group(self):
        print('--------------------------------')
        for i, item in enumerate(self.group):
            print('Номер студента: ' + str(i + 1))
            item.do_print()
            print('--------------------------------')

    def edit(self):
        self.print_group()
        student_to_edit = input('Введите номер студента для редактирования: ')
        self.group[int(student_to_edit)-1].do_edit()

    def save(self):
        f = open('./asm1904/st19/file', 'wb')
        pickle.dump(self.group, f)
        print('Список сохранен')

    def load(self):
        f = open('./asm1904/st19/file', 'rb')
        self.group = pickle.load(f)
        print('Список загружен')

    def clean(self):
        self.group = []

