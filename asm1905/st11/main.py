# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:55:36 2019

@author: alena
"""

if __name__ == '__main__':
    from .team import team
else:
    from .team import team

EXIT_CODE = "11"
team=team()

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
    EXIT_CODE: ("Exit", None)
    }

def main():
    while True:
        for key in menu:
            print(key + " " + menu[key][0])
        try:
            user_input = input(">>")
            if user_input == EXIT_CODE:
                break
            else:
                menu[user_input][1]()

        except Exception as ex:
            print("Exception raised: ", ex)
            
            
    
        
if __name__ == '__main__':
	main()


