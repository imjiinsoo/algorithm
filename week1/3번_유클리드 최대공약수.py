# 유클리드 알고리즘
def gcd(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

print(gcd(60,28))