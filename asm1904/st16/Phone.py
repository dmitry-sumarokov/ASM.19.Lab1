class Phone:

    OS = None
    RAM = None

    def __init__(self):
        self.set_data()

    def set_data(self):
        self.brand = input("Enter the brand of phone:")
        self.screen_size = input("Enter the screen size of phone:")
        self.housing_type = input("Enter the phone housing type:")
        self.os = self.OS.input()
        self.ram = self.RAM.input()

    def display_data(self):
        print(self.brand, self.screen_size, self.housing_type, self.os, self.ram)