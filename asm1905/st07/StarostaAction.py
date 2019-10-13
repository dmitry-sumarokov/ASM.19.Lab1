from .StudentAbstract import StudentAbs


class StarostaAction(StudentAbs):

    def __init__(self):
        super(StarostaAction, self).__init__()
        self.student_kind = 'Староста'
        self.salary = 0

    def do_input(self):
        super(StarostaAction, self).do_input()
        self.salary = input('Надбавка к стипендии: ')
        return self

    def do_print(self):
        super(StarostaAction, self).do_print()
        print('Надбавка к стипендии: ' + str(self.salary))
        pass

    def do_edit(self):
        self.do_input()

    def do_magic(self):
        print('отметить прогульщиков (Д/н): ')
        pass
