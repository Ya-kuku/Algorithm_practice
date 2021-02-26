for tc in range(int(input())):
    # N 사람오는 시간 갯수, M 초에 K개 붕어빵 만든다
    N, M, K = map(int,input().split())
    peo = list(map(int,input().split()))
    peo.sort()
    # 0초 부터 만들기 시작
    bread = [0] * 11112
    time = 0
    flag = False
    ans = 'Possible'
    while peo:
        if time and not time % M:
            bread[time] += K
        if time == peo[0]:
            while peo and time == peo[0]:
                if bread[time]:
                    bread[time] -= 1
                    peo.pop(0)
                else:
                    ans = 'Impossible'
                    flag = True
                    break
        bread[time+1] += bread[time]
        time += 1
        # if flag:
        #     break
    print('#{} {}'.format(tc+1,ans))