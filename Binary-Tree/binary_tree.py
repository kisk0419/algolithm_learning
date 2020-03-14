# coding: utf-8

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.left = None
        self.right = None
    
    def __str__(self):
        return 'id={}'.format(self.id)

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, node, current_node=None):
        if self.root is None:
            self.root = node
            return
        
        if current_node is None:
            current_node = self.root
            
        if node.id < current_node.id:
            if current_node.left:
                self.insert(node, current_node.left)
            else:
                current_node.left = node
                node.parent = current_node
        else:
            if current_node.right:
                self.insert(node, current_node.right)
            else:
                current_node.right = node
                node.parent = current_node
    
    def delete(self, id, current_node=None):
        if current_node is None:
            current_node = self.root
        
        if id == current_node.id:
            if current_node.left is None and current_node.right is None:
                
                if current_node.parent.left and current_node.parent.left.id == id:
                    current_node.parent.left = None
                else:
                    current_node.parent.right = None
            elif current_node.left and current_node.right:
                result = []
                self.walk_inorder(result, current_node)
                in_id = result[result.index(current_node.id)+1]
                current_node.id = in_id
                self.delete(in_id, current_node.right)
            else:
                child = None
                if current_node.left:
                    child = current_node.left
                else:
                    child = current_node.right
                
                if current_node.parent.left and current_node.parent.left.id == id:
                    child.parent = current_node.parent
                    current_node.parent.left = child
                else:
                    child.parent = current_node.parent
                    current_node.parent.right = child
        elif id < current_node.id:
            if current_node.left:
                self.delete(id, current_node.left)
        elif current_node.id < id:
            if current_node.right:
                self.delete(id, current_node.right)
                
    def walk_inorder(self, result, current_node=None):
        if current_node is None:
            current_node = self.root
        
        if current_node.left:
            self.walk_inorder(result, current_node.left)
            
        result.append(current_node.id)
        
        if current_node.right:
            self.walk_inorder(result, current_node.right)
    
    def walk_preorder(self, result, current_node=None):
        if current_node is None:
            current_node = self.root
        
        result.append(current_node.id)
        
        if current_node.left:
            self.walk_preorder(result, current_node.left)
            
        if current_node.right:
            self.walk_preorder(result, current_node.right)

    def find(self, id, current_node=None):
        if current_node is None:
            current_node = self.root
            
        if current_node.id == id:
            return True
        if id < current_node.id:
            if current_node.left and self.find(id, current_node.left):
                return True
        else:
            if current_node.right and self.find(id, current_node.right):
                return True
        return False

def main():
    n = int(input())
    tree = BinaryTree()
    
    for _ in range(n):
        cmd = input()
        if cmd[0] == 'p':
            result = []
            tree.walk_inorder(result)
            print('', *result)
            
            result = []
            tree.walk_preorder(result)
            print('', *result)
        elif cmd[0] == 'i':
            id = int(cmd.split()[1])
            node = Node(id)
            tree.insert(node)
        elif cmd[0] == 'd':
            id = int(cmd.split()[1])
            tree.delete(id)
        elif cmd[0] == 'f':
            id = int(cmd.split()[1])
            if tree.find(id):
                print('yes')
            else:
                print('no')

if __name__=='__main__':
    main()