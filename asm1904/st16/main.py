if __name__ == '__main__':
    from shop import shop
else:
    from .shop import shop

#from shop import Shop

shop = Shop()

menu = {"1": ("Add Mobile phone", shop.insert_MobilePhone),
        "2": ("Add Smart phone", shop.insert_SmartPhone),
        "3": ("Edit phone", shop.edit_phone),
        "4": ("Delete phone", shop.delete_phone),
        "5": ("Show phones", shop.display_shop),
        "6": ("Write shop to file", shop.write_to_file),
        "7": ("Read shop from file", shop.read_from_file),
        "8": ("Clear shop", shop.clear_shop),
        "9": ("Exit", "")
    }

def main():
    while True:
        for i in menu:
            print(i,": ", menu[i][0])
        k = input("Enter the number of command:")
        if k.isdigit():
            if int(k) <= len(menu):
               if int(k) == 9:
                   break
               else:
                   menu[k][1]()
            else:
                print("Number is out of range!")
        else:
            print("You should enter the NUMBER!")

if __name__ == "__main__":
    main()
            
        
