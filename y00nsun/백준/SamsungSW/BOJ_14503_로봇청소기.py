# BOJ
# 14503 : 로봇 청소기

n, m = map(int, (input().split()))
cur_r, cur_c, cur_d = map(int, (input().split()))  # d -> 0:북, 1:동, 2:남, 3:서
room = [list(map(int, input().split())) for _ in range(n)] # n x m

# 직진 가능 여부
def straight(r, c, d, room):
    if (d == 0):
        r -= 1
    elif (d == 1):
        c += 1
    elif (d == 2):
        r += 1
    else:
        c -= 1

    if room[r][c] == 0 :
        return r, c
    else :
        return False

# 후진 가능 여부
def back(r, c, d, room):
    if (d == 0):
        r += 1
    elif (d == 1):
        c -= 1
    elif (d == 2):
        r -= 1
    else:
        c += 1

    if (room[r][c] == 1): # 후진 불가능
        return False
    else:   # 후진 가능
        return r, c

# 반시계 회전
def rotate(d):
    if (d == 0):
        d = 3
    else :
        d -= 1
    return d


cnt = 0
while (True):
    # 0: 청소 안됨, 1: 벽, 2: 청소 완료
    
    # 현재 칸 청소 안됨
    if room[cur_r][cur_c] == 0:
        room[cur_r][cur_c] = 2
        cnt += 1
        print(f"({cur_r}, {cur_c}) 청소")
        print(f"d = {cur_d}")
        for i in range(n):
            for j in range(m):
                print(room[i][j], end=" ")
            print()
        input()
    else:
        # 주변이 다 청소됨
        if (room[cur_r-1][cur_c] != 0) and (room[cur_r][cur_c+1] != 0) and (room[cur_r+1][cur_c] != 0) and (room[cur_r][cur_c-1] != 0) :
            if (back(cur_r, cur_c, cur_d, room) == False): # 후진 불가
                break
            else: # 후진
                cur_r, cur_c = back(cur_r, cur_c, cur_d, room)
        else:
            # 반시계 90도 회전
            cur_d = rotate(cur_d) 
            # 직진 가능
            if (straight(cur_r, cur_c, cur_d, room) != False):
                cur_r, cur_c = straight(cur_r, cur_c, cur_d, room)  
            
print(cnt)


'''
GPT 해설
'''
# n, m = map(int, input().split())
# cur_r, cur_c, cur_d = map(int, input().split())  # d -> 0:북, 1:동, 2:남, 3:서
# room = [list(map(int, input().split())) for _ in range(n)]  # n x m

# # 방향 벡터 (북, 동, 남, 서)
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]

# def is_valid(r, c):
#     return 0 <= r < n and 0 <= c < m

# def straight(r, c, d):
#     nr, nc = r + dr[d], c + dc[d]
#     if is_valid(nr, nc) and room[nr][nc] == 0:
#         return nr, nc
#     else:
#         return False

# def back(r, c, d):
#     nr, nc = r - dr[d], c - dc[d]
#     if is_valid(nr, nc) and room[nr][nc] != 1:
#         return nr, nc
#     else:
#         return False

# def rotate(d):
#     return (d + 3) % 4  # 반시계 방향 회전

# cnt = 0
# while True:
#     # 현재 칸 청소 안됨
#     if room[cur_r][cur_c] == 0:
#         room[cur_r][cur_c] = 2
#         cnt += 1

#     all_cleaned = True
#     for i in range(4):
#         cur_d = rotate(cur_d)  # 반시계 방향으로 회전
#         next_pos = straight(cur_r, cur_c, cur_d)
#         if next_pos:
#             cur_r, cur_c = next_pos
#             all_cleaned = False
#             break

#     if all_cleaned:
#         back_pos = back(cur_r, cur_c, cur_d)
#         if back_pos:
#             cur_r, cur_c = back_pos
#         else:
#             break

# print(cnt)

