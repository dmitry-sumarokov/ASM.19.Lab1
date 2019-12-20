class Behavior:
    
    def __init__(self):
        pass
    
    def edit(self):
        print('Если нужно оставить неизменным, нажмите Enter без ввода значения')
        new_name = input('Введите новое название: ')
        self.name = new_name if new_name else self.name
        new_material = input('Введите новый материал: ')
        self.material = new_material if new_material else self.material
        new_price = input('Введите новую стоимость: ')
        self.price = int(new_price) if new_price else self.price

    def print(self):
        print('------------')
        print(f'Название: {self.name}',
              f'Материал: {self.material}',
              f'Стоимость: {self.price}')