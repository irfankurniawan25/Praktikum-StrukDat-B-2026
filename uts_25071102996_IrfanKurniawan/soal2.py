pasien_hari_ini = [
{"id": "P001", "nama": "Andi",  "usia": 34, "penyakit": "Flu",   "bayar": False},
{"id": "P002", "nama": "Budi",  "usia": 22, "penyakit": "Tifus", "bayar": True},
{"id": "P003", "nama": "Cici",  "usia": 45, "penyakit": "Flu",   "bayar": False},
{"id": "P004", "nama": "Dani",  "usia": 30, "penyakit": "Maag",  "bayar": True},
{"id": "P005", "nama": "Eva",   "usia": 28, "penyakit": "Tifus", "bayar": False},
{"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag",  "bayar": False},
]

def info_klinik():
    return (
        'Klinik Sehat Bersama', 
        'JL. Merdeka No. 10, Pekanbaru', 
        '0761-12345'
        )

def rekap_penyakit(pasien_hari_ini):
    penyakit_unik = set([item['penyakit'] for item in pasien_hari_ini])
    
    rekap = {}
    for item in pasien_hari_ini:
        penyakit = item['penyakit']
        # rekap[penyakit] = rekap.get(penyakit, 0) + 1
        if penyakit in rekap:
            rekap[penyakit] += 1
        else:
            rekap[penyakit] = 1
    
    max_jumlah = max(rekap.values())
    terbanyak = [k for k,v in rekap.items() if v == max_jumlah]
    # p1 = 0
    # p2 = 0
    # p3 = 0
    
    # # for item in pasien:
    # #     penyakit.add(item['penyakit'])
        
    # for i in pasien_hari_ini:
    #     if i['penyakit'] == 'Flu':
    #         p1 += 1
    #     if i['penyakit'] == 'Tifus':
    #         p2 += 1
    #     if i['penyakit'] == 'Maag':
    #         p3 += 1
    
    return penyakit_unik, rekap, terbanyak, max_jumlah #, p1, p2, p3

info = info_klinik()
print(f'Info Klinik:')
print(f'Nama   : {info[0]}')
print(f'Alamat : {info[1]}')
print(f'Telp   : {info[2]}')

penyakit_unik, rekap, terbanyak, max_jumlah = rekap_penyakit(pasien_hari_ini)

print('\njenis penyakit unik:',penyakit_unik)
print('jumlah jenis penyakit:',len(penyakit_unik))

print('\nRekap per penyakit:')
for k, v in rekap.items():
    print(f'{k : <5} : {v} penyakit')
# for i in penyakit_unik:
#     print(f'{i} : {a if i == 'Flu' else b if i == 'Tifus' else c} pasien')

print(f'\nPenyakit terbanyak: {', '.join(terbanyak)} ({max_jumlah} pasien)')
# for i in penyakit_unik:
#     print(i, end=' ')
# print(f'({int((a + b + c)/3)} pasien)')