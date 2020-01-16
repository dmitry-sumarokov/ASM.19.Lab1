# Класс описывающий элемент картотеки "Магазин"

class Market:
    def __init__(self): #атрибут описывающий эелементы
        self._name = None
        self._nameowner = None
        self._area = None

    def console_input(self):
        self._name = input("Название магазина: ")
        self._nameowner = input("Имя владельца магазина: ")
        self._area = input("Район: ")

    def console_output(self):
        print("Название магазина: " + self._name)
        print("Имя владельца магазина: " + self._nameowner)
        print("Район: " + self._area)

    def edit(self):
        self._name = input("Другой магазин: ")
        self._nameowner = input("Другое имя владельца: ")
        self._area = input("Другой район: ")