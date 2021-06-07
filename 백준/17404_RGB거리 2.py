n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
result = 1e9

# 첫 번째 색깔에 따라 각 비용을 계산한다.
for idx in range(3):
    # dp행렬을 3 * n으로 구성
    dp = [[0] * n for _ in range(3)]
    for i in range(3):
        if i == idx:
            dp[i][0] = lst[0][i]
            continue
        dp[i][0] = result

    # 비용 계산
    for i in range(1, n):
        dp[0][i] = lst[i][0] + min(dp[1][i - 1], dp[2][i - 1])
        dp[1][i] = lst[i][1] + min(dp[0][i - 1], dp[2][i - 1])
        dp[2][i] = lst[i][2] + min(dp[0][i - 1], dp[1][i - 1])

    for i in range(3):
        if i == idx:
            continue
        result = min(result, dp[i][-1])
print(result)