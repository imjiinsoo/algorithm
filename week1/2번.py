def gcd(a,b): # (60,28)
    alist = [] # 60의 약수
    blist = [] # 28의 약수
    clist = [] # 공약수 리스트
    for i in range(1,a+1):
        if a != i and a % i == 0:
            alist.append(i)

    for i in range(alist[-1],0,-1):
        if b != i and b % i == 0:
            blist.append(i)
        blist = sorted(blist)

    print(f'{a}의 약수는: {alist}')
    print(f'{b}의 약수는: {blist}')
    for i in range(len(alist)):
        if alist[i] in blist:
            clist.append(alist[i])
    print(f'{a}와 {b}의 최대 공약수 = {clist[-1]}')

gcd(60,28)
