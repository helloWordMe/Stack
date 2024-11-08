from abc import ABC , abstractmethod
from typing import TypeVar , Generic

T = TypeVar('T')

class DoubleLinkedListInterface(ABC, Generic[T]):
    
    @abstractmethod
    def insert_first(self, value :T):
        pass
    
    @abstractmethod
    def insert_last(self, value :T):
        pass
    
    @abstractmethod
    def remove_first(self) -> T:
        pass
    
    @abstractmethod
    def remove_first(self) -> T:
        pass


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList(DoubleLinkedListInterface[T]):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, data : T):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_last(self, data : T):
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_first(self) -> T:
        if not self.head:
            print("List is empty, nothing to remove.")
            return
        
        removed_data = self.head.data
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        return removed_data

    def remove_last(self) -> T:
        if not self.tail:
            print("List is empty, nothing to remove.")
            return
        
        removed_data = self.tail.data
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return removed_data

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("List:", elements)   

    