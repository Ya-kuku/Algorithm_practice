# def Z(board,x,y):
#     global ans
#     if board == 2:
#         if x == r and y == c:
#             print(ans)
#             return
#         ans +=1
#         if x == r and y + 1 == c:
#             print(ans)
#             return
#         ans += 1
#         if x + 1 == r and y == c:
#             print(ans)
#             return
#         ans += 1
#         if x + 1 == r and y +1 == c:
#             print(ans)
#             return
#         ans += 1
#     else:
#         Z(board / 2, x,y)
#         Z(board / 2, x, y + board / 2)
#         Z(board / 2, x + board / 2, y)
#         Z(board / 2, x + board / 2, y + board / 2)
#
# N,r,c = map(int,input().split())
# ans = 0
# Z(2**N,0,0)


n, r, c = map(int, input().split())
num = 0

while n > 0:
    a = 2**n // 2
    if n > 1:
        if a > r and a <= c:
            num = num + a**2
            c = c - 1
        elif a <= r and a > c:
            num = num + (a**2)*3
            r = r-a
        elif a <= r and a<=  c:
            num = num + (a**2)*3
            c = c-a
            r = r-a
    elif n == 1:
        if r == 0 and c == 1:
            num += 1
        elif r == 1 and c == 0:
            num += 2
        elif r == 1 and c == 1:
            num += 3
    n -= 1

print(num)
