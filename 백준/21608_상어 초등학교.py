import sys
input = sys.stdin.readline
N = int(input())
arr = [[0] * N for _ in range(N)]
info = [list(map(int,input().split())) for _ in range(N*N)]
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
res = 0
def arrange(idx,likes):
    pos = []
    for r in range(N):
        for c in range(N):
            if arr[r][c]: continue
            empty, cnt = 0, 0
            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]
                if 0 <= nr < N and 0 <= nc < N:
                    if arr[nr][nc] == 0: empty += 1
                    if arr[nr][nc] in likes: cnt += 1
            pos.append((cnt,empty,r,c))
    pos.sort(key=lambda data : (-data[0],-data[1],data[2],data[3]))
    arr[pos[0][2]][pos[0][3]] = idx

def satisfy(lst):
    global res
    num, like = lst[0], lst[1:]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == num:
                cnt = 0
                for dir in dirs:
                    nr, nc = r + dir[0], c + dir[1]
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] in like: cnt += 1

                if cnt == 2: res += 10
                elif cnt == 3: res += 100
                elif cnt == 4: res += 1000
                else: res += cnt

                return

for i in range(N*N):
    idx, likes = info[i][0], info[i][1:]
    arrange(idx,likes)

for i in range(N*N):
    satisfy(info[i])
print(res)