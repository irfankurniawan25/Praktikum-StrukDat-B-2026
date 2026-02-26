from tabulate import tabulate

judul = 'KONVERTER MATA UANG'

mata_uang = {
    'USD' : 16875, 
    'EUR' : 19995, 
    'SGD' : 13360, 
    'JPY' : 109,
    'IDR' : 1
}

header = 'Kode', 'Kurs'

data_tabel = []
for kode, kurs in mata_uang.items():
    if kode != 'IDR':
        kurs_format = format(kurs, ',').replace(',', '.')
        data_tabel.append([kode, kurs_format])
    
    
tabel = (tabulate(data_tabel, headers=header, tablefmt='psql', colalign=('left', 'right')))