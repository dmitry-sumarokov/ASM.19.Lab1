import pickle
import os

from .simple_student import SimpleStudent
from .starosta import Starosta
from .proforg import Proforg
from .student import Student
from .behav_starosta import BStarosta
from .behav_proforg import BProforg
from .behav_simp_student import BSimpStudent


class Group:
    __slots__ = ('_group_menu', '_students')

    def __init__(self):
        self._group_menu = [
            ['Добавить студента', SimpleStudent, BSimpStudent],
            ['Добавить старосту', Starosta, BStarosta],
            ['Добавить профорга', Proforg, BProforg]
        ]
        self._students = []

    def add_student(self):
        print()
        for i, item in enumerate(self._group_menu):
            print(f'{i} - {item[0]}')
        print()
        type_s = int(input())
        self._students.append(Student(self._group_menu[type_s][1](),
                                      self._group_menu[type_s][2]))

    def change_student(self):
        self._students[int(input('Введите номер студента: '))].edit_student()
        print('Изменения сохранены')

    def remove_student(self):
        self._students.pop(int(input('Введите номер студента: ')))

    def print_group(self):
        for i, student in enumerate(self._students):
            print('\nНомер студента: ' + str(i))
            student.print_info()

    def do_magic(self):
        self._students[int(input('Введите номер студента: '))].magic()

    def save_to_file(self):
        pickle.dump(self._students, open(os.path.join(os.path.abspath(__name__).replace('.st17.group', '/st17'), 'group.p'), 'wb'))
        print('Список сохранен')

    def load_from_file(self):
        self._students = pickle.load(open(os.path.join(os.path.abspath(__name__).replace('.st17.group', '/st17'), 'group.p'), 'rb'))
        print('Список загружен')
