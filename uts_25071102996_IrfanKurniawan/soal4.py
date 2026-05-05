class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class AntrianPasien:
    def __init__(self):
        self.head = None
        
    def tambah(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def tampilkan(self):
        print('\n==== ANTRIAN PASIEN ====')
        current = self.head
        i = 1
        
        while current:
            d = current.data
            print(f'[{i}] {d['id']} - {d['nama']} | {d['penyakit']}')
            current = current.next
            i += 1
            
        print('Total Antrian:', self.hitung())
            
    def panggil_berikutnya(self):
        if not self.head:
            print('Antrian kosong!')
            return
        
        print('\nMemanggil pasien berikutnya...')
        data = self.head.data
        print(f'Silakan masuk: {data['nama']} ({data['id']}) - {data['penyakit']}')
        self.head = self.head.next
        
    def cari(self, nama):
        print(f"\nMencari '{nama}'...")
        current = self.head
        posisi = 1
        
        while current:
            if current.data['nama'] == nama:
                d = current.data
                print(f"Ditemuka: {d['id']} - {d['nama']} | {d['penyakit']} (posisi ke-{posisi})")
                return
            current = current.next
            posisi +=1
            
        print('Tidak ditemukan!')
        
    def hapus_berdasarkan_id(self, id):
        print(f'\nMenghapus pasien dengan ID {id}...')
        
        if not self.head:
            print('Antrian kosong!')
            return
        
        if self.head.data['id'] == id:
            print(f"{self.head.data['nama']} ({id}) berhasil dihapus.")
            self.head = self.head.next
            return
        
        current = self.head
        while current:
            if current.next.data['id'] == id:
                print(f'{current.next.data['nama']} ({id}) berhasil dihapus.')
                current.next = current.next.next
                return
        current = current.next
        
        print("ID tidak ditemukan.")
        
    def hitung(self):
        count = 0
        current = self.head
        while current:
            count +=1 
            current = current.next
        return count


antrian = AntrianPasien()
antrian.tambah({"id": "P001", "nama": "Andi",  "penyakit": 
"Flu"})
antrian.tambah({"id": "P002", "nama": "Budi",  "penyakit": 
"Tifus"})
antrian.tambah({"id": "P003", "nama": "Cici",  "penyakit": 
"Flu"})
antrian.tambah({"id": "P004", "nama": "Dani",  "penyakit": 
"Maag"})
antrian.tampilkan()
antrian.panggil_berikutnya()
antrian.tampilkan()
antrian.hapus_berdasarkan_id("P003")
antrian.tampilkan()
antrian.cari('Dani')
print('\nTotal antrian:', antrian.hitung())

# print('''
# ===== ANTRIAN PASIEN =====
# [1] P001 - Andi  | Flu
# [2] P002 - Budi  | Tifus
# [3] P003 - Cici  | Flu
# [4] P004 - Dani  | Maag
# Total antrian: 4

# Memanggil pasien berikutnya...
# Silakan masuk: Andi (P001) - Flu

# ===== ANTRIAN PASIEN =====
# [1] P002 - Budi  | Tifus
# [2] P003 - Cici  | Flu
# [3] P004 - Dani  | Maag
# Total antrian: 3

# Menghapus pasien dengan ID P003...
# Cici (P003) berhasil dihapus dari antrian.

# ===== ANTRIAN PASIEN =====
# [1] P002 - Budi  | Tifus
# [2] P004 - Dani  | Maag
# Total antrian: 2
# Mencari 'Dani'...
# Ditemukan: P004 - Dani | Maag (posisi ke-2)

# Total antrian: 2
# ''')