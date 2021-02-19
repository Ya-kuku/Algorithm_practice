from itertools import zip_longest
for tc in range(int(input())):
    N = int(input())
    alpa = list(input().split())
    if N % 2:
        a = alpa[:N // 2+1]
        b = alpa[N // 2+1:]
    else:
        a = alpa[:N//2]
        b = alpa[N//2:]
    res = [a,b]
    zipped = zip_longest(*res)
    print('#{}'.format(tc+1),end=' ')
    for i in zipped:
        print(' '.join(filter(None,i)),end=' ')
    print()

