def cetakSiku(x):
    for i in range(0,x):
        print("*"*(i+1))
    
def PersegiEmpat(a,b):
    for i in range (a):
        if i==0 or i==a-1:
            print("@"*b)
        else :
            print("@"+" "*(b-2)+"@")
def jumlahHurufVokal(x):
    vokal="aiueoAIUEO"
    j = 0
    for i in x:
        if i in vokal:
            j+=1
    return (len(x),j)


def jumlahHurufKonsonan(x):
    vokal="aiueoAIUEO"
    j = 0
    for i in x:
        if i not in vokal:
            j+=1
    return (len(x),j)

def rerata(b=[]):
    x=0
    n=0
    if b != []:
        for i in b:
            x+=i
            n+=1
        return x/n
    return "illegal"

from math import sqrt as sq
def apakahPrima(n):
    n=int(n)
    assert n>=0
    primakecil=[2, 3, 5, 7, 11]
    bukanprima=[0, 1, 4, 6, 8, 9, 10]
    if n in primakecil:
        return True
    elif n in bukanprima:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if(n%i==0):
                return False
    return True

def cetakBilanganPrima():
    prima=list()
    for i in range(2,100):
        a = True
        for iter in prima:
            if(i%iter==0):
                a=False
                break
        if(a):
            print(i)
            prima.append(i)

def faktorPrima(n):
    prima=list()
    for i in range(2,n):
        a = True
        for iter in prima:
            if(i%iter==0):
                a=False
                break
        if a and n%i==0:
            prima.append(i)
    return prima

def apakahTerkandung(a,b):
    return a in b

def angka():
    for i in range(1,100):
        if (i%3)!=0 and (i%5)!=0:
            print(i)
        else:
            if (i%15)==0:
                print("python UMS")
            elif (i%3)==0:
                print("python")
            elif (i%5)==0:
                print("UMS")

def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    D=(b**2)-(4*a*c)
    if D<0:
        return "Determinannya negatif"
    return  "Determinannya positif"

def apakahKabisat(a):
    if(a%400==0):
        return True
    if(a%100==0):
        return False
    if(a%4==0):
        return True
    return False

import random
def permainan():
    a=random.randrange(0, 100)
    while(True):
        b=int(input("Masukan tebakan: "))
        if(b>a):
            print("Itu terlalu besar. Coba lagi")
        elif(b<a):
            print("Itu terlalu kecil. Coba lagi")
        else:
            print("Ya. Anda benar")
            break

def katakan(a):
    x={"0":"","1":"Se","2":"Dua ","3":"Tiga ","4":"Empat ","5":"Lima ","6":"Enam ","7":"Tujuh ","8":"Delapan ","9":"Sembilan "}
    y={-1:"",-2:"puluh ",-3:"ratus ",-4:"ribu ",-5:"puluh ",6:"ratus ",7:"juta ",8:"puluhjuta "}
    b=str(a)
    c=""
    i=-1
    while i>= -len(b):
        c=x[b[i]]+y[i]+c
        i-=1
    return c

def formatRupiah(a):
    b=str(a)
    c=""
    i = -1
    while i>= -len(b):
        if((i+1)%3==0 and (i+1)!=0):
            c="."+c
        c=b[i]+c
        i-=1
    return "Rp "+c
