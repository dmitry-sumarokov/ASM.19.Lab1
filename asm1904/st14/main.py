if __name__ == '__main__':
    from technic import Container
else:
    from .technic import Container

    
c = Container()
            
multiple={
    1:c.insertAM,
    2:c.insertMOTO,
    3:c.insertATV,
    4:c.show,
    5:c.edit,
    6:c.delete,
    7:c.spesial,
    8:c.writefile,
    9:c.readfile,
    10:c.clean
}
        


def main():
    while 1:
            print('1-Добавить автомобиль')
            print('2-Добавить мотоцикл')
            print('3-Добавть квадроцикл')
            print('4-Вывести')
            print('5-Редактировать')
            print('6-Удалить')
            print('7-Специальное действие')
            print('8-В файла')
            print('9-Из файл')
            print('10-Отчистка')
            print('11-Выход')
            

            try:
                 id=int(input())
                 mult=multiple[id]()
  
            except KeyError:
                 print('Выбирете номер')
       
            if id == 11:
                break

if __name__ == "__main__":
    main()
