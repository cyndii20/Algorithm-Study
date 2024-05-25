# BOJ
# 14658 : 하늘에서 별똥별이 빗발친다

# Solution 1
# 트램펄린의 모서리에 별이 들어오는 경우

def draw_rect(L, K, stars):
    cnt = 0
    for i in range(K):
        for j in range(K):
            tmp = 0
            for cur_x, cur_y in stars:
                if stars[i][0] <= cur_x <= stars[i][0]+L and stars[j][1] <= cur_y <= stars[j][1]+L :
                    tmp += 1
            cnt = max(tmp, cnt)  # 최대한 많은 별똥별을 튕겨냈을 때, 튕겨 나간 별똥별 수
    return cnt

N, M, L, K = map(int, input().split())
stars = [tuple(map(int, input().split())) for _ in range(K)]

result = K - draw_rect(L, K, stars)
print(result)


# Solution 2
# 트램펄린 1씩 이동하면서 가장 많이 튕겨내는 좌표 구하기
## 실패 - 시간 초과

# def count_star(N, M, L, stars):
#     cnt = 0
#     for i in range(N-L):
#         for j in range(M-L):
#             tmp = 0
#             for x, y in stars:
#                 if (i <= x <= i+L) and (j <= y <= j+L) :  # 별이 트램펄린 안에 들어옴
#                     tmp += 1
#             cnt = max(tmp, cnt)  # 최대한 많은 별똥별을 튕겨냈을 때, 튕겨 나간 별똥별 수
#     return cnt

# N, M, L, K = map(int, input().split())
# stars = [tuple(map(int, input().split())) for _ in range(K)]

# result = K - count_star(N, M, L, stars)
# print(result)


