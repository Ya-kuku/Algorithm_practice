from collections import deque
def bfs(st,ed):
    global res
    Q = deque([st])
    visited = [0] * 100001
    flag = True

    while flag:
        res += 1
        for _ in range(len(Q)):
            a = Q.popleft()
            if not visited[a]:
                visited[a] = 1
                if a == ed:
                    print(res,1)
                    flag = False
                    break
                if a -1 >= 0:
                    Q.append(a-1)
                if a + 1 <= 100000:
                    Q.append(a+1)
                if a * 2 <= 100000:
                    Q.append(a*2)

res = 0
N, K = map(int,input().split())
bfs(N,K)
print(res-1)