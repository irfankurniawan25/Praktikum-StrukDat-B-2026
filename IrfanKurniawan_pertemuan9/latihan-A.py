# Bagian A

class Node:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_tail(self, judul, pengarang):
        node_baru = Node(judul, pengarang)
        if self.head is None:
            self.head = self.tail = node_baru
        else:
            node_baru.prev = self.tail
            self.tail.next = node_baru
            self.tail = node_baru
            
    def print_forward(self):
        print('Daftar Buku (Dari Depan ke Belakang):')
        current = self.head
        while current:
            print(f'- {current.judul} karya {current.pengarang}')
            current = current.next
        print()
        
    def print_backward(self):
        print('Daftar Buku (Dari Belakang ke Depan):')
        current = self.tail
        while current:
            print(f'- {current.judul} karya {current.pengarang}')
            current = current.prev
        print()
        
    def delete_by_judul(self, judul):
        current = self.head
        while current:
            if current.judul == judul:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                    
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                break
            current = current.next

# Progaram Utama

TokoBuku = DoublyLinkedList()
TokoBuku.insert_tail('Laskar Pelangi', 'Andrea Hirata')
TokoBuku.insert_tail('Bumi Manusia', 'Pramoedya Ananta')
TokoBuku.insert_tail('Sang Pemimpi', 'Andrea Hirata')

TokoBuku.print_forward()
TokoBuku.print_backward()

TokoBuku.delete_by_judul('Bumi Manusia')
print('--- Setelah menghapus "Bumi Manusia" ---')
TokoBuku.print_forward()