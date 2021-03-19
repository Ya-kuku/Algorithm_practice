n = int(input())
data = list(map(int,input().split()))
data.sort()

i = 0
j = n - 1
res = []
Min = data[0] + data[-1]
cur_i = i
cur_j = j
while i != j:
    tmp = data[i] + data[j]
    if abs(tmp) < abs(Min):
        Min = tmp
        cur_i = i
        cur_j = j
        if Min == 0:
            break
    # 더한 값이 음수이면 절대값 기준으로 음수값이 더 크다는 뜻이므로 음수값을 줄여야한다. 즉 왼쪽 인덱스 늘리기
    if tmp < 0:
        i += 1
    # 더한 값이 양수이면 절대값 기준으로 양수값이 더 크다는 뜻
    else:
        j -=1

print(data[cur_i],data[cur_j])
