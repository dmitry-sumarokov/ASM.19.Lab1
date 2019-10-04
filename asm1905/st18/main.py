from abc import ABC, abstractmethod
import pickle
from enum import Enum

from Basic import Basic
from Student import Student
from Headman import Headman
from Container import Container
from Strategy import Console_menu

element_type = Enum('element_type', 'student headman')

if(__name__ == "__main__"):
    container = Container()
    cm = Console_menu(container)
    while(True):
        if(cm.user_menu() == 0):
            break
