def bar(n):
    if n <= 0:
        return 0
    if n == 1:
        return 2  # B, Y (2가지)
    if n == 2:
        return 5  # BB, BY, YB, YY, R (5가지)

    # f(1)과 f(2)를 초기값으로 설정
    f_prev_2 = 2  # f(i-2) 값 저장 (f(1))
    f_prev_1 = 5  # f(i-1) 값 저장 (f(2))

    # 3부터 n까지 반복 계산
    for i in range(3, n + 1):
        # 점화식 적용
        f_current = 2 * f_prev_1 + f_prev_2

        # 다음 반복을 위해 값 업데이트
        f_prev_2 = f_prev_1
        f_prev_1 = f_current

    return f_current

# f(6) 값 구하기
n = 3
result = bar(n)

print(f"f({n})의 값은 {result} 입니다.")
