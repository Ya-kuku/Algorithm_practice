from collections import deque

def dfs(st,visited):
    visited.append(st)
    for i in graph[st]:
        if i not in visited:
            dfs(i,visited)
    return visited

def bfs(st):
    visited = [st]
    Q = deque([st])
    while Q:
        a = Q.popleft()
        for i in graph[a]:
            if i not in visited:
                visited.append(i)
                Q.append(i)
    return visited

N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    v,e = map(int,input().split())
    graph[v].append(e)
    graph[e].append(v)

# 순서대로 입력이 안들어올 수 있으니 sort를 해줘서 작은 수부터 방문하도록 하기 위해
for e in graph:
    e.sort()

visited = []
res_dfs = dfs(V,visited)
res_bfs = bfs(V)
print(*res_dfs)
print(*res_bfs)