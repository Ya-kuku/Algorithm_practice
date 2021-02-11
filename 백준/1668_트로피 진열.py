N = int(input())
trophy = [int(input()) for _ in range(N)]
le_cnt = ri_cnt = 1
le = trophy[0]
ri = trophy[-1]
for i in range(1,N):
    if trophy[i] > le:
        le_cnt += 1
        le = trophy[i]
    elif trophy[i] <= le:
        continue
print(le_cnt)
for i in range(N-2,-1,-1):
    if trophy[i] > ri:
        ri_cnt += 1
        ri = trophy[i]
    elif trophy[i] <= ri:
        continue
print(ri_cnt)  