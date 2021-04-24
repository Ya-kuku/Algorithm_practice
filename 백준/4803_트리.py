from collections import deque
def check(node):
    visited[node] = 1
    q = deque()
    q.append((node,0))

    while q:
        cur_node, p = q.popleft()
        for node_next in G[cur_node]:
            if not visited[node_next]:
                visited[node_next] = 1
                q.append((node_next,cur_node))
            elif node_next != p:
                return 0
    return 1

Test_case = 1
while 1:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break

    G = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        G[a].append(b)
        G[b].append(a)

    visited = [0] * (n+1)
    trees = 0

    for node in range(1,n+1):
        if not visited[node]:
            trees += check(node)

    if trees > 1:
        print('Case {}: A forest of {} trees.'.format(Test_case, trees))
    elif trees == 1:
        print('Case {}: There is one tree.'.format(Test_case))
    else:
        print('Case {}: No trees.'.format(Test_case))

    Test_case += 1