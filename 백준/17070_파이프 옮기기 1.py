import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
res = 0
def dfs(r,c,dir):
    global res

    if r == n-1 and c == n- 1: res += 1

    # 파이프 오른쪽으로 이동할 때
    if dir == 0:
        # 오른쪽
        if c + 1 < n and arr[r][c+1] == 0:
            dfs(r,c+1,0)
        # 대각선
        if r + 1 < n and c + 1 < n:
            if not arr[r+1][c] and not arr[r][c+1] and not arr[r+1][c+1]:
                dfs(r+1,c+1,2)
    # 파이프 아래로 이동
    elif dir == 1:
        if r + 1< n and arr[r+1][c] == 0:
            dfs(r+1,c,1)
        if r + 1 < n and c + 1 < n:
            if not arr[r+1][c] and not arr[r][c+1] and not arr[r+1][c+1]:
                dfs(r+1,c+1,2)
    # 파이프 대각선으로 이동
    else:
        # 오른쪽 이동
        if c + 1 < n and arr[r][c+1] == 0:
            dfs(r,c+1,0)
        # 아래 이동
        if r + 1 <n and arr[r+1][c] == 0:
            dfs(r+1,c,1)
        # 대각선 이동
        if r + 1 < n and c + 1 < n:
            if not arr[r][c+1] and not arr[r+1][c] and not arr[r+1][c+1]:
                dfs(r+1,c+1,2)

# 시작은 파이프 (0,1)
dfs(0,1,0)
print(res)