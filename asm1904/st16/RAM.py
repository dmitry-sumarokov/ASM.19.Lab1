class RAM:
    def input(self):
        return 0

class ConstRAM(RAM):
    def input(self):
        print("Mobile phone always has 16MB of RAM")
        return "16MB"


class EnterRAM(RAM):
    def input(self):
        return input("Enter amount of RAM:")
