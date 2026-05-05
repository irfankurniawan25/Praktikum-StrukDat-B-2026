class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        
    def insert_BST(self, data):
        # langkah 1
        new = Node(data)
        
        # langkah 2
        if self.root is None:
            self.root = new
            return
        
        # langkah 3
        P = Q = self.root
        
        # langkah 4
        while Q != None and new.data != P.data:
            # langkah 5
            P = Q
            
            # langkah 6
            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right
                
        # langkah 7
        if new.data == P.data:
            print('data sama.')
            return
        
        # jika tidak
        if new.data < P.data:
            P.left =new
        else:
            P.right = new
        # selesai

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=' ')
        in_order(node.right)

bst = BST()

bst.insert_BST(5)
bst.insert_BST(23)
bst.insert_BST(6)
bst.insert_BST(65)
bst.insert_BST(19)

in_order(bst.root)