M=13
table = [None]*M
def hashFn(key):
    return key % M

class Node:
    def __init__(self,data,link=None):
        self.data=data
        self.link=link

def printTable():
    for i in range(M):
        n=table[i]
        if n!=None:
            print("[%2d]"%i, end="")
            while n is not None:
                print(n.data, end=' ')
                n=n.link
            print()
def insert(key):
    k = hashFn(key)
    n = Node(key)
    n.link = table[k]
    table[k]=n
def search(key):
    k = hashFn(key)
    n = table[k]
    while n is not None:
        if n.data == key : return n.data
        n=n.link
    return None
def delete(key):
    k = hashFn(key)
    n=table[k]
    before = None
    while n is not None:
        if n.data ==key:
            if before ==None:
                table[k]=n.link
            else:
                before.link = n.link
            return
        before = n
        n=n.link
data=[45, 27, 88, 9, 71,60,46,38,24 ]
for d in data: insert(d)
printTable()
print("38탐색 -> ", search(38))
print("45삭제")
delete(45)
print("99탐색 -> ", search(99))
printTable()