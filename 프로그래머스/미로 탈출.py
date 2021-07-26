from heapq import *

def solution(n, start, end, roads, traps):
    answer = 0
    adj=[[] for _ in range(n+1)]
    b_activated= [False for _ in range(n+1)]

    for src,dst,cost in roads:
        # 정방향
        adj[src].append([dst,cost,True])
        # 역방향
        adj[dst].append([src,cost,False])
    q = [(0,start,tuple(b_activated))]
    visited=set()

    while q:
        sum_cost,node,b_activated = heappop(q)
        if (node, b_activated) in visited:
            continue
        visited.add((node, b_activated))

        b_activated = list(b_activated)
        if node == end:
            return sum_cost
        if node in traps:
            b_activated[node] = not b_activated[node]
        b_activated = tuple(b_activated)

        for dst,cost,avail in adj[node]:
            # 원래 방향으로 가는 경우에 다음으로 갈 노드가 같은 방향인 경우
            if avail and b_activated[node] == b_activated[dst]:
                heappush(q,(sum_cost+cost, dst,b_activated))
            # 트랩을 밟고 가는 경우에 다음으로 갈 노드가 이전과 다른 방향인 경우
            if not avail and b_activated[node] != b_activated[dst]:
                heappush(q,(sum_cost+cost, dst,b_activated))
    return answer

solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2])