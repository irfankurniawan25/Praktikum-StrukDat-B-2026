kelas_A = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}

matkul_kedua_kelas = kelas_A & kelas_B
matkul_hanya_A = kelas_A.difference(kelas_B)
matkul_hanya_B = kelas_B.difference(kelas_A)
matkul_unik = matkul_hanya_A | matkul_hanya_B

print('mata kuliah yang diambil kedua kelas = ',matkul_kedua_kelas)
print('mata kuliah yang hanya diambil kelas A = ',matkul_hanya_A)
print('mata kuliah unik yang diambil oleh kelas A dan B =', matkul_unik)
