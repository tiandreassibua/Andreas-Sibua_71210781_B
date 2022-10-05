from NodeMahasiswa import NodeMahasiswa as Node

class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def addElementTail(self, nama, ipk):
        baru = Node(nama, ipk)
        if (self.size == 0):
            self.head = baru
            self.tail = baru
        else:
            self.tail._next = baru
            baru._prev = self.tail
            self.tail = baru
        print("data masuk ke tail\n")
        self.size += 1

    def printDescending(self):
        bantu = self.tail
        print("===== Print Descending =====")
        while (bantu != None):
            print("="*28)
            print("Nama:", bantu._element, "IPK:", bantu._ipk)
            bantu = bantu._prev
        print()
    
    def rataIpk(self):
        n = 0
        jumlah = 0
        bantu = self.tail
        print("===== Print Descending =====")
        while (bantu != None):
            jumlah += bantu._ipk
            n += 1
            bantu = bantu._prev
        rata2 = jumlah / n
        print("="*28)
        print("Rata-rata IPK: {:.1f}".format(rata2))
    
    def deleteLast(self):
        if self.__len__ == 1:
            self.head = None
            self.tail = None
        else:
            hapus = self.tail
            self.tail = self.tail._prev
            hapus._prev = None
            self.tail._next = None
            print(f"# Data {hapus._element} terhapus #\n")
            del hapus
        self.size -= 1



DLLNC = DoubleList()
DLLNC.addElementTail('Shalom', 3.9)
DLLNC.addElementTail('Nabilla', 3.8)
DLLNC.addElementTail('Kurniadi', 3.7)
DLLNC.addElementTail('Harris', 3.6)
DLLNC.printDescending()

DLLNC.deleteLast()
DLLNC.printDescending()

DLLNC.rataIpk()
