# BOJ
# 1157 : 단어공부

s = input().upper()
dc = {}  # {문자 : 개수}

for i in range(len(s)):
    if s[i] in dc:
        dc[s[i]] += 1
    else :
        dc[s[i]] = 1

num = max(dc.values())
result = [k for k, v in dc.items() if v == num]

if len(result) >= 2 :
    print("?")
else:
    print(result[0])

