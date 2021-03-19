n = int(input())
m = int(input())
arr = [[1e9] * n for _ in range(n)]
for _ in range(m):
    x,y, cost = map(int,input().split())
    # 연결된 도시의 노선이 하나가 아닐 수 있기때문에 최솟값 비교해서 넣어주기
    arr[x-1][y-1] = min(cost,arr[x-1][y-1])


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j: arr[i][j] = 0; continue
            # k가 모든 정점을 순환하는 인덱스를 가지니까 i -> k -> j 의 거친 값과 현재 가지고 있는 값을 비교해주는것
            if arr[i][k] + arr[k][j] < arr[i][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
            # arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

# 없느 노선의 경우는 Inf값이 그대로 들어가 있으니 바꿔주기
for i in arr:
    for j in i:
        if j == 1e9:
            print(0, end=' ')
        else:
            print(j,end=' ')
    print()
