from abc import ABC , abstractmethod

from typing import Generic , TypeVar

import threading

from double_linkedlist.double_linked_list import DoublyLinkedList 


T = TypeVar('T')

class StackInterface(ABC, Generic[T]):
    
    @abstractmethod
    def pop(self) -> T:
        """delete the first item and return that"""
        pass

    @abstractmethod
    def push(self , vallue : T) -> None:
        """insert the top and return nothing"""
        pass

class Stack(StackInterface[T]):

    def __init__(self):
        self._list = DoublyLinkedList[T]()
        self.lock = threading.Lock()

    def pop(self) -> T:
        print('Deleting ...')
        with self.lock :
            if self.empty == True:
                raise Exception("this list is empty")
            return self._list.remove_first()
        
    
    def push(self, value: T) -> None:
        with self.lock:
            print('Inserting ...')
            self._list.insert_first(value)
    

    def empty(self) -> bool:
        """return True if list empty"""
        return self._list.head is None
    
