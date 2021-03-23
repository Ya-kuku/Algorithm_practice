from collections import deque
dr = [0,0,1,-1]
dc = [1,-1,0,0]
def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1

    while q:
        x,y,z = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not arr[nx][ny] and visited[nx][ny][z] == -1:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx,ny,z))
                elif z == 0 and arr[nx][ny] and visited[nx][ny][z+1] == -1:
                    visited[nx][ny][z+1] = visited[x][y][z] + 1
                    q.append((nx,ny,z+1))

    return -1
# n 세로 m 가로
n, m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]
visited = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
print(bfs())





# import sys
# from collections import deque
# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     board = [list(map(int, input())) for _ in range(n)]
#     dist = [[[0] * m for _ in range(n)] for _ in range(2)]
#     dist[0][0][0] = 1
#     dist[1][0][0] = 1
#     dQ = deque()
#     dr = [-1, 0, 1, 0]
#     dc = [0, 1, 0, -1]
#     dQ.append((0, 0, 0))
#     while dQ:
#         r, c, ck = dQ.popleft()
#         if r == n-1 and c == m-1:
#             print(dist[ck][r][c])
#             sys.exit(0)
#         for i in range(4):
#             nr, nc = r+dr[i], c+dc[i]
#             if 0 <= nr < n and 0 <= nc < m:
#                 if board[nr][nc] == 0 and dist[ck][nr][nc] == 0:
#                     dist[ck][nr][nc] = dist[ck][r][c]+1
#                     dQ.append((nr, nc, ck))
#                 elif ck == 0 and board[nr][nc] == 1 and dist[1][nr][nc] == 0:
#                     dist[1][nr][nc] = dist[ck][r][c]+1
#                     dQ.append((nr, nc, 1))
#     print(-1)

