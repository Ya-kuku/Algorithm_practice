dr = [-1,-1,-1,0,1,1,1,0]
dc = [-1,0,1,1,1,0,-1,-1]
for tc in range(int(input())):
    N,M = map(int,input().split())
    # 1,B 흑돌  2,W 백돌
    arr =[[0] * (N+1) for _ in range(N+1)]
    st_p = N // 2
    arr[st_p][st_p] = arr[st_p + 1][st_p + 1] = 'W'
    arr[st_p + 1][st_p] = arr[st_p][st_p + 1] = 'B'

    for _ in range(M):
        r,c, stone = map(int,input().split())
        if stone == 1:
            arr[c][r] = 'B'; cur_stone= 'B'
        else:
            arr[c][r] = 'W'; cur_stone= 'W'

        for i in range(8):
            nc = c + dr[i]
            nr = r + dc[i]
            tmp = []
            while 1 <= nc <= N and 1 <= nr <= N:
                if arr[nc][nr] == 0: break
                if arr[nc][nr] != cur_stone:
                    tmp.append((nc,nr))
                if arr[nc][nr] == cur_stone:
                    if tmp:
                        for i in range(len(tmp)):
                            a,b = tmp[i]
                            arr[a][b] = cur_stone
                    break
                nc = nc + dr[i]
                nr = nr + dc[i]
    black = 0
    white = 0
    for i in range(1,N + 1):
        for j in range(1,N + 1):
            if arr[i][j] == 'B':
                black += 1
            if arr[i][j] == 'W':
                white += 1
    print('#{} {} {}'.format(tc+1,black,white))





