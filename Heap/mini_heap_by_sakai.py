import sys
from typing import Optional


class MiniHeap(object):

    def __init__(self) -> None:
        self.heap = [-1 * sys.maxsize]
        self.current_size = 0

    
    def parent_index(self, index: int) -> int:
        return index // 2

    
    def left_child_index(self, index: int) -> int:
        return index * 2

    
    def right_child_index(self, index: int) -> int:
        return (index * 2) + 1

    
    def swap(self, index1: int, index2: int) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    
    def heapify_up(self, index: int) -> None:
        while self.parent_index(index) > 0:
            if self.heap[self.parent_index(index)] > self.heap[index]:
                self.swap(index, self.parent_index(index))
            index = self.parent_index(index)
    
    
    def mini_child_index(self, index: int) -> int:
        if self.right_child_index(index) > self.current_size:
            return self.left_child_index(index)
        else:
            if self.heap[self.left_child_index(index)] < self.heap[self.right_child_index(index)]:
                return self.left_child_index(index)
            else:
                return self.right_child_index(index)


    def heapify_down(self, index: int) -> None:
        while self.left_child_index(index) <= self.current_size:
            min_child_index = self.mini_child_index(index)
            if self.heap[min_child_index] < self.heap[index]:
                self.swap(min_child_index, index)
            index = min_child_index


    def push(self, value: int) -> None:
        self.heap.append(value)
        self.current_size += 1
        self.heapify_up(self.current_size)


    def pop(self) -> Optional[int]:
        if len(self.heap) == 1:
            return
        
        root = self.heap[1]
        data = self.heap.pop()
        if len(self.heap) == 1:
            return root

        self.heap[1] = data
        self.current_size -= 1
        self.heapify_down(1)

        return root


    def status(self) -> None:
        print('-------------')
        print(self.heap)
        print(f'current_size: {self.current_size}')


if __name__ == '__main__':
    h = MiniHeap()
    # datas = [5, 6, 2, 9, 13, 11, 1]
    # for data in datas:
    #     h.push(data)
    
    # print('###### sakai')
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
