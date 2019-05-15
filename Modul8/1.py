class Stack(object):
    def __init__(self):
        self.items =[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.items)
    def peek(self):
        assert not self.isEmpy(), "Stack Kosong, Tidak Bisa DIINTIP!"
        return self.items[-1]
    def pop(self):
        assert not self.isEmpty(), "Stact kosong, Tidaak bisa DIPOP!!!"
        return self.items.pop()
    def push(self, data):
        self.items.append(data)

def cetakHexa(d):
    f = Stack()
    bil_Hexa = ['A','B','C','D','E','F']
    if d==0: f.push(0);
    while d!=0:
        sisa = d%16
        if (sisa>9):
            sisa = sisa-10
            sisa = bil_Hexa[sisa]
           
        d=d//16
        f.push(sisa)
    st = ""
    for i in range(len(f)):
        st = st+str(f.pop())
    return st
