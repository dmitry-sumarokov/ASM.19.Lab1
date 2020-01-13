from .StudentAbstract import StudentAbs


class ProforgAction(StudentAbs):

    def __init__(self):
        super(ProforgAction, self).__init__()
        self.student_kind = 'Профорг'
        self.group_number = ''

    def do_input(self):
        super(ProforgAction, self).do_input()
        self.group_number = input('Номер группы: ')
        return self

    def do_print(self):
        super(ProforgAction, self).do_print()
        print('Номер группы: ' + str(self.group_number))
        pass

    def do_edit(self):
        self.do_input()

    def do_magic(self):
        print('Собрать проф. билеты (Д/н): ')
        pass
