from .group import Group


def main():
    group = Group()

    options = [
        ('Добавить сотрудника', group.add_employee),
        ('Редактировать информацию о сотруднике', group.edit_employee),
        ('Удалить из сотрудника из списка', group.remove_employee),
        ('Вывести на экран список сотрудников', group.print_group),
        ('Очистить список', group.clear_group),
        ('Выполнить особое действие', group.do_magic),
        ('Сохранить список в файл', group.save_to_file),
        ('Загрузить список из файла', group.load_from_file)
    ]

    while True:
        for i, (x, _) in enumerate(options):
            print(f'{i}: {x}')
        try:
            choice = int(input())
            if choice >= 0 and choice < len(options):
                func = options[choice][1]
                func()
        except KeyboardInterrupt:
            break
