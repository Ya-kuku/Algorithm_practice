for tc in range(int(input())):
    cards = list(input())
    # S D H C
    arr = [[0]*13 for _ in range(4)]
    for i in range(0,len(cards),3):
        num = ''
        ptn = cards[i]
        num += cards[i+1]
        num += cards[i+2]
        if cards[i] == 'S':
            arr[0][int(num)-1] += 1
        if cards[i] == 'D':
            arr[1][int(num)-1] += 1
        if cards[i] == 'H':
            arr[2][int(num)-1] += 1
        if cards[i] == 'C':
            arr[3][int(num)-1] += 1
    res = []
    flag = True
    for i in range(4):
        cnt = 0
        for j in range(13):
            if arr[i][j] == 2:
                flag = False
                break
            elif arr[i][j] == 0:
                cnt += 1
        if not flag:
            break
        else:
            res.append(cnt)
    print('#{}'.format(tc+1),end=' ')
    if not flag:
        print('ERROR')
    else:
        print(*res)
