T = int(input())
for tc in range(1,T+1):
    L,U,X = map(int,input().split())
    ans = -1
    if X < L:
        ans = L - X
    elif L <= X <= U:
        ans = 0

    print('#{} {}'.format(tc,ans))