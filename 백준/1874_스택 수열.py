N = int(input())

stack = []
ans = []
tmp = 1
for i in range(1,N+1):
    data = int(input())
    while tmp <= data:
        stack.append(tmp)
        tmp += 1
        ans.append('+')
    if stack[-1] == data:
        stack.pop()
        ans.append('-')
    else:
        # pop을 하는 경우에 스택에 쌓여있는 데이터가 내림차순이 아니면 불가능
        print('NO')
        exit(0)

print(*ans,sep='\n')
# print('\n'.join(ans))