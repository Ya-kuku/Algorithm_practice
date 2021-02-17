def dfs(v):
    # global cnt
    # cnt += 1
    visited[v] = 1
    for i in com[v]:
        if not visited[i]:
            dfs(i)
    return sum(visited)
N, M = map(int,input().split())
com = [[] for i in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    com[b].append(a)
res = []
Max = - 1
for i in range(N):
    visited = [0] * (N+1)
    cnt = 0
    res.append(dfs(i))
# print(res)
for i in range(len(res)):
    if res[i] == max(res):
        print(i,end=' ')