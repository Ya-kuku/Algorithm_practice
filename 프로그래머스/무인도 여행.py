def solution(maps):
    answer = []
    new_maps = []
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    size = len(maps)
    for i in range(len(maps)):
        new_maps.append(list(maps[i]))

    visited = [[] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if new_maps[i][j] != 'X' and visited[i][j] == 0:
                tmp = int(new_maps[i][j])
                visited[i][j] = 1
                for dir in dirs:
                    x = i + dir[0]
                    y = j + dir[1]
                    if new_maps[x][y] != 'X' and visited == 0:
                        visited[x][y] = 1
                        tmp += int(new_maps[x][y])



    return answer

solution(["X591X","X1X5X","X231X", "1XXX1"])