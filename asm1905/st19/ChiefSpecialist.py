from .Worker import Worker
from random import randint


class ChiefSpecialist(Worker):
    def do_init(self):
        self._share = int(input('Введите ставку отката: '))

    def do_edit(self):
        new_share = input('Введите ставку отката: ')
        self._share = int(new_share) if new_share else self._share

    def do_magic(self):
        rand = randint(0, 210)
        self._share = rand
        ret=''
        if rand == 0:
            ret += 'Вас поймал шеф, придется залечь на дно\n'
        else:
            ret += 'Удачная сделка с афганскими ребятами\n'
            self._share += 100
        ret += 'Откат составляет {0}% от месячного дохода'.format(self._share)
        return(ret)

    def do_print(self):
        return('Должность: Главный специалист\nОткат составляет {0}% от месячного дохода'.format(self._share))


