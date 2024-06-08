# BOJ
# 14889 : 스타트와 링크
# https://www.acmicpc.net/problem/14889


def calc_ability(team, s):
    ability = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            ability += s[team[i]][team[j]] + s[team[j]][team[i]]
    return ability


n = int(input()) 
s = [list(map(int, input().split())) for _ in range(n)]
visit = [False] * n

min_dif = float('inf')
comb = 2 ** n   # 가능한 조합 수
for i in range(comb):
    start = []
    link = []

    for j in range(n):
        if i & (2**j):
            start.append(j)
        else:
            link.append(j)
    
    if (len(start) == n//2) and (len(link) == n//2) :
        start_ab = calc_ability(start, s)
        link_ab = calc_ability(link, s)
        min_dif = min(min_dif, abs(start_ab - link_ab))

print(min_dif)
         