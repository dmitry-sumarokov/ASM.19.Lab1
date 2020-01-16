import os
import pickle
from .Stores import Stores

stores = Stores()
EXIT_CODE = "9"

menu = {
    "1": ("Добавить магазин", stores.add_market),
    "2": ("Добавить отдел", stores.add_department),
    "3": ("Удалить магазин", stores.remove_dept),
    "4": ("Изменить магазин", stores.edit_dept),
    "5": ("Показать все магазины и отделы", stores.print_staff),
    "6": ("Записать название в файл", stores.write_to_file),
    "7": ("Выбрать из файла", stores.read_from_file),
    "8": ("Удалить все", stores.clear_staff),
    EXIT_CODE: ("Выход", None)
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
            print("Указано не корректное значение: ", ex)

if __name__ == '__main__':
    main()