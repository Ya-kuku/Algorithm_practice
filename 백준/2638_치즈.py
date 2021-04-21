'''
1. 외부와 맞닿은 부분이 2군데 이상이면 치즈가 녹음
1-1. 치즈로 감싸있는 부분이지만 빈 부분은 외부 공기 유입 x, 치즈 녹지 않음
치즈는 한번에 녹임
'''
import copy
from collections import deque
def check_air(r,c,arr,cnt):
    q = deque()
    q.append((r,c))
    while q:
        a,b = q.popleft()
        arr[a][b] = cnt
        for dir in dirs:
            na = a + dir[0]
            nb = b + dir[1]
            if 0 <= na < n and 0 <= nb < m and cheese[na][nb] != 1 and arr[na][nb] != cnt:
                arr[na][nb] = cnt
                q.append((na,nb))
    return arr
def check_cheese(q,arr):
    while q:
        a, b = q.popleft()
        cnt = 0
        for dir in dirs:
            na = a + dir[0]
            nb = b + dir[1]
            if 0 <= na < n and 0 <= nb < m and arr[na][nb] == 10:
                cnt += 1
        if cnt > 1 :
            cheese[a][b] = 'C'
def del_cheese(arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'C':
                arr[i][j] = 0
    return arr
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
n, m = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(n)]
time = 0
while 1:
    tmp = copy.deepcopy(cheese)
    cnt = 10
    for i in range(n):
        for j in range(m):
            if not tmp[i][j]:
                tmp = check_air(i,j,tmp,cnt)
                cnt -= 1
    cheese_q = deque()
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 1:
                cheese_q.append((i,j))
    if len(cheese_q) == 0:
        break
    check_cheese(cheese_q,tmp)
    cheese = del_cheese(cheese)
    time += 1
print(time)