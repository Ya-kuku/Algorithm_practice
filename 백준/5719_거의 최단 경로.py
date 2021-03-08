from collections import deque
from sys import stdin
import heapq
input = stdin.readline
def dijkstra():
    heap_data = []
    heapq.heappush(heap_data,(0, st))
    distance[st] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            # 맨 처음 다익스트라에서 drop 테이블은 전부 False
            # 다시 돌리는 다익스트라에서는 맨처음 최단경로의 값들을 drop 테이블에 True로 저장했으므로 조건만족 x
            if distance[i[0]] > cost and not dropped[now][i[0]]:
                # 최소 가중치를 더해줘야 하기 때문에
                distance[i[0]] = cost
                heapq.heappush(heap_data,(cost,i[0]))
def bfs():
    q = deque()
    q.append(end)
    while q:
        now = q.popleft()
        if now == st:
            continue
        # 추적하기 위해서 간선정보 반대로 입력한 값 2 -> 3 으로 가는 정보였으면 역추적으로 3 -> 2로 가는 정보
        for prev, cost in reverse_adj[now]:
            if distance[now] == distance[prev] + cost:
                dropped[prev][now] = True
                # 역추적 정보 담아주기
                q.append(prev)
while 1:
    n, m = map(int,input().split())
    if n == 0:
        break
    st, end = map(int,input().split())
    adj = [[] for _ in range(n+1)]
    reverse_adj = [[] for _ in range(n+1)]

    for _ in range(m):
        x, y, cost = map(int,input().split())
        adj[x].append((y,cost))
        reverse_adj[y].append((x,cost))

    dropped = [[False] * (n+1) for _ in range(n+1)]
    distance = [1e9] * (n+1)
    dijkstra()
    bfs()
    # 새롭게 distance배열 만들기
    distance = [1e9] * (n+1)
    dijkstra()
    if distance[end] != 1e9:
        print(distance[end])
    else:
        print(-1)