# dfs test code
mygraph = { "A" : {"B","D","E"},
            "B" : {"A", "E", "F", "C"},
            "C" : {"B", "G"},
            "D" : {"A", "E"},
            "E" : {"A", "B", "D"},
            "F" : {"B", "G"},
            "G" : {"C", "F"}
          }

def dfs(graph, start, visited):
    if start not in visited:
        visited.add(start)
        print(start, end=" ")
        nbr = sorted(graph[start]-visited) # 집합 그대로 쓰면 답이 매번 바뀌는데, 정렬해버리면 순서가 항상 같음
        for v in nbr:
            dfs(graph, v, visited)

print('DFS : ', end='')
dfs(mygraph, "A", set() )
print()

# bfs test code
import queue

def bfs(graph, start):
    visited = {start}
    que = queue.Queue()
    que.put(start)
    while not que.empty():
        v = que.get()
        print(v, end=" ")
        nbr = sorted(graph[v]-visited)
        for u in nbr:
            visited.add(u)
            que.put(u)

mygraph = { "A" : {"B","D","E"},
            "B" : {"A", "E", "F", "C"},
            "C" : {"B", "G"},
            "D" : {"A", "E"},
            "E" : {"A", "B", "D"},
            "F" : {"B", "G"},
            "G" : {"C", "F"}
          }

# print('BFS : ', end='')
# bfs(mygraph, "A")
# print()
