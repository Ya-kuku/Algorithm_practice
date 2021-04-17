'''
1. 종수의 위치가 먼저 움직임
1-1. 종수 cmd로 움직였을 때 아두이노가 있으면 실패값 출력
2. 미친 아두이노들 벡터크기 가장 작은 방향으로 움직임
3. 미친 아두이노 겹치면 모두 파괴(한번에 파괴해야함)
4. cmd 종료되면 보드값 출력
'''
import sys
from collections import deque
def check(tmp_board):
    for i in range(r):
        for j in range(c):
            if len(arr[i][j]) > 1:
                tmp_board[i][j] = '.'

def jongsu(a,b,cur):
    na = a + dirs[cur-1][0]
    nb = b + dirs[cur-1][1]
    if 0 <= na < r and 0 <= nb < c:
        if board[na][nb] == 'R':
            print('kraj '+str(cmd_cur+1))
            sys.exit()
        if board[na][nb] == '.':
            board[a][b] = '.'
            board[na][nb] = 'I'
    return na,nb

def arduino(x,y):
    q = deque()
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                q.append((i,j))
    tmp_board = [['.'] * c for _ in range(r)]
    while q:
        a,b = q.popleft()
        Min = 1e9
        _r,_c = 0,0
        for dir in ar_dirs:
            na = a + dir[0]
            nb = b + dir[1]
            if 0 <= na < r and 0<= nb < c:
                tmp = abs(na-x) + abs(nb-y)
                if tmp < Min:
                    Min = tmp
                    _r, _c = na,nb
        if board[_r][_c] == 'I':
            print('kraj '+str(cmd_cur+1))
            sys.exit()
        tmp_board[_r][_c] = 'R'
        arr[_r][_c].append('R')

    check(tmp_board)
    return tmp_board

dirs = [(1,-1),(1,0),(1,1),(0,-1),(0,0),(0,1),(-1,-1),(-1,0),(-1,1)]
ar_dirs = [(1,-1),(1,0),(1,1),(0,-1),(0,1),(-1,-1),(-1,0),(-1,1)]
r,c = map(int,input().split())
board = [list(map(str,input())) for _ in range(r)]
cmd = list(map(int,input()))
cmd_cur = 0
while cmd_cur < len(cmd):
    arr = [[[] for _ in range(c)] for _ in range(r)]
    a,b = 0,0
    flag = False
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'I':
                a, b = i,j
                flag = True
                break
        if flag:
            break
    x,y = jongsu(a,b,cmd[cmd_cur])
    tmp_board = arduino(x,y)
    tmp_board[x][y] = 'I'
    board = tmp_board
    cmd_cur += 1

for i in range(r):
    tmp = ''
    for j in range(c):
        tmp += board[i][j]
    print(tmp)