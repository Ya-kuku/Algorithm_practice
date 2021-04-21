from collections import deque

dirs = (-1, 0), (1, 0), (0, -1), (0, 1)

def bfs(start, board, roads):
    q = deque()
    visited = [[0] * N for _ in range(N)]

    q.append((start[0] - 1, start[1] - 1))
    visited[start[0] - 1][start[1] - 1] = 1

    meet_cnt = 0
    while q:
        r, c = q.popleft()

        for dir in dirs:
            nr, nc = r + dir[0], c + dir[1]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if (nr, nc) not in roads[r][c]:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    if board[nr][nc] != -1:
                        meet_cnt += 1

    return K - meet_cnt - 1


def solve():
    board = [[-1] * N for _ in range(N)]

    for i, cow in enumerate(cows):
        r, c = cow
        board[r - 1][c - 1] = i

    road_map = [[set() for _ in range(N)] for _ in range(N)]

    for road in roads:
        start_r, start_c, end_r, end_c = road
        road_map[start_r - 1][start_c - 1].add((end_r - 1, end_c - 1))
        road_map[end_r - 1][end_c - 1].add((start_r - 1, start_c - 1))
    print(road_map)
    ret = 0

    for cow in cows:
        ret += bfs(cow, board, road_map)

    return ret // 2


N, K, R = map(int, input().split())

roads = list(tuple(map(int, input().split())) for _ in range(R))
cows = list(tuple(map(int, input().split())) for _ in range(K))

print(solve())