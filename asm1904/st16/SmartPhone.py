#from Phone import Phone
#from OS import WithOS
#from RAM import EnterRAM

if __name__ == '__main__':
    from Phone import Phone
else:
    from .Phone import Phone

if __name__ == '__main__':
    from OS import WithOS
else:
    from .OS import WithOS

if __name__ == '__main__':
    from RAM import EnterRAM
else:
    from .RAM import EnterRAM

class SmartPhone(Phone):
    OS = WithOS()
    RAM = EnterRAM()

