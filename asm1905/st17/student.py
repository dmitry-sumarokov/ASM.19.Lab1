from abc import ABC


class Student(ABC):

    def __init__(self, type_student, behavior):
        self._student = type_student
        self._behavior = behavior
        self.input_info()

    def input_info(self):
        self._behavior.do_input(self._student)

    def print_info(self):
        self._behavior.do_print(self._student)

    def edit_student(self):
        self._behavior.do_edit(self._student)

    def magic(self):
        self._behavior.do_magic(self._student)
