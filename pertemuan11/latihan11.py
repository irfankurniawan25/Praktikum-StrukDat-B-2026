class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.tail is None:
            self.head = self.tail = self.curren = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.count += 1
        print(f'[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self.count})')
        
    def isEmpty(self):
        print('[CEK] Apakah antrian masih kosong?', end='')
        if self.head is None:
            print('Ya, antrian masih kosong.\n')
        else:
            print('Ada antrian.\n')
    
    def dequeue(self):
        if not self.head:
            return "Belum ada antrian."
        
        temp = self.head
        self.head = temp.next
        self.count -= 1
        
        if self.head is None:
            self.tail = None
            
        print(f'\n[PANGGIL] Dokter memanggil: {temp.nama} (keluhan: {temp.keluhan})')
        return temp
    
    def peek(self):
        if not self.head:
            return "Belum ada antrian."
        
        temp = self.head
        print(f'Pasien berikutnya: {temp.nama} - {temp.keluhan}')
    
    def size(self):
        print(f'\nJumlah pasien menunggu: {self.count} orang')
    
    def printPasien(self):
        if not self.head:
            print('Antrian kosong.')
            return
        
        print('[ANTRIAN SAAT INI]')
        temp = self.head
        nomor = 1
        while temp:
            print(f'{nomor}. {temp.nama} -> {temp.keluhan}')
            temp = temp.next
            nomor += 1
    
    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0
        print(f'[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.')

# Program utama

myQueue = Queue()

print('''
====================================
SISTEM ANTRIAN POLI UMUM
RS Sehat Bersama
====================================
''')

myQueue.isEmpty()

myQueue.enqueue('BUDI', 'demam tinggi')
myQueue.enqueue('ANI', 'batuk pilek')
myQueue.enqueue('CITRA', 'sakit kepala')

myQueue.size()
myQueue.peek()
myQueue.dequeue()
myQueue.enqueue('DODI', 'nyeri perut')
print()
myQueue.printPasien()

myQueue.dequeue()
myQueue.size()
print()
myQueue.clear()

myQueue.isEmpty()
print('''====================================
Simulasi Selesai!
====================================
''')