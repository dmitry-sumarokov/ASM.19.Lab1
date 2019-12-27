import pickle
from .products import Table, Wardrobe, Bed

class Shop:

    def __init__(self):
        self.menu = [
            ['Добавить шкаф', Wardrobe],
            ['Добавить кровать', Bed],
            ['Добавить стол', Table]
        ]
        self.store = []

    def add_store(self):
        print()
        for i, item in enumerate(self.menu):
            print(f'{i} - {item[0]}')
        print()
        num = int(input('Введите номер продукции: '))
        self.store.append(self.menu[num][1]())

    def edit_store(self):
        for i, store in enumerate(self.store):
            print(store.__class__.__name__+'[id: '+str(i)+']')
        self.store[int(input('Введите номер продукции: '))].edit()
        print('--------------------')
        print('Изменения сохранены')

    def delete_store(self):
        self.store.pop(int(input('Введите номер продукции: ')))

    def delete_all(self):
        self.store.clear()

    def show_store(self):
        for i, store in enumerate(self.store):
            print()
            print(store.__class__.__name__+'[id:'+str(i)+']')
            store.print()

    def save_store(self):
        f = open(r'data.txt', 'wb')
        pickle.dump(self.store, f)
        f.close()
        print('Список сохранен')

    def load_store(self):
        f = open(r'data.txt', 'rb')
        self.store = pickle.load(f)
        print('Список загружен')
