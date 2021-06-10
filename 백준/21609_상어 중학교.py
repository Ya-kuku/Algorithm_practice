from collections import deque
import sys
import copy
input = sys.stdin.readline
n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
res = 0
def bfs(r,c,idx):
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    # 일반블록 수
    cnt = 1
    # 무지개 블록 위치
    rainbow = []
    # 무지개 블록 수
    rainbow_cnt = 0
    tmp_pos = [[r,c]]

    while q:
        x, y = q.popleft()
        for dir in (0,1),(0,-1),(1,0),(-1,0):
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if arr[nx][ny] == idx or arr[nx][ny] == 0:
                    cnt += 1
                    if not arr[nx][ny]:
                        rainbow.append((nx,ny))
                        rainbow_cnt += 1
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    tmp_pos.append([nx,ny])

    if cnt >= 2:
        pos.append([cnt,rainbow_cnt,tmp_pos])
    for bow in rainbow:
        visited[bow[0]][bow[1]] = 0

def move():
    tmp = list(map(list, zip(*arr)))

    for _ in range(n):
        for i in range(n):
            for j in range(n-1):
                if (tmp[i][j] != 6 and tmp[i][j] != -1 and tmp[i][j]) or (tmp[i][j] != 6 and tmp[i][j] != -1 and not tmp[i][j]):
                    if tmp[i][j+1] == 6:
                        tmp[i][j], tmp[i][j+1] = tmp[i][j+1], tmp[i][j]

    tmp = rotate(list(map(list, zip(*tmp))))

    _tmp = list(map(list, zip(*tmp)))
    for _ in range(n):
        for i in range(n):
            for j in range(n-1):
                if (_tmp[i][j] != 6 and _tmp[i][j] != -1 and _tmp[i][j]) or (_tmp[i][j] != 6 and _tmp[i][j] != -1 and not _tmp[i][j]):
                    if _tmp[i][j+1] == 6:
                        _tmp[i][j], _tmp[i][j+1] = _tmp[i][j+1], _tmp[i][j]

    return list(map(list, zip(*_tmp)))

def rotate(lst):
    rotate_lst = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            rotate_lst[n-1-c][r] = lst[r][c]

    return rotate_lst

while True:
    pos = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] or arr[i][j] == -1 or not arr[i][j] or arr[i][j] == 6: continue
            bfs(i,j,arr[i][j])

    if not pos:
        print(res)
        sys.exit()

    pos.sort(key = lambda data : (data[0],data[1],data[2][0],data[2][1]))
    pos.sort(reverse=True)
    # print(pos)
    res += pos[0][0] ** 2
    for p in pos[0][2]:
        arr[p[0]][p[1]] = 6

    arr = move()
    visited = [[0] * n for _ in range(n)]
    # arr = copy.deepcopy(tmp_arr)
    #
    # for q in arr:
    #     print(q)
    # print()

