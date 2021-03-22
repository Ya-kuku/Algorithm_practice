V, E = map(int,input().split())
G = [[1e9] * (V+1) for _ in range(V+1)]

for _ in range(E):
    x, y, cost = map(int,input().split())
    G[x][y] = cost

for k in range(V+1):
    for i in range(V+1):
        for j in range(V+1):

            if G[i][k] + G[k][j] < G[i][j]:
                G[i][j] = G[i][k] + G[k][j]

Min = 1e9
for i in range(V+1):
    if G[i][i] != 0:
        Min = min(Min,G[i][i])
if Min == 1e9:
    print(-1)
else:
    print(Min)

