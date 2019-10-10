if __name__ == '__main__':
    from group import group
else:
    from .group import group

gr=group()

Menu = [
            ["0 - Выход", None],  
            ["1 - Добавить объект типа 'студент'", gr.addStudent],
            ["2 - Добавить объект типа 'староста'", gr.addStarosta],        
            ["3 - Добавить объект типа 'профорг'", gr.addProforg],
            ["4 - Вывести список учеников", gr.show_list],
            ["5 - Изменить данные ученика", gr.change],
            ["6 - Удалить ученика из списка группы", gr.delete_card],
            ["7 - Сохранить список группы в файл", gr.write_file],
            ["8 - Считать список группы из файла", gr.read_file]
        ]

def menu():
    print()
    print("Меню программы:")
    for i, item in enumerate(Menu):
        print(f'{item[0]}')
    print()
    
    return int(input('Введите номер пункта меню: '))

def main():
    try:
        while True:
            Menu[menu()][1]()
    except Exception as e:
        print(e, 'Пока!')

if __name__ == '__main__':
	main()
