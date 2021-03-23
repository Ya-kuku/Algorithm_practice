import heapq
def dijkstra(st):
    heap_data = []
    distance = [1e9] * (n + 1)

    heapq.heappush(heap_data,(0,st))
    distance[st] = 0

    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist: continue

        for i in arr[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap_data,(cost,i[0]))

    return distance
for tc in range(int(input())):
    # n = 교차로 m = 도로 t = 목적지 후보
    n, m, t = map(int,input().split())
    # s = 출발지 g, h = 교차로를 지나고 있다
    s, g, h = map(int,input().split())
    arr = [[] for _ in range(n+1)]
    for _ in range(m):
        # c = cost
        a, b, c = map(int,input().split())
        arr[a].append((b,c))
        arr[b].append((a,c))
    eds = []
    for _ in range(t):
        eds.append(int(input()))

    start = dijkstra(s)
    arrival_g = dijkstra(g)
    arrival_h = dijkstra(h)
    ans = []
    for ed in eds:
        if start[g] + arrival_g[h] + arrival_h[ed] == start[ed] or start[h] + arrival_h[g] + arrival_g[ed] == start[ed]:
           ans.append(ed)
    ans.sort()
    print(*ans)



