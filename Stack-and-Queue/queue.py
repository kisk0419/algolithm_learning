from typing import Any
from collections import deque


class Queue(object):

    def __init__(self):
        self.queue = []

    
    def enqueue(self, value: Any) -> None:
        self.queue.append(value)


    def dequeue(self) -> Any:
        if self.queue:
            return self.queue.pop(0)


if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.queue)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.queue)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.queue)

    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
    

