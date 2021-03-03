def gcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return x, y


for T in range(1, int(input()) + 1):
    A, B = map(int, input().split())
    x, y = gcd(A, B)
    print('#{} {} {}'.format(T, x, y))