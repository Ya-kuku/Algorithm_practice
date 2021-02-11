# for _ in range(10):
#     tc = int(input())
#     password = list(map(int,input().split()))
#     flag = 1
#     while flag:
#         for i in range(1,6):
#             if flag:
#                 tmp = password.pop(0)
#                 tmp -= i
#                 if tmp <= 0:
#                     tmp = 0
#                     flag = 0
#                 password.append(tmp)
#             else:
#                 break
#     print('#{}'.format(tc),end=' ')
#     print(*password)

from collections import deque
for _ in range(10):
    tc = int(input()) 
    password = deque(map(int,input().split()))
    print(password[-1])
    while password[-1] != 0:
        for i in range(1,6):
            tmp = password.popleft()
            tmp -= i
            if tmp <= 0:
                password.append(0)
                break
            else:
                password.append(tmp)
    print('#{}'.format(tc), end=' ')
    print(*password)