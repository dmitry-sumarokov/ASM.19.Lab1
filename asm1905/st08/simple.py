from abc import ABC, abstractmethod

class simple(ABC):

    def __init__(self):
        self._id = ''
        self._fullname = ''
        self._pay = ''
        self._age = ''
        self._email = ''
    
    @abstractmethod
    def input_inf(self):
        pass
    @abstractmethod
    def print_inf(self):
        pass
    @abstractmethod
    def edit_inf(self):
        pass
    @abstractmethod
    def special(self):
        pass
