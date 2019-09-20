from .Worker import Worker
from random import randint


class Engeneer(Worker):
    def do_init(self):
        self._vac = int(input('Введите количетво выходных дней: '))

    def do_edit(self):
        _vac = input('Введите количетво выходных дней: ')
        self._vac = int(new_vac) if new_vac else self._vac

    def do_magic(self):
        rand = randint(-2, 5)
        self._vac += rand
        ret=''
        if rand < 0:
            ret += 'Вы забыли сделать бэкап в пятницу, а Ниночке из бухгалтерии было просто необходимо зарядить свой айфон пока она строила глазки нашему новому стажеру\n'
        else:
            ret += 'Идея нанять в коллценр картавого Никиту Еремина помогла хоть как-то нормировать рабочий график\n'
        ret += 'Отпуск через 100500 лет, длительностью {0} дней'.format(self._vac)
        return(ret)

    def do_print(self):
        return('Должность: Инженер\nОтпуск через 100500 лет, длительностью {0} дней'.format(self._vac))


