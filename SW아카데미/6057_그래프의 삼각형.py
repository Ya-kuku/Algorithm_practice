for tc in range(int(input())):
    N,M = map(int,input().split())
    tri = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        x,y = map(int,input().split())
        tri[x][y] = tri[y][x] = 1
    ans = 0
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            for k in range(j+1,N+1):
                if tri[i][j] and tri[i][k] and tri[j][k]:
                    ans += 1
    print('#{} {}'.format(tc+1,ans))