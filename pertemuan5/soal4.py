# 4. Diberikan data buku dalam bentuk dictionary:
transaksi = [
{"produk": "Buku", "harga": 10000, "jumlah": 3},
{"produk": "Pena", "harga": 5000, "jumlah": 10},
{"produk": "Penghapus", "harga": 2000, "jumlah": 2}
]

# a. Ubah jumlah buku menjadi 8.
for data in transaksi:
    if data['produk'] == 'Buku':
        data.update({'jumlah': 8})
    print(data)

# b. Tambahkan 2 produk baru.
transaksi.append({'produk' : 'hvs', 'harga' : 500, 'jumlah' : 12})
transaksi.append({'produk' : 'pensil', 'harga' : 2500, 'jumlah' : 12})

# c. Hitung Total Pendapatan (Harga x Jumlah) untuk setiap transaksi menggunakan
# perulangan.
# Tampilkan ringkasan seperti ini:
# Produk: Buku | Total: 30000 Produk: Pena | Total: 50000 ... dan seterusnya.

for data in range(len(transaksi)):
    total = transaksi[data]['harga'] * transaksi[data]['jumlah']
    print(f'produk : {transaksi[data]['produk']} | total: {total}')