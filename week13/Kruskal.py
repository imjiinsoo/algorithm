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
myMap.sort()
print(myMap)

print("초기 부모 테이블:", parent)
for edge in myMap:
    cost,a,b=edge
    if find(a) != find(b):
        union(a,b)
        result += cost
        print(f"{a}와 {b} 연결 후 parent 변화: {parent}")
    # print(a,b,myMap)
print(result)
print("--- 최종 부모 노드 확인 ---")
for i in range(1, v + 1):  # 1번 노드부터 v번 노드까지
    print(f"{i}번 노드의 부모: {find(i)}")