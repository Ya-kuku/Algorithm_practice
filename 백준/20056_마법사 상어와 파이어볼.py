import copy
# n 배열크기, m 발사한 파이어볼 개수, k 이동 횟수
n, m, k = map(int,input().split())
arr = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    # r,c 위치, m 질량, s 속력, d 방향
    r, c, m, s, d = map(int,input().split())
    if m:
        arr[r-1][c-1].append((m,s,d))
dirs = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# k만큼 반복
for _ in range(k):
    tmp_arr = [[[] for _ in range(n)] for _ in range(n)]

    for r in range(n):
        for c in range(n):
            if arr[r][c]:
                for info in arr[r][c]:
                    m, s, d = info
                    # 속력 s칸만큼 이동
                    nr = r + dirs[d][0] * s
                    nc = c + dirs[d][1] * s
                    nx = (nr + n) % n
                    ny = (nc + n) % n
                    tmp_arr[nx][ny].append((m,s,d))

    for x in range(n):
        for y in range(n):
            if len(tmp_arr[x][y]) >= 2:
                cm, cs, cd = 0,0,[]
                cnt = len(tmp_arr[x][y])
                for c in range(cnt):
                    cm += tmp_arr[x][y][c][0]
                    cs += tmp_arr[x][y][c][1]
                    # 방향 홀수 짝수 판별
                    cd.append(tmp_arr[x][y][c][2] % 2)
                cm = cm // 5
                cs = cs // cnt
                tmp_arr[x][y] = []
                # 질량이 0이면 소멸
                if cm:
                    # 홀짝판별에서 나머지값으로 봤을때 합이 0이면 모두 짝수, 합이 그 배열의 길이만큼이면 모두 홀수
                    if sum(cd) == 0 or sum(cd) == cnt:
                        for i in range(4):
                            tmp_arr[x][y].append((cm,cs,i * 2))
                    else:
                        for i in range(4):
                            tmp_arr[x][y].append((cm, cs, i * 2 +1))

    arr = copy.deepcopy(tmp_arr)

res = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            for num in arr[i][j]:
                res += num[0]
print(res)