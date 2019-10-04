from abc import ABC, abstractmethod
import pickle
from enum import Enum

from Basic import Basic
from Student import Student
from Headman import Headman
from Container import Container

element_type = Enum('element_type', 'student headman')

class Console_menu():
    def __init__(self, cont):
        self.menu_main = {
            'Загрузить картотеку из файла': self.read_data,
            'Записать картотеку в файл': self.write_data,
            'Добавить объект в список': self.add_element,
            'Удалить объект из списка': self.del_element,
            'Редактировать объект списка': self.edit_element,
            'Отобразить объекты из списка': self.print_info,
            'Очистить список': self.clear,
            'Выход': self.exit
        }
        self.mc = cont

    def read_data(self):
        filename = input("Введите название файла: ")
        self.mc.read_data(filename)

    def write_data(self):
        filename = input("Введите название файла: ")
        self.mc.write_data(filename)

    def add_element(self):
        global element_type
        menu_add = {
            'Студент': element_type.student,
            'Староста': element_type.headman,
        }
        menu_array = []
        counter = 0
        for el in menu_add.keys():
            menu_array.append(el)
            counter += 1
            print(str(counter) + ". " + el)
        el = int(input("Выберите пункт меню: ")) - 1
        e_type = menu_add.get(menu_array[el])
        fio = input("Введите ФИО: ")
        age = input("Введите возраст: ")
        if(e_type == element_type.student):
            email = input("Введите email: ")
            element = Student(fio, age, email)
        elif(e_type == element_type.headman):
            tel_number = input("Введите номер телефона: ")
            element = Headman(fio, age, tel_number)
        self.mc.add_element(element)

    def edit_element(self):
        print("Оставьте поле пустым если не нужно изменять!\n")
        ids = int(input("Выберите элемент: "))
        idx = mc.find_index(ids)
        if(idx < 0):
            return
        el = mc.my_list[idx]
        fio = input("Введите ФИО: ")
        if(fio == ""):
            fio = mc.my_list[idx].fio
        age = input("Введите возраст: ")
        if(age == ""):
            age = mc.my_list[idx].age
        if(type(el).__name__ == "Student"):
            email = input("Введите email: ")
            if(email == ""):
                email = mc.my_list[idx].email
            element = Student(fio, age, email)
        elif(type(el).__name__ == "Headman"):
            tel_number = input("Введите номер телефона: ")
            if(tel_number == ""):
                tel_number = mc.my_list[idx].tel_number
            element = Headman(fio, age, tel_number)
        self.mc.edit_element(element, idx)

    def del_element(self):
        ids = int(input("Выберите элемент: "))
        self.mc.del_element(ids)

    def print_info(self):
        for el in self.mc.my_list:
            print()
            print("#" + str(el.ids))
            print("\tКатегория: " + el.type)
            print("\tФИО: " + el.fio)
            print("\tВозраст: " + str(el.age))
            if(type(el).__name__ == "Student"):
                print("\tЭл. почта: " + el.email)
            elif(type(el).__name__ == "Headman"):
                print("\tТелефон: " + el.tel_number)
        print()

    def clear(self):
        self.mc.clear()

    def exit(self):
        return 0;

    def user_menu(self):
        menu_array = []
        counter = 0
        for el in self.menu_main.keys():
            menu_array.append(el)
            counter += 1
            print(str(counter) + ". " + el)
        el = int(input("Выберите пункт меню: ")) - 1
        return self.menu_main.get(menu_array[el])()
