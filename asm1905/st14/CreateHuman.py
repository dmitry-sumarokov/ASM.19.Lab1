from Human import Human
from State import man_beh, woman_beh

class woman(Human):

    def __init__(self):
        super().__init__()
        self.sadness = int(input('Сколько грусти необходимо добавить?(от 0 до 100): '))
        self.happyness = int(input('Насколько будет счастлив Ваш человек?(от 0 до 100): '))
        self.disease = str(input('Добавьте щепотку болезней (по желанию): '))
        if ((self.sadness==100)&(self.happyness==100)):
            print('------------------- \n Мои поздравления, Вам удалось сделать отъявленную психопатку \n-------------------')

    def edit(self):
        woman_beh.edit(self)

    def print(self):
        woman_beh.print(self)



class man(Human):

    def __init__(self):
        super().__init__()
        self.sadness = int(input('Сколько грусти необходимо добавить?(от 0 до 100): '))
        self.happyness = int(input('Насколько будет счастлив Ваш человек?(от 0 до 100): '))
        self.disease = input('Добавьте щепотку болезней (по желанию): ')
        if ((self.sadness==100)&(self.happyness==100)):
            print('------------------- \n Мои поздравления, Вам удалось сделать отъявленного психопата \n-------------------')

    def edit(self):
        man_beh.edit(self)

    def print(self):
        man_beh.print(self)