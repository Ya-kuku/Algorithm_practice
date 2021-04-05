# 방향 1~8 위,왼위,왼.....오른,오른위
# 4 x 4 배열
import copy
def dfs(r,c):
    pass
dirs = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
arr = [[[]] * 4 for _ in range(4)]
for i in range(4):
    tmp = list(map(int,input().split()))
    for j in range(0,8,2):
        arr[i][j//2] = tmp[j:j+2]

def move(arr):
    for i in range(1,17):
        flag = False
        for a in range(4):
            if flag: break
            for b in range(4):
                if arr[a][b][0] == i:
                    flag = True
                    now = arr[a][b][1]
                    cur_info = arr[a][b]
                    while 1:
                        cur_dir = dirs[(now-1)%8]
                        na = a + cur_dir[0]
                        nb = b + cur_dir[1]
                        if 0<= na < 4 and 0<= nb < 4 and arr[na][nb][0] != 'shark':
                            if arr[na][nb] == 0:
                                arr[na][nb] = arr[a][b]
                                break
                            else:
                                arr[a][b] = arr[na][nb]
                                arr[na][nb] = [cur_info[0],(now-1)%8+1]
                                break
                        else:
                            now += 1
                if flag: break
    return arr
def move_shark(arr,r,c,shark_dir):
    tmp = []
    for i in range(1,4):
        nr = r + dirs[shark_dir-1][0]
        nc = c + dirs[shark_dir-1][1]
        if 0<= nr < 4 and 0 <= nc < 4 and arr[nr][nc][0]:
            tmp.append((nr,nc))
        r,c = nr,nc
    return tmp

def dfs(arr,r,c,total):
    global ans
    arr = copy.deepcopy(arr)
    eat_fish = arr[r][c][0]
    shark_dir = arr[r][c][1]
    arr[r][c] = ['shark', shark_dir]
    # 물고기 움직임
    arr = move(arr)

    # 상어 이동 가능
    res = move_shark(arr,r,c,shark_dir)

    ans = max(ans,total+eat_fish)
    for a in res:
        arr[r][c] = [0,0]
        dfs(arr,a[0],a[1],total+eat_fish)

ans = 0
dfs(arr,0,0,0)
print(ans)
