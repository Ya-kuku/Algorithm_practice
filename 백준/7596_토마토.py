from collections import deque
dirs = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]
def bfs(info):
    q = deque()
    for i in info:
        q.append(i)
    while q:

        a,b,c = q.popleft()
        for dir in dirs:
            # 수직높이 # 높이 # 너비
            na = a + dir[0]; nb = b + dir[1]; nc = c + dir[2]
            if 0 <= na < H and 0 <= nb < N and 0 <= nc < M:
                if arr[na][nb][nc] == 1: continue
                if arr[na][nb][nc] == -1: continue
                if arr[na][nb][nc] == 0:
                    arr[na][nb][nc] += arr[a][b][c] + 1
                    q.append((na,nb,nc))

M, N, H = map(int,input().split())
# 1 익은 토마토, 0 안익은 토마토, -1 토마토 업성
arr = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
info = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                info.append((i,j,k))
bfs(info)

Max = -1
flag = False
for _h in range(H):
    for _y in range(N):
        if arr[_h][_y].count(0) > 0:
            flag = True
            Max = 0
            break
        else:
            Max = max(Max, max(arr[_h][_y]))
    if flag:
        break

print(Max - 1)