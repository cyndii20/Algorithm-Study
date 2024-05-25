# BOJ
# 10870 : 피보나치 수 5

# Case 1
##########################################
def fib(i):
    if i <= 1:
        return i
    return fib(i-1) + fib(i-2)

n = int(input()) 
print(fib(n))


# Case 2
###########################################
# a, b = 0, 1
# n = int(input())
# for i in range(n):
#     a, b = b, a + b
# print(a)