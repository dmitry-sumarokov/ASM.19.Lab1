class Behavior:

    def __init__(self):
        pass

    def edit(self):
        print('Если нужно оставить неизменным, нажмите Enter без ввода значения')
        new_name = input('Введите новое имя: ')
        self.name = new_name if new_name else self.name
        new_surname = input('Введите новую фамилию: ')
        self.surname = new_surname if new_surname else self.surname
        new_age = input('Введите новый возраст: ')
        self.age = int(new_age) if new_age else self.age
        new_wexp = input('Введите новый стаж работы: ')
        self.wexp = int(new_wexp) if new_wexp else self.wexp

    def print(self):
        print('------------')
        print(f'Имя: {self.name}',
              f'Фамилия: {self.surname}',
              f'Возраст: {self.age}',
              f'Стаж: {self.wexp}', sep='\n')
        

