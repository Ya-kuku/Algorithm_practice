def devide(a,b):
    if b == 1:
        return a % C
    elif b == 2:
        return a * a % C
    else:
        tmp = devide(a,b//2)
        if b % 2 == 0:
            return tmp * tmp % C
        else:
            return tmp * tmp * a % C

A, B, C = map(int,input().split())
print(devide(A,B))

# def x_y(x, y):
#     xy = 1
#     while y > 0:
#         if(y % 2) == 1:
#             xy *= x % C
#             y -= 1
#             # xy %= m
#         x *= x % C
#         # x %= m
#         y /= 2
#     return xy
# A, B, C = map(int,input().split())
# print(x_y(A,B) % C)