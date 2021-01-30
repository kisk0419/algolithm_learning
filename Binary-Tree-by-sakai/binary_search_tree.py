
class Node(object):
    
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):
    
    def __init__(self) -> None:
        self.root = None


    def insert(self, value: int) -> None:
        def _insert(node: Node, value: int) -> Node:
            if not node:
                return Node(value)

            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)


    def inorder(self) -> None:
        def _inorder(node: Node) -> None:
            if not node:
                return
            _inorder(node.left)
            print(node.value)
            _inorder(node.right)

        _inorder(self.root)


    def search(self, value: int) -> bool:
        def _search(node: Node, value: int) -> bool:
            if node is None:
                return False
            
            if node.value == value:
                return True
            elif value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        return _search(self.root, value)


    def min_value(self, node: Node) -> Node:
        current_node = node
        while current_node.left:
            current_node = current_node.left
        return current_node


    def remove(self, value: int) -> None:
        def _remove(node: Node, value: int) -> Node:
            if node is None:
                return None

            if value < node.value:
                node.left = _remove(node.left, value)
            elif node.value < value:
                node.right = _remove(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                
                temp = self.min_value(node.right)
                node.value = temp.value
                node.right = _remove(node.right, temp.value)
                
            return node

        self.root = _remove(self.root, value)


if __name__ == '__main__':
    bst = BinarySearchTree()
    datas = [3, 6, 5, 7, 1, 10, 2]
    for data in datas:
        bst.insert(data)

    bst.inorder()
    print(bst.search(6))
    print(bst.search(4))
    bst.remove(6)
    print('###########')
    bst.inorder()