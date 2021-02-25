def check(idx,cal,taste):
    global Max
    if cal > L:
        return

    elif idx >= N:
        if cal <= L:
            Max = max(taste,Max)

    else:
        check(idx+1,cal+arr[idx][1],taste+arr[idx][0])
        check(idx+1,cal,taste)

for tc in range(int(input())):
    N, L = map(int,input().split())
    arr = []
    Max = 0
    for _ in range(N):
        arr.append(tuple(map(int,input().split())))
    check(0,0,0)
    print('#{} {}'.format(tc+1,Max))

# def check(n,score, limit):
#     global Max
#     if limit > L:
#         return
#     Max = max(Max, score)
#     for i in range(n+1, N+1):
#         check(i, score + taste[i], limit + cal[i])
#
# for tc in range(int(input())):
#     N, L = map(int, input().split())
#     taste = [0]
#     cal = [0]
#     Max = 0
#     for _ in range(1, N + 1):
#         a, b = map(int, input().split())
#         taste.append(a)
#         cal.append(b)
#     check(0,0,0)
#     print('#{} {}'.format(tc + 1, Max))