class Animal:
    animal_behavior = None
    display = None    
    
    def __init__(self, name =' ', age =' ', gender = ' '):
        self.name = name
        self.age = age
        self.gender = gender
        
    #def put(self):
        #print('Name:')
        #self.name=input()
        #print('Age:')
        #self.age=input()
        #print('Gender:')
        #self.gender=input()
        
    """def output(self):
        print(self.name)
        print(self.age)
        print(self.gender)"""

    def SetBehaviour (self, animal_behavior, display):  
        self.animal_behavior = animal_behavior
        self.display = display
        
    def put(self):
        self.display.put(self)
        
    def output(self):
        self.display.output(self)
        
    def different(self):
        self.animal_behavior.different(self)
        
"""class AnimalBehavior:
        def different(self, name):
            raise NotImplementedError() """    
    
    


    

