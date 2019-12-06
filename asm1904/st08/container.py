import pickle
from os import path

from . import tea as _tea


class Container:

    _database = "asm1904/st08/database.dat"

    def __init__(self):
        self._list = []
        self.tea = [_tea.ChineseTea, _tea.IndianTea]

    def show(self):
        if len(self._list) != 0:
            print("ID".ljust(5) + "Тип".ljust(20) + "Формат".ljust(20) + "Происхождение".ljust(20))
            for k, v in enumerate(self._list, start=1):
                print(f"{str(k).ljust(5)} {v}")

    def add_new(self):
        try:
            t = int(input("1 Китайский чай\n2 Индийскйи чай\n> "))
            tea = self.tea[t - 1]()
            tea.set()
            self._list.append(tea)
        except (IndexError, KeyError):
            print(f"\nНет такого номера в списке.\n")

    def edit(self):
        if len(self._list) != 0:
            self.show()
            try:
                t = int(input("Номер записи: "))
                self._list[t - 1].update()
            except (ValueError, IndexError):
                print(f"\nНет такого номера в списке.\n")

    def behaviour(self):
        if len(self._list) != 0:
            self.show()
            try:
                t = int(input("Номер записи: "))
                print(self._list[t - 1].behaviour())
            except (ValueError, IndexError):
                print(f"\nНет такого номера в списке.\n")

    def delete(self):
        if len(self._list) != 0:
            self.show()
            try:
                t = int(input("Номер записи: "))
                del self._list[t - 1]
            except (ValueError, IndexError):
                print(f"\nНет такого номера в списке.\n")

    def clear(self):
        self._list.clear()

    def save_list(self):
        with open(self._database, "wb") as f:
            pickle.dump(self._list, f)

    def laod_list(self):
        if path.exists(self._database):
            with open(self._database, "rb") as f:
                self._list = pickle.load(f)
