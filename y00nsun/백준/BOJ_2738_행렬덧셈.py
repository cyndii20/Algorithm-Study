# BOJ
# 2738: 행렬 덧셈

n, m = map(int, input().split())  # n x m
a = []
b = []
result = [[0]*m for _ in range(n)]

for i in range(n):
    a.append(list(map(int, input().split())))
for j in range(n):
    b.append(list(map(int, input().split())))

for k in range(n):
    for l in range(m):
        result[k][l] = a[k][l] + b[k][l]
        print(result[k][l], end = " ")
    print()