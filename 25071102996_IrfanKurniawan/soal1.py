def tambah_buku(nama, harga, stok):
    if harga <= 0 or stok <= 0:
        print('Error: harga harus lebih besar dari 0 dan stok tidak boleh bernilai negatif.')
        return None
    else:
        return {'nama': nama, 'harga': harga, 'stok': stok} 

daftar_buku = []
for i in range(3):
    print(f'\nMasukkan data buku ke-{i+1}')
    nama = input('Nama buku: ')
    harga = int(input('Masukkan harga buku: '))
    stok = int(input('Masukkan stok buku: '))
    
    buku = tambah_buku(nama, harga, stok)
    if buku:
        daftar_buku.append(buku)

print('\nDaftar buku yang berhasil ditambahkan')
if not daftar_buku:
    print('Tidak ada buku yang berhasil ditambahkan!')
else:
    for buku in daftar_buku:
        print(f'Nama buku: {buku['nama']}, Harga: Rp. {buku['harga']}, Stok: {buku['stok']} unit')
