# .평지 * 벽돌 # 강철 - 물
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
move = {'U':(-1,0),
        'D':(1,0),
        'L':(0,-1),
        'R':(0,1)}
point = ['^','v','<','>']
for tc in range(int(input())):
    H,W = map(int,input().split())
    arr = [list(input()) for _ in range(H)]
    N = int(input())
    orders = input()
    st_r = 0
    st_c = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] in point:
                st_r = i
                st_c = j
                break
    # 현재 방향
    cur_p = point.index(arr[st_r][st_c])
    for order in orders:
        if order == 'S':
            nr = st_r + dr[cur_p]
            nc = st_c + dc[cur_p]
            while 0 <= nr < H and 0 <= nc < W:
                if arr[nr][nc] == '#':
                    break
                if arr[nr][nc] == '*':
                    arr[nr][nc] = '.'
                    break
                nr = nr + dr[cur_p]
                nc = nc + dc[cur_p]
        else:
            if order == 'U':
                cur_p = 0
                arr[st_r][st_c] = point[cur_p]
                nr = st_r + move[order][0]
                nc = st_c + move[order][1]
                if nr < 0 or nr == H or nc < 0 or nc == W: continue
                if arr[nr][nc] == '.':
                    arr[nr][nc] = point[cur_p]
                    arr[st_r][st_c] = '.'
                    st_r,st_c = nr, nc
            if order == 'D':
                cur_p = 1
                arr[st_r][st_c] = point[cur_p]
                nr = st_r + move[order][0]
                nc = st_c + move[order][1]
                if nr < 0 or nr == H or nc < 0 or nc == W: continue
                if arr[nr][nc] == '.':
                    arr[nr][nc] = point[cur_p]
                    arr[st_r][st_c] = '.'
                    st_r, st_c = nr, nc
            if order == 'L':
                cur_p = 2
                arr[st_r][st_c] = point[cur_p]
                nr = st_r + move[order][0]
                nc = st_c + move[order][1]
                if nr < 0 or nr == H or nc < 0 or nc == W: continue
                if arr[nr][nc] == '.':
                    arr[nr][nc] = point[cur_p]
                    arr[st_r][st_c] = '.'
                    st_r, st_c = nr, nc
            if order == 'R':
                cur_p = 3
                arr[st_r][st_c] = point[cur_p]
                nr = st_r + move[order][0]
                nc = st_c + move[order][1]
                if nr < 0 or nr == H or nc < 0 or nc == W: continue
                if arr[nr][nc] == '.':
                    arr[nr][nc] = point[cur_p]
                    arr[st_r][st_c] = '.'
                    st_r, st_c = nr, nc
    print('#{}'.format(tc+1), end=' ')
    for i in arr:
        print(*i,end='\n',sep='')
