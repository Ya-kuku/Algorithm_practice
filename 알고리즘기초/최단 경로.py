import heapq

# 다익스트라 알고리즘 / 최소힙
# queue = []
#
# heapq.heappush(queue,[2,'A'])
# heapq.heappush(queue,[5,'B'])
# heapq.heappush(queue,[1,'C'])
# heapq.heappush(queue,[7,'D'])
# print(queue)
#
# for index in range(len(queue)):
#     print(heapq.heappop(queue))


mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

def dijkstra(graph,start):
    # inf는 무한대 나타내는 표현
    distances = {node:float('inf') for node in graph}
    print(distances)
    distances[start] = 0
    queue = []
    heapq.heappush(queue,[distances[start],start])
    print(queue)

    while queue:
        current_distance, current_node = heapq.heappop((queue))
        print(current_distance,current_node)
        # 현재 노드에 저장된 거리값이 큐에서 뽑은 거리 가중치값보다 작으면 넘긴다
        if distances[current_node] < current_distance:
            continue

        # 현재노드의 value값을 나타내줌
        # 노드, 가중치
        for adjacent, weight in graph[current_node].items():
            # distance라는 변수에 현재 노드거리에 가중치를 더해 저장
            distance = current_distance + weight

            # 경로를 계산했을 때 현재 거리가 저장된 노드의 거리값보다 작은 경우 최단경로 값으로 수정
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                # queue에 변화된 노드의 거리와 노드를 넣어줌
                heapq.heappush(queue,[distance,adjacent])

    return distances

print(dijkstra(mygraph, 'A'))