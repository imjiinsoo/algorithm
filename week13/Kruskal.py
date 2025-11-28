# 나중에 코드 정리하기(출력값 위주로)
import sys
sys.stdin = open('input3.txt', 'r')
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b: parent[b] = a
    else: parent[a] = b
v,e = map(int,input().split())
parent = [i for i in range(v+1)]
print(parent)
myMap = []
result = 0

for _ in range(e):
    a,b,cost = map(int,input().split())
    myMap.append((cost,a,b))
print(myMap)

for edge in myMap:
    cost,a,b=edge
    if find(a) != find(b):
        union(a,b)
        result += cost
    print(a,b,myMap)
print(result)
