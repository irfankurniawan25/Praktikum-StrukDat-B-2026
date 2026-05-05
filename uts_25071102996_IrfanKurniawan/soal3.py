class Pasien:
    jumlah_pasien = 0
    
    def __init__(self, Id, nama, penyakit):
        self.__Id = Id
        self.__nama = nama
        self.__penyakit = penyakit
        Pasien.jumlah_pasien += 1
        
    def get_nilai(self):
        return self.__Id, self.__nama, self.__penyakit
    
    def tampilkan_info(self):
        id, nama, penyakit = self.get_nilai()
        
        print(f'Id: {id}')
        print(f'Nama: {nama}')
        print(f'Penyakit: {penyakit}')
    
    @staticmethod
    def hitung_pasien():
        return Pasien.jumlah_pasien

class PasienPrioritas(Pasien):
    def __init__(self, Id, nama, penyakit, prioritas):
         super().__init__(Id, nama, penyakit)
         self.prioritas = prioritas
         
    def tampilkan_info(self):
        super().tampilkan_info()
        print()
        if self.prioritas.lower() == 'darurat':
            print('** Segera tangani! **')

p1 = Pasien('P001', 'Andi', 'Flu')
p1.tampilkan_info()

p2 = PasienPrioritas('P007', 'Budi', 'Sesak napas', 'Darurat')
p2.tampilkan_info()

print('\nTotal pasien terdaftar:',Pasien.hitung_pasien())