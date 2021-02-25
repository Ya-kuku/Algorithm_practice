dp = [0] * 102
dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(4,101):
    dp[i] = dp[i-2] + dp[i-3]
for tc in range(int(input())):
    N = int(input())
    print('#{} {}'.format(tc+1,dp[N]))
