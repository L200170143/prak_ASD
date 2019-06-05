class _SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

def cetakDataLevel(akar, level = -1):
    level +=1
    if akar is not None:
        print (akar.data, "Level", level)
        cetakDataLevel (akar.kiri,level)
        cetakDataLevel (akar.kanan,level)
        
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
