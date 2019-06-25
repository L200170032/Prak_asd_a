#Nama : Dimas Kurniawan S
#Nim  : L200170032


#nomer 6
class SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None
   

A = SimpulPohonBiner("Ambarawa")
B = SimpulPohonBiner("Bantul")
C = SimpulPohonBiner("Cimahi")
D = SimpulPohonBiner("Denpasar")
E = SimpulPohonBiner("Enrekang")
F = SimpulPohonBiner("Flores")
G = SimpulPohonBiner("Garut")
H = SimpulPohonBiner("Halmahera Timur")
I = SimpulPohonBiner("Indramayu")
J = SimpulPohonBiner("Jakarta")

A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; C.kanan = G
E.kiri = H
G.kanan = I

def ukuranPohon(akar):
    ukuran = 0
    if akar is not None:
        if akar.kiri is None and akar.kanan is None:
            ukuran +=1
        else:
            hasil = ukuranPohon(akar.kiri)
            ukuran += hasil
            hasil = ukuranPohon(akar.kanan)
            ukuran += hasil
    return ukuran

#nomer 7
def tinggiPohon(akar):
    if akar is None:
        return 0
    else:
        kiri = tinggiPohon(akar.kiri)
        kanan = tinggiPohon(akar.kanan)
        if kiri > kanan :
            return kiri +1
        else:
            return kanan +1

#nomer 8
def cetakDataDanLevel(akar, level =-1):
    level += 1
    if akar is not None:
        print(akar.data, "Level", level)
        cetakDataDanLevel(akar.kiri,level)
        cetakDataDanLevel(akar.kanan,level)
    
