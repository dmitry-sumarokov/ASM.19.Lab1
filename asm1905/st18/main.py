from abc import ABC, abstractmethod
import pickle
from enum import Enum

from .Container import Container
from .Strategy import Console_menu

element_type = Enum('element_type', 'student headman')

def main():
    container = Container()
    cm = Console_menu(container)
    while(True):
        if(cm.user_menu() == 0):
            break
