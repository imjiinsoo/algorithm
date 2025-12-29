# 분할정복기법
def knapsack_dq(W,wt,val,n):
    if n == 0 or W == 0:
        return 0
    if (wt[n-1] > W):
        return knapsack_dq(W,wt,val,n-1)
    else:
        # 1번 우주: 이 물건을 안 넣는 경우 (Exclude)
        valWithout = knapsack_dq(W,wt,val,n-1)

        # 2번 우주: 이 물건을 넣는 경우 (Include)
        # 내 가치(val) + (내 무게를 뺀 나머지 용량으로 구한 최대 가치)
        valWith = val[n-1] + knapsack_dq(W-wt[n-1],wt,val,n-1)

        return max(valWith, valWithout)

# 동적 계획법
def knapSack_dp(W,wt,val,n):
    A = [[0 for x in range(W+1)] for x in range(n+1)] # ppt 표처럼 w, item 행 열 그래프 만들기

    for i in range(1, n+1): # 한 행씩 (item하나씩 개방)
        for w in range(1, W+1): # 한 열씩. w는 수용 가능 최대 무게
            if wt[i-1] > w: # 수용 가능 무게보다 추가하려는게 무게가 많이 나가면
                A[i][w] = A[i-1][w] #  한 행 위에거 갖다 쓰기
            else: # 수용 가능 무게보다 추가하려는게 무게가 많이 나가지는 않으면
                valWith = val[i-1] + A[i-1][w-wt[i-1]] # 추가한거랑
                valWithout = A[i-1][w] # 추가 안 한거랑 크기 비교해서 더 큰거 선택
                A[i][w] = max(valWith, valWithout)

    return A[n][W]

val = [60, 100, 190, 120, 200, 150]
wt = [2, 5, 8, 4, 7, 6]
W = 18
n = len(val)
print("0-1배낭문제(분할 정복): ", knapsack_dq(W, wt, val, n))
print("0-1배낭문제(동적 계획): ", knapSack_dp(W, wt, val, n))

