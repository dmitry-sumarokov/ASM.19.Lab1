from .group import Group

myG = Group()

MENU = [
    ['Добавить студента', myG.add_student],
    ['Редактировать информацию о студенте', myG.change_student],
    ['Удалить из списка', myG.remove_student],
    ['Вывести на экран весь список', myG.print_group],
    ['Выполнить особые действия', myG.do_magic],
    ['Сохранить список в файл', myG.save_to_file],
    ['Загрузить список из файла', myG.load_from_file]
]


def menu():
    print()
    for i, item in enumerate(MENU):
        print(f'{i}) {item[0]}')
    print()
    return int(input('Введите номер пункта меню: '))

def main():
    try:
        while True:
            MENU[menu()][1]()
    except Exception as e:
        print(e, 'Game over', sep='\n')

