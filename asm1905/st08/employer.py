from simple import simple

class employer(simple):
    def input_inf(self):
        self._departament = str(input('В каком департмаенте работает: '))

    def edit_inf(self):
        new_departament = input('Перевод в другой департамент: ')
        self._departament = str(new_departament) if new_departament else self._departament

    def special(self):
        _addpay = int(input('Выплатить премию:'))
        self._pay += _addpay if _addpay else self._pay
        print("В этом месяце будет премия")

    def print_inf(self):
        print('\nРаботник')
        print(f'Департамент: {self._departament}')
