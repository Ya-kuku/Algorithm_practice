n = int(input())
data = list(map(int,input().split()))
x = int(input())
data.sort()
cnt = 0

i = 0
j = n - 1
while i != j:
    if data[i] + data[j] == x:
        cnt += 1
        # 정렬된 수에서 동일한 숫자가 존재할수 있으니 i의 인덱스를 늘리는게 맞음
        # 단 이 문제에서는 서로 다른 양수니까 j -= 1 추가도 가능
        i += 1
    elif data[i] + data[j] > x:
        j -= 1
    else:
        i += 1

print(cnt)