from item import Item
from items_beh import Table_beh, Bed_beh, Wardrobe_beh

class Table(Item):

    def __init__(self):
        super().__init__()
        self.high = input('Введите высоту: ')

    def edit(self):
        Table_beh.edit(self)

    def print(self):
        Table_beh.print(self)

class Wardrobe(Item):

    def __init__(self):
        super().__init__()
        self.doors = input('Введите количество дверей: ')

    def edit(self):
        Wardrobe_beh.edit(self)

    def print(self):
        Wardrobe_beh.print(self)

class Bed(Item):

    def __init__(self):
        super().__init__()
        self.width = input('Введите ширину: ')

    def edit(self):
        Bed_beh.edit(self)

    def print(self):
        Bed_beh.print(self)        