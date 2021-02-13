for tc in range(10):
    T = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    Max = 0
    for i in range(100):
        Max = max(sum(arr[i][:]),Max)
    for i in range(100):
        c_res = 0
        for j in range(100):
            c_res += arr[j][i]
        Max = max(c_res,Max)

    line_r = line_l = 0
    for i in range(100):
        line_r += arr[i][i]
        line_l += arr[99-i][99-i]
    Max = max(line_r,Max, line_l)

    print('#{} {}'.format(T,Max))