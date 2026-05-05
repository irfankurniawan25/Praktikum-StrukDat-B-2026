class Node:
    def __init__(self, data):
        self.data = data
        self.left = None   # child kiri
        self.right = None  # child kanan

class BST:
    def __init__(self):
        self.root = None

    # INSERT: masukin data ke tree
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, current_node, data):
        # Kalau data lebih kecil, masuk kiri
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        # Kalau data lebih besar, masuk kanan
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)
        # Kalau sama, skip. BST nggak boleh duplikat

    # SEARCH: cari data ada atau nggak
    def search(self, data):
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, current_node, data):
        if current_node is None:
            return False
        if data == current_node.data:
            return True
        elif data < current_node.data:
            return self._search_recursive(current_node.left, data)
        else:
            return self._search_recursive(current_node.right, data)

    # TRAVERSAL
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)   # Kiri
            result.append(node.data)                    # Root
            self._inorder_recursive(node.right, result) # Kanan

    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.data)                    # Root
            self._preorder_recursive(node.left, result) # Kiri
            self._preorder_recursive(node.right, result)# Kanan

    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result) # Kiri
            self._postorder_recursive(node.right, result)# Kanan
            result.append(node.data)                     # Root

# ===== TESTING =====
print("=== BINARY SEARCH TREE ===")
bst = BST()

# Insert data
data_list = [50, 30, 70, 20, 40, 60, 80]
for d in data_list:
    bst.insert(d)

print(f"Data dimasukkan: {data_list}")
# Tree yang kebentuk:
#       50
#      /  \
#    30    70
#   / \    / \
#  20 40  60  80

print(f"Inorder: {bst.inorder()}")     # [20, 30, 40, 50, 60, 70, 80] -> selalu urut
print(f"Preorder: {bst.preorder()}")   # [50, 30, 20, 40, 70, 60, 80]
print(f"Postorder: {bst.postorder()}") # [20, 40, 30, 60, 80, 70, 50]

print(f"Cari 40: {bst.search(40)}") # True
print(f"Cari 99: {bst.search(99)}") # False