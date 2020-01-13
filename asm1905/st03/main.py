from .shop import Shop

Shop = Shop()

Main_menu = [
    ['Добавить продукцию', Shop.add_store],
    ['Редактировать информацию о продукции',Shop.edit_store],
    ['Удалить продукцию из списка', Shop.delete_store],
    ['Очитстить список продукции', Shop.delete_all],
    ['Вывести на экран список продукции', Shop.show_store],
    ['Сохранить список продукции в файл', Shop.save_store],
    ['Загрузить список продукции из файла', Shop.load_store]
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
