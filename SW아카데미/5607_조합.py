def fermat(a,b):
    if b == 0:
        return 1
    if b % 2: # 홀수면 곱하기 하나가 남아서 a를 한번 곱해주는거
        return (fermat(a,b//2) ** 2 * a) % mod
    else:
        return (fermat(a,b//2) ** 2 ) % mod

T = int(input())
for tc in range(T):
    N, R = map(int,input().split())
    mod = 1234567891

    facto = [1 for _ in range(N+1)]

    for i in range(2,N+1):
        facto[i] = facto[i-1] * i % mod

    up = facto[N]
    bottom = (facto[N-R] * facto[R]) % mod
    ans = ((up % mod) * (fermat(bottom, mod-2) % mod)) % mod

    print('#{} {}'.format(tc+1,ans))
#
#
# # def nCr(n, r, mod):
# #     lst = [0] * (n+1)
# #     lst[0] = 1
# #     for i in range(1, n+1):
# #         lst[i] = lst[i-1] * i % mod
# #     A = lst[n]
# #     B = pow(lst[r], (mod-2), mod) % mod
# #     C = pow(lst[n-r], (mod-2), mod) % mod
# #     return (A * B * C) % mod
# #
# #
# # for T in range(1, int(input()) + 1):
# #     N, R = map(int,input().split())
# #     answer = nCr(N, R, 1234567891)
# #     print('#{} {}'.format(T, answer))


def x_y(x, y):
    xy = 1
    while y > 0:
        if(y % 2) == 1:
            xy *= x
            y -= 1
            # xy %= m
        x *= x
        # x %= m
        y /= 2
    return xy

print(x_y(2,10))