class Karyawan:
    _nama = ""
    _umur = ""
    _jenisKelamin = ""
    _upahPerHari = ""

    def __init__(self, nama, umur):
        self._nama = nama
        self._umur = umur
        self._jenisKelamin = None
        self._upahPerHari= None
    
    def setNama(self, nama):
        self._nama = nama

    def setUmur(self, umur):
        self._umur = umur

    def setJenisKelamin(self, jenisKelamin):
        self._jenisKelamin = jenisKelamin

    def setUpahPerHari(self, upahPerHari):
        self._upahPerHari = upahPerHari

    def getNama(self):
        return self._nama

    def getUmur(self):
        return self._umur

    def getJenisKelamin(self):
        return self._jenisKelamin

    def getUpahPerHari(self):
        return self._upahPerHari
    
    def printInfo(self):
        print("="*12+" INFO "+"="*12)
        print("Nama\t\t:",self.getNama())
        print("Umur\t\t:",self.getUmur())
        print("Jenis Kelamin\t:",self.getJenisKelamin())
        print("Upah Perhari\t:",self.getUpahPerHari())
    
    def hitungGajiBulanan(self, hari):
        if self._upahPerHari == None:
            print("ERROR! Upah per Hari belum di inputkan!")
        else:
            print("Gaji bulan Ini : Rp",self.getUpahPerHari()*hari)


orang1 = Karyawan("Haniif", 90)
orang1.printInfo()

orang2 = Karyawan("Sindu", 190)
orang2.setJenisKelamin("Laki-laki")
orang2.setUpahPerHari(30000)
orang2.printInfo()

orang1.hitungGajiBulanan(28)
orang2.hitungGajiBulanan(30)