def dfs(i,cnt):
    global ans
    visited[i] = 1
    ans = max(ans,cnt)
    for w in G[i]:
        if visited[w]: continue
        dfs(w,cnt+1)
    visited[i] = 0
for tc in range(int(input())):
    N, M = map(int,input().split())
    G = [[] for _ in range(N+1)]
    ans = -1
    for _ in range(M):
        a,b = map(int,input().split())
        G[a].append(b)
        G[b].append(a)
    for i in range(N):
        visited = [0] * (N+1)
        dfs(i,1)
    print('#{} {}'.format(tc+1,ans))


