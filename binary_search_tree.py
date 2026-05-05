class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, id_buku, judul):
        new = Node(id_buku, judul)
        
        print(f'[INSERT] Berhasil Memasukkan: ID {id_buku} - {judul}')
        
        if not self.root:
            self.root = new
            return
        
        P = Q = self.root
        
        while Q != None and new.id_buku != P.id_buku:
            P = Q
            
            if new.id_buku < P.id_buku:
                Q = P.left
            else:
                Q = P.right
        
        if new.id_buku == P.id_buku:
            print('data sama.')
            return
        
        if new.id_buku < P.id_buku:
            P.left = new
        else:
            P.right = new
    
    def search(self, id_buku):
        print(f'[SEARCH] Mencari ID {id_buku}...', end=' ')
        
        node = self.root
        while node is not None:
            if id_buku == node.id_buku:
                print(f'Ditemukan! Judul: {node.judul}')
                return
            
            elif id_buku < node.id_buku:
                node = node.left
            else:
                node = node.right
        
        print('Data tidak ditemukan.')
        return

def traversal_inorder(node, hasil):
    if node is not None:
        traversal_inorder(node.left, hasil)
        hasil.append([node.id_buku, node.judul])
        traversal_inorder(node.right, hasil)
    return hasil

def get_min(node):
    current = node
    while current and current.left:
        current = current.left
    return current.id_buku 

def get_max(node):
    current = node
    while current and current.right:
        current = current.right
    return current.id_buku 

def height(node):
    if node is None:
        return -1
    
    tinggi_kiri = height(node.left)
    tinggi_kanan = height(node.right)
    
    if tinggi_kiri > tinggi_kanan:
        return tinggi_kiri + 1
    else:
        return tinggi_kanan + 1


# Program Utama

bst = BST()

print('''SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"
=========================================''')

bst.insert(50, 'Dasar Pemrograman')
bst.insert(30, 'Struktur Data')
bst.insert(70, 'Kecerdasan Buatan')
bst.insert(20, 'MAtematika Diskrit')
bst.insert(40, 'Basis Data')
bst.insert(60, 'Jaringan Komputer')
bst.insert(80, 'Sistem Operasi')

print('\n[INFO] Koleksi Buku (In-Order Traversal) :')
trav = traversal_inorder(bst.root, [])
for i in range(len(trav)):
    print(f'{i+1}. {trav[i][0]} - {trav[i][1]}')
print()

bst.search(60)
bst.search(100)

print(f'\n[STATISTIK] ID Terkecil: {get_min(bst.root)}')
print(f'[STATISTIK] ID Terbeasar: {get_max(bst.root)}')
print(f'[INFO] Tinggi (height) Tree: {height(bst.root)}')
print('''===========================================
Simulasi Selesai!''')