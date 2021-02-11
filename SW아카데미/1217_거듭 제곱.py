def multi(a,b):
    if b == 1:
        return a
    return multi(a,b-1)*a
for _ in range(1,11):
    tc = int(input())
    a,b = map(int,input().split())
    ans = multi(a,b)
    print('#{} {}'.format(tc,ans))