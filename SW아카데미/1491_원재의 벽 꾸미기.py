# 시간 초과 코드
# for tc in range(int(input())):
#     N,A,B = map(int,input().split())
#     tmp = []
#     Min_N = int(N**(0.5))
#     for i in range(1,N):
#         for j in range(1,N):
#             if i*j <= N and i*j >= Min_N**2:
#                 tmp.append((i,j))
#     print(tmp)
#     mid = len(tmp) // 2 -1
#     Min = 9999999999
#     while mid < len(tmp):
#         r,c = tmp[mid]
#         res = A * abs(r-c) + B * (N - r*c)
#         Min = min(res,Min)
#         mid += 1
#     print('#{} {}'.format(tc+1,Min))


for tc in range(int(input())):
    N, A, B = map(int, input().split())
    Min = 0xffffff
    for i in range(1, int(N ** (1 / 2))+1):
        for j in range(1, N // i+1):
            Min = min(Min, (A * abs(i - j) + B * (N - i * j)))

    print('#{} {}'.format(tc + 1, Min))