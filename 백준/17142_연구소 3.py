from collections import deque
from itertools import combinations
import copy
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
virus = []
def bfs(start):
    q = deque()
    visited = [[0] * n for _ in range(n)]
    for st in start:
        a,b = st
        visited[a][b] = 1
        q.append(st)
    cnt = 0
    while q:
        if virus_count == cnt:
            break
        r,c = q.popleft()
        for dir in dirs:
            nr = r + dir[0]
            nc = c + dir[1]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] += visited[r][c] + 1
                    cnt += 1
                    arr[nr][nc] = 3
                    q.append((nr,nc))
                elif arr[nr][nc] == 2 and visited[nr][nc] == 0:
                    visited[nr][nc] += visited[r][c] +1
                    arr[nr][nc] = 3
                    q.append((nr,nc))

    time = 0
    # print(arr,'arr')
    # print(visited,'visited')
    for x in arr:
        if x.count(0):
            return 0
    for x in visited:
        time = max(time,max(x))
    return time
virus_count = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            virus.append((i,j))
        elif arr[i][j] == 0:
            virus_count += 1
tmp = copy.deepcopy(arr)
pos_virus = list(combinations(virus,m))
res = []
for pos in pos_virus:
    tmp = copy.deepcopy(arr)
    res.append(bfs(pos))
    arr = tmp
if sum(res) == 0:
    print(-1)
else:
    res.sort()
    for i in res:
        if i != 0:
            print(i-1)
            break

# 5 1
# 2 2 2 1 1
# 2 1 1 1 1
# 2 1 1 1 1
# 2 1 1 1 1
# 2 2 2 2 0
#
# 1
#
# 5 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 2 0 0 2 0
# 1 1 1 1 1
#
# 2
# 5 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 0 2 0 2 0
# 1 1 1 1 1