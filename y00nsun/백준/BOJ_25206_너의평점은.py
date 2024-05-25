# BOJ
# 25206 : 너의 평점은

import sys

scores = []
cnt = 0
while(cnt < 20) :
        score = list(sys.stdin.readline().split())
        scores.append(float(score[1]))
        cnt+= 1

print(cnt)
print(scores)
sum = 0
for i in range(len(scores)):
    sum += scores[i]
result = sum / len(scores)
print(result)