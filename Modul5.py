#No 1
class MhsTIF(object):
    def __init__(self, nim):
        self.nim = nim

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        MhsTIF = i
        while MhsTIF > 0 and nilai < A[MhsTIF - 1]:
            A[MhsTIF] = A[MhsTIF-1]
            MhsTIF = MhsTIF-1
        A[MhsTIF] = nilai

   
c0 = 200170001
c1 = 200170003
c2 = 200170007
c3 = 200170005
c4 = 200170002
c5 = 200170006

Daftar = [c0, c1, c2, c3, c4, c5]
insertionSort(Daftar)
print("Berikut adalah NIM Mahasiswa secara urut :","\n",Daftar, "\n")

#No 2
A = ["Ayas", "Nindi" , "Tika" , "Corry" , "Yarin"]
B = ["A143" , "A147 " , "A156" , "A152" , "A155"]
C =[]
C.extend(A)
C.extend(B)

def insertionSort(A) :
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1] :
            A[pos] = A[pos-1]
            pos = pos - 1
        A[pos] =  nilai
insertionSort(C)
print("Nilai C yang telah urut adalah : ","\n",C,"\n")

#No 3
from time import time as detak
from random import shuffle as kocok

def swap(A,p,q):
    tmp = A[p]
    A[q]= A[q]
    A[q]= tmp
    
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range (n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
                
def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil=dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i]<A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil   

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)
            
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai
        
k=[]
for i in range(1, 6001):
    k.append(i)
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub);ak=detak();print("bubble : %g detik" %(ak-aw));
aw = detak();selectionSort(u_bub);ak=detak();print("selection: %g detik" %(ak-aw));
aw = detak();insertionSort(u_bub);ak=detak();print("insertion : %g detik" %(ak-aw));
