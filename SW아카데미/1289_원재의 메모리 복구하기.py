for tc in range(1,int(input()) + 1):
    memory = input()
    st= memory[0]
    ans = 0
    for i in range(len(memory)):
        if memory[i] == st:
            continue
        else:
            st = memory[i]
            ans += 1
    if memory[0] == '1':
        ans +=1
    print('#{} {}'.format(tc,ans))


