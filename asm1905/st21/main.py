from .scrumTeam import team
from colorama import init
from colorama import Fore, Style


# - данные сохраняются с помощью модуля pickle.

def getMenuInput():
    for i, key in enumerate(MENU):
        print(Fore.YELLOW + str(i) + ') ' + key[0])
    response = ''

    while not response.isdigit():
        response = input(Fore.BLUE + 'Please, input your choice:')

    return response


MENU = [
    ['See menu', getMenuInput],
    ['See list of employees', 'lala'],
    ['Add employee', 'omega'],
    ['Edit employee', 'gamma'],
    ['Fire employee', 'assadasd'],
    ['Export to file', 'adasd'],
    ['Import from file', 'ds']
]


def main():
    init(autoreset=True)
    print(Fore.MAGENTA + '~~~ You were accepted as head of our HR Departament! ~~~')
    print(Fore.CYAN + 'Feel free to change/add/delete positions')
    getMenuInput()

    try:
        while 1:
            print(MENU[int(getMenuInput())])
    except Exception as e:
        print(Fore.MAGENTA + e + ' YOU DIED ')

    # team().f()


if __name__ == '__main__':
    main()
