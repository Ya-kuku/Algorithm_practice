import sys
sys.setrecursionlimit(10000)
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def dfs(r,c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr,nc)

for tc in range(int(input())):
    M, N, K = map(int,input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        a,b = map(int,input().split())
        arr[b][a] = 1

    res = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] and visited[i][j] == 0:
                visited[i][j] = 1
                res += 1
                dfs(i,j)

    print(res)
