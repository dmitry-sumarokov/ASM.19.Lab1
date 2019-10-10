if __name__ == '__main__':
    from workers import workers 
else:
    from .workers import workers 

#from .Human import workers 

workers=workers()

def main():
    menu = {"1":("Добавить бурильщика", workers.insertDriller),
        "2":("Добавить геолог", workers.insertGeologist),
        "3":("Добавить разработчика", workers.insertDeveloper),        
        "4":("Особое действие", workers.execute),
        "5":("Редактировать", workers.edit),
        "6":("Удалить", workers.delete),
        "7":("Показать", workers.show),
        "8":("Считать из файла", workers.readfile),
        "9":("Записать в файл", workers.writefile),
        "10":("Очистить", workers.clean),
        "11":("Выход", None)}
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
            print('Некорректный ввод')
        


if __name__ == '__main__':
	main()


