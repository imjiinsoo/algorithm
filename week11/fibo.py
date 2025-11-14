# 분할정복(divide and conquer)
def fibo(n):
    if n <= 1: return n
    else:
        return fibo(n-1) + fibo(n-2)

# 메모이제이션
def fibo_mem(n):
    if mem[n] == None:
        if n < 2 : mem[n] = n

        else:
            mem[n] = fibo_mem(n-1) + fibo_mem(n-2)
    return mem[n]

mem = [None] * 100

# 같은 문제를 반복해서 계산하기 때문에 비효율적임
print("분할정복 방식: ", end='')
print(fibo(9))

# 시/공간 복잡도가 n에서 끝남
print("메모제이션 방식: ", end='')
print(fibo_mem(9))