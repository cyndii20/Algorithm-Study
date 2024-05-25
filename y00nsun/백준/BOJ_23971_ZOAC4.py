# BOJ
# 23971 : ZOAC 4

import math
H, W, N, M = map(int, input().split())
#math.ceil()함수는 숫자의 올림을 계산해 줍니다
x = math.ceil(H/(N+1))
y = math.ceil(W/(M+1))

result = x*y
print(result)