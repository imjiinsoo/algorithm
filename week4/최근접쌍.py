import math

# 두 점 거리 구하는 공식
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def closest_pair(p):
    n = len(p)
    # 원래 float(실수)인데 inf, -inf, nan같은 특수 문자열은 넣을 수 있다고 함. 그래서 초기값에 그냥 min_dist에 무한으로 큰 수를 넣어놓기
    min_dist = float("inf")

    # 거리 계산 로직
    for i in range(n-1):
        for j in range(i+1, n):
            dist = distance(p[i], p[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist

p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print("최근접 거리:", closest_pair(p))
