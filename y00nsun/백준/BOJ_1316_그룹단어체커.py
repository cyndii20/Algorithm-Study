# BOJ
# 1316 : 그룹 단어 체커

n = int(input())
words = []

for _ in range(n):
    words.append(input())

cnt = 0
for word in words:
    tmp = word[0]
    token = []
    for alph in word:
        if alph not in token:  # 그룹 변경됨
            token.append(tmp)
            tmp = alph
            continue
        elif (alph != tmp) and (alph in token):  # 떨어져 나타남
            break
    else :
        cnt += 1  # 반복문을 무사히 마치면 그룹 단어임

print(cnt)



'''
Solution 2
'''

# cnt = 0
# for word in words:
#     check = []
#     flag = True
#     for alph in word:
#         if alph not in check:
#             check.append(alph)
#         else:
#             if alph != check[-1]:
#                 flag = False
#                 break
#     if flag:
#         cnt += 1

# print(cnt)