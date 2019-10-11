if __name__ == '__main__':
    from MobilePhone import MobilePhone
else:
    from .MobilePhone import MobilePhone

if __name__ == '__main__':
    from SmartPhone import SmartPhone
else:
    from .SmartPhone import SmartPhone
    
import pickle

class Shop:
    
    shop = []
    
    def __init__(self):
        pass
        
    def insert_MobilePhone(self):
        mobile_phone = MobilePhone()
        len1 = len(self.shop)
        self.shop.append(mobile_phone)
        len2 = len(self.shop)
        if len1<len2:
            print("MobilePhone successfully added!")
        else:
            print("Error!")

    def insert_SmartPhone(self):
        smart_phone = SmartPhone()
        len1 = len(self.shop)
        self.shop.append(smart_phone)
        len2 = len(self.shop)
        if len1<len2:
            print("SmartPhone successfully added!")
        else:
            print("Error!")

    def edit_phone(self):
        if self.shop:
            self.display_shop()
            k = int(input("Enter the number of phone for editing:"))
            if k > len(self.shop):
                print("Number out of range!")
            else:
                self.shop[k-1].set_data()
        else:
            print("There is no phone in the shop!") 

    def delete_phone(self):
        if self.shop:
            self.display_shop()
            k = int(input("Enter the number of phone for deleting:"))
            if k > len(self.shop):
                print("Number out of range!")
            else:   
                self.shop.pop(k-1)
                print("Phone number ", k, " was deleted!")
        else:
            print("There is no phone in the shop!")
        
    def display_shop(self):
        if not self.shop:
            print("There is no phone in the shop!")
        else:    
            for i in range (0, len(self.shop)):
                print("Phone number ", i+1)
                self.shop[i].display_data()

    def read_from_file(self):
        file = open('mobile_phone_shop.dat', 'rb')
        self.shop = pickle.load(file)
        #if pickle.UnpicklingError:
            #print("Error!")
       # else:    
        print("Success!")
        file.close()

    def write_to_file(self):
        file = open('mobile_phone_shop.dat', 'wb')
        pickle.dump(self.shop, file)
        #if pickle.PicklingError:
         #   print("Error!")
        #else:        
        print("Success!")
        file.close()    
            
    def clear_shop(self):
        self.shop.clear()
        print("Shop is empty!")
        
