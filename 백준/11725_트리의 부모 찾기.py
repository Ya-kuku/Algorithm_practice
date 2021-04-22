import sys
sys.setrecursionlimit(1000000)
n = int(input())
G = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

res = [0] * (n+1)
def DFS(st, tree, parents):
    for i in tree[st]:  # 연결된 노드 모두탐색
        if parents[i] == 0:  # 한번도 방문한적이 없다면
            parents[i] = st  # 부모노드 저장
            DFS(i, tree, parents)

DFS(1, G, res)
for x in res[2:]:
    print(x)