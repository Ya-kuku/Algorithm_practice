for tc in range(10):
    num = int(input())
    building = list(map(int,input().split()))
    ans = 0
    for i in range(2,num-2):
        a = max(building[i-1],building[i-2],building[i+1],building[i+2])
        if building[i] > a:
            ans += building[i] - a

    print('#{} {}'.format(tc+1  ,ans))