from collections import deque


def reverse_deque(queue: deque) -> deque:
    q = deque()
    while queue:
        q.append(queue.pop())
    return q


if __name__ == '__main__':

    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)
    print(reverse_deque(q))
