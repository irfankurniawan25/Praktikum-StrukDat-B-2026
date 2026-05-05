antrean_array = ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

def sisipkan_pasien_darurat_array(nama_pasien, posisi):
    antrean_array.insert(posisi - 1, nama_pasien)
    print("antrean akhir:",antrean_array)

print('antrean awal:', antrean_array)

sisipkan_pasien_darurat_array('Pasien D (Darurat)', 2)
print()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class AnrianLinkedList:
    def __init__(self):
        self.head = None
        
    def cetak_antrian(self):
        tampilkan = self.head
        while tampilkan:
            print(tampilkan.data, end=" -> ")
            tampilkan = tampilkan.next
        print("null")
        
    def insert_at_posisi(self, nama, posisi):
        nama = Node(nama)
        
        if posisi == 1:
            nama.next = self.head
            self.head = nama
            return None
        
        akhir = self.head
        hitung = 1
        
        while akhir.next and hitung < posisi - 1:
            akhir = akhir.next
            hitung += 1
            
        nama.next = akhir.next
        akhir.next = nama
        
    def append(self, data):
        nama_pasien = Node(data)
        
        if not self.head:
            self.head = nama_pasien
            return None
        
        akhir = self.head
        while akhir.next:
            akhir = akhir.next
        
        akhir.next = nama_pasien

antrian = AnrianLinkedList()

antrian.append("Pasien A (Stabil)")
antrian.append("Pasien B (Stabil)")
antrian.append("Pasien C (Stabil)")

print('antrian awal.')
antrian.cetak_antrian()

antrian.insert_at_posisi("Pasien R (Darurat)", 1)
antrian.insert_at_posisi("Pasien F (Darurat)", 10)

print('\nantrian setelah update.')
antrian.cetak_antrian()