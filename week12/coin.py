def min_coins_dp(coins, W):
    INF = float('inf')
    N = len(coins)

    # DP 테이블 C[i][j] 생성 (최소 동전 개수 저장)
    C = [[INF] * (W + 1) for _ in range(N + 1)]

    # 0원(j=0)은 0개 동전으로 만들 수 있음
    for i in range(N + 1):
        C[i][0] = 0

    for i in range(1, N + 1):
        d_i = coins[i - 1]
        for j in range(1, W + 1):
            # 바로 위에 행꺼 쓰기 (현재 동전 skip한다면)
            skip_coin = C[i - 1][j]

            if j >= d_i:
                use_coin = C[i][j - d_i] + 1
                C[i][j] = min(use_coin, skip_coin)
            else:
                C[i][j] = skip_coin

    final_result = C[N][W]

    # 결과 테이블 출력
    print("--- DP Table C ---")
    for row in C:
        print([x if x != INF else 'INF' for x in row])
    print("------------------")

    if final_result == INF:
        return "해당 금액을 만들 수 없습니다."
    else:
        return final_result


# 문제에서 주어진 입력으로 실행 (동전: 1원, 4원, 6원 / 목표 금액: 8원)
coins_input = [1, 4, 6]
target = 8
min_count = min_coins_dp(coins_input, target)

print(f"\n[동전: {coins_input}, 목표 금액: {target}]")
print(f"최소 동전 개수: {min_count}")