from Earth import Earth
if __name__ == '__main__':
    from group import group
else:
    from .group import group

Earth = Earth()
print('Добро пожаловать в лабораторию создания человеков, от нелюдей для людей')
Main_menu = [
    ['Добавить человека (создать запись)', Earth.add_humans],
    ['Изменить особенности человека (изменить запись)',Earth.edit_humans],
    ['Выслать смерть за одним человеком (удалить запись по id)', Earth.delete_humans],
    ['Уничтожить человечество (удалить все записи)', Earth.delete_all],
    ['Заставить правителей провести перепись населения (показать все записи)', Earth.show_humans],
    ['Отнести данные переписи населения в всемирную библиотеку (экспорт)', Earth.save_humans],
    ['Импортировать новое поколение из файла (импорт)', Earth.load_humans]
]

def menu():
    print()
    for i, item in enumerate(Main_menu):
        print(f'{i}. {item[0]}')
    print()
    return int(input('Выберите пункт меню: '))

def main():
    group().f()
    try:
        while True:
            Main_menu[menu()][1]()
    except Exception as e:
        print(e, 'Выход', sep='\n')

if __name__ == '__main__':
	main()    






