# BOJ
# 27433 : 팩토리얼2

N = int(input())

def fact(n):
    if n <= 1 :
        return 1
    return n * fact(n-1)

print(fact(N))