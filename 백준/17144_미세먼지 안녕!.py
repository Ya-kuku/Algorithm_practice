dr = [0,0,1,-1]
dc = [1,-1,0,0]
# r = 세로 c = 가로 t = 시간
r, c, t = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(r)]
cur_time = 0

def move(dust_info):
    tmp = [[0] * c for _ in range(r)]
    # 미세먼지 확산
    for dust in dust_info:
        x,y = dust
        cnt = 0
        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]
            if 0 <= nx < r and 0 <= ny < c:
                if arr[nx][ny] != -1:
                    cnt += 1
                    tmp[nx][ny] += arr[x][y] // 5
        tmp[x][y] += (arr[x][y] - (arr[x][y] // 5) * cnt)

    # 공기 청정기 바람 이동
    high = airwasher[0]
    row = airwasher[-1]
    # 윗 부분
    for i in range(high[0],0,-1):
        tmp[i][0] = tmp[i-1][0]
    for i in range(1,c):
        tmp[0][i-1] = tmp[0][i]
    for i in range(0,high[0]):
        tmp[i][c-1] = tmp[i+1][c-1]
    for i in range(c-1,1,-1):
        tmp[high[0]][i] = tmp[high[0]][i-1]
    tmp[high[0]][1] = 0
    # 아랫 부분
    for i in range(row[0],r-1):
        tmp[i][0] = tmp[i+1][0]
    for i in range(1,c):
        tmp[r-1][i-1] = tmp[r-1][i]
    for i in range(r-1,row[0],-1):
        tmp[i][c-1] = tmp[i-1][c-1]
    for i in range(c-1,1,-1):
        tmp[row[0]][i] = tmp[row[0]][i-1]
    tmp[row[0]][1] = 0

    return tmp

while cur_time < t:
    dust_info = []
    airwasher = []
    for i in range(r):
        for j in range(c):
            if arr[i][j] not in [-1,0]:
                dust_info.append((i,j))
            if arr[i][j] == -1:
                airwasher.append((i,j))
    arr = move(dust_info)
    for i in airwasher:
        arr[i[0]][i[1]] = -1
    cur_time += 1

res = 0
for i in arr:
    res += sum(i)
print(res+2)


