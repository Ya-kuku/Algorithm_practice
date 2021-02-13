for tc in range(int(input())):
    a,b,c = map(int,input().split())
    cnt = [0] * 101
    cnt[a] += 1
    cnt[b] += 1
    cnt[c] += 1
    res = 0
    for i in range(len(cnt)):
        if cnt[i] == 1 or cnt[i] ==3:
            res = i

    print('#{} {}'.format(tc+1,res))
