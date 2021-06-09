# from collections import deque
# dirs = [(0,1),(0,-1),(1,0),(-1,0)]
# R, C = map(int,input().split())
# lake = [list(input()) for _ in range(R)]
# st = []
# def check():
#     visited = [[0] * C for _ in range(R)]
#     visited[st[0][0]][st[0][1]] = 1
#     q = deque()
#     q.append(st[0])
#
#     while q:
#         x,y = q.popleft()
#         for dir in dirs:
#             nx = x + dir[0]
#             ny = y + dir[1]
#             if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and not lake[nx][ny] == 'X':
#                 if lake[nx][ny] == 'L':
#                     return True
#                 visited[nx][ny] = 1
#                 q.append([nx,ny])
#
#     melt_pos = []
#     for i in range(R):
#         for j in range(C):
#             if not check_position[i][j] and not lake[i][j] == 'X':
#                 check_position[i][j] = 1
#                 for dir in dirs:
#                     ni = i + dir[0]
#                     nj = j + dir[1]
#                     if 0 <= ni < R and 0 <= nj < C and lake[ni][nj] == 'X':
#                         melt_pos.append([ni,nj])
#
#     for melt in melt_pos:
#         lake[melt[0]][melt[1]] = '.'
#
#     # for l in lake:
#     #     print(l)
#     # print()
#
#     return False
#
# for i in range(R):
#     for j in range(C):
#         if lake[i][j] == 'L':
#             st.append([i,j])
#
# check_position = [[0] * C for _ in range(R)]
# days = 0
# while True:
# # for _ in range(3):
#     if check():
#         print(days)
#         break
#     days += 1

from collections import deque
from sys import stdin
input = stdin.readline

ex, ey, ans = 0, 0, 0
dx, dy = (0, -1, 0, 1), (-1, 0, 1, 0)
R, C = map(int, input().split())
a = [list(input().strip()) for _ in range(R)]
wc = [[False]*C for _ in range(R)]
sc = [[False]*C for _ in range(R)]
wq1, wq2 = deque(), deque()
sq1, sq2 = deque(), deque()

def water():
    while wq1:
        x, y = wq1.popleft()
        a[x][y] = '.'
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or wc[nx][ny]:
                continue
            if a[nx][ny] == '.':
                wq1.append((nx, ny))
            else:
                wq2.append((nx, ny))
            wc[nx][ny] = True

def swan():
    while sq1:
        x, y = sq1.popleft()
        if x == ex and y == ey:
            return True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or sc[nx][ny]:
                continue
            if a[nx][ny] == '.':
                sq1.append((nx, ny))
            else:
                sq2.append((nx, ny))
            sc[nx][ny] = True
    return False

for i in range(R):
    for j in range(C):
        if a[i][j] == 'L':
            if not sq1:
                sq1.append((i, j))
                sc[i][j] = True
            else:
                ex, ey = i, j
            a[i][j] = '.'
        if a[i][j] == '.':
            wq1.append((i, j))
            wc[i][j] = True
while True:
    water()
    if swan():
        break
    wq1 = wq2
    sq1 = sq2
    wq2 = deque()
    sq2 = deque()
    ans += 1
print(ans)