from itertools import permutations
import sys
input = sys.stdin.readline
n, m, k = map(int,input().split())
arrs = [list(map(int,input().split())) for _ in range(n)]
lst = [list(map(int,input().split())) for _ in range(k)]
cmds = list(permutations(lst,k))
res = []
def move(arr,cmd):
    for cm in cmd:
        r, c, s = cm
        x1, y1 = r - s - 1, c - s - 1
        x2, y2 = r + s - 1, c + s - 1

        while x1 < x2 or y1 < y2:
            r_up, r_down, l_down = arr[x1][y2], arr[x2][y2], arr[x2][y1]

            for i in range(y2,y1,-1):
                arr[x1][i] = arr[x1][i-1]

            for i in range(x2,x1,-1):
                arr[i][y2] = arr[i-1][y2]
            arr[x1+1][y2] = r_up

            for i in range(y1,y2):
                arr[x2][i] = arr[x2][i+1]
            arr[x2][y2-1] = r_down

            for i in range(x1,x2):
                arr[i][y1] = arr[i+1][y1]
            arr[x2-1][y1] = l_down

            x1 += 1
            y1 += 1
            x2 -= 1
            y2 -= 1

    ans = 1e9
    for a in arr:
        ans = min(ans,sum(a))
    res.append(ans)

for cmd in cmds:
    arr = []
    for a in arrs:
        arr.append(a[:])
    move(arr,cmd)
print(min(res))