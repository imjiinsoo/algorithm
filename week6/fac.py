# 하향식 축소 정복
def fac1(n):
    if n == 1:
        return 1
    else:
        return n * fac1(n-1)

# 상향식 축소 정복
def fac2(n):
    result = 1
    for k in range(1, n+1):
        result *= k
    return result

print(fac1(5))
print(fac2(5))

