import heapq
def dijkkstra(st):
    heap_data = []
    heapq.heappush(heap_data,(0, st))
    distance[st] = 0

    while heap_data:
        dist, now = heapq.heappop(heap_data)

        if distance[now] < dist:
            continue

        for i in G[now]:
            cur_cost = dist + i[1]
            if distance[i[0]] > cur_cost:
                distance[i[0]] = cur_cost
                # i[0] 갈 수 있는 정점 좌표, i[1] 해당 좌표의 가중치
                heapq.heappush(heap_data,(cur_cost,i[0]))

V, E = map(int,input().split())
G = [[] for _ in range(V+1)]
st = int(input()) 
distance = [1e9] * (V+1)
for _ in range(E):
    x,y, cost = map(int,input().split())
    # 방향이 정해진 그래프
    G[x].append((y,cost))

dijkkstra(st)
for i in range(1,V+1):
    if distance[i] == 1e9:
        print('INF')
    else:
        print(distance[i])