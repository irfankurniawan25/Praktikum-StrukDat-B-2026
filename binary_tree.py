class Node:
    def __init__(self, data):
        self.data =data
        self.left = None
        self.right = None

def traverse_preorder(node, hasil):
    if node is not None:
        hasil.append(node.data)
        traverse_preorder(node.left, hasil)
        traverse_preorder(node.right, hasil)
    return hasil

def traverse_inorder(node, hasil):
    if node is not None:
        traverse_inorder(node.left, hasil)
        hasil.append(node.data)
        traverse_inorder(node.right, hasil)
    return hasil

def traverse_postorder(node, hasil):
    if node is not None:
        traverse_postorder(node.left, hasil)
        traverse_postorder(node.right, hasil)
        hasil.append(node.data)
    return hasil

def insert_manual():
    root = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    F = Node('F')
    
    root.left = B
    root.right = C
    
    B.left = D
    B.right = E
    
    C.right = F
    return root

def get_leaf_nodes(node, hasil):
    if node is not None:
        if node.left is None and node.right is None:
            hasil.append(node.data)
        get_leaf_nodes(node.left, hasil)
        get_leaf_nodes(node.right, hasil)
    return hasil

# Program Utama

print('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
print('======================================')
print('[INFO] Membangun Struktur Gudang...')
print('[INFO] Struktur berhasil dibuat.\n')
print('Hasil Audit:')

pre = traverse_preorder(insert_manual(), [])
inor = traverse_inorder(insert_manual(), [])
post = traverse_postorder(insert_manual(), [])
ujung = get_leaf_nodes(insert_manual(), [])

print(f'1. pre-order  : {' - '.join(pre)}')
print(f'2. in-order   : {' - '.join(inor)}')
print(f'3. post-order : {' - '.join(post)}')

print(f'\n[DATA] Gudang Ujuang (Leaf Nodes) : {' - '.join(ujung)}')

print('''======================================
Audit Selesai!
''')