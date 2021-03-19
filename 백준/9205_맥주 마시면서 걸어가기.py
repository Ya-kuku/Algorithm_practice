# from collections import deque
#
# def bfs(x, y):
#     q, c = deque(), []
#     q.append([x, y, 20])
#     c.append([x, y, 20])
#     while q:
#         x, y, beer = q.popleft()
#         if x == ed[0] and y == ed[1]:
#             print("happy")
#             return
#         for nx, ny in dists:
#             if [nx, ny, 20] not in c:
#                 l1 = abs(nx - x) + abs(ny - y)
#                 if beer*50 >= l1:
#                     q.append([nx, ny, 20])
#                     c.append([nx, ny, 20])
#     print("sad")
#     return
# for tc in range(int(input())):
#     n = int(input())
#     st = tuple(map(int,input().split()))
#     dists = []
#     for _ in range(n):
#         dists.append(tuple(map(int,input().split())))
#     ed = tuple(map(int,input().split()))
#     dists.append((ed[0],ed[1]))
#     bfs(st[0],st[1])



max = 1e9
for tc in range(int(input())):
    n = int(input()) # 0 <= n <= 100
    arr = [tuple(map(int, input().split()))]
    for _ in range(n):
        arr.append(tuple(map(int, input().split())))
    arr.append(tuple(map(int, input().split())))

    graph = [[max] * (n + 2) for _ in range(n + 2)]

    # 정점 간 이동 가능 표시
    for i in range(n + 2):
        for j in range(n + 2):
            if i == j:
                graph[i][j] = 0
                continue
            x1, y1 = arr[i]
            x2, y2 = arr[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            # 갈수 있는 정점만 표시를 해두고
            if dist <= 1000:
                graph[i][j] = 1

    # 여기선 최단거리라기 보단 갈 수 있는지를 확인하기 때문에
    # 갈 수 없다면 graph[i][j] 가 Inf의 값으로 표시 될것임

    for k in range(n + 2):
        for i in range(n + 2):
            for j in range(n + 2):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    if 0 < graph[0][n +1] < max:
        print('happy')
    else:
        print('sad')