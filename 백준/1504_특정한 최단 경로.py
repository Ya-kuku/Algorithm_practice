import heapq
def dijkstra(st):
    heap_data = []
    distance = [1e9] * (N + 1)
    heapq.heappush(heap_data,(0,st))
    distance[st] = 0

    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist: continue

        for i in adj[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap_data,(cost,i[0]))
    return distance
N, E = map(int,input().split())
adj = [[] for _ in range(N+1)]
for _ in range(E):
    x, y, weight = map(int,input().split())
    adj[x].append((y,weight))
    adj[y].append((x,weight))
v1, v2 = map(int,input().split())
start = dijkstra(1)
_v1 = dijkstra(v1)
_v2 = dijkstra(v2)
res = min(start[v1] + _v1[v2] + _v2[N], start[v2] + _v2[v1] + _v1[N])
if res >= 1e9:
    print(-1)
else:
    print(res)


