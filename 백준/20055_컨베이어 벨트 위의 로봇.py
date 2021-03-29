from collections import deque
n, k = map(int,input().split())
arr = deque(map(int,input().split()))
robo = deque([0]* (2*n))
res = 1
while 1:
    arr.rotate(1)
    robo.rotate(1)
    robo[n-1] = 0

    # 올라가 있는 로봇부터 옮기기
    for i in range(n-2,-1,-1):
        if robo[i] != 0 and robo[i+1] == 0 and arr[i+1] >= 1:
            arr[i+1] -= 1
            robo[i+1] = 1
            robo[i] = 0

    # 내리기
    robo[n-1] = 0

    # 올리기
    if robo[0] == 0 and arr[0] >= 1:
        arr[0] -= 1
        robo[0] = 1

    if arr.count(0) >= k:
        break
    else:
        res += 1
print(res)
