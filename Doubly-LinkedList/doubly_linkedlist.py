from __future__ import annotations
from typing import Any, Optional


class Node(object):
    def __init__(self, data: Any) -> None:
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList(object):
    def __init__(self) -> None:
        self.head = None

    
    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
    

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node


    def remove(self, data: Any) -> None:
        current_node = self.head
        if current_node and current_node.data == data:
            if current_node.next is None:
                self.head = None
                current_node = None
                return
            else:
                next_node = current_node.next
                self.head = next_node
                next_node.prev = None
                current_node = None
                return

        while current_node and current_node.data != data:
            current_node = current_node.next
        
        if current_node is None:
            return
        
        if current_node.next is None:
            prev_node = current_node.prev
            prev_node.next = None
            current_node = None
            return
        else:
            prev_node = current_node.prev
            next_node = current_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            current_node = None
            return
           


    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


if __name__ == '__main__':
    l = DoublyLinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.print()
    l.insert(0)
    print('#####')
    l.print()
    l.remove(0)
    l.remove(3)
    print('#####')
    l.print()
    
