from collections import deque
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def bfs(r,c):
    q = deque()
    visited[r][c] = 1
    len_cnt = 0
    area_cnt = 0
    q.append((r,c))

    while q:
        area_cnt += 1
        # 우선 면적
        x,y = q.popleft()
        for dir in dirs:
            nx = x + dir[0]
            ny = y + dir[1]
            # 면적
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == '#' and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny))
            # 길이
            if nx < 0 or nx >= n:
                len_cnt += 1
            if ny < 0 or ny >= n:
                len_cnt += 1
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == '.':
                len_cnt += 1

    return [area_cnt,len_cnt]

res = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == '#' and not visited[i][j]:
            res.append(bfs(i,j))

res.sort(key = lambda data : (data[0], -data[1]))
print(*res[-1])