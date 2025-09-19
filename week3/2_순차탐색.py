import time
import random
def seq_serach(a,key):
    for i in range(len(a)):
        if a[i] == key:
            return 1
        return -1
REPEATS = 50000
num = list(range(1,1000))
num2 = [random.randint(1,1000) for _ in range(1000)]

start = time.time()
for _ in range(REPEATS):
    seq_serach(num, 1)
end = time.time()
t1 = end - start

start = time.time()
for _ in range(REPEATS):
    seq_serach(num, 999)
end = time.time()
t2 = end - start

start = time.time()
for _ in range(REPEATS):
    seq_serach(num2, 1)
end = time.time()
t3 = end - start

start = time.time()
for _ in range(REPEATS):
    seq_serach(num2, 999)
end = time.time()
t4 = end - start

print(f"1찾기: 총 {t1:.5f}초")
print(f"999찾기: 총 {t2:.5f}초")
print(f"1찾기(num2): 총 {t3:.5f}초")
print(f"999찾기(num2): 총 {t4:.5f}초")
