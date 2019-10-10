import pickle
import os
import random

from .Student import Bachelor, Master, Graduate_student


class group:
    def __init__(self):
        self.group = []

    def AddBachelor(self):
        AddedBachelor = Bachelor()
        AddedBachelor.read()
        self.group.append(AddedBachelor)
        print('Bachelor was added')

    def AddMaster(self):
        AddedMaster = Master()
        AddedMaster.read()
        self.group.append(AddedMaster)
        print('Master was added')

    def AddGraduate_student(self):
        AddedGraduate_student = Graduate_student()
        AddedGraduate_student.read()
        self.group.append(AddedGraduate_student)
        print('Graduate student was added')

    def Loto(self):
        if len(self.group) == 0:
            print('Please add somebody')
        else:
            print('play if you are not afraid and select who you')
            self.ShowList()
            print('Enter a number: ')
            f = int(input())
            print('Enter nubmer from 1 to 10')
            i = int(input())
            n = print(random.randint(1, 10))
            if i == n:
                print('You win, tomorrow you can stay home ')
            else:
                self.group.pop(f - 1)
                print('TI OTCHISLEN')

    def ShowList(self):
        for (i, group) in enumerate(self.group):
            print(i + 1)
            group.write()

    def edit(self):
        if len(self.group) == 0:
            print('Please add somebody')
        else:
            self.ShowList()
            print('Enter a number: ')
            i = int(input())
            self.group[i - 1].read()

            print('Has been edited ')

    def Delete(self):
        if len(self.group) == 0:
            print('Please add somebody')
        else:
            self.ShowList()
            print('Enter a number: ')
            i = int(input())
            self.group.pop(i - 1)
            print('Was deleted')

    def ClearAllList(self) :
        self.group.clear()
        print('Was deleted')

    def readfromfile(self):
        self.group = pickle.load(
            open(os.path.join(os.path.abspath(__name__).replace('.st06.group', '/st06'), 'group.dat'), 'rb'))
        print('All List')

    def writetofile(self):
        self.group = pickle.dump(self.group, open(
            os.path.join(os.path.abspath(__name__).replace('.st06.group', '/st06'), 'group.dat'), 'wb'))
        print('Saved')




