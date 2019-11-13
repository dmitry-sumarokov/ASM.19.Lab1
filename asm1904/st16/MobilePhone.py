#from Phone import Phone
#from OS import NoOS
#from RAM import ConstRAM

if __name__ == '__main__':
    from Phone import Phone
else:
    from .Phone import Phone

if __name__ == '__main__':
    from OS import NoOS
else:
    from .OS import NoOS

if __name__ == '__main__':
    from RAM import ConstRAM
else:
    from .RAM import ConstRAM

class MobilePhone(Phone):
    OS = NoOS()
    RAM = ConstRAM()
