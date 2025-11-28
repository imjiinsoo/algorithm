def min_coins_greedy(coins, V):
    count = []
    for i in coins:
        cnt = V//i
        count.append(cnt)
        V -= cnt*i
    return count

coins = [500, 100, 50, 10, 5, 1]
V = 580
print(min_coins_greedy(coins, V))
