def dfs(aa, bb, cc, dd, temp):
    global ans

    if ans or abs(bb - cc) >= 2:
        return
    if aa + bb + cc + dd == 0:
        ans = temp
        return

    if temp[-1] == '0':
        if aa:
            dfs(aa - 1, bb, cc, dd, temp + '0')
        if bb:
            dfs(aa, bb - 1, cc, dd, temp + '1')
    elif temp[-1] == '1':
        if cc:
            dfs(aa, bb, cc - 1, dd, temp + '0')
        if dd:
            dfs(aa, bb, cc, dd - 1, temp + '1')



t = int(input())
for tc in range(1, t + 1):
    a, b, c, d = map(int, input().split())

    ans = ''

    dfs(a, b, c, d, '0')
    dfs(a, b, c, d, '1')

    if not ans:
        ans = 'impossible'

    print(f'#{tc} {ans}')