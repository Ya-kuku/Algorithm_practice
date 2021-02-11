# import time
# start_time = time.time()
# for tc in range(int(input())):
#     keys = list(input())
#     password = list()
#     i = 0
#     for key in keys:
#         if key == '<':
#             if password:
#                 i -= 1
#         elif key == '>':
#             i += 1
#         elif key == '-':
#             if password:
#                 password.pop()
#         else:
#             password.insert(i,key)
#             i += 1
#     print(*password, sep='')

# end_time = time.time() # 측정 종료
# print("time:", end_time - start_time) # 수행 시간 출력

for tc in range(int(input())):
    keys = list(input())
    left,right = [],[]
    for key in keys:
        if key == '-':
            if left:
                left.pop()
        elif key == '<':
            if left:
                right.append(left.pop())
        elif key == '>':
            if right:
                left.append((right.pop()))
        else:
            left.append(key)
    # 오른쪽 배열이 스택으로 쌓이기 때문에 reverse 해줘야함
    left.extend(right[::-1])
    print(*left, sep='')