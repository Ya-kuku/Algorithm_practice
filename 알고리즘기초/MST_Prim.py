# 신장 트리(Spanning Tree)
# 모든 노드가 서로 연결
# 트리의 속성을 만족(사이클이 존재 x)

# 최소 신장 트리(MST, Minimum Spanning Tree)
# 가능한 신장트리 중 간선의 가중치 합이 최소인 신장트리

# 크루스칼 알고리즘 = 모든 간선을 대상으로 해서 가장 가중치가 작은 간선 부터 연결함
# 프림 알고리즘 = 지금 연결된 노드에 붙어 있는 간선 중에서 가중치가 작은 간선을 선택하는 방식

# Prim's algorithm
import heapq

queue = []
graph_data = [[2, 'A'], [5, 'B'], [3, 'C']]

# for edge in graph_data:
#     heapq.heappush(queue, edge)

# for index in range(len(queue)):
#     print(heapq.heappop(queue))

# heapify를 쓰면 위에 코드와 같다
heapq.heapify(graph_data)

for index in range(len(graph_data)):
    print(heapq.heappop(graph_data))

# defaultdict 함수를 사용해서, key에 대한 value를 지정하지 않았을 시, 빈 리스트로 초기화하기
from collections import defaultdict

list_dict = defaultdict(list)
print (list_dict['key1'])



myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

from heapq import *

def prim(start_node, edges):
    adjacent_edges = defaultdict(list)
    mst = list()
    for weight, n1, n2 in edges:
        # n1에서 n2로 가는 경우
        adjacent_edges[n1].append((weight,n1,n2))
        # n2에서 n1로 가는 경우
        adjacent_edges[n2].append((weight,n1,n2))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        # 여기서 추출되는 값은 간선의 가중치 중 가장 작은값이 뽑힘 / n1은 현재 정점, n2는 n1과 연결된 인접 정점
        weight, n1, n2 = heappop(candidate_edge_list)
        # 인접정점이 이미 연결된 노드 집합에 없으면, 연결된 노드 set에 포함해야 한다
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight,n1,n2))

            # 인접 정점의 새로운 인접 정점들의 리스트를 후보군에 넣어 준다
            for edge in adjacent_edges[n2]:
                # 새로운 인접 정점의 연결된 정점들 중에서 이미 연결된 노드에 들어있지 않는 경우만
                # 시간복잡도 줄여주기 위한 조건
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)

    return mst

print(*prim('A',myedges),sep='\n')


# 개선된 프림 알고리즘(간선이 아닌 노드 중심으로) 다시 공부

