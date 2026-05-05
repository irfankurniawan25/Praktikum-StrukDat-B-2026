# Bagian B

class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_tail(self, nama):
        node_baru = Node(nama)
        if self.head is None:
            self.head = node_baru
            self.tail = node_baru
            node_baru.next = self.head
        else:
            self.tail.next = node_baru
            self.tail = node_baru
            self.tail.next = self.head
            
    def print_antrian(self):
        if self.head is None:
            print('Antrian kosong.')
            return
        
        current = self.head
        print('Isi Antrian: ', end='')
        while True:
            print(current.nama, end=' -> ')
            current = current.next
            if current == self.head:
                print(f'(kembali ke {self.head.nama})')
                break
        print()
        
    def delete_head(self):
        if self.head is None:
            return
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

# Program Utama

# Tambah pelanggan
antrian = CircularLinkedList()
antrian.insert_tail('Andi')
antrian.insert_tail('Budi')
antrian.insert_tail('Citra')
antrian.insert_tail('Dina')
antrian.print_antrian()

# Tambahkan Edo dia akhir
print('--- Menambahkan Edo ke antrian ---')
antrian.insert_tail('Edo')
antrian.print_antrian()

# Hapus andi
antrian.delete_head()
print('--- Hapus Andi (sudah dilayani) ---')
antrian.print_antrian()