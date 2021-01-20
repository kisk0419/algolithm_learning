from __future__ import annotations
from typing import Any, Optional


class Node(object):
    def __init__(self, data: Any, prev_node: Node = None, next_node: Node = None) -> None:
        self.prev = prev_node
        self.data = data
        self.next = next_node


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
           

    def reverse_iter_kk(self) -> None:
        current_node = self.head
        if current_node is None:
            return

        while current_node.next:
            prev_node = current_node.prev
            next_node = current_node.next
            current_node.next = prev_node
            current_node.prev = next_node
            prev_node = current_node
            current_node = next_node
        self.head = current_node
        current_node.next = current_node.prev
        current_node.prev = None


    def reverse_iter(self) -> None:
        previous_node = None
        current_node = self.head
        
        while current_node:
            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node
            current_node = current_node.prev

        if previous_node:
            self.head = previous_node.prev
        

    def reverse_recursive_kk(self) -> None:
        def _reverse_recursive(prev_node: Node, current_node: Node) -> Node:
            if current_node.next is None:
                return current_node

            next_node = current_node.next
            current_node.next = prev_node
            current_node.prev = next_node

            return _reverse_recursive(current_node, next_node)    
        
        if self.head is None:
            return

        self.head = _reverse_recursive(None, self.head)
        self.head.next = self.head.prev
        self.head.prev = None


    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: Node) -> Optional[Node]:
            if current_node is None:
                return None

            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node
            
            if current_node.prev is None:
                return current_node

            return _reverse_recursive(current_node.prev)    
        
        self.head = _reverse_recursive(self.head)
        

    def sort_kk(self) -> DoublyLinkedList:
        current_node = self.head
        tail_node = self.head
        
        if self.head is None:
            return self

        while tail_node.next:
            tail_node = tail_node.next

        while self.head != tail_node:
            while current_node.next and current_node != tail_node:
                if current_node.data > current_node.next.data:
                    current_node.data, current_node.next.data = current_node.next.data, current_node.data
                current_node = current_node.next
            tail_node = current_node.prev
            current_node = self.head
            
        return self


    def sort(self) -> None:
        if self.head is None:
            return
        
        current_node = self.head
        
        while current_node.next:
            next_node = current_node.next
            
            while next_node:
                if current_node.data > next_node.data:
                    current_node.data, next_node.data = next_node.data, current_node.data
                next_node = next_node.next

            current_node = current_node.next
            
        
    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


if __name__ == '__main__':
    l = DoublyLinkedList()
    l.append(1)
    l.append(10)
    l.append(5)
    l.append(2)
    l.append(9)
    l.print()
    print('#####')
    l.sort()
    l.print()
    
