mahasiswa = {
"A001": {"nama": "Budi", "prodi": "Informatika",     "ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "SistemInformasi", "ipk": 3.20},
"A003": {"nama": "Andi", "prodi": "Informatika",     "ipk": 3.75}
}

for data in mahasiswa.values():
    if data["ipk"] > 3.5:
        print(f'mahasiswa dengan ipk di atas 3.5 yaitu {data['nama']}')
        
print(f'{[data['nama'] for data in mahasiswa.values() if data['ipk'] > 3.5]}')

        
totalIpk = sum(data["ipk"] for data in mahasiswa.values()) / len(mahasiswa)
rataRata = totalIpk / len(mahasiswa)

print(f'rata-rata ipk seluruh mahasiswa adalah: {round(totalIpk, 2)}')

mahasiswa["A004"] = {"nama": "toni", "prodi": "TeknikKomputer", "ipk": 3.80}

print(mahasiswa)