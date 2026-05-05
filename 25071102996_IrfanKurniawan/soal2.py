katalog = [ 
{'nama': 'Belajar Python',  'harga': 75000, 'stok': 5}, 
{'nama': 'Struktur Data',   'harga': 95000, 'stok': 3}, 
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}, 
] 

def cari_buku(katalog, keyword):
    hasil_pencarian = []
    for item in katalog:
        if keyword in  item['nama'].lower():
            hasil_pencarian.append(item)
    return hasil_pencarian

keyword = input('Masukkan keyword: '.lower())

buku = cari_buku(katalog, keyword)

if buku:
    for item in buku:
        print(f'buku {item['nama']} - Rp. {item['harga']} | stok: {item['stok']}')
else:
    print('Buku tidak ditemukan!')