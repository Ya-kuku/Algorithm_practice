# def find(x):
#     if x == parent[x]:
#         return x
#     else:
#         p = find(parent[x])
#         parent[x] = p
#         return parent[x]
# def union(x,y):
#     x = find(x)
#     y = find(y)
#
#     if x < y:
#         parent[y] = x
#     else:
#         parent[x] = y
#
# N = int(input())
# com= int(input())
# net = [list(map(int,input().split())) for _ in range(com)]
#
# parent = [0] * (N+1)
# for i in range(1,N+1):
#     parent[i] = i
# # print(parent)
# # print(net)
# for _ in range(2):
#     for x,y in net:
#         # print(x,y)
#         union(x,y)
#
# res = 0
# for i in range(2,N+1):
#     if parent[i] == 1:
#         res += 1
# print(res)

def dfs(v):
    global res
    visited[v] = 1
    for i in G[v]:
        if not visited[i]:
            res += 1
            dfs(i)

N = int(input())
com = int(input())
G = [[] for i in range(N+1)]
visited = [0] * (N+1)
res = 0
for _ in range(com):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
dfs(1)
print(res)