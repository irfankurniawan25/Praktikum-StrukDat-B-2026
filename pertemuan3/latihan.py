class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        
    def ubah_prodi(self, prodibaru):
        self.prodi = prodibaru
        
    def getNama(self):
        return self.nama
        
    def getProdi(self):
        return self.prodi
    
        
m1 = Mahasiswa("irfan", "25071102996", 'teknik informatika')
m2 = Mahasiswa("faris", "250711056473", "teknik mesin")
m3 = Mahasiswa('faiz', '25071102141', 'teknik elektro')

print(m1.getNama())
print(m2.getProdi())
m2.ubah_prodi("akuntansi")
print(m2.getProdi())
print(m3.nama)