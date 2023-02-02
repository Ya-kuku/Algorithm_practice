    def solution(maps):
        answer = []
        new_maps = []
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        size = len(maps[0]) # 가로
        size_2 = len(maps) # 세로
        for i in range(len(maps)):
            new_maps.append(list(maps[i]))
        print(new_maps)
        visited = [[0] * size for _ in range(size_2)]
        tmp = 0
        for i in range(size_2):
            for j in range(size):
                #print(new_maps[i][j])
                if new_maps[i][j] != 'X' and visited[i][j] == 0:
                    tmp += int(new_maps[i][j])
                    visited[i][j] = 1

                    Q = [(i,j)]
                    while Q:
                        x,y = Q.pop()
                        print(x,y)
                        for dir in dirs:
                            dx = x + dir[0]
                            dy = y + dir[1]
                            #print(dx,dy)
                            if 0 <= dx < size_2 and 0 <= dy < size:
                                if new_maps[dx][dy] != 'X' and visited[dx][dy] == 0:
                                    visited[dx][dy] = 1
                                    tmp += int(new_maps[dx][dy])
                                    Q.append((dx,dy))
                if tmp != 0:
                    answer.append(tmp)
                tmp = 0

        if len(answer) == 0: return [-1]
        else: return sorted(answer)

    print(solution(["X591X","X1X5X","X231X", "1XXX1"]))