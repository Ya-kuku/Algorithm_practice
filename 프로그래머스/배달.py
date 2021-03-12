import heapq
def dijkstra(start,adj,distance):
    heap_data = []
    # 처음 시작점 가중치 0, 시작점 삽입
    heapq.heappush(heap_data,(0,start))
    distance[start] = 0

    while heap_data:
        # 현재 가중치, 현재 노드
        dist, now = heapq.heappop(heap_data)
        # 현재 정점의 값이 현재 가중치 보다 작으면 넘어감
        if distance[now] < dist:
            continue

        # 현재 정점에서 갈 수 있는 다른 정점 뽑기
        for i in adj[now]:
            # cost는 현재 가중치 + 갈 수 있는 다른정점의 가중치 값
            cost = dist + i[1]
            # 갈 수 있는 정점의 가중치 값을 cost와 비교
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap_data,(cost,i[0]))

def solution(N, road, K):
    answer = 0
    distance = [1e9] * (N+1)
    adj = [[] for _ in range(N+1)]

    for info in road:
        x, y, cost = info
        adj[x].append((y,cost))
        adj[y].append((x, cost))
    dijkstra(1,adj,distance)
    print(distance)
    for i in distance:
        if i <= K: answer += 1

    return answer

solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)
