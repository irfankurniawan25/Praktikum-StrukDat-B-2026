katalog = [ 
{'nama': 'Belajar Python',  'harga': 75000, 'stok': 5}, 
{'nama': 'Struktur Data',   'harga': 95000, 'stok': 3}, 
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}, 
] 
riwayat_transaksi = set()

def proses_transaksi(katalog, nama_buku, jumlah_beli):
    buku_ditemukan = False
    for buku in katalog:
        if nama_buku in buku['nama'].lower():
            buku_ditemukan = True
            if buku['stok'] >= jumlah_beli:
                buku['stok'] -= jumlah_beli
                harga = buku['harga'] * jumlah_beli
                riwayat_transaksi.add(buku['nama'])
                print(f'Total harga untuk {jumlah_beli} {buku['nama']} yang harus dibayar Rp. {harga:,.2f}')
            else:
                print(f"stok buku {buku['nama']} tidak cukup")
            break
        
    if not buku_ditemukan:
        print(f'Buku {nama_buku} tidak ditemukan!')
        
for i in range(3):
    print(f'\n===Transaksi ke-{i+1} ===')
    nama_buku = input('buku yang dibeli: '.lower())
    jumlah_beli = int(input('jumlah buku yang dibeli: '))
    proses_transaksi(katalog, nama_buku, jumlah_beli)


print(f'\n=== Riwayat Transaksi ===\n{riwayat_transaksi}')
# if hasil:
#     print('Total harga yang harus dibayar Rp.', hasil)
# else:
#     print('Buku tidak ditemukan')