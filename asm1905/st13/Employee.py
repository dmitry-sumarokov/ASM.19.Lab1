from abc import ABC


class Employee(ABC):
    def __init__(self):
        self.nickname = ''
        self.exp = 0
        self.sex = ''
        self.age = 0

    def enter_emp_params(self):
        pass

    def print_emp_params(self):
        pass

    def print_emp_brief(self):
        pass

    def alter_emp_params(self):
        pass

    def emp_special_action(self):
        pass
