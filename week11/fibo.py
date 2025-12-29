# 분할정복(divide and conquer)
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

# 메모이제이션
def fibo_mem(n):
    if mem[n] == None:
        if n < 2 : # fibo0, 1은 각각 값도 0, 1이라서 그냥 처음부터 지정해주기
            mem[n] = n

        else:
            mem[n] = fibo_mem(n-1) + fibo_mem(n-2)
    return mem[n]

# 테이블화
def fibo_table(n):
    f = [None] * 100
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

mem = [None] * 100
# 같은 문제를 반복해서 계산하기 때문에 비효율적임
print("분할정복 방식: ", end='')
print(fibo(9))

# 하향식 방법, 시/공간 복잡도가 n에서 끝남
print("메모제이션 방식: ", end='')
print(fibo_mem(9))

# 상향식 방법
print("테이블화 방식: ", end='')
print(fibo_table(9))