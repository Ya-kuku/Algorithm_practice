import sys
import copy
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
di = [0, [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[1, 2], [1, 3], [0, 2], [0, 3]],
      [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], [[0, 1, 2, 3]]]

MIN = 1e9

def dfs(start, MAP, cctv):
    global MIN
    if start == len(cctv):
        cnt = 0
        for y in range(0, row):
            for x in range(0, col):
                if MAP[y][x] == 0:
                    cnt += 1
        MIN = min(MIN, cnt)
        return

    num, y, x = cctv[start]
    for dir in di[num]:
        tmp = copy.deepcopy(MAP)
        for i in dir:
            ny, nx = y + dy[i], x + dx[i]
            while row > ny >= 0 and col > nx >= 0:
                if tmp[ny][nx] == 6:
                    break
                elif tmp[ny][nx] == 0:
                    tmp[ny][nx] = '#'
                ny += dy[i]
                nx += dx[i]
        dfs(start + 1, tmp, cctv)

row, col = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(row)]
cctv = []
for y in range(0, row):
    for x in range(0, col):
        if MAP[y][x] not in [0, 6]:
            cctv.append([MAP[y][x], y, x])
dfs(0, MAP, cctv)
print(MIN)




dx = (0, 1, 0, -1)  # 동,남,서,북
dy = (1, 0, -1, 0)
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
# cctv 갯수, 위치 파악
cctv = list()
for i in range(n):
    for j in range(m):
        if 1 <= a[i][j] <= 5:
            cctv.append((i, j, a[i][j]))
l = len(cctv)


def check(b, x, y, dir):
    while 0 <= x + dx[dir] < n and 0 <= y + dy[dir] < m:
        x += dx[dir]
        y += dy[dir]
        if b[x][y] == 6:
            return
        b[x][y] = -1


def count(b):
    cnt = 0
    n, m = len(b), len(b[0])
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0:
                cnt += 1
    return cnt


def go(idx, dirs):
    if idx == l:
        b = [row[:] for row in a]  # 깊은 복사
        for i, (x, y, no) in enumerate(cctv):
            # 회전 및 체크
            if no == 1:
                check(b, x, y, dirs[i])
            elif no == 2:
                check(b, x, y, dirs[i])
                check(b, x, y, (dirs[i] + 2) % 4)
            elif no == 3:
                check(b, x, y, dirs[i])
                check(b, x, y, (dirs[i] + 1) % 4)
            elif no == 4:
                check(b, x, y, dirs[i])
                check(b, x, y, (dirs[i] + 1) % 4)
                check(b, x, y, (dirs[i] + 2) % 4)
            elif no == 5:
                check(b, x, y, 0)
                check(b, x, y, 1)
                check(b, x, y, 2)
                check(b, x, y, 3)
        return count(b)
    ans = n * m
    # 방향 선택
    for k in range(4):  # 계산하기 쉽게 4개로 통일. 수가 크지 않으므로.
        temp = go(idx + 1, dirs + [k])
        if temp < ans:
            ans = temp
    return ans


print(go(0, []))