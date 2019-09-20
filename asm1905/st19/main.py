if __name__ == '__main__':
    from group import Group
else:
    from .group import Group

cur_group = Group()

Menu_list = [
        ['Добавить сотрудника', cur_group.add_worker],
        ['Редактировать информацию о сотруднике', cur_group.change_worker],
        ['Вывести на экран список сотрудников', cur_group.print_group],
        ['Удалить из сотрудника из списка', cur_group.remove_worker],
        ['Очистить список', cur_group.clear_worker],
        ['Выполнить особое действие', cur_group.do_magic],
        ['Сохранить список в файл', cur_group.save_to_file],
        ['Загрузить список из файла', cur_group.load_from_file]

        ]


def menu():
    print("------------------------------")
    for i, item in enumerate(Menu_list):
        print("{0:2}. {1}".format(i, item[0]))
    print("------------------------------")
    return int(input())


def main():
    try:
        while True:
            Menu_list[menu()][1]()
    except Exception as e:
        print(e, "\nFinally")

if __name__ == '__main__':
	main()


