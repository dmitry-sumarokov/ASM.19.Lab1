from .Person import *

class Director(Person):
    def write(self):
        super().write()
        self.staff=input("Сотрудников в подчинении: ")
        self.departament=input("Структурное подразделение: ")

    def __str__(self):
        return 'Руководитель:\n Имя: %s\n Фамилия: %s\n Стаж работы: %s\n Заработная плата: %s\n Сотрудников в подчинении: %s\n Структурное подразделение: %s\n' %(self.firstname, self.lastname, self.experience, self.salary, self.staff, self.departament)
