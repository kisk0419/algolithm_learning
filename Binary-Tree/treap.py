# coding: utf-8

class TreapNode:
    def __init__(self, id, priority):
        self.id = id
        self.priority = priority
        self.left = None
        self.right = None
    
    def __str__(self):
        return 'id={}, priority={}'.format(self.id, self.priority)


    def _rotate_left(self):
        r = self.right
        self.right = r.left
        r.left = self
        return r
    
    def _rotate_right(self):
        l = self.left
        self.left = l.right
        l.right = self
        return l
    
    
    def _delete_node(self):
        if self.left is None and self.right is None:
            return None
        elif self.left is None:
            node = self._rotate_left()
        elif self.right is None:
            node = self._rotate_right()
        else:
            if self.left.priority < self.right.priority:
                node = self._rotate_left()
            else:
                node = self._rotate_right()
                
        return node.delete(self.id)

        
    def insert(self, id, priority):
        if self.id == id:
            return self
            
        if id < self.id:
            if self.left:
                self.left = self.left.insert(id, priority)
            else:
                self.left = TreapNode(id, priority)
            
            if self.priority < self.left.priority:
                return self._rotate_right()
        else:
            if self.right:
                self.right = self.right.insert(id, priority)
            else:
                self.right = TreapNode(id, priority)
                
            if self.priority < self.right.priority:
                return self._rotate_left()
                
        return self

    def delete(self, id):
        if id < self.id:
            if self.left:
                self.left = self.left.delete(id)
        elif id > self.id:
            if self.right:
                self.right = self.right.delete(id)
        else:
            return self._delete_node()
            
        return self
    
                
    def inorder(self, result):
        if self.left:
            self.left.inorder(result)
            
        result.append(self.id)
        
        if self.right:
            self.right.inorder(result)
    
    
    def preorder(self, result):
        result.append(self.id)
        
        if self.left:
            self.left.preorder(result)
            
        if self.right:
            self.right.preorder(result)

    def find(self, id):
        if self.id == id:
            return True
        if id < self.id:
            if self.left and self.left.find(id):
                return True
        else:
            if self.right and self.right.find(id):
                return True
        return False

class Treap:
    def __init__(self):
        self.root = None
    
    def insert_node(self, id, priority):
        if self.root:
            self.root = self.root.insert(id, priority)
        else:
            self.root = TreapNode(id, priority)
    
    def delete_node(self, id):
        if self.root:
            self.root = self.root.delete(id)
    
    def find_node(self, id):
        if self.root:
            return self.root.find(id)
        else:
            return False
            
    def walk_inorder(self):
        result = []
        if self.root:
            self.root.inorder(result)
        return result
    
    def walk_preorder(self):
        result = []
        if self.root:
            self.root.preorder(result)
        return result
    

def main():
    n = int(input())
    treap = Treap()
    
    for _ in range(n):
        cmd = input()
        if cmd[0] == 'p':
            result = treap.walk_inorder()
            print('', *result)
            
            result = treap.walk_preorder()
            print('', *result)

        elif cmd[0] == 'i':
            id, priority = [int(i) for i in cmd.split()[1:3]]
            treap.insert_node(id, priority)
            
        elif cmd[0] == 'd':
            id = int(cmd.split()[1])
            treap.delete_node(id)
            
        elif cmd[0] == 'f':
            id = int(cmd.split()[1])
            if treap.find_node(id):
                print('yes')
            else:
                print('no')

if __name__=='__main__':
    main()