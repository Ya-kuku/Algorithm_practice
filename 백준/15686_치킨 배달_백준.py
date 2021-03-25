
def check(k,r):
    global Len
    if k == M:
        result = []
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 1:
                    Min = 987654321
                    for k in range(len(store)):
                        a, b = store[k]
                        c = abs(a - i) + abs(b - j)
                        if Min > c :
                            Min = c
                    result.append(Min)
        if Len > sum(result):
            Len = sum(result)

    else:
        for i in range(r,len(house)):
            if visit[i]: continue
            visit[i] = 1
            store.append(house[i])
            check(k+1,i)
            store.pop()
            visit[i] = 0

N, M = map(int,input().split())
arr = [list(map(int,input().split()))for _ in range(N)]

house = []
store = []

Len = 987654
for i in range(N):
    for j in range(N):
        if arr[i][j] ==2:
            house.append((i,j))
visit = [0] * (len(house))
check(0,0)
# print(house)
print(Len)

