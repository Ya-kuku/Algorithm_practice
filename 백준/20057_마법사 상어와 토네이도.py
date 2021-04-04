import sys
dirs = [(0,-1),(1,0),(0,1),(-1,0)]
per_dirs = [
    [(-1,-1,10),(-1,0,7),(-1,1,1),(1,1,1),(1,0,7),(1,-1,10),(0,-2,5),(-2,0,2),(2,0,2)],
    [(-1,-1,1),(-1,1,1),(0,1,7),(1,1,10),(1,-1,10),(0,-1,7),(0,-2,2),(0,2,2),(2,0,5)],
    [(-1,-1,1),(-1,0,7),(-1,1,1),(1,1,10),(1,0,7),(1,-1,1),(-2,0,2),(0,2,5),(2,0,2)],
    [(-1,-1,10),(-1,1,10),(0,1,7),(1,1,1),(1,-1,1),(0,-1,7),(-2,0,5),(0,2,2),(0,-2,2)]
]
def spread(r,c,dir):
    global sand
    remain = arr[r][c]
    for a in per_dirs[dir]:
        nr = r + a[0]
        nc = c + a[1]
        if 0 <= nr < n and 0 <= nc < n:
            arr[nr][nc] += int(remain * a[2] * 0.01)
            arr[r][c] -= int(remain * a[2] * 0.01)
        else:
            sand += int(remain * a[2] * 0.01)
            arr[r][c] -= int(remain * a[2] * 0.01)

    if 0 <= r + dirs[dir][0] <n and 0 <= c + dirs[dir][1] <n:
        x = r + dirs[dir][0]
        y = c + dirs[dir][1]
        arr[x][y] += arr[r][c]
        arr[r][c] = 0
    else:
        x = r + dirs[(dir+1)%4][0]
        y = c + dirs[(dir+1)%4][1]
        arr[x][y] += arr[r][c]
        arr[r][c] = 0
    for i in arr:
        print(i)
    print()
    if (r,c) == (0,0):
        print(sand)
        sys.exit()
def go(r,c):
    cur_dir = 0
    for p in range(1,n+1):
        dir = cur_dir % 4
        for i in range(p):
            r = r + dirs[dir][0]
            c = c + dirs[dir][1]
            spread(r,c,dir)
        cur_dir += 1
        dir = cur_dir % 4
        for i in range(p):
            r = r + dirs[dir][0]
            c = c + dirs[dir][1]
            spread(r, c,dir)
        cur_dir += 1
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
sand = 0
# arr1 = [[0] * n for _ in range(n)]
go(n//2,n//2)