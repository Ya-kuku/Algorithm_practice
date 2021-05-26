# import sys
#
# n,m,h = map(int,sys.stdin.readline().split())
# num_list = [0]*n
# dp_list = [0]*1001
#
# for a in range(n):
#     num_list[a] = list(map(int,sys.stdin.readline().split()))
#     # num_list[a].sort()
# for a in num_list[0]:
#     dp_list[a] = 1
#
# for a in range(1,n):
#     temp_list = [0]*1001
#     for b in range(1,h+1):
#         if dp_list[b]:
#             for num in num_list[a]:
#                 if b + num <= h:
#                     temp_list[b+num] += dp_list[b]
#     for b in num_list[a]:
#         dp_list[b] += 1
#     for b in range(1,h+1):
#         dp_list[b] += temp_list[b]
#
# print(dp_list[h]%10007)


N, M, H = map(int, input().split())

dp = [0] * (H + 1)
dp[0] = 1   # 초기화
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(H, -1, -1):
        for k in tmp:
            if j >= k:
                dp[j] = (dp[j] + dp[j - k]) % 10007
print(dp)
print(dp[H])