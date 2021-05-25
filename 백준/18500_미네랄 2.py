from collections import deque

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(r,c):
    visited = [[0] * C for _ in range(R)]
    q =deque()
    q.append((r,c))
    visited[r][c] = 1

    while q:
        x,y = q.popleft()
        if x == R-1:
            return

        for dir in dirs:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < R and 0 <= ny < C and mineral[nx][ny] == 'x' and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny))

    locate = []
    floors = []
    for i in range(C):
        for j in range(R-1,-1,-1):
            if visited[j][i]:
                locate.append((j,i))
                if 0 <= j+1 < R and mineral[j+1][i] == '.':
                    floors.append((j,i))

    move_cnt = 101
    for floor in floors:
        x,y = floor
        x += 1
        f = False
        while x < R:
            if mineral[x][y] == '.':
                x += 1
            else:
                if (x,y) in locate:
                    f = True
                    break
                else:
                    break
        if f: continue
        else:
            move_cnt = min(move_cnt,x - floor[0]-1)
    for lo in locate:
        mineral[lo[0]][lo[1]] = '.'

    for lo in locate:
        mineral[lo[0] + move_cnt][lo[1]] = 'x'

R, C = map(int,input().split())
mineral = [list(input()) for _ in range(R)]
times = int(input())
heights = list(map(int,input().split()))

for direction in range(times):
    r, c = 0,0
    flag = False
    if direction % 2:
        for i in range(C - 1, -1, -1):
            if mineral[R - heights[direction]][i] == 'x':
                mineral[R - heights[direction]][i] = '.'
                r, c = R - heights[direction], i
                flag = True
                break
    else:
        for i in range(C):
            if mineral[R - heights[direction]][i] == 'x':
                mineral[R - heights[direction]][i] = '.'
                r, c = R - heights[direction], i
                flag = True
                break

    if flag:
        for dir in dirs:
            nr = r + dir[0]
            nc = c + dir[1]
            if 0 <= nr < R and 0 <= nc < C and mineral[nr][nc] == 'x':
                bfs(nr,nc)

for mi in mineral:
    print(''.join(mi))
print()
