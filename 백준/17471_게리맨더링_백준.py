from collections import deque
def bfs(x):
    Q = deque()
    check = [0] * N
    Q.append(x[0])
    check[x[0]] = 1
    ans = 0
    cnt = 1
    while Q:
        a= Q.popleft()
        ans += peoples[a]
        for w in G[a]:
            if w in x and not check[w]:
                check[w] = 1
                cnt += 1
                Q.append(w)
    if cnt == len(x):
        return ans
    else:
        return 0
def dfs(cnt, x, end):
    global Min
    if cnt == end:
        gery1, gery2 = deque(), deque()
        for i in range(N):
            if visit[i]:
                gery1.append(i)
            else:
                gery2.append(i)
        ans1 = bfs(gery1)
        if not ans1:
            return
        ans2 = bfs(gery2)
        if not ans2:
            return
        Min = min(Min,abs(ans1-ans2))
        return

    for i in range(x,N):
        if visit[i]: continue
        visit[i]= 1
        dfs(cnt+1,i,end)
        visit[i] = 0

N = int(input())
peoples = list(map(int,input().split()))
G = [[] for _ in range(N)]
for i in range(N):
    section = list(map(int,input().split()))
    for j in range(1,section[0]+1):
        G[i].append(section[j]-1)
#        인덱스가 0부터 시작이니까 여기서 -1해줘야 함
Min = 0xffffff
for i in range(1,N//2+1):
    visit = [0] * N
    dfs(0,0,i)

if Min == 0xffffff:
    print(-1)
else:
    print(Min)


# n = int(input())
# people = list(map(int, input().split()))
#
# a = [[] for _ in range(n)]
# for i in range(n):
#     x = list(map(int, input().split()))
#     for j in range(1, x[0]+1):
#         a[i].append(x[j])
# print(a)