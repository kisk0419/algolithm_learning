from __future__ import annotations

class Node(object):

    def __init__(self, data: int, parent_node: Node = None, 
        left_node: Node = None, right_node: Node = None):
        
        self.parent = parent_node
        self.left = left_node
        self.right = right_node
        self.data = data

    
class BinarySearchTree(object):

    def __init__(self, root_node: Node = None):
        self.root = root_node


    def insert(self, data: int) -> Node:
        def _insert(current_node: Node, data: int) -> Node:
            if not current_node:
                return Node(data)

            if data < current_node.data:
                current_node.left = _insert(current_node.left, data)
            else:
                current_node.right = _insert(current_node.right, data)
            return current_node

        self.root = _insert(self.root, data)
        

if __name__ == '__main__':
    b = BinarySearchTree()
    datas = [3, 6, 5, 7, 1, 10, 2]
    for data in datas:
        b.insert(data)

    print(b.root.data)
    print(b.root.left.right.data)
    print(b.root.right.left.data)

        
