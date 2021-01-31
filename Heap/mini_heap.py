import sys
from typing import Optional, NewType

Index = NewType('Index', int)


class MiniHeap(object):
    def __init__(self):
        self.heap = [-1 * sys.maxsize]
        self.current_size = 0


    def parent_index(self, index: Index) -> Index:
        return index // 2

    
    def left_child_index(self, index: Index) -> Index:
        return index * 2
    

    def right_child_index(self, index: Index) -> Index:
        return (index * 2) + 1


    def swap(self, index1: Index, index2: Index) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]


    def heapify_up(self, index: Index) -> None:
        if self.parent_index(index) <= 0:
            return
        parent_index = self.parent_index(index)
        if self.heap[index] < self.heap[parent_index]:
            self.swap(index, parent_index)
            self.heapify_up(parent_index)


    def min_child_index(self, index: Index) -> Index:
        if self.right_child_index(index) > self.current_size:
            return self.left_child_index(index)
        else:
            if self.heap[self.left_child_index(index)] < self.heap[self.right_child_index(index)]:
                return self.left_child_index(index)
            else:
                return self.right_child_index(index)
    

    def heapify_down(self, index: Index) -> None:
        if self.left_child_index(index) > self.current_size:
            return
        min_child_index = self.min_child_index(index)
        if self.heap[min_child_index] < self.heap[index]:
            self.swap(min_child_index, index)
            self.heapify_down(min_child_index)
        

    def push(self, value: int) -> None:
        self.heap.append(value)
        self.current_size += 1
        if self.current_size == 1:
            return
        
        self.heapify_up(self.current_size)


    def pop(self) -> Optional[int]:
        if self.current_size == 0:
            return

        pop_value = self.heap[1]
        last_value = self.heap.pop()
        self.current_size -= 1

        if self.current_size == 0:
            return pop_value

        self.heap[1] = last_value
        self.heapify_down(1)

        return pop_value


    def status(self) -> None:
        print('-------------')
        print(self.heap)
        print(f'current_size: {self.current_size}')


if __name__ == '__main__':
    h = MiniHeap()
    
    # datas = [5, 6, 2, 9, 13, 11, 1]
    # for data in datas:
    #     h.push(data)
    
    # print('###### baba')
    # print(h.heap)
    # print(h.pop())
    # print(h.heap)
    # print(h.pop())
    # print(h.heap)
    # print(h.pop())
    # print(h.heap)
    h.status()
    h.push(1)
    h.status()
    print(h.pop())
    h.status()
    h.push(2)
    h.status()