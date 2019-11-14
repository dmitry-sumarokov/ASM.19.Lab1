from .StudentAbstract import StudentAbs


class StudentAction(StudentAbs):

    def __init__(self):
        super(StudentAction, self).__init__()
        self.student_kind = 'Cтудент'
        self.absent = ''

    def do_input(self):
        super(StudentAction, self).do_input()
        self.absent = input('Кол-во пропусков: ')
        return self

    def do_print(self):
        super(StudentAction, self).do_print()
        print('Кол-во пропусков: ' + str(self.absent))
        pass

    def do_edit(self):
        self.do_input()

    def do_magic(self):
        print('Прогулять пару (Д/н): ')
        pass
