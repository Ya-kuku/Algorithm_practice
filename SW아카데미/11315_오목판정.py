dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]
def check():
    global tc
    cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                for i in range(8):
                    cnt = 1
                    nr = r + dr[i]
                    nc = c + dc[i]
                    while 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == '.': break
                        cnt += 1
                        if cnt == 5:
                            return "#{} YES".format(tc+1)
                        nr = nr + dr[i]
                        nc = nc + dc[i]
    return "#{} NO".format(tc+1)
for tc in range(int(input())):
    N = int(input())
    arr = [input() for _ in range(N)]
    print(check())
