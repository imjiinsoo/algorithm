def knapSack_fractional_greedy(obj, W):
    obj.sort(key = lambda o: o[2]/o[1], reverse=True)

    totalValue = 0
    for o in obj:
        if W <= 0: break
        if W - o[1] >= 0:
            W -= o[1]
            totalValue += o[2]
        else:
            fraction = W / o[1]
            totalValue += o[2] * fraction
            W = int(W - o[1] * fraction)

    return totalValue

obj = [("A", 10, 80), ("B", 12, 120), ("C", 8, 60)]
print(knapSack_fractional_greedy(obj, 18))