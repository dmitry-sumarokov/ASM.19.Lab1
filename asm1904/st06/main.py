from .Encyclo import Encyclo

def main():
    NewEncyclo=Encyclo()
    Menu = [
        ['Добавить животное.', NewEncyclo.Edit_newAnimal],
        ['Удалить животное из энциклопедии и внести в красную книгу.', NewEncyclo.delete_Animal],
        ['Вывести состав энциклопедии.', NewEncyclo.Write_Encyclo],
        ['Модифицировать животное.', NewEncyclo.modify_Animal],
        ['Чтение из файла.', NewEncyclo.readEncyclo_File],
        ['Выгрузка в файл.', NewEncyclo.writeEncyclo_File],
        ['Особенность данного класса.', NewEncyclo.Feature_animal],
        ['Удалить энциклопедию.', NewEncyclo.delete_Encyclo]
        ]
    try:
        while True:
            print("------------------------------")
            print("\n Выберите действие из меню: \n")
            print("------------------------------")
            for i, item in enumerate(Menu):
                print("{0:2}. {1}".format(i, item[0]))
                print("------------------------------")
            choise=int(input())
            Menu[choise][1]()
    except Exception as e:
        print('\n')


if __name__ == "__main__":
    main()
