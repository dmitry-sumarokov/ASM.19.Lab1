import asm1904.st00.main
import asm1904.st01.main
import asm1905.st00.main
import asm1905.st02.main
import asm1905.st11.main
import asm1905.st17.main
import asm1905.st19.main
#	добавить импорт своего модуля по шаблону
#	import asm<код группы>.st<номер по журналу>.main

MENU = [
		["[1904-00] Образец 1904", asm1904.st00.main.main],
		["[1904-01] Абраменкова", asm1904.st01.main.main],
		["[1905-02] Вотинцев", asm1905.st02.main.main],
		["[1905-11] Ремизова", asm1905.st11.main.main],
		["[1905-17] Суфьянов", asm1905.st17.main.main],
		["[1905-19] Шишкин", asm1905.st19.main.main],

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
