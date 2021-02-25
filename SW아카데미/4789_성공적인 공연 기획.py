for tc in range(int(input())):
    arr = list(map(int,input()))
    now = 0
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            if now >= i:
                continue
            # else:
            #     cnt += i - now
            #     now += i - now
        else:
            if now >= i:
                now += arr[i]
            else:
                cnt += i - now
                now += i - now
                now += arr[i]
    print('#{} {}'.format(tc+1,cnt))
