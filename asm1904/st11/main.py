from .Organization import *
from .Menu import *
import os

organization = Organization()


def create_menu():
    mainMenu = []
    mainMenu.append(MenuItem(1, "Добавить сотрудника", organization.addPerson))
    mainMenu.append(MenuItem(2, "Добавить руководителя", organization.addDirector))
    mainMenu.append(MenuItem(3, "Изменить информацию о сотруднике", organization.updatePerson))
    mainMenu.append(MenuItem(4, "Удалить сотрудника из списка", organization.deletePerson))
    mainMenu.append(MenuItem(5, "Вывести список персонала", organization.showList))
    mainMenu.append(MenuItem(6, "Сохранить список персонала в файл", organization.writeToFile))
    mainMenu.append(MenuItem(7, "Загрузить список персонала из файла", organization.readFromFile))
    mainMenu.append(MenuItem(8, "Очистить список", organization.clearList))
    mainMenu.append(MenuItem(0, "Выйти", None))
    return mainMenu


def show_menu(mainMenu):
    for item in mainMenu:
        print('{} -> {}'.format(item.id, item.label))

	
def main():
    mainMenu = create_menu()
    id_list = [item.id for item in mainMenu]
    while True:
        show_menu(mainMenu)
        try:
            selected_id = int(input())
            if selected_id not in id_list:
                raise ValueError
            if selected_id == 0:
                return
            os.system('cls')
            mainMenu[selected_id - 1].function()
            print("\nНажмите Enter для возврата в меню...")
            input()
            os.system('cls')
        except ValueError:
            print("\nУказано не корректное значение\n")
        except EOFError:
            print("\nФайл со списком персонала пуст\n")
			

if __name__ == '__main__':
    main()
