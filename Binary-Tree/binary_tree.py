# coding: utf-8
# Your code here!

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.left = None
        self.right = None
    
    def insert(self, node):
        if node.id < self.id:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
                node.parent = self
        else:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node
                node.parent = self
    
    def walk_inorder(self, result):
        if self.left:
            self.left.walk_inorder(result)
        result.append(self.id)
        if self.right:
            self.right.walk_inorder(result)
    
    def walk_preorder(self, result):
        result.append(self.id)
        if self.left:
            self.left.walk_preorder(result)
        if self.right:
            self.right.walk_preorder(result)

    def find_node(self, id):
        if self.id == id:
            return True
        if id < self.id:
            if self.left and self.left.find_node(id):
                return True
        else:
            if self.right and self.right.find_node(id):
                return True
        return False

def main():
    n = int(input())
    root = None
    for _ in range(n):
        cmd = input()
        if cmd[0] == 'p' and root:
            result = []
            root.walk_inorder(result)
            print('', *result)
            
            result = []
            root.walk_preorder(result)
            print('', *result)
        elif cmd[0] == 'i':
            id = int(cmd.split()[1])
            node = Node(id)
            if root:
                root.insert(node)
            else:
                root = node
        elif cmd[0] == 'f':
            id = int(cmd.split()[1])
            if root.find_node(id):
                print('yes')
            else:
                print('no')

if __name__=='__main__':
    main()
    