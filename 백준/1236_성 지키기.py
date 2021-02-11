N,M = map(int,input().split())
castle = [list(input()) for _ in range(N)]
row_res = col_res = 0
for i in range(N):
    if 'X' not in castle[i]:
        row_res += 1
for j in range(M):
    if ("X" not in [castle[i][j] for i in range(N)]):
        col_res += 1
print(max(row_res,col_res))