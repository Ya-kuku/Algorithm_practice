from collections import deque
# 1오른쪽 2아래 3왼쪽 4위
dirs = {0:(0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}
n = int(input())
board = [[0]*n for _ in range(n)]
for _ in range(int(input())):
    a,b = map(int,input().split())
    # 사과 위치 표시
    board[a-1][b-1] = 'apple'

directions = []
for _ in range(int(input())):
    directions.append(list(input().split()))
directions.sort(key=lambda data : -int(data[0]))
st_dir = 0
q = deque()
q.append((0,0))
# 지나간 길 기록
q1 = deque()
q1.append((0,0))
cnt = 0
while q:
    if directions:
        if cnt == int(directions[-1][0]):
            time, D = directions.pop()
            if D == 'L':
                st_dir -= 1
            else:
                st_dir += 1
    r,c = q.popleft()
    board[r][c] = 1
    cnt += 1

    nr = r + dirs[st_dir % 4][0]
    nc = c + dirs[st_dir % 4][1]
    # 벽에 부딪힘
    if nr < 0 or nr >= n or nc < 0 or nc >= n:
        break
    else:
        # 사과 먹을 때
        if board[nr][nc] == 'apple':
            board[nr][nc] = 1
            q.append((nr,nc))
            q1.append((nr,nc))
        # 내 몸에 부딪힐 때
        elif board[nr][nc] == 1:
            break
        else:
            x,y = q1.popleft()
            board[x][y] = 0
            board[nr][nc] = 1
            q.append((nr, nc))
            q1.append((nr,nc))

print(cnt)