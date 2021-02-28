res = []
for tc in range(int(input())):
    n = input()
    while 1:
        ans = 0
        for i in range(len(n)):
            ans += int(n[i])
        if len(n) == 1:
            res.append(int(ans))
            break
        else:
            n = str(ans)
k = 1
for i in res:
    print('#{} {}'.format(k,i))
    k += 1