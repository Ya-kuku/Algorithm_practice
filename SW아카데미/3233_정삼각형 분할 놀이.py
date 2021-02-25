for tc in range(int(input())):
    A, B = map(int,input().split())
    tmp = A // B
    res = 0
    for i in range(tmp):
        res += 2*i + 1
    print('#{} {}'.format(tc+1,res))