from .ZooWorker import ZooWorker, Behaviour_DirectorZoo, Behaviour_SecurityZoo, Behaviour_KeeperZoo, Behaviour_IceCreamSellerZoo, A_Display, DirectorZoo,SecurityZoo,KeeperZoo,IceCreamSellerZoo
import pickle
import os

class Zoo():
    def __init__(self):
        self.ZooWorkers =[]

    def hire_newWorker(self):
        print('Выберите, кого не хватает в Вашем чудном зоопарке!')
        Menu = [['Директор зоопарка', self.hire_DirectorZoo],
                ['Охранник зоопарка', self.hire_SecurityZoo],
                ['Смотритель зоопарка', self.hire_KeeperZoo],
                ['Продавец мороженого', self.hire_IceCreamSellerZoo]
                ]
        try:
            while True:
                print("\n Выберите снова, если хотите добавить ещё сотрудника или нажмите 5 \n ")
                print("------------------------------")
                for i, item in enumerate(Menu):
                    print("{0:2}. {1}".format(i, item[0]))
                    print("------------------------------")
                choise=int(input())
                Menu[choise][1]()
        except Exception as e:
            print("\n Попробуйте снова, если что-то пошло не так, или выберите новое действие.")
        
    def hire_DirectorZoo(self):
        hireDirector = DirectorZoo()
        hireDirector.Read()
        self.ZooWorkers.append(hireDirector)
        
    def hire_SecurityZoo(self):
        hireSecurity = SecurityZoo()
        hireSecurity.Read()
        self.ZooWorkers.append(hireSecurity)
        
    def hire_KeeperZoo(self):
        hireKeeper = KeeperZoo()
        hireKeeper.Read()
        self.ZooWorkers.append(hireKeeper)
        
    def hire_IceCreamSellerZoo(self):
        hireIceCreamSeller = IceCreamSellerZoo()
        hireIceCreamSeller.Read()
        self.ZooWorkers.append(hireIceCreamSeller)

    def Write_ZooTeam(self):
        if len(self.ZooWorkers)==0:
            print('Зоопарк пустует')
        else:
            for i in range(len(self.ZooWorkers)):
                print("------------------------------")
                print(i, end=' ')
                self.ZooWorkers[i].Write()
                print("------------------------------")

    def dismiss_Worker(self):
        print("Кого сегодня уволим? \n")
        if len(self.ZooWorkers)==0:
            print('Хотя, мы и так постарались, больше некого.. \n')
        else:
            for i in range(len(self.ZooWorkers)):
                print("------------------------------")
                print(i, end=' ')
                self.ZooWorkers[i].Write()
                print("------------------------------")
            change = int(input('Введите штатный номер несчастного:'))
            self.ZooWorkers.pop([change])

    def update_Worker(self):
        print("Кого будем изменять? \n")
        if len(self.ZooWorkers)==0:
            print('Зоопарк пуст \n')
        else:
            for i in range(len(self.ZooWorkers)):
                print("------------------------------")
                print(i, end=' ')
                self.ZooWorkers[i].Write()
                print("------------------------------")
            change = int(input('Введите штатный номер изменяемого:'))
            self.ZooWorkers[change].Read()

    def Do_something(self):
        print("За кем понаблюдаем? \n")
        if len(self.ZooWorkers)==0:
            print('Зоопарк пуст \n')
        else:
            for i in range(len(self.ZooWorkers)):
                print("------------------------------")
                print(i, end=' ')
                self.ZooWorkers[i].Write()
                print("------------------------------")
            change = int(input('Введите штатный номер интересующего сотрудника:'))
            self.ZooWorkers[change].Do()
    
    def delete_Zoo(self):
        if len(self.ZooWorkers)==0:
            print('Зоопарк пуст, Вы свободны! \n')
        else:
            self.ZooWorkers.clear()
            print('Зоопарк пуст, Вы свободны! \n')

    def writeZoo_File(self):
        with open(os.path.join(os.path.abspath(__name__).replace('.st20.Zoo', '\\st20'), 'Zoo.p'), 'wb') as f:
            pickle.dump(self.ZooWorkers, f)
        print('Теперь зоопарк всегда с Вами! \n')
        
        
    def reedZoo_File(self):
        with open(os.path.join(os.path.abspath(__name__).replace('.st20.Zoo', '\\st20'), 'Zoo.p'), 'rb') as f:
            self.ZooWorkers = pickle.load(f)
        print('Ваш зоопарк:')
        self.Write_ZooTeam()
        



