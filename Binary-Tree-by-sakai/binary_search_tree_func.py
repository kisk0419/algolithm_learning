class Node(object):
    
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


def insert(node: Node, value: int) -> Node:
    if not node:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node


if __name__ == '__main__':
    root = None
    datas = [3, 6, 5, 7, 1, 10, 2]
    for data in datas:
        root = insert(root, data)

    print(root.value)
    print(root.left.right.value)
    print(root.right.left.value)