from .Animals import Animals, Behaviour_Mammals, Behaviour_Fish, Behaviour_Bird, Behaviour_Reptile, Disp, Mammals,Fish,Bird,Reptile
import pickle
import os

class Encyclo():
    def __init__(self):
        self.Animals=[]

    def Edit_newAnimal(self):
        Menu = [['Млекопитающие', self.Edit_Mammals],
                ['Рыбы', self.Edit_Fish],
                ['Птицы', self.Edit_Bird],
                ['Рептилии', self.Edit_Reptile]
                ]
        try:
            while True:
                print("------------------------------")
                for i, item in enumerate(Menu):
                    print("{0:2}. {1}".format(i, item[0]))
                    print("------------------------------")
                choise=int(input())
                Menu[choise][1]()
        except Exception as e:
            print("\n ")
        
    def Edit_Mammals(self):
        EditMammals = Mammals()
        EditMammals.Read()
        self.Animals.append(EditMammals)
        
    def Edit_Fish(self):
        EditFish = Fish()
        EditFish.Read()
        self.Animals.append(EditFish)
        
    def Edit_Bird(self):
        EditBird = Bird()
        EditBird.Read()
        self.Animals.append(EditBird)
        
    def Edit_Reptile(self):
        EditReptile = Reptile()
        EditReptile.Read()
        self.Animals.append(EditReptile)

    def Write_Encyclo(self):
        if len(self.Animals)==0:
            print('Животных нет.. \n')
        else:
            for i, item in enumerate(self.Animals):
                print("------------------------------")
                print(i, end=' ')
                self.Animals[i].Write()
                print("------------------------------")

    def delete_Animal(self):
        if len(self.Animals)==0:
            print('Животных нет.. \n')
        else:
            for i, item in enumerate(self.Animals):
                print("------------------------------")
                print(i, end=' ')
                self.Animals[i].Write()
                print("------------------------------")
            change = int(input('Кого съели? \n'))
            self.Animals.pop(change)

    def modify_Animal(self):
        if len(self.Animals)==0:
            print('Животных нет.. \n')
        else:
            for i, item in enumerate(self.Animals):
                print("------------------------------")
                print(i, end=' ')
                self.Animals[i].Write()
                print("------------------------------")
            change = int(input('Кого будем модифицировать? \n'))
            self.Animals[change].Read()

    def Feature_animal(self):
        if len(self.Animals)==0:
            print('Животных нет.. \n')
        else:
            for i, item in enumerate(self.Animals):
                print("------------------------------")
                print(i, end=' ')
                self.Animals[i].Write()
                print("------------------------------")
            change = int(input('Номер животного \n'))
            self.Animals[change].Feature()
    
    def delete_Encyclo(self):
        if len(self.Animals)==0:
            print('Животных нет.. \n')
        else:
            self.Animals.clear()
            print('Животных нет!!! \n')

    def writeEncyclo_File(self):
        with open(os.path.join(os.path.abspath(__name__).replace('.st06.Encyclo', '\\st06'), 'Encyclo.p'), 'wb') as f:
            pickle.dump(self.Animals, f)
        print('Записано!!! \n')
        
        
    def readEncyclo_File(self):
        with open(os.path.join(os.path.abspath(__name__).replace('.st06.Encyclo', '\\st06'), 'Encyclo.p'), 'rb') as f:
            self.Animals= pickle.load(f)
        self.Write_Encyclo()
        

