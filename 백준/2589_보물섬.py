from collections import deque
dr = [0,0,1,-1]
dc = [1,-1,0,0]
def bfs(r,c):
    visited = [[0]* w for _ in range(l)]
    visited[r][c] = 1

    q = deque()
    q.append((r,c))

    while q:
        x,y, = q.popleft()
        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]
            if 0 <= nx < l and 0 <= ny < w:
                if arr[nx][ny] =='L' and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    Max = -1
    for i in visited:
        Max = max(max(i),Max)

    return Max-1

l, w = map(int,input().split())
arr = [list(map(str,input())) for _ in range(l)]

ans = -1
for i in range(l):
    for j in range(w):
        if arr[i][j] == 'L':
            ans = max(bfs(i,j),ans)
print(ans)