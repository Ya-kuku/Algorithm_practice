for tc in range(int(input())):
    a,b = map(int,input().split())
    ans = 0
    for i in range(a,b+1):
        if str(round(i**(1/2),1))[-1] == '0':
            if str(i) == str(i)[::-1] and str(int(i**(1/2))) == str(int(i**(1/2)))[::-1]:
                ans += 1
    print('#{} {}'.format(tc+1,ans))
# def is_palindrome(w):
#     if w == w[::-1]:
#         return True
#     return False
#
#
# for T in range(int(input())):
#     a, b = map(int, input().split())
#     res = 0
#     for i in range(a, b + 1):
#         j = i ** (1 / 2)
#         if j == int(j):
#             if is_palindrome(str(i)) and is_palindrome(str(int(j))):
#                 res += 1
#     print("#{} {}".format(T + 1, res))