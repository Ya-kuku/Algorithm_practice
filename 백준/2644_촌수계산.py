from collections import deque
def bfs(st,ed):
    q = deque()
    visited[st] = 1
    q.append((st,0))
    while q:
        x, cur = q.popleft()
        if x == ed:
            return cur
        for i in G[x]:
            if not visited[i]:
                visited[i] = 1
                q.append((i, cur+1))
    return -1
n = int(input())
st, ed = map(int,input().split())
m = int(input())
G = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
print(bfs(st,ed))