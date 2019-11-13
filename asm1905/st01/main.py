if __name__ == '__main__':
    from nursery import Nursery
else:
    from .nursery import Nursery




cur_nursery = Nursery()

Menu_list = [
        ['Add a nursery', cur_nursery.add_cat],
        ['Edit information about nursery', cur_nursery.change_cat],
        ['Print list of nurserys', cur_nursery.print_cats],
        ['Delete the nursery from list', cur_nursery.remove_the_cat],
        ['Clear list', cur_nursery.clear_cats_list],
        ['Do special function', cur_nursery.do_special_meow],
        ['Save the list in the file', cur_nursery.save_to_file],
        ['Download the list from the file', cur_nursery.load_from_file]

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


