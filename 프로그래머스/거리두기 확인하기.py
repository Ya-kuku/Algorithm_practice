from collections import deque
def solution(places):
    answer = []
    for place in places:
        arr = []
        for pl in place:
            arr.append(list(pl))
        candidates = []
        for i in range(5):
            for j in range(5):
                if arr[i][j] == 'P':
                    candidates.append((i, j))
        for candidate in candidates:
            possible = bfs(candidate[0], candidate[1], arr)

            if not possible:
                answer.append(possible)
                break
        else:
            answer.append(1)

    return answer

def bfs(r, c, arr):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited = [[0] * 5 for _ in range(5)]
    visited[r][c] = 1
    q = deque()
    q.append((r, c))

    while q:
        x, y = q.popleft()
        for dir in dirs:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < 5 and 0 <= ny < 5 and not arr[nx][ny] == 'X' and not visited[nx][ny]:
                if arr[nx][ny] == 'P':
                    visited[nx][ny] = visited[x][y] + 1
                    if visited[nx][ny] <= 3:
                        return 0
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return 1
solution([
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
])