# import sys
#
# sys.setrecursionlimit(300000)
#
#
# def dfs(x, a, board):
#     global visited
#     global answer
#     global length
#
#     now = a[x]
#     visited[x] = 1
#
#     for i in board[x]:
#         if visited[i] == 0:
#             now += dfs(i, a, board)
#
#     answer += abs(now)
#
#     return now
#
#
# def solution(a, edges):
#     global visited
#     global answer
#     global length
#
#     answer = 0
#
#     if sum(a) != 0:
#         return -1
#
#     length = len(a)
#     board = [[] for _ in range(length)]
#
#     for i, j in edges:
#         board[i].append(j)
#         board[j].append(i)
#
#     visited = [0] * length
#     dfs(0, a, board)
#     return answer

import sys
sys.setrecursionlimit(10**7)
def solution(a, edges):
    if sum(a):
        return -1
    # greedy
    # 부모 자식간의 관계를 트리로 생성
    cp_link = [list() for i in range(len(a))]
    # cp_link[0] 은 부모노드, 최상위 노드혹은 없는 경우 -1
    visited = [0] * len(a)
    for i in range(len(edges)):
        cp_link[edges[i][0]].append(edges[i][1])
        cp_link[edges[i][1]].append(edges[i][0])
    global answer
    answer = 0

    # 트리 순회. leaf node부터 연산
    def preorder(node):
        global answer
        # 무향 그래프를 그대로 사용하므로 방문한 노드인지 체크
        if visited[node]:
            return 0
        # 방문하지 않았으면 방문 체크
        visited[node] = 1
        # 인접한 모든 노드 방문
        for i in range(len(cp_link[node])):
            a[node] += preorder(cp_link[node][i])
        # 모든 노드 방문했으면 위로 올라가
        son = a[node]
        a[node] = 0
        answer += abs(son)
        return son

    preorder(0)
    if not a[0]:
        return answer
    return -1

solution([-5,0,2,1,2],[[0,1],[3,4],[2,3],[0,3]]	)