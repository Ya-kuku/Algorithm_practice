for tc in range(int(input())):
    N, M = map(int,input().split())
    set_1 = set(input().split())
    set_2 = set(input().split())
    result = set_1 & set_2
    print('#{} {}'.format(tc+1,len(result)))
