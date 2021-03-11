from collections import deque
dr = [0,0,1,-1]
dc = [1,-1,0,0]
def bfs(r,c,maps):
    # n = 행, m = 열
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((r,c))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            return visited[n-1][m-1]
        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny]:
                if not visited[nx][ny]:
                    maps[nx][ny] = 0
                    visited[nx][ny] += visited[x][y] + 1
                    q.append((nx,ny))

    return -1

def solution(maps):
    answer = bfs(0,0,maps)
    return answer


# dfs 이용
# def search(row, col, maps, visited, ans, mov):
#     if row == len(maps) - 1 and col == len(maps[0]) - 1:
#         if ans[0] > mov:
#             ans[0] = mov
#             return
#     if mov > len(maps) * len(maps[0]):
#         return
#
#     visited[row][col] = True
#     print(visited)
#     rowl = [0, 0, -1, 1]
#     coll = [1, -1, 0, 0]
#
#     for i in range(4):
#         nrow = row + rowl[i]
#         ncol = col + coll[i]
#         if nrow >= 0 and nrow < len(maps) and ncol >= 0 and ncol < len(maps[0]):
#             if maps[nrow][ncol] == 1:
#                 if visited[nrow][ncol] == False:
#                     search(nrow, ncol, maps, visited, ans, mov + 1)
#                     visited[nrow][ncol] = False
#
#
# def solution(maps):
#     ans = [100000000]
#     visited = []
#     for i in maps:
#         tmp = []
#         for j in i:
#             tmp.append(False)
#         visited.append(tmp)
#
#     search(0, 0, maps, visited, ans, 1)
#     if ans[0] != 100000000:
#         return ans[0]
#     else:
#         return -1
#
#     return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))