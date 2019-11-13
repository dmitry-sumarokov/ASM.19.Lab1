class OS:
    def input(self):
        return 0

class NoOS(OS):
    def input(self):
        print("Mobile phone does not have an operating system")
        return "NoOS"


class WithOS(OS):
    def input(self):
        return input("Enter the name of operating system:")
