for tc in range(int(input())):
    N = int(input())
    arr = [0] * N
    res = 0
    for i in range(N):
        arr[i] = int(input())
    avg = sum(arr[:]) // N
    for i in range(N):
        res += abs(arr[i]-avg)
    print('#{} {}'.format(tc+1,res // 2))