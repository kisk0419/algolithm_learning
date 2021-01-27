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


def inorder(node: Node) -> None:
    if not node:
        return
    inorder(node.left)
    print(node.value)
    inorder(node.right)


def search(node: Node, value: int) -> bool:
    if node is None:
        return False
    
    if node.value == value:
        return True
    elif value < node.value:
        return search(node.left, value)
    else:
        return search(node.right, value)



if __name__ == '__main__':
    root = None
    datas = [3, 6, 5, 7, 1, 10, 2]
    for data in datas:
        root = insert(root, data)

    inorder(root)
    print(search(root, 11))