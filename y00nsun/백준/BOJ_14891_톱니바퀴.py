# BOJ
# 14891: 톱니 바퀴


def rotate(t, v):
    if v == 1 :  # 시계 방향
        return t[-1] + t[:-1]
    elif v == -1 :  # 반시계 방향
        return t[1:] + t[0]

def l_check(t, left_t):
    if t[6] == left_t[2]:
        return False
    else:
        return True

def r_check(t, right_t):
    if t[2] == right_t[6]:
        return False
    else:
        return True


lst = []
for _ in range(4):
    lst.append(input())

k = int(input())
N = []
V = []
for _ in range(k):
    n1, v1 = map(int, input().split())
    n1 -= 1
    N.append(n1)
    V.append(v1)

result = 0
for a in range(k):
    n = N[a]
    v = V[a]

    # Check state
    state = [False for _ in range(4)]
    state[n] = True
    if n == 0:
        if (r_check(lst[0], lst[1])):
            state[1] = True
            if (r_check(lst[1], lst[2])):
                state[2] = True
                if (r_check(lst[2], lst[3])):
                    state[3] = True
    elif n == 1:
        if (r_check(lst[1], lst[2])):
                state[2] = True
                if (r_check(lst[2], lst[3])):
                    state[3] = True
        if (l_check(lst[1], lst[0])):
            state[0] = True
    elif n == 2:
        if (r_check(lst[2], lst[3])):
            state[3] = True
        if (l_check(lst[2], lst[1])):
            state[1] = True
            if (l_check(lst[1], lst[0])):
                state[0] = True
    else :
        if (l_check(lst[3], lst[2])):
            state[2] = True
            if (l_check(lst[2], lst[1])):
                state[1] = True
                if (l_check(lst[1], lst[0])):
                    state[0] = True

    if n == 0  or n == 2:
        v_lst = [v, -v, v, -v]
    elif n == 1 or n == 3:
        v_lst = [-v, v, -v, v]

    # print("vlist =", v_lst)
    # print("state = ", state)
    for i in range(4):
        if state[i]:
            lst[i] = rotate(lst[i], v_lst[i])


if lst[0][0] == '1':
    result += 1
if lst[1][0] == '1':
    result += 2
if lst[2][0] == '1':
    result += 4
if lst[3][0] == '1':
    result += 8

print(result)

    
