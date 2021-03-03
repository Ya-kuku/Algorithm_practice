for tc in range(int(input())):
    N = int(input())
    nums = list(map(int,input().split()))
    Max = -9999999
    Sum = 0
    for i in range(N):
        Sum += nums[i]
        Max = max(Sum,Max)
        if Sum < 0: Sum = 0
    print('#{} {}'.format(tc+1,Max))