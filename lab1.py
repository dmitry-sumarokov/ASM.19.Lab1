﻿import asm1904.st00.main
import asm1904.st01.main
import asm1904.st16.main
import asm1905.st00.main
import asm1905.st02.main
import asm1905.st11.main
import asm1905.st13.main
import asm1905.st17.main
import asm1905.st18.main
import asm1905.st19.main
import asm1905.st20.main
import asm1905.st08.main
import asm1905.st05.main
#	добавить импорт своего модуля по шаблону
#	import asm<код группы>.st<номер по журналу>.main

MENU = [
		["[1904-00] Образец 1904", asm1904.st00.main.main],
		["[1904-01] Абраменкова", asm1904.st01.main.main],
		["[1904-16] Садыкова", asm1904.st16.main.main],
		["[1905-02] Вотинцев", asm1905.st02.main.main],
		["[1905-11] Ремизова", asm1905.st11.main.main],
        ["[1905-13] Рыжов", asm1905.st13.main.main],
		["[1905-17] Суфьянов", asm1905.st17.main.main],
		["[1905-18] Тарасов", asm1905.st18.main.main],
		["[1905-19] Шишкин", asm1905.st19.main.main],
		["[1905-20] Шишкина", asm1905.st20.main.main],
		["[1905-08] Никандров", asm1905.st08.main.main],
                ["[1905-05] Коробка", asm1905.st05.main.main],

#		добавить пункт меню для вызова своей главной функции по шаблону:
#		["[<код группы>-<номер по журналу>] <Фамилия>", <ссылка на функцию>],
	]

def menu():
	print("------------------------------")
	for i, item in enumerate(MENU):
		print("{0:2}. {1}".format(i, item[0]))
	print("------------------------------")
	return int(input())

try:
	while True:
		MENU[menu()][1]()
except Exception as ex:
	print(ex, "\nbye")
