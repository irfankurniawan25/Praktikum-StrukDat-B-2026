level_diskon = ( 
(500000, 15),   # belanja >= 500.000 -> diskon 15% 
(300000, 10),   # belanja >= 300.000 -> diskon 10% 
(100000,  5),   # belanja >= 100.000 -> diskon  5% 
(0,        0),  # default            
) 

def hitung_diskon(total_belanja, level_diskon, index = 0):
    if index >= len(level_diskon):
        return (0, 0, total_belanja)
    
    min_belanja, persen_diskon = level_diskon[index]
    
    if total_belanja >= min_belanja:
        nominal_diskon = (total_belanja * persen_diskon) / 100
        total_bayar = total_belanja - nominal_diskon
        return (persen_diskon, nominal_diskon, total_bayar)
    else:
        return hitung_diskon(total_belanja, level_diskon, index + 1)

nama = input('Masukkan nama anda: ')
total_belanja = float(input('Total belanja anda: Rp. '))

persen, nominal, bayar = hitung_diskon(total_belanja, level_diskon)

print('\n=== Rincian Diskon ===')
print('Nama Pelanggan:', nama)
print(f'Diskon: {persen}%\n')

if total_belanja < 100000:
    print("Tidak ada diskon!")
else:
    print(f'Total belanja: Rp. {total_belanja:,.2f}')
    print('\n=== Rincian Belanja ===')
    print(f"Diskon: {persen}%")
    print(f"Total yang harus dibayar: Rp. {bayar:,.2f}")