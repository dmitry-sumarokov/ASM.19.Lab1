from .group import group

group = group()

Menu = [["Add bachelor", group.AddBachelor],
        ["Add master", group.AddMaster],
        ["Add graduate student", group.AddGraduate_student],
        ["To do smth", group.Loto],
        ["Edit", group.edit],
        ["Delete", group.Delete],
        ["Show all list", group.ShowList],
        ["Read file", group.readfromfile],
        ["Write file", group.writetofile],
        ["Delete all", group.ClearAllList],
        ]

def menu():
    print("------------------------------")
    for i, item in enumerate(Menu):
        print("{0:2}. {1}".format(i, item[0]))
    print("------------------------------")
    return int(input())

def main():
    try:
        while True:
            Menu[menu()][1]()
    except Exception as e:
        print(e, "Some problems")





if __name__ == '__main__':
	main()