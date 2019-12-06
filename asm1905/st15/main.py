if __name__ == '__main__':
    from group import group
else:
    from .group import group

#from .Worker import group

group=group()

def main():
    menu = {"1":("Добавить механика", group.insertMechanic),
        "2":(" Добавить главного инженера", group.insertMainEngineer),
        "3":("Добавить охранника", group.insertSecurity),        
        "4":("Специальное действие", group.execute),
        "5":("Добавить действие", group.edit),
        "6":("Удалить", group.delete),
        "7":("Показать список", group.show),
        "8":("Прочитать из файла", group.readfile),
        "9":("Записать в файл", group.writefile),
        "10":("Очистка", group.clean),
        "11":("Выход", None)}
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