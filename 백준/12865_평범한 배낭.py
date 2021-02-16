# N 물건의 수, K 무게
N, K = map(int,input().split())
dp = [[0] * (K+1) for _ in range(N+1)]
for i in range(1,N+1):
    W, V = map(int,input().split())
    for j in range(1,K+1):
        if j < W:
            dp[i][j] = dp[i-1][j]
        else:
            # 이전에 미리 구해둔 해당 물건의 무게만큼을 제외했을 때의 최댓값에 현재 물건의 무게를 더해준값
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-W]+V)

print(dp[N][K])
