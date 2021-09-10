import sys
import math
from collections import deque, defaultdict

r, c = map(int, sys.stdin.readline().split())
maps = []
for _ in range(r):
    maps.append(list(map(int, sys.stdin.readline().split())))


# 1. 각 섬별로 라벨링하기.
def bfs(start, maps, continent_name):
    queue = deque()
    queue.append(start)
    dirs = [(0, 1), (-1, 0), (1, 0), (0, -1)]
    while queue:
        y, x = queue.popleft()
        # 해당 섬을 continent_name으로 라벨링한다.
        maps[y][x] = continent_name
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == 1:
                # 해당 섬을 continent_name으로 라벨링한다.
                maps[ny][nx] = continent_name
                queue.append((ny, nx))


# 2. 각 섬별로 최소거리를 구하는 함수
def get_distance(maps):
    # 최소거리를 저장하기 위해 dictionary를 생성하고, 기본값을 math.inf로 설정했다.
    table = defaultdict(lambda: math.inf)

    # iters = [가로, 세로]
    iters = [maps, list(map(list, zip(*maps)))]
    for each_maps in iters:
        for y in range(len(each_maps)):
            continent = None
            checked = set()
            for x in range(1, len(each_maps[0])):
                # 섬 -> 바다로 바뀌는 경우, 섬의 마지막 좌표를 기억한다
                if each_maps[y][x] == 0 and each_maps[y][x - 1] != 0:
                    continent = x - 1

                # 바다 -> 섬으로 바뀌면서 이전에 통과한 섬이 있을 경우
                if each_maps[y][x] != 0 and continent is not None:
                    # 이전 섬과 현재 섬 거리를 계산한다
                    distance = x - continent - 1

                    # 거리가 2 이상이고, 현재 섬이 아직 거리계산을 하지 않은 섬일 경우
                    if distance >= 2 and each_maps[y][x] not in checked:
                        # table에 섬 라벨링을 통일하기 위한 작업.
                        small = min(each_maps[y][continent], each_maps[y][x])
                        large = max(each_maps[y][continent], each_maps[y][x])
                        # 섬과 섬의 거리를 최솟값으로 업데이트한다.
                        table[(small, large)] = min(table[(small, large)], distance)

                    # 현재 섬의 라벨을 저장한다. 이전 섬 - 현재 섬 거리를 중복 계산하면 안 되기 때문
                    checked.add(each_maps[y][x])

    return table


# union find에 필요한 함수
def get_parent(x, parent):
    if x == parent[x]:
        return x
    p = get_parent(parent[x], parent)
    parent[x] = p
    return p


def union_find(y, x, parent):
    y = get_parent(y, parent)
    x = get_parent(x, parent)
    parent[x] = y


def get_min_distance(table, continents):
    # 거리 짦은 순서대로 정렬
    table = sorted(list(table.items()), key=lambda x: x[1])
    result = 0

    # union_find의 parent들
    parent = {i: i for i in range(2, max(continents) + 1)}

    for (y, x), value in table:
        # 두 섬이 '직접 / 간접' 어느 것으로든 연결되어 있지 않은 경우
        if get_parent(y, parent) != get_parent(x, parent):
            # 두 섬을 union_find로 연결한다.
            union_find(y, x, parent)
            result += value

        # 모든 섬이 연결되어 있다면, 모든 섬의 parent를 조사했을 때 값이 1개만 존재한다
        if len(set([get_parent(i, parent) for i in parent])) == 1:
            return result
    return -1


# 섬 라벨링. 처음에 모든 섬이 1로 초기화되어 있어서 2부터 라벨링
continent_num = 2
for y in range(r):
    for x in range(c):
        if maps[y][x] == 1:
            # 각 섬 라벨링 작업
            bfs((y, x), maps, continent_num)
            # 라벨 + 1
            continent_num += 1

# 섬 연결하는 최소거리 구하기
table = get_distance(maps)
# 모든 섬이 연결되었는지 확인하기
print(get_min_distance(table, set(range(2, continent_num))))