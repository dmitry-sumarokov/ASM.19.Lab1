from .company import Company

Co = Company()

Main_menu = [
    ['Добавить сотрудника', Co.add_staff],
    ['Редактировать информацию о сотруднике', Co.edit_staff],
    ['Удалить сотрудника из списка', Co.delete_staff],
    ['Очитстить список сотрудников', Co.delete_all],
    ['Вывести на экран список сотрудников', Co.show_staff],
    ['Сохранить список сотрудников в файл', Co.save_staff],
    ['Загрузить список сотрудников из файла', Co.load_staff]
]

def menu():
    print()
    for i, item in enumerate(Main_menu):
        print(f'{i}. {item[0]}')
    print()
    return int(input('Выберите пункт меню: '))

def main():
    try:
        while True:
            Main_menu[menu()][1]()
    except Exception as e:
        print(e, 'Выход', sep='\n')

main()
