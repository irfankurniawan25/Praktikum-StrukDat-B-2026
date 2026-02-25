from kurs import mata_uang

def konverter(dari, ke, jumlah):
    if dari in mata_uang and ke in mata_uang:
        idr = jumlah * mata_uang[dari] # diubah dulu ke rupiah
        hasil = idr / mata_uang[ke]    # baru dikonversi ke mata uang yang lain
        return hasil
    else:
        print("\nHarap masukkan mata uang yang benar!")

def format_rupiah(jumlah):
    return f'RP {jumlah:,.0f}'.replace(',', '.')