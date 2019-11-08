if __name__ == '__main__':
	from group import group
	from menu import startMenu
else:
	from .group import group
	from .menu import startMenu


def main():
	group().f()
	startMenu()



if __name__ == '__main__':
	main()


