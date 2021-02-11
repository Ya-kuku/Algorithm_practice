from collections import deque
# def bfs(a,b):
#     st_x, st_y = a-1,a-1
#     end_x, end_y = b-1, b-1
#     tmp = []
#     for i in range(N):
#         if island[st_x][i]:
#             tmp.append((st_x,i))
#         # elif island[i][st_y]:
#         #     tmp.append((i,st_y))
#     # print(tmp)
#     res = 0
#     for i in range(len(tmp)):
#         # Q = deque((tmp[i][0],tmp[i][1]))
#         Q = deque()
#         Q.append((tmp[i][0],tmp[i][1]))
#         visit= [[0]*N for _ in range(N)]
#         cnt = 999999
#         while Q:
#             x,y = Q.popleft()
#             visit[x][y] = 1
#             if x == end_x or y == end_y:
#                 cnt = min(cnt,island[x][y])
#                 break
#             for i in range(N):
#                 if island[x][i] and not visit[x][i]:
#                     visit[x][i] = 1
#                     visit[i][x] = 1
#                     Q.append((x,i))
#                     cnt = min(cnt,island[x][i])
#         res = max(res,cnt)
#
#     return res
#
# N, M = map(int,input().split())
# island = [ [0] * N for _ in range(N)]
# for _ in range(M):
#     x,y,w = map(int,input().split())
#     island[x-1][y-1] = w
#     island[y-1][x-1] = w
# st, end = map(int,input().split())
# print(bfs(st,end))
from collections import deque

def bfs(mid):
    Q = deque([st_p])
    visit = [0] * (N+1)
    visit[st_p] = 1
    while Q:
        x = Q.popleft()
        for y, w in island[x]:
            # 현재 mid라고 정해진 중량보다 작으면 건널 수 없어서 w가 크거나 같아야 함
            if not visit[y] and w >= mid:
                visit[y] = 1
                Q.append(y)
    # 최종 목적지까지 가능한지 판별
    return visit[end_p]

N,M = map(int,input().split())
island = [[] for _ in range(N+1)]
st = 999999999999
end = 1

for _ in range(M):
    x,y,w = map(int,input().split())
    island[x].append((y,w))
    island[y].append((x,w))
# print(island)
    # 중량의 범위가 크기 때문에 처음부터 중량의 크기로 탐색
    st = min(st,w)
    end = max(end,w)

st_p, end_p = map(int,input().split())

result = st
while st <= end:
    mid = (st+end) // 2
    if bfs(mid):
        result = mid
        st = mid + 1
    else:
        end = mid-1

print(result)
