mygraph = { "A" : {"B","C"},
            "B" : {"A", "D"},
            "C" : {"A", "D", "E"},
            "D" : {"B", "C", "F"},
            "E" : {"C", "G", "H"},
            "F" : {"D"},
            "G" : {"E", "H"},
            "H" : {"E", "G"}
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
