from .ACS_SC_dep import ACS_SC_dep


def main():
    dep = ACS_SC_dep()
    print('Congratulations!!! You have just become the head of Automated Control Systems Security Center department')
    print('What do you want to do?')
    main_menu = (('Hire employee', dep.hire_employee),
                 ('Alter employee params', dep.alter_employee),
                 ('Print employees list', dep.print_emp_list),
                 ('Show special employees abilities', dep.special_action),
                 ('Fire employee', dep.fire_employee),
                 ('Save employees list to file', dep.save_to_file),
                 ('Load employees list from file', dep.load_from_file),
                 ('Close department (delete all info about employees)', dep.close_dep))
    # ('Exit department', exit))

    while True:
        try:
            print("------------------------------")
            for i, item in enumerate(main_menu):
                print("{0:2}. {1}".format(i, item[0]))
            print("------------------------------")
            choice = input()
            if choice.isdigit():
                main_menu[int(choice)][1]()
            else:
                print('Enter a number from main menu!')
        except Exception as e:
            print(e, "\n\nEnd of working day")
