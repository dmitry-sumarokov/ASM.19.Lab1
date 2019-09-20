from .Worker import Worker
from random import randint


class Specialist(Worker):
    def do_init(self):
        self._deadline = int(input('Введите количество дней до дедлайна: '))

    def do_edit(self):
        new_deadline = input('Введите количество дней до дедлайна: ')
        self._deadline = int(new_deadline) if new_deadline else self._deadline

    def do_magic(self):
        rand = randint(-42, 0)
        self._deadline = self._deadline + rand if self._deadline + rand > 0 else 0
        ret=''
        if rand == 0 and self._deadline > 0:
            ret += 'Корпоратив прошел удачно, сроки сдвинулись\n'
        elif self._deadline==0:
            ret += 'Срочно, срочно за бугор\n'
        else:
            ret += 'Отлично прокрастинируем, отмазку придумаем потом\n'
        ret += 'Дней до дедлайна: {0}'.format(self._deadline)
        return(ret)

    def do_print(self):
        return('Должность: Специалист\nДней до дедлайна: {0}'.format(self._deadline))


