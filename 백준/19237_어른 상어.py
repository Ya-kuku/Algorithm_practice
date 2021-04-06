# from collections import deque
# # 상 하 좌 우
# dirs = [(-1,0),(1,0),(0,-1),(0,1)]
# def bfs(cur_shark):
#     q = deque()
#     for shark in cur_shark:
#         q.append([shark[0],shark[1]] + sea[shark[0]][shark[1]])
#     while q:
#         r,c, being, idx, cnt, cur_dir = q.popleft()
#         # 현재 번호 상어의 방향
#         pos_dirs = priority_dirs[idx][cur_dir]
#         # 주변에 냄새가 아예 없는 경우
#         for dir in pos_dirs:
#             nr = r + dirs[dir-1][0]
#             nc = c + dirs[dir-1][1]
#             if 0<= nr < n and 0<= nc < n:
#                 # 해당 순서에 상어도 같이 모이지 않음
#                 if arr[nr][nc] == 0 and not sea[nr][nc]:
#                     sea[nr][nc] = [True,idx,k,dir]
#                     sea[r][c] = [False,idx,cnt,-1]
#                     # sea[r][c][-1] = -1
#                     break
#                 # 동시에 상어가 들어왔다
#                 if arr[nr][nc] == 0 and sea[nr][nc] and sea[nr][nc][0] == True:
#                     x= nr
#                     y= nc
#                     # 사방이 냄새로 가득
#                     flag = False
#                     for dir in pos_dirs:
#                         if flag: break
#                         nr = r + dirs[dir - 1][0]
#                         nc = c + dirs[dir - 1][1]
#                         if 0 <= nr < n and 0 <= nc < n and sea[nr][nc]:
#                             if sea[nr][nc][1] == idx:
#                                 sea[nr][nc] = [True, idx, k, dir]
#                                 sea[r][c] = [False, idx, cnt, -1]
#                                 flag = True
#                     else:
#                         sea[r][c] = [False,idx,cnt,-1]
#                         break
#         else:
#             # 사방이 냄새로 가득
#             for dir in pos_dirs:
#                 nr = r + dirs[dir - 1][0]
#                 nc = c + dirs[dir - 1][1]
#                 if 0 <= nr < n and 0 <= nc < n and sea[nr][nc]:
#                     if sea[nr][nc][1] == idx:
#                         sea[nr][nc] = [True, idx, k, dir]
#                         sea[r][c] = [False, idx, cnt, -1]
#     # 냄새를 빼준다
#     tmp = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if sea[i][j] and sea[i][j][0] == False:
#                 sea[i][j][2] -= 1
#                 if sea[i][j][2] == 0:
#                     sea[i][j] = []
#             # 옮겨진 상어 위치 초기화
#             if sea[i][j] and sea[i][j][0] == True:
#                 tmp[i][j] = sea[i][j][1]
#     print(tmp)
#     return tmp
#
# # n 격자, m 상어 수, k 냄새 지속 시간
# n, m, k = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(n)]
# st_dirs = list(map(int,input().split()))
# priority_dirs = dict()
# # 1 2 3 4
# #상 하 좌 우
# for i in range(1,m+1):
#     priority_dirs[i] = dict()
#     for direction in range(1,5):
#         priority_dirs[i][direction] = list(map(int,input().split()))
# sea = [[[]] * n for _ in range(n)]
# cur_shark = []
# time = 1
# for i in range(n):
#     for j in range(n):
#         if arr[i][j]:
#             # 상어유무, 상어idx, 냄새, 방향
#             sea[i][j] = [True,arr[i][j],k,st_dirs[arr[i][j]-1]]
#             cur_shark.append([i,j,arr[i][j]])
# cur_shark.sort(key=lambda data:data[2])
# arr = bfs(cur_shark)
# while time < 100:
#     cur_shark = []
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j]:
#                 cur_shark.append([i,j,arr[i][j]])
#     cur_shark.sort(key=lambda data:data[2])
#     arr = bfs(cur_shark)
#     Sum = 0
#     time += 1
#     for i in sea:
#         print(i)
#     print()
#     for i in arr:
#         Sum += sum(i)
#     if Sum == 1:
#         break
# print(time)
import sys

input = sys.stdin.readline
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

n, m, k = map(int, input().split())

a, shark = [], [[] for _ in range(m)]
for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(n):
        if a[i][j]:
            shark[a[i][j]-1].extend([i, j])
            a[i][j] = [a[i][j], k]

d = list(map(int, input().split()))
for i in range(m):
    shark[i].append(d[i])

dir = [[] for _ in range(m)]
idx = -1
for i in range(4*m):
    if i % 4 == 0:
        idx += 1
    dir[idx].append(list(map(int, input().split())))

ans = 0
while True:
    ans += 1
    if ans == 1001:
        print(-1)
        break

    check = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        if shark[i] != 0:
            x, y, d, flag = shark[i][0], shark[i][1], shark[i][2], 0
            for j in range(4):
                ndir = dir[i][d-1][j]
                nx, ny = x + dx[ndir], y + dy[ndir]
                if 0 <= nx < n and 0 <= ny < n:
                    if a[nx][ny] == 0:
                        flag = 1
                        break
            if flag == 0:
                for j in range(4):
                    ndir = dir[i][d-1][j]
                    nx, ny = x + dx[ndir], y + dy[ndir]
                    if 0 <= nx < n and 0 <= ny < n:
                        if a[nx][ny][0] == i+1:
                            break

            if check[nx][ny]:
                if check[nx][ny] < i+1:
                    shark[i] = 0
                else:
                    shark[check[nx][ny]-1] = 0
            else:
                check[nx][ny] = i+1
                shark[i] = [nx, ny, ndir]

    for i in range(n):
        for j in range(n):
            if a[i][j]:
                a[i][j][1] -= 1
                if a[i][j][1] == 0:
                    a[i][j] = 0

    for i in range(m):
        if shark[i]:
            x, y = shark[i][0], shark[i][1]
            a[x][y] = [i+1, k]

    if shark.count(0) == m-1:
        print(ans)
        break