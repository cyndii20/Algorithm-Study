# BOJ
# 14501 : 퇴사

n = int(input())
dp = [0] * (n+1)
T = []
P = []

for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# Top-down
for i in range(n-1, -1, -1):  # 9 ~ 0
    # i 일에 상담하는 것이 퇴사일을 넘기면 상담을 하지 않음
    if i + T[i] > n:
        dp[i] = dp[i+1]
    else:
        # i일에 상담을 하는 것과 안 하는 것 중 큰 것을 선택
        dp[i] = max(dp[i+1], P[i] + dp[i + T[i]])

print(dp[0])
