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

nilai = Stack()
for i in range (16):
    if i % 3 == 0:
        nilai.push(i)
print(nilai.items)
