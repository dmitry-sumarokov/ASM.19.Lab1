from MobilePhone import MobilePhone

class SmartPhone(MobilePhone):

    def __init__(self):
        self.set_data()
        
    def set_data(self):
        MobilePhone.set_data(self)
        self.os = input("Enter the name of operating system:")
        self.ram = input("Enter amount of RAM:")
        
    def display_data(self):
        print(self.brand, self.screen_size, self.housing_type, self.os, self.ram)
    
        
