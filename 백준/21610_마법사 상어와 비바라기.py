import sys
input = sys.stdin.readline
dirs = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
N, M = map(int,input().split())
basket = [list(map(int,input().split())) for _ in range(N)]
cmd = [list(map(int,input().split())) for _ in range(M)]

def cloud_move(lst,clouds):
    way, dist = lst[0], lst[1]
    move_clouds = []

    for cloud in clouds:
        x,y = cloud
        nx, ny = (x + dirs[way-1][0] * dist) % N, (y + dirs[way-1][1] * dist) % N
        basket[nx][ny] += 1
        move_clouds.append((nx,ny))

    rain(move_clouds)

    return move_clouds

def rain(move_clouds):
    for c in move_clouds:
        x,y = c

        for w in (-1,-1),(-1,1),(1,1),(1,-1):
            nx = x + w[0]
            ny = y + w[1]
            if 0 <= nx < N and 0 <= ny < N and basket[nx][ny]:
                basket[x][y] += 1

for i in range(M):
    if i == 0:
        clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
    else:
        clouds = []
        for r in range(N):
            for c in range(N):
                if basket[r][c] >= 2 and (r,c) not in before:
                    clouds.append((r,c))
                    basket[r][c] -= 2

    before = cloud_move(cmd[i],clouds)

for r in range(N):
    for c in range(N):
        if basket[r][c] >= 2 and (r, c) not in before:
            basket[r][c] -= 2
res = 0
for b in basket:
    res += sum(b)
print(res)