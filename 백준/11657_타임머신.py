def bf(start):
    # 시작 노드 초기화
    dist[start] = 0
    # 전체 n번의 라운드를 반복
    for i in range(n):
        # 매 반복마다 모든 간선을 확인
        for j in range(m):
            # 담겨 있는 모든 간선 정보를 확인
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우 최단 거리 갱신
            if dist[cur] != 1e9 and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환 존재
                # 항상 최단거리를 구해서 저장했는데 전체 최단거리를 구한 후 한번더 반복문을 돌렸을 때 최솟값이 갱신이 된다는것은
                # 음수의 사이클이 존재하기 때문에 최솟값이 갱신이 되는 것
                if i == n-1:
                    return True
    return False

n, m = map(int,input().split())
# 모든 간선에 대한 정보 담는 리스트
edges = []
# 최단 거리를 담아주는 리스트
dist = [1e9] * (n+1)

for _ in range(m):
    a, b, c = map(int,input().split())
    edges.append((a,b,c))

# 벨만 포드 알고리즘
check_cycle = bf(1)

print(dist)
if check_cycle:
    print(-1)
else:
    for i in range(2,n+1):

        if dist[i] == 1e9:
            print(-1)
        else:
            print(dist[i])



# import sys
# # 놓친부분: 출발점에서 도달 할 수 없는 정점 간에 음수 경로가 존재할 때, 1->2 버스 노선이 여러 개일 수 있다.
# def bellman():
#     global n, has_neg_cycle, infi
#     for repeat in range(n): # n번을 돌려서 최단 거리를 구한다.
#         for i in range(1, n+1): # i 주변의 점들을 update
#             for ver, wei in adj[i]:  # j는 i 주변의 점이다.
#                 if timed[ver] > timed[i] + wei and timed[i] != infi:
#                     if repeat == n - 1: # n번째 돌렸는데 변하는 구간이 있다면 음의 사이클이 있는 것이다.
#                         has_neg_cycle = True
#                         return
#                     timed[ver] = timed[i] + wei
#
#
# if __name__ == '__main__':
#     # n개 도시 1~500, m개 버스 1~6000
#     # a,b,c : 시작, 도착, 걸리는 시간(-10000 ~ 10000) c가 0이면 순간이동 음수면 타임머신
#     n, m = map(int, sys.stdin.readline().rstrip().split())
#
#     # 최대 시간: 각 도시마다 만시간 걸림: 500*10000
#     infi = 10000000000
#     adj = [[] for _ in range(n+1)]
#     # 버스 정보 저장
#     for _ in range(m):
#         s,e,t = map(int, sys.stdin.readline().rstrip().split())
#         adj[s].append((e,t))
#
#     has_neg_cycle = False
#     timed = [infi for _ in range(n+1)]
#     start = 1
#     timed[start] = 0
#
#     bellman()
#     # 무한히 줄어들면 -1, 가는 경로 없다면 -1, 이외는 가장 빠른 시간
#     if has_neg_cycle:
#         print(-1)
#     else:
#         for i in range(2, n + 1):
#             print(-1 if timed[i] == infi else timed[i])