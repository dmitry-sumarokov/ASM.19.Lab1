class Edithuman:
    
    def __init__(self):
        pass
    
    def edit(self):
        print('Если не хотите менять судьбы людей, нажмите Enter животворящий')
        new_name = input('Введите новое Имя (человек побегает по МФЦ): ')
        self.name = new_name if new_name else self.name
        new_race = input('Введите новую расу, не знаю как, Майкл Джексон же смог: ')
        self.race = new_race if new_race else self.race
        new_age = input('Введите новую продолжительность жизни (возможно понадобится внезапный камаз): ')
        self.age = int(new_age) if new_age else self.age


    def print(self):
        print('------------')
        print(f'\n Имя: {self.name} \n Раса: {self.race} \n Продолжительность жизни: {self.age} \n')
        