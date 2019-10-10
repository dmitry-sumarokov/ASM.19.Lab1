if __name__ == '__main__':
    from group import group
else:
    from .group import group

#from .Human import group

group=group()
 
def main():
    menu = {"1":("Add Engineer", group.insertEngineer),
        "2":("Add Specialist", group.insertSpecialist),
        "3":("Add Department", group.insertDepartment),        
        "4":("Special action", group.execute),
        "5":("Edit", group.edit),
        "6":("Delete", group.delete),
        "7":("Show", group.show),
        "8":("Read in file", group.readfile),
        "9":("Write in file", group.writefile),
        "10":("Clean", group.clean),
        "11":("Exit", None)}
    while True:
        print('')
        print('Menu:')
        for k in range(1,12):
            print(k, " : ", menu[str(k)][0])
        x = input()
        if int(x)==11:
            break
        if int(x) >= 1 and int(x) < 12:
            menu[x][1]()
        else:
            print('Error: incorrect input')
        


if __name__ == '__main__':
	main()

