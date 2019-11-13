if __name__ == '__main__':
    from library import library
else:
    from .library import library

#from .Human import group

library=library()

def main():
    menu = {"1":("Добавить книгу", library.insertBook),
        "2":("Добавить журнал", library.insertJournal),
        "3":("Добавить газету", library.insertNewspaper),        
        "4":("Редактировать", library.edit),
        "5":("Удалить", library.delete),
        "6":("Показать", library.show),
        "7":("Считать из файла", library.readfile),
        "8":("Записать в файл", library.writefile),
        "9":("Очистить", library.clean),
        "10":("Выход", None)}
    while True:
        print('')
        print('Меню:')
        for k in range(1,11):
            print(k, " : ", menu[str(k)][0])
        x = input()
        if int(x)==10:
            break
        if int(x) >= 1 and int(x) < 12:
            menu[x][1]()
        else:
            print('Error')
        


if __name__ == '__main__':
	main()


