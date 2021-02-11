for tc in range(1,11):
    N, password = map(str,input().split())
    password = list(map(int,password))
    print(password)
    idx = 0
    while True:
        for i in range(len(password)-1):
            if password[i] == password[i+1]:
                password.pop(i)
                password.pop(i)
                break
        else:
            break
    print('#{}'.format(tc),end=' ')
    print(*password, sep='')