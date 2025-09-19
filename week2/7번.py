import time
def insert(bag, e):
    bag.append(e)

myBag = []
start = time.time()
for i in range(1000000):
    insert(myBag, '축구공')
end = time.time()
print("실행시간 = ", end - start)
