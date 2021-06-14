import sys

r, c, m = map(int, sys.stdin.readline().split())
maps = [[0 for _ in range(c)] for _ in range(r)]
for _ in range(m):
    y, x, s, d, z = map(int, sys.stdin.readline().split())
    maps[y - 1][x - 1] = (s, d - 1, z)
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]


# 가장 가까운 거리의 상어 잡기
def get_shark(column_idx, maps):
    size = 0
    for idx in range(len(maps)):
        if maps[idx][column_idx] != 0:
            speed, dirs, size = maps[idx][column_idx]
            maps[idx][column_idx] = 0
            break
    return size


def move_sharks(maps):
    new_shark = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] != 0:
                speed, i, size = maps[y][x]
                # 왕복 횟수 제거
                if i == 0 or i == 1:
                    speed %= ((2 * len(maps)) - 2)
                elif i == 2 or i == 3:
                    speed %= ((2 * len(maps[0])) - 2)

                ny, nx = y, x
                # 시작부터 방향 반대로 바꿔줘야 하는 경우
                if ny == 0 and i == 0:
                    i = 1
                elif ny == len(maps) - 1 and i == 1:
                    i = 0
                elif nx == len(maps[0]) - 1 and i == 2:
                    i = 3
                elif nx == 0 and i == 3:
                    i = 2
                # 상어 이동
                for _ in range(speed):
                    if i == 0:
                        ny -= 1
                        if ny - 1 < 0:
                            i = 1
                    elif i == 1:
                        ny += 1
                        if ny + 1 >= len(maps):
                            i = 0
                    elif i == 2:
                        nx += 1
                        if nx + 1 >= len(maps[0]):
                            i = 3
                    elif i == 3:
                        nx -= 1
                        if nx - 1 < 0:
                            i = 2
                # 이동한 지점에 상어가 없거나, 자리잡은 상어보다 크기가 큰 경우
                if new_shark[ny][nx] == 0 or size > new_shark[ny][nx][2]:
                    new_shark[ny][nx] = (speed, i, size)

    return new_shark


shark_size = 0
for idx in range(c):
    shark_size += get_shark(idx, maps)
    maps = move_sharks(maps)
print(shark_size)
