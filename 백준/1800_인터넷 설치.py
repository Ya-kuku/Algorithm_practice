import heapq
# N 개수, P 케이블 수, K 무료 케이블 수
N, P, K = map(int,input().split())
adj = [[] for _ in range(N+1)]
def dijkstra(st,Max):
    heap_date = []
    distance = [1e9] * (N+1)

    # 가중치, 시작점
    heapq.heappush(heap_date,(0,st))
    distance[st] = 0

    while heap_date:
        dist, now = heapq.heappop(heap_date)

        if distance[now] < dist: continue

        for i in adj[now]:
            if i[1] > Max:
                if dist + 1 < distance[i[0]]:
                    distance[i[0]] = dist+1
                    heapq.heappush(heap_date,(dist+1,i[0]))
            else:
                if dist < distance[i[0]]:
                    distance[i[0]] = dist
                    heapq.heappush(heap_date,(dist,i[0]))

    if distance[N] > K:
        return False
    else:
        return True

for _ in range(P):
    x, y, cost = map(int,input().split())
    adj[x].append((y,cost))
    adj[y].append((x,cost))

le, ri = 0, 1000001
ans = 1e9
while le <= ri:
    mid = (le + ri) // 2
    pos = dijkstra(1,mid)

    if pos:
        ri = mid - 1
        ans = mid
    else:
        le = mid + 1

if ans == 1e9: print(-1)
else: print(ans)