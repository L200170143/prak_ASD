class mhsTIF():
    def __init__(self, nama, kotaTinggal, uangSaku):
        self.nama = nama
        self.kotaTinggal = kotaTinggal
        self.uangSaku = uangSaku

c0 = mhsTIF('Ika','Sukoharjo',240000)
c1 = mhsTIF('Budi','Sragen', 230000)
c2 = mhsTIF('Ahmad','Surakarta',250000)
c3 = mhsTIF('Chandra','Surakarta',235000)
c4 = mhsTIF('Eka','Boyolali',240000)
c5 = mhsTIF('Fandi','Salatiga',250000)
c6 = mhsTIF('Deni','Klaten',245000)
c7 = mhsTIF('Galuh','Wonogiri',245000)
c8 = mhsTIF('Janto','Klaten',245000)
c9 = mhsTIF('Hasan','Karanganyar',270000)
c10 = mhsTIF('Khalid','Purwodadi',265000)

daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

#No 1
def kota(n):
    baru = []
    for i in range(len(n)):
        if(n[i].kotaTinggal.lower() == 'klaten'):
            baru.append(i)
    return baru


#No 2
def sakuKecil(n):
    baru = n[0].uangSaku
    for i in range(len(n)):
        if(n[i].uangSaku<baru):
            baru = n[i].uangSaku
    return baru


#No 3
def sakuTerkecil(n):
    baru = n[0].uangSaku
    list = []
    for i in range(len(n)):
        if(n[i].uangSaku==baru):
            list.append(n[i].nama)
        elif(n[i].uangSaku<baru):
            baru = n[i].uangSaku
            list = []
            list.append(n[i].nama)
    return list


#No 4
def sakuKurangDuaLima(n):
    batas = 250000
    list = []
    for i in range(len(n)):
        if(n[i].uangSaku < batas):
            list.append(n[i].nama)
    return list


#No 5
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class LinkedList: 
    def __init__(self): 
        self.head = None
    def pushAw(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
        return self.head
    def search(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return "True"
            current = current.next
        return "False"
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next   
    
llist = LinkedList() 
llist.pushAw(21)
llist.pushAw(22)
llist.pushAw(12)
llist.pushAw(14)
llist.pushAw(2)
llist.pushAw(19)

#No 6
def binSe(list, target):
    low = 0
    high = len(list) - 1
    while(low<=high):
        mid = (low+high)//2
        if(list[mid] == target):
            return "target di index "+str(mid)
        elif(target<list[mid]):
            high = mid - 1
        else:
            low = mid +1
    return "target tidak ditemukan di index berapapun"

#No 7
def binSe(kumpulan, target):
    temp = []
    low = 0
    high = len(kumpulan)-1
    while low <= high :
        mid = (high+low)//2
        if kumpulan[mid] == target:
            midKiri = mid-1
            while kumpulan[midKiri] == target:
                temp.append(midKiri)
                midKiri = midKiri-1
            temp.append(mid)
            midKanan = mid+1
            while kumpulan[midKanan] == target:
                temp.append(midKanan)
                midKanan = midKanan+1
            return temp
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False


