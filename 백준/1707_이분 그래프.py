from collections import deque
def bfs(st):
    q.append(st)
    visited[st] = 1

    while q:
        x = q.popleft()
        for nx in G[x]:
            print(visited)
            if not visited[nx]:
                visited[nx] = -1 * visited[x]
                q.append(nx)
            elif visited[nx] == visited[x]:
                return 1
    return 0
 for tc in range(int(input())):
    v, e = map(int,input().split())
    G = [[] for _ in range(v)]
    visited = [0] * v
    for _ in range(e):
        a, b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    q = deque()
    ans = 0
    for i in range(v):
        if not visited[i]:
            ans = bfs(i)
            if ans == 1:
                break
    if ans == 0:
        print("YES")
    else:
        print("NO")

