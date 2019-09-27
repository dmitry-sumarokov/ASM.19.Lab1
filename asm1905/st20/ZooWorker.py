from random import randint

class ZooWorker():
    Behaviour = None
    AbilityDisplay = None
    
    def __init__(self):
        self.Name = ''
        self.Surname = ''
        self.Age = ''
        self.Gender = ''
        self.Position = ''

    def SetBehaviour(self, Behaviour, AbilityDisplay):
        self.Behaviour = Behaviour
        self.AbilityDisplay = AbilityDisplay

    def Do(self):
        self.Behaviour.Do_something(self)

    def Read (self):
        self.AbilityDisplay.Read(self)

    def Write (self):
        self.AbilityDisplay.Write(self)

class Behaviour_DirectorZoo():
        def Do_something(self, ZooWorker):
            Animals = ['слона', 'пантеру', 'крокодила', 'ламу', 'обезьянку', 'бегемота']
            newAnimals = Animals[randint(0, 5)]
            print('\n Внимание посетителям! Нам есть что показать! Недавно мы привезли ', newAnimals, '!!!','\n')
            
class Behaviour_SecurityZoo():
        def Do_something(self, ZooWorker):
            print('\n Купание запрещено - вольер с крокодилами! Кто у крокодилов утонет, тот больше купаться не будет!')
    
class Behaviour_KeeperZoo():
        def Do_something(self, ZooWorker):
            print('\n SOOOOOOOOOOOOOOS! Бегемот сбежал! Кто-нибудь видел бегемота?')
    
class Behaviour_IceCreamSellerZoo():
        def Do_something(self, ZooWorker):
            IceCream_menu = ['ванильное', 'шоколадное', 'клубничное', 'фисташковое', 'малиновое', 'банановое']
            IceCream = IceCream_menu[randint(0, 5)]
            print('\n Держите Ваше ', IceCream, ' мороженое!','\n')

class A_Display():
    def Read(self, ZooWorker):
        ZooWorker.Name = input("Введите имя сотрудника: \n")
        ZooWorker.Surname = input("Введите фамилию сотрудника: \n")
        ZooWorker.Age = input("Введите возраст сотрудника: \n")
        while ZooWorker.Age.isdigit()==0:
            print('Что-то пошло не так, введите количество полных лет числом.')
            ZooWorker.Age = input("Введите возраст сотрудника: \n")
        ZooWorker.Gender = input("Введите пол сотрудника: \n")
        ZooWorker.Position = input("Введите точную должность сотрудника: \n")
        
    def Write(self, ZooWorker):
        print(ZooWorker.Name, ZooWorker.Surname, ZooWorker.Age, ZooWorker.Gender, ZooWorker.Position)


class DirectorZoo(ZooWorker):
    def __init__(self):
        self.SetBehaviour(Behaviour_DirectorZoo(), A_Display())
        
class SecurityZoo(ZooWorker):
    def __init__(self):
        self.SetBehaviour(Behaviour_SecurityZoo(),A_Display())
        
class KeeperZoo(ZooWorker):
    def __init__(self):
        self.SetBehaviour(Behaviour_KeeperZoo(),A_Display())
        
class IceCreamSellerZoo(ZooWorker):
    def __init__(self):
        self.SetBehaviour(Behaviour_IceCreamSellerZoo(),A_Display())

