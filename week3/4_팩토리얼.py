def fac1(n):
    if n == 0: return 1
    else: return n * fac1(n-1)

def fac2(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

print(f"팩토리얼 순환(3) : ", fac1(3))
print(f"팩토리얼2 순환(3) : ", fac2(3))

