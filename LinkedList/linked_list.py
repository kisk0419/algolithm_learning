from typing import Any, NewType


IndexNum = NewType('IndexNum', int)


class Element(object):
    def __init__(self, value: Any):
        self.data = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
    
    def insert(self, value: Any, index: IndexNum = None) -> IndexNum:
        el = Element(value)
        if self.head is None:
            self.head = el
            return 0

        if index is None:
            last_el = self.head
            i = 0
            while last_el.next is not None:
                last_el = last_el.next
                i += 1
            last_el.next = el
            return i
        else:
            last_el = self.head
            pre_el = None
            i = 0
            while el.next is not None and index >= i:
                if el.next is None:
                    break
                pre_el = last_el
                last_el = last_el.next
                i += 1
            pre_el.next = el
            el.next = last_el
            return i

    
    def get(self, index: IndexNum) -> Any:
        el = self.head
        i = 0
        while el is not None and index > i:
            el = el.next
            i += 1
        if el is not None:
            return el.data
        else:
            raise IndexError()

    
    def delete(self, index: IndexNum) -> bool:
        el = self.head
        pre_el = None
        i = 0
        while el is not None and index > i:
            pre_el = el
            el = el.next
            i += 1
        
        if index == 0:
            self.head = el.next
        elif el is not None:
            pre_el.next = el.next
            return True
        else:
            raise IndexError()

    def print_all(self):
        el = self.head
        while el is not None:
            print(el.data)
            el = el.next


if __name__ == '__main__':
    l = LinkedList()
    l.insert(0)
    l.insert(1)
    l.insert(2)
    #print(l.get(0))
    l.delete(3)
    l.print_all()
