for tc in range(int(input())):
    N = int(input())
    farm = [list(map(int,input())) for _ in range(N)]
    res = 0
    st  = (N-1) // 2
    for i in range((N-1) // 2):
        res += sum(farm[i][st-i:st+i+1])

    res += sum(farm[(N-1)//2 ][:])

    st = 1
    for i in range((N-1) // 2 + 1 , N):
        res += sum(farm[i][st:N-st])
        st += 1
    print('#{} {}'.format(tc+1,res))
