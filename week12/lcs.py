def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)
    # L[i][j] = LCS of X[0..i-1] and Y[0..j-1]
    L = [[None] * (n + 1) for _ in range(m + 1)] # 테이블 생성

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0: # base case: 하나의 길이라도 0이면
                L[i][j] = 0 # LCS --> 0
            elif X[i - 1] == Y[j - 1]: # 마지막 글자가 같으면
                L[i][j] = L[i - 1][j - 1] + 1
            else: # 마지막 글자가 다르면
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    for i in range(m + 1):
        print(L[i])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    print("LCS = ", lcs_dp_traceback(X, Y, L))


def lcs_dp_traceback(X, Y, L):
    lcs = ""  # 1
    i = len(X)  # 2
    j = len(Y)  # 2

    while i > 0 and j > 0:
        v = L[i][j]

        # # 3: 문자가 매칭되는 경우 (LCS 길이가 이전 대각선보다 1 커졌을 때)
        # 이 조건은 L[i-1][j]와 L[i][j-1] 보다 v가 클 경우를 의미함
        if v > L[i][j - 1] and v > L[i - 1][j] and v > L[i - 1][j - 1]:
            i -= 1
            j -= 1
            lcs = X[i] + lcs  # 찾은 문자를 LCS 앞에 추가 (역순으로 탐색했기 때문에)

        # # 4: Y의 마지막 문자를 스킵하는 경우 (왼쪽 L[i][j-1]의 값과 같고, 위쪽 L[i-1][j]보다 클 때)
        elif v == L[i][j - 1] and v > L[i - 1][j]:
            j -= 1

            # # 5: X의 마지막 문자를 스킵하는 경우 (기타/위쪽 L[i-1][j]의 값과 같을 때)
        else:
            i -= 1

    return lcs

X = 'GAME OVER'
Y = 'HELLO WORLD'
print("X = ", X)
print("Y = ", Y)
print("LCS(동적 계획)", lcs_dp(X, Y))
