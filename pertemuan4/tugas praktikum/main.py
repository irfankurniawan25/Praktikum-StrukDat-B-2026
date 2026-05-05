from kurs import tabel, judul
from konverter import konverter, format_rupiah as fr

def main():
    print(f'\n\n=== {judul} ===\n')
    print(f'{tabel}\n')

    dari = input('Dari (IDR/USD/EUR/SGD/JPY): ').upper()
    ke = input('Ke (IDR/USD/EUR/SGD/JPY): ').upper()
    jumlah = float(input('Jumlah = '))

    hasil = konverter(dari, ke, jumlah)

    if dari == 'IDR':
        print(f'\n{fr(jumlah)} = {hasil:.2f} {ke}')
    elif ke == 'IDR':
        print(f'\n{jumlah} {dari} = {fr(hasil)}')
    elif hasil == None:
        hasil
    else:
        print(f'\n{jumlah} {dari} = {round(hasil, 2)} {ke}')
        
if __name__ == '__main__':
    main()