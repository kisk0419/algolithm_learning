from typing import Any, Optional


class Stack(object):
    def __init__(self) -> None:
        self.values = []

    
    def push(self, value: Any) -> None:
        self.values.append(value)


    def pop(self) -> Optional[Any]:
        if self.values:
            return self.values.pop()

    
if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.values)
    print(stack.pop())
    print(stack.values)
    print(stack.pop())
    print(stack.values)
    print(stack.pop())
    print(stack.pop())

