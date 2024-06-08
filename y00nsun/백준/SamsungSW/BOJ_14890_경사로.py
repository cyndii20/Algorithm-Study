# BOJ
# 14890 : 경사로 (골드3)
# https://www.acmicpc.net/problem/14890


def can_slope(road, L):
    used = [False] * len(road)
    for i in range(len(road) - 1):
        if road[i] == road[i+1]:  # 높이 같음
            continue
        if abs(road[i] - road[i+1]) > 1: # 높이 차이 1보다 큼
            return False
        if road[i] > road[i+1]:  # 내리막
            for j in range(i+1, i+1+L):
                if j >= len(road) or road[j] != road[i+1] or used[j]:
                    return False
                used[j] = True
        elif road[i] < road[i+1]:  # 오르막
            for j in range(i, i-L, -1):
                if j < 0 or road[j] != road[i] or used[j]:
                    return False
                used[j] = True
    return True


N, L = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
count = 0

for i in range(N):  # 가로길
    if can_slope(map[i], L):
        count += 1

for i in range (N):  # 세로길
    col = [map[j][i] for j in range(N)]
    if can_slope(col, L):
        count += 1

print(count)
