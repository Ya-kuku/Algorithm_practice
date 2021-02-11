for tc in range(1,int(input()) + 1):
    N = int(input())
    income = list(map(int,input().split()))
    mean = sum(income) / N
    ans = 0
    for i in range(N):
        if income[i] <= mean:
            ans +=1
    print('#{} {}'.format(tc,ans))
