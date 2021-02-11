# 위상 정렬 문제
# 순서가 정해져 있는 작업을 차례로 수행할 때, 순서를 결정하는 알고리즘
# 시간 복잡도는 O(V+E)

# 순서
# 1) 진입 차수가 0인 정점을 큐에 삽입
# 2) 큐에서 원소를 꺼내 해당 원소와 간선을 제거
# 3) 제거 이후 진입 차수가 0이 된 정점을 큐에 삽입
# 4) 큐가 빌 때까지 2~3 반복

# 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재하는 것
# 모든 원소를 방문했다면, 큐에서 꺼낸 순서가 위상 정렬의 결과

import heapq
# N = 문제 수, M = 문제 정보 수
N, M = map(int,input().split())
# 연결된 노드의 정보를 담고 있는 변수
array = [[] for i in range(N+1)]
# 해당 노드에 연결된 간선의 수를 기록하는 변수
indegree = [0] * (N+1)

heap = []

for _ in range(M):
    x, y = map(int,input().split())
    array[x].append(y)
    # x -> y 연결이기 때문에 indegree[y]에 연결된 간선 수를 하나씩 더함
    indegree[y] += 1

for i in range(1,N+1):
    if indegree[i] == 0:
        # 들어오는 간선이 없는, 즉, 시작노드를 찾아 우선순위큐를 활용해 heap에 담아준다
        heapq.heappush(heap,i)
# 결과 값을 담은 변수
result = []

while heap:
    data = heapq.heappop(heap)
    result.append(data)
    # 연결된 노드의 값들을 꺼내서
    for y1 in array[data]:
        # 진입차수의 값을 지워준다
        indegree[y1] -= 1
        if indegree[y1] == 0:
            heapq.heappush(heap,y1)

print(*result)