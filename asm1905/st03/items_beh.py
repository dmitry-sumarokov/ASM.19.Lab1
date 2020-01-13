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

class Table_beh():

    def init(self):
        pass

    def edit(self):
        Behavior.edit(self)
        new_high = input('Введите новую высоту: ')
        self.high = int(new_high) if new_high else self.high

    def print(self):
        Behavior.print(self)
        print(f'Высота: {self.high}')

class Bed_beh():

    def init(self):
        pass

    def edit(self):
        Behavior.edit(self)
        new_width = input('Введите новую ширину: ')
        self.width = int(new_width) if new_width else self.width

    def print(self):
        Behavior.print(self)
        print(f'Ширина: {self.width}')        

class Wardrobe_beh():

    def init(self):
        pass

    def edit(self):
        Behavior.edit(self)
        new_doors = input('Введите новое количество дверей: ')
        self.doors = int(new_doors) if new_doors else self.doors

    def print(self):
        Behavior.print(self)
        print(f'Кол-во дверей: {self.doors}')        
