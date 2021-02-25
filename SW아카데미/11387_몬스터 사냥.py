for tc in range(int(input())):
    D,L,N = map(int,input().split())
    damage = 0
    for i in range(N):
        damage += D*(1+i*(L/100))
    print('#{} {}'.format(tc+1,int(damage)))