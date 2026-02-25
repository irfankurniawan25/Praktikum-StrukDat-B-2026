# 1. Diberikan list nilai mahasiswa: nilai_tugas = [70, 85, 90, 65, 80]
nilai_tugas = [70, 85, 90, 65, 80]

# a. Ganti nilai 65 menjadi 75 menggunakan pencarian indeks.
ganti = nilai_tugas.index(65)
nilai_tugas.pop(ganti)
nilai_tugas.insert(ganti, 75)
print(nilai_tugas)

# b. Tambahkan nilai 95 ke dalam list, lalu urutkan list tersebut dari yang terbesar ke terkecil.
nilai_tugas.append(95)
nilai_tugas.sort(reverse=True)
print(nilai_tugas)

# c. Tampilkan jumlah total seluruh nilai dalam list tersebut.
total = sum(nilai_tugas) 
print('jumlah total: ', total)

# d. Tampilkan pesan "Ada nilai sempurna" jika angka 100 ada di dalam list, jika tidak tampilkan "Tidak ada”.
for data in nilai_tugas:
    if data == 100:
        print('Ada nilai sempurna')
else:
    print('Tidak ada')