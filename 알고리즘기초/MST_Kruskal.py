# 신장 트리(Spanning Tree)
# 모든 노드가 서로 연결
# 트리의 속성을 만족(사이클이 존재 x)

# 최소 신장 트리(MST, Minimum Spanning Tree)
# 가능한 신장트리 중 간선의 가중치 합이 최소인 신장트리

# 크루스칼 알고리즘 = 모든 간선을 대상으로 해서 가장 가중치가 작은 간선 부터 연결함
# 프림 알고리즘 = 지금 연결된 노드에 붙어 있는 간선 중에서 가중치가 작은 간선을 선택하는 방식

# Kruskal's Algorithm
mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

parent = dict()
rank = dict()

def find(node):
    # path compression 기법
    # parent[node] == node / 루트노드
    # 루트노드가 아닐 시에 루트노드를 찾기 위한 과정
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v,node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2

        # 랭크가 같을 시에 두 루트노드 중 아무거나 하나를 루트노드로 만들어준다
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = list()

    # 1. 초기화
    for node in graph['vertices']:
        make_set(node)

    # 2. 간선 weight 기반 sorting
    # 크루스칼에서 간선 가중치를 크기별로 정렬해줘야 함
    edges = graph['edges']
    edges.sort()

    # 3. 간선 연결(사이클 없는)
    for edge in edges:
        weight, node_v, node_u = edge
        # 사이클이 없는지 확인
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    return mst

# 한줄씩 출력할때 언패킹을 해줘야 각각의 요소로 출력 가능
print(*kruskal(mygraph),sep='\n')
