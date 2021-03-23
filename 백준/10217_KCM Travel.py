for tc in range(int(input())):
    # n 공항의 수, m 지원 비용, k 티켓정보
    n, m, k = map(int,input().split())
    arr = [[] for _ in range(n+1)]
    for _ in range(k):
        # u 출발, v 도착, c 비용, d 시간
        u, v, c, d = map(int,input().split())
        arr[u].append((v, c, d))

    # col 비용, row 공항 수(도착지)
    dp = [[1e9] * (m + 1) for _ in range(n+1)]
    dp[1][0] = 0

    for c in range(m+1):
        for d in range(1,n+1):
            # c의 비용으로 d에 도착하는 경우가 없을 때
            if dp[d][c] == 1e9: continue

            # c의 비용으로 d에 도착했을 때의 소요시간
            time = dp[d][c]
            # d에서 출발하는 모든 경우
            for dv, dc, dd in arr[d]:
                # 비용이 초과되는 경우는 넘어감
                if dc + c > m: continue
                # 이미 저장된 값과 새롭게 들어오는 소요시간 중 작은값
                dp[dv][dc+c] = min(dp[dv][dc+c], time+dd)

    res = min(dp[n])

    if res == 1e9:
        print('Poor KCM')
    else:
        print(res)


