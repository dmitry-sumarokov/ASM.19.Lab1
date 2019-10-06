from .simple import simple

class manager(simple):
    def input_inf(self):
        self._employers_count = int(input('Сколько людей в подчинении: '))

    def edit_inf(self):
        new_employers_count = int(input('Кол-во нанятых/уволенных: '))
        self.employers_count= int(new_employers_count) if new_employers_count else self._employers_count

    def special(self):
        addpay = int(input('1 - успешный квартал, 0 - неуспешный: '))
        if addpay == 1:
            self._pay *= 1.5
            print("В этом месяце будет премия")
        else:
            print("В этом месяце без премии")

    def print_inf(self):
        print('\nManager')
        print(f'Кол-во подчиненных: {self._employers_count}')
