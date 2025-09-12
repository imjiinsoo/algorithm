math = (['3+2',5,3], ['5÷2의 몫',2,5], ['10-2',8,3], ['10^2*2', 200, 2], ['1-(10÷4의 나머지)',-1,5], ['2^4',16,3], ['4÷2', 2, 3],)

ansCnt, wrongCnt, totalScore = 0,0,0
for i in math:
    print(f'문제 : {i[0]}')
    ans = int(input("정답을 입력하세요"))
    if ans == i[1]:
        ansCnt += 1
        totalScore += i[2]

    else: # 틀렸을 때
        wrongCnt += 1

print("-"*20)
print(f"정답 개수: {ansCnt}")
print(f"오답 개수: {wrongCnt}")
print(f"총점: {totalScore}")

