pasien_hari_ini = [
{"id": "P001", "nama": "Andi",  "usia": 34, "penyakit": "Flu",   "bayar": False},
{"id": "P002", "nama": "Budi",  "usia": 22, "penyakit": "Tifus", "bayar": True},
{"id": "P003", "nama": "Cici",  "usia": 45, "penyakit": "Flu",   "bayar": False},
{"id": "P004", "nama": "Dani",  "usia": 30, "penyakit": "Maag",  "bayar": True},
{"id": "P005", "nama": "Eva",   "usia": 28, "penyakit": "Tifus", "bayar": False},
{"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag",  "bayar": False},
]

#SOAL 1
def tampilkan_pasien(pasien):
    print(f'\n{' ' * 12}=== DATA PASIEN KLINIK ===')
    print('No | ID   | Nama  | Usia | Penyakit | Status Bayar')
    print('---+------+-------+------+----------+-------------')
    
    for i, data in enumerate(pasien, start=1):
        status = 'Lunas' if data['bayar'] else 'Belum'
        # if data['bayar']:
        #     data['bayar'] = 'Lunas'
        # else:
        #     data['bayar'] = 'Belum Bayar'
        print(f'{i}  | {data['id']} | {data['nama'] : <5} | {data['usia']}   | {data['penyakit'] : <5}    | {status}')

def filter_belum_bayar(pasien):
    psn = [data['nama'] for data in pasien if not data['bayar']]
    psn.sort()
    
    print('\n=== Pasien Belum Bayar ===')
    for i,j in enumerate(psn, start=1):
        print(f'{i}. {j}')
        
    print('Total belum bayar:', len(psn), 'pasien')


tampilkan_pasien(pasien_hari_ini)
filter_belum_bayar(pasien_hari_ini)