for tc in range(int(input())):
    D, H, M = map(int,input().split())
    res = (D - 11)*24*60 + (H-11)*60 + (M-11)
    if res < 0:
        res = - 1
    print('#{} {}'.format(tc+1,res))