# BOJ
# 10809 : 알파벳 찾기

S = input()
result = [-1] * 26

# 소문자 알파벳 아스키코드 : a~z = 97~122
for i in range(len(S)):
    if result[ord(S[i])-97] == -1:
        result[ord(S[i])-97] = i

for j in result:
    print(j, end=" ")