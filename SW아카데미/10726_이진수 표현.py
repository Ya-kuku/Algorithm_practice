def bin_num(n):
    if n == 0: return '0'
    if n == 1: return '1'
    ans = ''
    while 1:
        if not n % 2:
            ans += '0'
        else:
            ans += '1'
        n = n // 2

        if n == 1:
            ans += '1'
            return ans
for tc in range(int(input())):
    N, M = map(int,input().split())
    bit = bin_num(M)
    res = 'ON'
    if len(bit) >= N:
        for i in range(N):
            if M == 0 or not int(bit[i]):
                res ='OFF'
                break
    else:
        for i in range(len(bit)):
            if M == 0 or not int(bit[i]):
                res ='OFF'
                break
    print('#{} {}'.format(tc+1,res))


def check(M):
    for i in range(N):
        if M % 2 != 1:
            return "OFF"
        else:
            M = M // 2
    return "ON"

for tc in range(int(input())):
    N, M = map(int, input().split())

    print('#{} {}'.format(tc+1,check(M)))