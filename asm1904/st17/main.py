from .conteiner import Container
con=Container()

multiple={
    1:con.addCat,
	2:con.addDog,
    3:con.edit_elem,
    4:con.printlist,
    5:con.remove_elem,
    6:con.recording,
    7:con.read,
    8:con.different,
	9:con.clearlist
}
        


def main():
	
	while True:
		print('_______________________________')
		print('Меню')
		print('1-Добавить котика')
		print('2-Добавить пёселя')
		print('3-Редактировать элемент')
		print('4-Вывести список элементов')
		print('5-Удалить элемент')
		print('6-Записать в файл')
		print('7-Считать из файла')
		print('8-Специальное действие')
		print('9-Очистить список элементов')
		print('10-Выход')
		print('_______________________________')
		print('Выберете действие')
		print('_______________________________')
		id=int(input())
		if id == 10:
			print ('Довольно-таки жаль')
			break

		mult=multiple[id]()
  
	#	except KeyError:
	#		
       
                                    

if __name__ == "__main__":
    main()
