# BOJ
# 25501 : 재귀의 귀재
# 어떤 문자열이 팰린드롬인지 여부를 판단

# NOTE
# recursion 메서드의 l+1이 곧 cnt이므로, cnt 변수 선언 필요 없음
# cnt를 사용하지 않음으로써 메모리와 실행시간 단축 가능함 

def recursion(s, l, r):
    # global cnt
    # cnt += 1``
    if l >= r: return 1, l+1
    elif s[l] != s[r]: return 0, l+1
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    # global cnt
    # cnt = 0
    return recursion(s, 0, len(s)-1)

T = int(input())
S = []
# global cnt

for i in range(T) :
    s = input()
    S.append(s)
    
for i in range(T) :
    x, y = isPalindrome(S[i])
    print(x, y)
