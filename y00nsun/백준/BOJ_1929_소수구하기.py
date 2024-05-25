# BOJ
# # 1929: 소수 구하기 (에라토스테네스의 체)

import math

M, N = map(int, input().split())

for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(math.sqrt(i))+1):
        if (i % j == 0):
            break
    else:
        print(i)