from .Edit import Edithuman

class woman_beh():

    def init(self):
        pass

    def edit(self):
        Edithuman.edit(self)
        new_sadness = input('Введите новое значение опечаленности: ')
        self.sadness = int(new_sadness) if new_sadness else self.sadness
        new_happyness = input('Введите новое значение счастья человека: ')
        self.happyness = int(new_happyness) if new_happyness else self.happyness
        new_disease = input('Изменение болезни: ')
        self.disease = int(new_disease) if new_disease else self.disease
        
    def print(self):
        Edithuman.print(self)
        print(f'\n Грусть: {self.sadness} \n Радость: {self.happyness} \n Болезни: {self.disease}')

class man_beh():

   def init(self):
        pass

   def edit(self):
       Edithuman.edit(self)
       new_sadness = input('Введите новое значение опечаленности: ')
       self.sadness = int(new_sadness) if new_sadness else self.sadness
       new_happyness = input('Введите новое значение счастья человека: ')
       self.happyness = int(new_happyness) if new_happyness else self.happyness
       new_disease = input('Измение болезни: ')
       self.disease = int(new_disease) if new_disease else self.disease
       
   def print(self):
       Edithuman.print(self)
       print(f'\n Грусть: {self.sadness} \n Радость: {self.happyness} \n Болезни: {self.disease}')
