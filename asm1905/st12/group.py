import pickle
from .human import Student, Starosta, Proforg
        
class group:
    def __init__(self):
        self.group=[]

    def addStudent(self):
        newStudent = Student()
        newStudent.read()
        self.group.append(newStudent)
        print()
        print('Добавлен студент')
        
    def addStarosta(self):
        newStarosta = Starosta()
        newStarosta.read()
        self.group.append(newStarosta)
        print()
        print('Добавлен староста')
        
    def addProforg(self):
        newProforg = Proforg()
        newProforg.read()
        self.group.append(newProforg)
        print()
        print('Добавлен профорг')
 
        
    def show_list(self):
        print()
        print('Список группы:')
        for (i,group) in enumerate (self.group):
            print(i+1)
            group.write()
            self.group[i].action()

    def change(self):
        self.show_list()
        print()
        print('Выберите номер ученика, которого хотите изменить: ')
        i=int(input())
        self.group[i-1].read()
        print('Данные ученика изменены')
        
           
    def delete_card(self):
        self.show_list()
        print()
        print('Введите номер ученика, которого нужно убрать из списка группы: ')
        i=int(input())
        self.group.pop(i-1)
        print()
        print('Ученик удален')

    def write_file(self):
        f=open('C://temp/lab1_Ruchkina/list.dat','wb')
        pickle.dump(self.group,f)
        print()
        print('Записано в файл')
        
    def read_file(self):
        f=open('C://temp/lab1_Ruchkina/list.dat','rb')
        self.group = pickle.load(f)
        print()
        print('Считано из файла')

 
        