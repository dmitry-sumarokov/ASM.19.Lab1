from .Worker import Worker

class Context():

    def __init__(self, worker: Worker):

        self._worker = worker

    def do_magic_logic(self):
        print(self._worker.do_magic())
    def do_add_worker(self):
        self._worker._first_name = input('Введите имя: ')
        self._worker._second_name = input('Введите фамилию: ')
        self._worker._gender = input('Введите пол: ')
        self._worker._age = int(input('Введите возраст: '))
        self._worker.do_init()

    def do_print(self,number):
        print('________________{0}_________________\nФамилия: {1}\nИмя: {2}\nПол: {3}\nВозраст: {4}\n{5}'.format(
                                number, self._worker._second_name, self._worker._first_name, self._worker._gender, self._worker._age, self._worker.do_print()))


    def do_edit(self):
        print('Если не хотите вносить изменения, оставьте поля пустыми')
        new_first_name = input('Введите имя: ')
        self._worker._first_name = new_first_name if new_first_name else self._worker._first_name
        new_second_name = input('Введите фамилию: ')
        self._worker._second_name = new_second_name if new_second_name else self._worker._second_name
        new_gender = input('Введите пол: ')
        self._worker._gender = new_gender if new_gender else self._worker._gender
        new_age = input('Введите возраст: ')
        self._worker._age = int(new_age) if new_age else self._worker._age 
        self._worker.do_edit()
      
