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


def min_value(node: Node) -> Node:
    current_node = node
    while current_node.left:
        current_node = current_node.left
    return current_node


def remove(node: Node, value: int) -> Node:
    if node is None:
        return None

    if value < node.value:
        node.left = remove(node.left, value)
    elif node.value < value:
        node.right = remove(node.right, value)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        
        temp = min_value(node.right)
        node.value = temp.value
        node.right = remove(node.right, temp.value)
        
    return node


if __name__ == '__main__':
    root = None
    datas = [3, 6, 5, 7, 1, 10, 2]
    for data in datas:
        root = insert(root, data)

    remove(root, 3)
    inorder(root)