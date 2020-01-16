from .Market import Market

class Department(Market):
    def __init__(self):
        super().__init__()
        self._namedept = None
        self._product= None

    def console_input(self):
        super().console_input()
        self._namedept = input("Название отдела: ")
        self._product = input("Вид продута: ")

    def console_output(self):
        super().console_output()
        print("Название отдела: " + self._namedept)
        print("Вид продута: " + self._product)

    def edit(self):
        super().edit()
        self._namedept = input("Новый отдел: ")
        self._product = input("Новый продутк: ")