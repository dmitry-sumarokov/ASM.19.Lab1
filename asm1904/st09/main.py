if __name__ == '__main__':
    from association import association
else:
    from .association import association

#from .Creative import association

association=association()

def main():
    menu = {"1":("Добавить художника", association.insertArtist),
        "2":(" Добавить писателя", association.insertWriter),
        "3":("Добавить поэта", association.insertPoet),
        "4":("Специальное действие", association.execute),
        "5":("Добавить действие", association.edit),
        "6":("Удалить", association.delete),
        "7":("Показать список", association.show),
        "8":("Прочитать из файла", association.readfile),
        "9":("Записать в файл", association.writefile),
        "10":("Очистка", association.clean),
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
            print('Ошибка: неправильный ввод')



if __name__ == '__main__':
	main()
