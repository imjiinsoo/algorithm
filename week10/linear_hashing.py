M = 13
table = [None] * M
def hashFn(key):
    return key%M

def insert(key):
    i = hashFn(key) # 원래 가야 할 자리 계산
    count = M # 무한 루프 방지용 (테이블 꽉 차면 멈춰야 함)
    while count > 0:
        if table[i] == None or table[i] == -1: break
        i = (i+1) % M
        count -= 1
    if count > 0:table[i] = key

def search(key):
    i = hashFn(key)
    count = M
    while count > 0:
        if table[i] == None: return None
        if table[i] == key: return i
        i = (i+1) % M
        count -= 1
    return None

def delete(key):
    i = hashFn(key)
    count = M
    while count > 0:
        if table[i] == key:
            table[i] = -1
            return
        if table[i] == None: return
        i = (i+1) % M
        count -= 1

data = [45,27,88,9,71,60,46,38,24]
for d in data:
    print('h(%2d) = %2d' %(d, hashFn(d)), end=' ')
    insert(d)
    print(table)

print("46탐색-> ", search(46))
print("71삭제-> ", end='')
delete(71)
print(table)