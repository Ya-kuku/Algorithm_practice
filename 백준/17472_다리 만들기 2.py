from collections import deque
N,M = map(int,input().split())
island = [list(map(int,input().split())) for _ in range(N)]
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
visited = [[0] * M for _ in range(N)]

def get_parent(idx):
    if parent[idx] == idx:
        return idx
    parent[idx] = get_parent(parent[idx])
    return parent[idx]

def union_parent(a,b):
    a = get_parent(a)
    b = get_parent(b)
    if a < b:
        parent[b]=a
    else:
        parent[a] = b

def find(a,b):
    a = get_parent(a)
    b = get_parent(b)
    return a == b
def make_bridge(r,c,idx):
    for dir in dirs:
        nr = r + dir[0]
        nc = c + dir[1]
        cnt = 0

        while True:
            if nr < 0 or nr >= N or nc < 0 or nc >= M: break
            # 탐색한 부분이 각은 섬이면 중지
            if island[nr][nc] == idx: break
            # 탐색한 부분이 바다면 계속 이어감
            if island[nr][nc] == 0:
                nr += dir[0]
                nc += dir[1]
                cnt += 1
                continue
            # 다리 길이가 2미만이면 중지
            if cnt < 2: break
            # 위의 조건들에 걸리지 않고 여기까지 온거면 다른 섬에 도착했다는 뜻
            other_island_idx = island[nr][nc]
            # 각 섬의 다리 길이 정보가 있는 2차 배열에 최솟값 저장
            distances[idx-1][other_island_idx-1] = min(distances[idx-1][other_island_idx-1],cnt)
            break

def bfs(r,c):
    global idx
    q = deque()
    visited[r][c] = 1
    island[r][c] = idx
    q.append((r,c))

    while q:
        x,y = q.popleft()
        for dir in dirs:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and island[nx][ny]:
                island[nx][ny] = idx
                visited[nx][ny] = 1
                q.append((nx,ny))
idx = 0
for i in range(N):
    for j in range(M):
        if island[i][j] and not visited[i][j]:
            idx += 1
            bfs(i,j)
# for z in island:
#     print(z)
parent = [i for i in range(idx)]
distances = [[1e9] * idx for _ in range(idx)]
costs = []
ans = 0

for i in range(N):
    for j in range(M):
        if island[i][j]:
            make_bridge(i,j,island[i][j])

# for d in distances:
#     print(d)
for i in range(idx):
    for j in range(idx):
        if distances[i][j] != 1e9 and [j,i,distances[i][j]] not in costs:
            costs.append([i,j,distances[i][j]])

# print(costs)
costs.sort(key=lambda data: data[2])

for cost in costs:
    if not find(cost[0],cost[1]):
        ans += cost[2]
        union_parent(cost[0],cost[1])

for i in range(idx):
    if get_parent(i) != 0:
        ans = -1
        break
print(ans)