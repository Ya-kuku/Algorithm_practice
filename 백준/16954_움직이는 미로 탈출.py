from collections import deque
dirs = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0),(1, 1), (1, -1), (-1, 1), (-1, -1)]

def bfs(start):
    q = deque([start])

    while q:
        # 벽이 이동한 후에, 다시 체크해줘야한다.
        visited = [[False] * 8 for _ in range(8)]
        for _ in range(len(q)):
            cur_x, cur_y = q.popleft()

            if [cur_x, cur_y] == [0, 7]:
                return 1

            if graph[cur_x][cur_y] == '#':
                continue

            for x, y in dirs:
                next_x, next_y = cur_x + x, cur_y + y

                if 0 <= next_x < 8 and 0 <= next_y < 8 and graph[next_x][next_y] == '.' and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    q.append([next_x, next_y])

        # 행을 아래로 이동
        graph.pop()
        graph.insert(0, ['.', '.', '.', '.', '.', '.', '.', '.'])

    return 0

graph = [list(map(str,input())) for _ in range(8)]
print(bfs([7, 0]))