class Person:
    def write(self):
        self.firstname=input("Имя: ")
        self.lastname=input("Фамилия: ")
        self.experience=input("Стаж работы: ")
        self.salary=input("Заработная плата: ")

    def __str__(self):
        return 'Сотрудник:\n Имя: %s\n Фамилия: %s\n Стаж работы: %s\n Заработная плата: %s\n' %(self.firstname, self.lastname, self.experience, self.salary)
