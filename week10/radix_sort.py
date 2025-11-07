import random

def radix_sort(A):
    buckets = [[] for _ in range(BUCKETS)]
    n = len(A)
    factor = 1
    # 자리수만큼 반복
    for d in range(DIGITS):
        for i in range(n):
            buckets[(A[i] // factor) % BUCKETS].append(A[i])

        j = 0
        for b in range(BUCKETS):
            for num in buckets[b]:
                A[j] = num
                j += 1
        buckets = [[] for _ in range(BUCKETS)]
        factor *= BUCKETS
        print('step', d+1, A)

# 최대 4자리수인 랜덤 수 10개를 data에 넣기
BUCKETS = 10
DIGITS = 4
data = [random.randint(1,9999) for _ in range(10)]
print('original: ', data)
radix_sort(data)
print('sorted: ', )