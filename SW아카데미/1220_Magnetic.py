for tc in range(10):
    N = int(input())
    magnetic = [list(map(int,input().split())) for _ in range(100)]
    # 1 = N, 2 = S
    ans = 0
    for i in range(100):
        now = 0
        for j in range(100):
            if magnetic[j][i] == 1:
                now = 1
            elif magnetic[j][i] == 2:
                if now == 1:
                    now = 0
                    ans += 1
    print('#{} {}'.format(tc+1,ans))

