from .Worker import Worker
from random import randint

class Chief(Worker):
    def do_init(self):
        self._award = int(input('Введите коэффициент годовой премии: '))

    def do_edit(self):
        new_award = input('Введите коэффициент годовой премии: ')
        self._award = int(new_award) if new_award else self._award

    def do_magic(self):
        rand = randint(-10, 10)
        self._award += 10*rand
        ret=''
        if rand < 0:
            ret += 'Ваш подчиненный перепутал названия фирм поставщиков, вами заинтересовались органы\n'
        else:
            ret += 'Вы смогли наладить отношения с тегеранскими поставщиками\n'
        ret += 'Премия составляет {0}% от годового дохода'.format(self._award)
        return(ret)

    def do_print(self):
        return('Должность: Начальник\nПремия составляет {0}% от годового дохода'.format(self._award))

