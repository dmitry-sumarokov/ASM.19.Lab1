from . import behaviour


class Tea:

    def __str__(self):
        return f"{self.type.ljust(20)} {self.form.ljust(20)} {self.var.ljust(20)}"

    def set_behaviour(self, beh):
        self._behaviour = beh()

    def behaviour(self):
        return self._behaviour.action()

    def set(self):
        self.type = input("Тип: ")
        self.form = input("Формат: ")

    def update(self):
        new_type = input("Тип: ")
        new_form = input("Формат: ")
        self.type = new_type or self.type
        self.form = new_form or self.form


class ChineseTea(Tea):
    var = "chinese"

    def __init__(self):
        self.set_behaviour(behaviour.Chinese_Tea_Behaviour)


class IndianTea(Tea):
    var = "indian"

    def __init__(self):
        self.set_behaviour(behaviour.Indian_Tea_Behaviour)
