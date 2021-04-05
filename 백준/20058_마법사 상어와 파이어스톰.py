from collections import deque
n,q = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(2 ** n)]
l = list(map(int,input().split()))
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(r,c):
    global total_ice
    visited[r][c] = 1
    total_ice += arr[r][c]
    q= deque()
    q.append((r,c))
    cnt = 1
    while q:
        x,y = q.popleft()
        for dir in dirs:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0<=nx < 2**n and 0 <= ny < 2**n and visited[nx][ny] == 0 and arr[nx][ny] !=0:
                visited[nx][ny] = 1
                q.append((nx,ny))
                total_ice += arr[nx][ny]
                cnt += 1

    return cnt

for l_ in l:
    # 회전
    rotate_arr = [[0] * (2**n) for _ in range(2**n)]
    for i in range(0,2**n,2 ** l_):
        for j in range(0,2**n,2 ** l_):
            for x in range(2**l_):
                for y in range(2**l_):
                    rotate_arr[i+y][j + 2**l_ - x - 1] = arr[i+x][j+y]

    # 얼음 녹이기
    arr = [[0] * (2**n) for _ in range(2**n)]
    for a in range(2 ** n):
        for b in range(2 ** n):
            cnt = 0
            for dir in dirs:
                na = a + dir[0]
                nb = b + dir[1]
                if 0 <= na < 2**n and 0 <= nb < 2**n and rotate_arr[na][nb] != 0:
                    cnt += 1
            if rotate_arr[a][b] >0:
                if cnt < 3:
                    arr[a][b] = rotate_arr[a][b] -1
                else:
                    arr[a][b] = rotate_arr[a][b]
visited = [[0] * (2**n) for _ in range(2**n)]
total_ice = 0
Max = 0
for i in range(2**n):
    for j in range(2**n):
        if arr[i][j] != 0 and visited[i][j] == 0:
            Max = max(Max,bfs(i,j))
print(total_ice)
print(Max)