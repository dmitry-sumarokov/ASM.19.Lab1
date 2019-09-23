# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:55:36 2019

@author: alena
"""

if __name__ == '__main__':
    from .team import team
else:
    from .team import team


team=team()

"""def main():    
    print("Menu")
    print("1. Analyst")
    print("2. Developer")
    print("3. Tester") 
    print("4. Show")
    print("5. Clear")
    print("6. Save")
    print("7. Edit")
    print("8. Special")
    print("9. Download")    
    print("0. Exit")
    choice = input(" >>  ")
    menu(choice)

def menu(choice):
    try:
        menu_actions[choice](team)
    except KeyError:
        print("Error")
    if choice != '0':       
        menu_actions['main']()

menu_actions = {
    'main': main,
    '1': team.insertAnalyst,
    '2': team.insertDeveloper,
    '3': team.insertTester,
    '4': team.show,
    '5': team.clean,
    '6': team.writefile,
    '7': team.edit,
    '8': team.execute,
    '9': team.readfile
}"""
def main():
    menu = {"1":("Analyst", team.insertAnalyst),
        "2":("Developer", team.insertDeveloper),
        "3":("Tester", team.insertTester),        
        "4":("Edit", team.edit),
        "5":("Delete", team.delete),
        "6":("Show", team.show),
        "7":("Read", team.readfile),
        "8":("Save", team.writefile),
        "9":("Clear", team.clean),
        "10":("Special", team.special),
        "11":("Exit", None)}
    while True:
        print('')
        print('Меню:')
        for k in range(1,12):
            print(k, " : ", menu[str(k)][0])
        x = input()
        if int(x)==11:
            break
        if int(x) >= 1 and int(x) < 12:
            menu[x][1]()
        else:
            print('Error')
        
        
if __name__ == '__main__':
	main()


