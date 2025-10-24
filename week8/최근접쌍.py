import math

def closest_pair(p):
    n = len(p)  # 점의 전체 개수
    mindist = float("inf")  # 최근접 거리 초기화(무한대)
    for i in range(n - 1):
        for j in range(i + 1, n):
            dist = distance(p[i], p[j])  # 유클리드 거리 계산
            if dist < mindist:
                mindist = dist
    return mindist

# Euclidean 거리 계산 함수
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# P는 점들의 집합, d는 거리
def strip_closest(P,d):
    n = len(P)
    d_min = d
    # X축을 기준으로 정렬
    P.sort(key = lambda point: point[1])
    for i in range(n):
        j = i + 1
        while j < n and (P[j][1] - P[i][1]) < d_min:
            dij = distance(P[i], P[j])
            if dij < d_min:
                d_min = dij
            j += 1
    return d_min

def closest_pair_dis(P,n):
    if n <= 3:
        return closest_pair(P)
    mid = n // 2
    mid_x = P[mid][0]
    dl = closest_pair_dis(P[:mid], mid)
    dr = closest_pair_dis(P[mid:], n-mid)
    d = min(dl, dr)
    Pm = []
    for i in range(n):
        if abs(P[i][0]-mid_x) < d:
            Pm.append(P[i])

    ds = strip_closest(Pm, d)
    return min(d, ds)

P = [(2,3), (12,30), (40,50), (5,1), (12,10), (3,4)]
# x값만을 기준으로 작은거부터 정렬
P.sort(key = lambda point:point[0])

print(closest_pair_dis(P,len(P)))