def count_apt(n):
    if mem[n] is None:
        if n == 1: mem[n] = 2
        elif n == 2: mem[n] = 3
        else: mem[n] = count_apt(n-1) + count_apt(n-2)
    return mem[n]

n = 8
mem = [None] * (n+1)
print('아파트 칠하는 방법의 수: ', count_apt(8))