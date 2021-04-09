from collections import deque
import sys
def move(r,c,dx,dy):
    count = 0
    while board[r+dx][c+dy] != '#' and board[r][c] != 'O':
        r += dx
        c += dy
        count += 1
    return r,c,count
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
n,m = map(int,input().split())
board = [list(map(str,input())) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
rx, ry, bx, by = 0,0,0,0
q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 'B':
            bx,by = i,j
        elif board[i][j] == 'R':
            rx,ry = i,j
q.append((rx,ry,bx,by,1))
visited[rx][ry][bx][by] = True
while q:
    rx,ry,bx,by,cnt = q.popleft()
    if cnt > 10:
        break
    for dir in dirs:
        nrx,nry,rcnt = move(rx,ry,dir[0],dir[1])
        nbx, nby, bcnt = move(bx, by, dir[0], dir[1])
        if board[nbx][nby] != 'O':
            if board[nrx][nry] == 'O':
                print(1)
                sys.exit()
            if nrx == nbx and nry == nby:
                # res.append(dir)
                if rcnt > bcnt:
                    nrx -= dir[0]
                    nry -= dir[1]
                else:
                    nbx -= dir[0]
                    nby -= dir[1]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx,nry,nbx,nby,cnt+1))

print(0)