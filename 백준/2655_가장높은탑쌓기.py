N = int(input())
array = [(0,0,0,0)]

for i in range(1,N+1):
    A,H,W = map(int,input().split())
    array.append((i,A,H,W))

    # 무게에 대해 정렬
array.sort(key=lambda x:x[3])

dp = [0] * (N+1)

for i in range(1,N+1):
    for j in range(i):
        if array[i][1] > array[j][1]:
            dp[i] = max(dp[i],dp[j] + array[i][2])

Max = max(dp)
idx = N
res = []

while idx != 0:
    if Max == dp[idx]:
        res.append(array[idx][0])
        Max -= array[idx][2]
    idx -= 1

print(len(res))
res.reverse()
[print(i) for i in res]



