import random

def radix_sort(A):
    buckets = [[] for _ in range(BUCKETS)]
    n = len(A)
    factor = 1
    # 자리수만큼 반복
    for d in range(DIGITS):
        for i in range(n):
            buckets[(A[i] // factor) % BUCKETS].append(A[i]) # 숫자를 factor로 나누면 지금 비교중인 n번째 자리의 숫자가 나오고, 그 숫자에 맞는 buckets에 숫자를 추가함

        # 버킷에 담긴 순서대로 원본 리스트 A를 재정렬하고 다시 버킷 비움
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
print('sorted: ', data)