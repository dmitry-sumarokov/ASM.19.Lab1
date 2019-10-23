import pickle
import os
from .employee import Employee
from .menuItems import ADDITION_MENU
from .commonFunctions import get_menu_input
from colorama import Fore
from .commonFunctions import return_number


class ScrumTeam:
    __slots__ = ('lala', '_employees')

    def __init__(self):
        self._employees = []

    def add_employee(self):
        e = ADDITION_MENU[int(get_menu_input(ADDITION_MENU))]
        self._employees.append(Employee(e[1], e[2]))

    def edit_employee(self):
        self._employees[return_number()].edit()
        print(Fore.YELLOW + 'Saved!')

    def remove_employee(self):
        self._employees.pop(return_number())
        print(Fore.YELLOW + 'Deleted!')

    def show_scrum_team(self):
        for i, employee in enumerate(self._employees):
            print(Fore.MAGENTA + '~Employee №' + str(i) + '~')
            employee.print_data()

    def listen_personal(self):
        self._employees[return_number()].saying()

    def save_to_file(self):
        pickle.dump(self._employees,
                    open(os.path.join(os.path.abspath(__name__).replace('.st21.scrumTeam', '/st21'), 'employees'), 'wb'))
        print(Fore.MAGENTA + 'Saved to file!')

    def load_from_file(self):
        self._employees = pickle.load(
            open(os.path.join(os.path.abspath(__name__).replace('.st21.scrumTeam', '/st21'), 'employees'), 'rb'))
        print(Fore.MAGENTA + 'Loaded from file!')
