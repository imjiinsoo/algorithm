# 걍 앞에서부터 하나씩 넣어서 조합해보고(크기가 M보다 작을때까지) 그 합이 M인것만 찾기
def all_sum_of_subsets(S,M):
    DFS_sum_of_subsets(S,M,0,[],sum(S))

def DFS_sum_of_subsets(S,M,level,sol,remaining):
    print(sol) # 중간중간 sol 체크용
    if sum(sol) == M:
        print(sol)
        return
    if sum(sol)>M or (remaining+sum(sol)) < M:
        return

    for i in range(level, len(S)):
        sol.append(S[i])
        DFS_sum_of_subsets(S,M,i+1,sol,remaining-S[i])
        sol.pop()

nums = [3,34,4,12,5,2]
M=9
print("입력 집합: ", nums, "M = ",M)
solution = all_sum_of_subsets(nums, M)
