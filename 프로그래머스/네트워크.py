from collections import deque
def bfs(n,computers, i ,visited):
    visited[i] = 1
    q = deque()
    q.append(i)

    while q:
        x = q.popleft()
        visited[x] = 1

        for y in range(n):
            if y != x and computers[x][y] == 1:
                if not visited[y]:
                    q.append(y)

def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            bfs(n,computers,i,visited)
            answer += 1
    print(answer)
    return answer


solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])
