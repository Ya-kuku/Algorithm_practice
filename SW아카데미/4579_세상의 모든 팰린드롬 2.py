def pal(st):
    if len(st) < 2 or st[0] == '*' or st[-1] == '*':
        return 'Exist'
    if st[0] != st[-1]:
        return 'Not exist'
    return pal(st[1: -1])


for t in range(1, int(input()) + 1):
    st = input()
    print('#{} {}'.format(t, pal(st)))