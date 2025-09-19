def gcd(a,b): # (60,28)
    alist = [] # 60의 약수
    blist = [] # 28의 약수
    for i in range(1,a+1):
        if a % i == 0:
            alist.append(i)

    for i in range(1,b+1):
        if b % i == 0:
            blist.append(i)

    print(f'{a}의 약수는: {alist}')
    print(f'{b}의 약수는: {blist}')
    for i in range(len(alist)-1,-1,-1):
        if alist[i] in blist:
            return(alist[i])


print(f'{60}와 {28}의 최대 공약수 = {gcd(60,28)}')