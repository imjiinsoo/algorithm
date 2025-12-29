def isSafe(maze, x, y, mark):
    W,H = len(maze[0]), len(maze)
    # 1. 지도 밖으로 나가는지 검사 (인덱스 에러 방지)
    if x >= 0 and x<W and y >=0 and y<H:
        # 2. 벽(0)이 아닌지 확인 AND 이미 왔던 길(mark==1)이 아닌지 확인
        if maze[y][x]!=0 and mark[y][x]==0:
            return True
    return False

def solve_maze(maze,x,y):
    W,H = len(maze[0]), len(maze)
    # 정답 경로를 그릴 종이(sol)와 방문 기록을 남길 종이(mark)를 0으로 초기화해서 만듦
    sol = [[0 for j in range(W)] for i in range(H)]
    mark = [[0 for j in range(W)] for i in range(H)]

    # 탐험가(DFS_maze)를 출발시킴
    if DFS_maze(maze,x,y,sol,mark) == False:
        print('출구를 찾을 수 없음')
    else:
        for i in sol: print(i)

def DFS_maze(maze, x, y, sol, mark):
    W,H = len(maze[0]), len(maze)

    if not isSafe(maze,x,y,mark):
        return False

    mark[y][x] = 1
    sol[y][x] = 1
    if maze[y][x] == 2:
        return True

    if DFS_maze(maze, x+1, y, sol, mark)==True: return True
    if DFS_maze(maze, x, y+1, sol, mark)==True: return True
    if DFS_maze(maze, x-1, y, sol, mark)==True: return True
    if DFS_maze(maze, x, y-1, sol, mark)==True: return True

    sol[y][x] = 0
    return False

maze = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2],
        [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
solve_maze(maze, 3, 0)
