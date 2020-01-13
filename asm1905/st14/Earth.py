import pickle
from .CreateHuman import man, woman

class Earth:

    def __init__(self):
        print('Добро пожаловать в конфигуратор человеков')
        self.menu = [
            ['Добавить мужчину', man],
            ['Добавить женщину', woman],
        ]
        self.humans = []

    def add_humans(self):
        print()
        for i, item in enumerate(self.menu):
            print(f'{i} - {item[0]}')
        print()
        num = int(input('Введите номер человека: '))
        self.humans.append(self.menu[num][1]())

    def edit_humans(self):
        for i, humans in enumerate(self.humans):
            print(humans.__class__.__name__+'[id: '+str(i)+']')
        self.humans[int(input('Введите номер человека: '))].edit()
        print('--------------------')
        print('Изменения сохранены')

    def delete_humans(self):
        self.humans.pop(int(input('Введите номер человека: ')))

    def delete_all(self):
        self.humans.clear()
        print(' \n \n Метеорит вылетел \n . \n . \n . \n . \n . \n . \n Прилетел')

    def show_humans(self):
        for i, humans in enumerate(self.humans):
            print()
            print(humans.__class__.__name__+'[id:'+str(i)+']')
            humans.print()

    def save_humans(self):
        f = open(r'data.txt', 'wb')
        pickle.dump(self.humans, f)
        f.close()
        print('Список сохранен')

    def load_humans(self):
        f = open(r'data.txt', 'rb')
        self.humans = pickle.load(f)
        print('Список загружен')
