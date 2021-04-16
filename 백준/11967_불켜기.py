from collections import deque
dirs = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(r,c):
    q = deque()
    q.append((r,c))
    farm[r][c] = 1
    visited[r][c] = True
    while q:
        a,b = q.popleft()
        for x,y in G[a][b]:
            if not farm[x][y]:
                farm[x][y] = 1
                for dir in dirs:
                    nx = x + dir[0]
                    ny = y + dir[1]
                    if 0<= nx < n and 0<= ny < n and visited[nx][ny]:
                        q.append((nx,ny))
        for dir in dirs:
            na = a + dir[0]
            nb = b + dir[1]
            if 0<= na < n and 0<= nb < n and farm[na][nb] and not visited[na][nb]:
                visited[na][nb] = True
                q.append((na,nb))
n, m = map(int,input().split())
farm = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
G = [[[] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    x,y,a,b = map(int,input().split())
    G[x-1][y-1].append((a-1,b-1))
bfs(0,0)
res = 0
for i in farm:
    res+= sum(i)
print(res)