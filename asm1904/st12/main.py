from .group import Group

Group = Group()


def main():
    menu = {
            "1": ("Добавить человека", Group.get_action_list),
            # "2": ("Специальное действие", Group.execute),
            "2": ("Редактировать", Group.edit),
            # "4": ("Удалить", Group.delete),
            "3": ("Вывод списка людей", Group.print_group),
            "4": ("Считать из файла", Group.load),
            "5": ("Записать в файл", Group.save),
            "6": ("Очистить", Group.clean),
            "7": ("Выход", None)
            }

    while True:
        print('')
        print('Кого добавить:')
        for k in range(1, len(menu)+1):
            print(k, " - ", menu[str(k)][0])
        x = input()
        # Проверяем int ли это
        try:
            int(x)
        except ValueError:
            print('Нужно ввести число от 1 до '+ str(len(menu)))
            continue
        if int(x) == 7:
            break
        if 1 <= int(x) <= len(menu):
            menu[x][1]()
        else:
            print('Такой команды нет')


if __name__ == '__main__':
    main()
