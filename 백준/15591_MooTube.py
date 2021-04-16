import sys
sys.setrecursionlimit(10000)
def check(k,v):
    global cnt
    if G[v]:
        for a in G[v]:
            if a[1] >= k and not visited[a[0]]:
                cnt += 1
                visited[a[0]] = 1
                check(k,a[0])
    return cnt -1
N, Q = map(int,input().split())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    p,q,r = map(int,input().split())
    G[p].append((q,r))
    G[q].append((p,r))
print(G)
for _ in range(Q):
    cnt = 0
    k,v = map(int,input().split())
    visited = [0] * (N+1)
    res = check(k,v)
    if res == -1:
        print(0)
    else:
        print(res)