from .container import Container


def main():
    c = Container()

    menu = {
        1: {"text": "Добавить запись", "callback": c.add_new},
        2: {"text": "Вывести список", "callback": c.show},
        3: {"text": "Уникальная информация", "callback": c.behaviour},
        4: {"text": "Обновить запись", "callback": c.edit},
        5: {"text": "Удалить запись", "callback": c.delete},
        6: {"text": "Очистить список", "callback": c.clear},
        7: {"text": "Сохранить список", "callback": c.save_list},
        8: {"text": "Загрузисть список", "callback": c.laod_list},
        0: {"text": "Выход", "callback": lambda: exit(0)},
    }

    while True:
        print("-" * 20)
        for k in menu.keys():
            print(f"{k} {menu[k]['text']}")

        try:
            cmd = int(input("> "))
            menu[cmd]['callback']()
        except (ValueError, KeyError):
            print(f"\nНет такого пункта меню.\n")
