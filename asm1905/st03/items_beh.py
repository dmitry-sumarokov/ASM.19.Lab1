from behavior import Behavior

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