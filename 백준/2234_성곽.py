from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def binary(s):
    return format(int(s), '04b')
n, m = map(int,input().split())
arr = [list(map(binary, input().split())) for _ in range(m)]
visited = [[0]* n for _ in range(m)]
cnt, area, Maxarea = 0,0,0

def bfs(r,c,idx):
    visited[r][c] = idx
    count = 0
    q = deque()
    q.append((r,c))

    while q:
        x,y = q.popleft()
        count += 1
        if arr[x][y] == '1111':
            return count

        for i in range(4):
            if arr[x][y][i] == '0':
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = idx
                    q.append((nx,ny))
    return count
room = []
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            cnt += 1
            tmp_area = bfs(i,j,cnt)
            room.append(tmp_area)
            area = max(area,tmp_area)

for i in range(m):
    for j in range(n):
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < m and 0 <= y < n and visited[i][j] != visited[x][y]:
                Maxarea = max(Maxarea,(room[visited[i][j]-1] + room[visited[x][y]-1]))
print(cnt)
print(area)
print(Maxarea)