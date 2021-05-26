import sys
dirs = [(0,1),(0,-1),(-1,0),(1,0)]
N, K = map(int,input().split())
chess = [list(map(int,input().split())) for _ in range(N)]
pieces = [[[] * N for _ in range(N)] for _ in range(N)]

for idx in range(K):
    r, c, way = map(int,input().split())
    pieces[r-1][c-1].append([idx+1,way-1])

def move(r,c,dist):
    cur_dist = dirs[dist]
    nr = r + cur_dist[0]
    nc = c + cur_dist[1]

    if 0 <= nr < N and 0 <= nc < N:
        if chess[nr][nc] == 0:
            pieces[nr][nc].extend(pieces[r][c])
            pieces[r][c] = []
            if len(pieces[nr][nc]) >= 4:
                print(k)
                sys.exit()
        elif chess[nr][nc] == 1:
            pieces[nr][nc].extend(pieces[r][c][::-1])
            pieces[r][c] = []
            if len(pieces[nr][nc]) >= 4:
                print(k)
                sys.exit()
        else:
            if dist == 0 or dist == 1:
                if dist == 0:
                    _dist = 1
                else:
                    _dist = 0
            else:
                if dist == 2:
                    _dist = 3
                else:
                    _dist = 2
            tmp_dist = dirs[_dist]
            _nr = r + tmp_dist[0]
            _nc = c + tmp_dist[1]
            # 파랑칸으로 이동하는 경우 4가지 수
            if 0 <= _nr < N and 0 <= _nc < N:
                # 1. 흰칸으로 진입
                if chess[_nr][_nc] == 0:
                    pieces[r][c][0][1] = _dist
                    pieces[_nr][_nc].extend(pieces[r][c])
                    pieces[r][c] = []
                    if len(pieces[_nr][_nc]) >= 4:
                        print(k)
                        sys.exit()
                # 2. 빨강칸으로 진입
                elif chess[_nr][_nc] == 1:
                    pieces[r][c][0][1] = _dist
                    pieces[_nr][_nc].extend(pieces[r][c][::-1])
                    pieces[r][c] = []
                    if len(pieces[_nr][_nc]) >= 4:
                        print(k)
                        sys.exit()

    # 범위 벗어난 경우
    else:
        if dist == 0 or dist == 1:
            if dist == 0:
                _dist = 1
            else:
                _dist = 0
        else:
            if dist == 2:
                _dist = 3
            else:
                _dist = 2
        tmp_dist = dirs[_dist]
        _nr = r + tmp_dist[0]
        _nc = c + tmp_dist[1]
        # 파랑칸으로 이동하는 경우 4가지 수
        # 1. 흰칸으로 진입
        if chess[_nr][_nc] == 0:
            pieces[r][c][0][1] = _dist
            pieces[_nr][_nc].extend(pieces[r][c])
            pieces[r][c] = []
            if len(pieces[_nr][_nc]) >= 4:
                print(k)
                sys.exit()
        # 2. 빨강칸으로 진입
        elif chess[_nr][_nc] == 1:
            pieces[r][c][0][1] = _dist
            pieces[_nr][_nc].extend(pieces[r][c][::-1])
            pieces[r][c] = []
            if len(pieces[_nr][_nc]) >= 4:
                print(k)
                sys.exit()

k = 1

while k < 1001:

    for i in range(1,K+1):
        flag = False
        for x in range(N):
            if flag:
                break
            for y in range(N):
                if pieces[x][y]:
                    if pieces[x][y][0][0] == i:
                        move(x,y,pieces[x][y][0][1])
                        flag = True
                        break
    k += 1
print(-1)
