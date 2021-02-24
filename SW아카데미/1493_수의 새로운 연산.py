for tc in range(int(input())):
    p,q = map(int,input().split())
    arr = [[0] * 400 for _ in range(400)]
    cur = 1
    for i in range(1,400):
        r = i
        c = 1
        for j in range(1,i+1):
            arr[r][c] = cur
            cur += 1
            r -= 1
            c += 1
    a = b = 0
    for i in range(1,400):
        for j in range(1,400):
            if arr[i][j] == p or arr[i][j] == q:
                a += i
                b += j
                if p == q:
                    a *= 2
                    b *= 2
    print('#{} {}'.format(tc+1,arr[a][b]))

# for tc in range(1, int(input()) + 1):
#     p, q = map(int, input().split())
#
#     sol = []
#     for i in range(1, 300):
#         for j in range(1, i + 1):
#             sol.append((j, i - j + 1))
#
#     res = sol.index((sol[p - 1][0] + sol[q - 1][0], sol[p - 1][1] + sol[q - 1][1])) + 1
