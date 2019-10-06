from company import Company

def main():
    company_menu = Company()

    company_menu = (('Добавить работника', company_menu.input_employer),
                 ('Редактировать информацию ', company_menu.edit_employer),
                 ('Вывести список рабочих', company_menu.print_company),
                 ('Выполнить специальное действие', company_menu.special),
                 ('Удалить работника', company_menu.delete_employer),
                 ('Очистить список', company_menu.clear_employersList),
                 ('Сохранить список в файл', company_menu.save),
                 ('Загрузить список из файла', company_menu.load))


    while True:
        try:
            print("------------------------------")
            for i, item in enumerate(company_menu):
                print("{0:2}. {1}".format(i, item[0]))
            print("------------------------------")
            choice = input()
            if choice.isdigit():
                company_menu[int(choice)][1]()
            else:
                print('введите номер!')
        except Exception as e:
            print(e, "\nконец")

main()
