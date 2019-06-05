class _SimpulPohonBiner(object) :
    def __init__(self, data) :
        self.data = data
        self.kiri = None
        self.kanan = None
def ukuranPohon(akar) :
    ukuran = 0
    if akar is not None :
        if akar.kiri is None and akar.kanan is None:
            ukuran += 1
        else :
            hasil = ukuranPohon(akar.kiri)
            ukuran += hasil
            hasil = ukuranPohon(akar.kanan)
            ukuran += hasil
    return ukuran

A = _SimpulPohonBiner('Jakarta')
B = _SimpulPohonBiner('Solo')
C = _SimpulPohonBiner('Cilacap')
D = _SimpulPohonBiner('Semarang')
E = _SimpulPohonBiner('Surabaya')
F = _SimpulPohonBiner('Malang')
G = _SimpulPohonBiner('Magelang')
H = _SimpulPohonBiner('Bandung')
I = _SimpulPohonBiner('Yogyakarta')
J = _SimpulPohonBiner('Banten')

A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; C.kanan = G
E.kiri = H
G.kanan = I
