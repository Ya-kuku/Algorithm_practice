N, S ,M = map(int,input().split())
volume = list(map(int,input().split()))
dp = [[0] * (M+1) for _ in range(N+1)]
dp[0][S] = 1
# N 노래 수
for i in range(1,N+1):
    # M 볼륨의 크기
    for j in range(M+1):
        # 이전 단계의 볼륨의 값이 false면 고려할 필요 없으니 넘어가기
        if dp[i-1][j] == 0:
            continue
        if j - volume[i-1] >= 0:
            # 현재 볼륨에서 더해주고 뺀값들을 dp에 쌓아두기
            dp[i][j - volume[i-1]] = 1
        if j + volume[i-1] <= M:
            dp[i][j + volume[i-1]] = 1

res = - 1
for i in range(M,-1,-1):
    if dp[N][i]:
        res = i
        break
print(res)