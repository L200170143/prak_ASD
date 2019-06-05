class _SimpulPohonBiner(object) :
    def __init__(self, data) :
        self.data = data
        self.kiri = None
        self.kanan = None

def tinggiPohon(akar):
    if akar is None :
        return 0
    else :
        kiri = tinggiPohon(akar.kiri)
        kanan = tinggiPohon(akar.kanan)
        if kiri > kanan :
            return kiri+1
        else :
            return kanan+1

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
