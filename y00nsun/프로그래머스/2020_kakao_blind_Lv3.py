# PROGRAMMERS
# 2020 KAKAO BLIND RECRUITMENT
# Lv.3 자물쇠와 열쇠
# https://school.programmers.co.kr/learn/courses/30/lessons/60059

def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]

def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]

def rotate90(arr):
    return list(zip(*arr[::-1]))

def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if (board[M+i][N+j] != 1):  # 종료조건 : lock-key 불일치
                return False
    return True

def solution(key, lock):
    M, N = len(key), len(lock)

    board = [[0] * (M*2 + N) for _ in range(M*2 + N)]  # [ (M*2 + N) x (M*2 +N) ]
    # 중앙에 lock 배치
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]

    rotated_key = key
    # 4번 회전(360도) 루프
    for _ in range(4):
        rotated_key = rotate90(rotated_key)   
        for x in range(1, M+N):
            for y in range(1, M+N):
                # key 넣어보기
                attach(x, y, M, rotated_key, board)
                # key 맞는지 check
                if (check(board, M, N)) :   # 종료조건 : check == True
                    return True
                # key 제거하기
                detach(x, y, M, rotated_key, board)
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(f"key \t\t lock \t\t result")
print(f"{key} {lock} {solution(key, lock)}")